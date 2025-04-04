from smolagents import LiteLLMModel
import torch

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)
