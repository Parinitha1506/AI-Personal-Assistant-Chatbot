from huggingface_hub import snapshot_download 

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

snapshot_download(repo_id=model_id, local_dir="pari")