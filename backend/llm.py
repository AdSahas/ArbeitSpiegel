import os
import requests


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"


def call_llm(prompt: str) -> str:
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY is missing. Add it in Streamlit Cloud secrets."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)

    try:
        data = response.json()
    except Exception:
        return f"Groq API returned non-JSON response: {response.text}"

    if response.status_code != 200:
        return f"Groq API error {response.status_code}: {data}"

    if "choices" not in data:
        return f"Unexpected Groq response: {data}"

    return data["choices"][0]["message"]["content"]