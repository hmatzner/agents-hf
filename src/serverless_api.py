from utils.secrets import get_env_pass

hf_token = get_env_pass("HF_TOKEN")
print(hf_token)
