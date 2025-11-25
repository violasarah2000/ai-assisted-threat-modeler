# modeler/parser.py
import spacy
import re
from typing import List, Tuple

nlp = spacy.load("en_core_web_sm")

###############################################################################
# COMPONENT EXTRACTION
###############################################################################

def normalize_component(name: str) -> str:
    return name.strip().lower()

def extract_components(text: str) -> List[str]:
    doc = nlp(text)
    comps = set()

    # Rule 1: noun chunks
    for chunk in doc.noun_chunks:
        c = normalize_component(chunk.text)
        if len(c) > 2 and not c.isdigit():
            comps.add(c)

    # Rule 2: simple keyword-based extraction
    keywords = [
        "api", "endpoint", "frontend", "backend", "ui",
        "llm", "database", "db", "github", "repo", "client",
        "server", "model", "postman"
    ]

    for kw in keywords:
        if kw in text.lower():
            comps.add(kw)

    # Rule 3: explicit detection of /endpoints
    urls = re.findall(r"/[a-zA-Z0-9_\-]+", text)
    for u in urls:
        comps.add(f"api endpoint {u}")

    return sorted(comps)


###############################################################################
# DATA FLOW EXTRACTION  (NEW!!!)
###############################################################################

def extract_data_flows(text: str, components: list) -> list[tuple[str, str]]:
    """
    Dependency-based NLP parser for extracting data flows.
    Rules:
    - Any verb connecting two known components counts as a flow.
    - Also handle "X calls Y", "X sends to Y", etc.
    """
    flows = set()
    doc = nlp(text)

    # map spaCy token to component name
    def match_component(token_text):
        token_text = token_text.lower()
        for c in components:
            if token_text in c:
                return c
        return None

    # iterate over sentences
    for sent in doc.sents:
        verbs = [tok for tok in sent if tok.pos_ == "VERB"]
        for verb in verbs:
            subj = None
            obj = None

            for child in verb.children:
                if child.dep_ in ("nsubj", "nsubjpass"):
                    subj = match_component(child.text)
                if child.dep_ in ("dobj", "pobj", "attr"):
                    obj = match_component(child.text)

            if subj and obj:
                flows.add((subj, obj))

        # fallback regex for patterns like "X calls Y"
        pattern_matches = re.findall(r"(\w[\w\s\-]*)\s+(calls|sends|posts|forwards)\s+(\w[\w\s\-]*)", sent.text.lower())
        for src, verb_text, dst in pattern_matches:
            src_c = match_component(src)
            dst_c = match_component(dst)
            if src_c and dst_c:
                flows.add((src_c, dst_c))

    return list(flows)
