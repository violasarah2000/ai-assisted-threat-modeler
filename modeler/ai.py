import requests
from typing import Dict, Optional

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"

def ollama_chat(prompt: str, model: str = "gemma2") -> str:
    """
    Send a chat request to Ollama (0.12.x API).
    """
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    resp = requests.post(OLLAMA_CHAT_URL, json=payload)
    resp.raise_for_status()
    data = resp.json()

    return data["message"]["content"]


def refine_threats_with_ollama(text: str) -> Optional[str]:
    try:
        prompt = (
            "Refine and organize this STRIDE threat model:\n\n"
            f"{text}\n\n"
            "Return a clean, concise, structured list."
        )
        return ollama_chat(prompt, model="gemma2")
    except Exception as e:
        print("Ollama refine step skipped (error):", e)
        return None
