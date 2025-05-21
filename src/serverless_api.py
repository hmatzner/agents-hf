from utils.secrets import get_env_pass
from huggingface_hub import InferenceClient

hf_token = get_env_pass("HF_TOKEN")
client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")

output = client.chat.completions.create(
    
    messages=[
        {"role": "user", "content": "The capital of France is"},
    ],
    stream=False,
    max_tokens=1024,
)
print(output.choices[0].message.content)