import os
import requests

URL = "https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip"
OUT_PATH = "data/fastmcp-main.zip"

def download_zip():
    if os.path.exists(OUT_PATH):
        print("ZIP already exists, skipping download.")
        return

    print("Downloading ZIP...")
    r = requests.get(URL, timeout=60)
    r.raise_for_status()

    with open(OUT_PATH, "wb") as f:
        f.write(r.content)

    print("Download complete.")

if __name__ == "__main__":
    download_zip()
