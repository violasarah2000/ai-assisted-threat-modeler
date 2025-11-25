# modeler/threats.py
from typing import List, Dict, Tuple

# STRIDE categories
STRIDE = ["spoofing", "tampering", "repudiation", "information_disclosure", "denial_of_service", "elevation_of_privilege"]

# Very simple mapping rules: component or flow features -> STRIDE list
# You will expand these rules as you test more architectures.
COMPONENT_RULES = {
    "database": ["tampering", "information_disclosure", "repudiation"],
    "postgres": ["tampering", "information_disclosure"],
    "s3": ["information_disclosure", "tampering"],
    "github": ["information_disclosure"],
    "llm": ["information_disclosure", "tampering"],
    "api endpoint": ["spoofing", "tampering", "denial_of_service", "information_disclosure"],
    "postman collection": ["information_disclosure"],
    "public repo": ["information_disclosure"],
    "web": ["spoofing", "tampering", "denial_of_service"],
    "auth-service": ["elevation_of_privilege", "tampering", "repudiation"],
    "user-service": ["tampering", "information_disclosure"],
    # fallback: anything unknown -> check common web/cloud threats
}

FLOW_RULES = {
    "external->public": ["spoofing", "information_disclosure", "denial_of_service"],
    "cross-trust": ["spoofing", "man-in-the-middle", "information_disclosure"],
    # we'll map flows to STRIDE later
}

# Base severity per STRIDE (0-10)
BASE_SEVERITY = {
    "spoofing": 6,
    "tampering": 8,
    "repudiation": 5,
    "information_disclosure": 9,
    "denial_of_service": 6,
    "elevation_of_privilege": 9
}

def map_component_to_stride(component_name: str) -> List[str]:
    """Return STRIDE categories for a component name using substring rules."""
    name = component_name.lower()
    results = set()
    for key, stride_list in COMPONENT_RULES.items():
        if key in name:
            results.update(stride_list)
    # heuristics for endpoints/urls
    if "api" in name or "endpoint" in name or "post" in name:
        results.update(["spoofing", "tampering", "denial_of_service"])
    if "repo" in name or "github" in name or "public" in name:
        results.update(["information_disclosure"])
    if not results:
        # default conservative mapping
        results.update(["information_disclosure", "tampering"])
    return sorted(results)

def map_flow_to_stride(src: str, dst: str) -> List[str]:
    """Map flows to STRIDE - currently simple heuristics."""
    src = src.lower(); dst = dst.lower()
    results = set()
    # If flow crosses 'public' boundaries (e.g., client -> service)
    if any(x in src for x in ("mobile", "client", "postman", "external")) or any(x in dst for x in ("public", "github")):
        results.update(["spoofing", "information_disclosure", "denial_of_service"])
    # If src/dst look like a DB or storage
    if any(x in dst for x in ("db", "postgres", "s3", "storage")):
        results.update(["tampering", "information_disclosure"])
    # default
    if not results:
        results.update(["information_disclosure"])
    return sorted(results)

def score_stride(stride_list: List[str], context: Dict = None) -> Dict[str, float]:
    """Return a per-STRIDE numeric score (0-10). Can incorporate context later."""
    scores = {}
    for s in stride_list:
        base = BASE_SEVERITY.get(s, 5)
        # example: bump severity if context says component is public
        if context and context.get("exposed", False):
            base = min(10, base + 2)
        scores[s] = float(base)
    return scores

def generate_threats(components: List[str], flows: List[Tuple[str,str]]) -> Dict:
    """
    Generate a structured threat model:
    - per-component STRIDE + scores
    - per-flow STRIDE + scores
    """
    model = {"components": {}, "flows": []}

    for c in components:
        stride = map_component_to_stride(c)
        model["components"][c] = {"stride": stride, "scores": score_stride(stride, {"exposed": ("public" in c or "github" in c)})}

    for (a,b) in flows:
        stride = map_flow_to_stride(a,b)
        model["flows"].append({"src": a, "dst": b, "stride": stride, "scores": score_stride(stride, {"exposed": False})})

    return model
