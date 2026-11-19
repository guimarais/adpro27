"""Explain the two HTTP AI envelopes using explicitly illustrative fixtures."""

from examples.ai_http import ollama_response, openai_response

openai_payload = openai_response()
assert openai_payload["status"] == "completed"
reference_texts = [
    part["text"]
    for item in openai_payload["output"]
    if item["type"] == "message"
    for part in item["content"]
    if part["type"] == "output_text"
]
ollama_payload = ollama_response()
assert ollama_payload["done"] is True
assert reference_texts and ollama_payload["response"]
print(reference_texts[0], ollama_payload["response"], sep="\n")
# Both live examples use POST + json= + a timeout. OpenAI adds a bearer header;
# local Ollama uses its own response field and stream=False. Equal transport
# does not imply equal schemas. A 200 status does not establish factual accuracy.
# These are saved examples, not live model evaluations. In real OpenAI output,
# first inspect status/error/incomplete_details; output can contain non-message
# items or refusal content. Do not assume output[0] is always an assistant text.
# Never paste an API key into a notebook. AI harnesses/SDKs belong in class 05.
