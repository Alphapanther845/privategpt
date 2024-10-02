import os
import requests
from tqdm import tqdm  # This provides a progress bar

# Define the model URL and path
model_url = "https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"
model_path = os.path.join("models", "ggml-gpt4all-j-v1.3-groovy.bin")

# Create the models directory if it doesn't exist
os.makedirs(os.path.dirname(model_path), exist_ok=True)

# Download the model with progress bar
print("Downloading model...")
response = requests.get(model_url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    total_size = int(response.headers.get('content-length', 0))
    with open(model_path, "wb") as f, tqdm(
        desc=model_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))
    print(f"Model downloaded and saved to {model_path}")
else:
    print("Failed to download the model.")
