import requests
import subprocess
import sys
import os

GITHUB_RAW_URL = "https://raw.githubusercontent.com/Dodox98/youtube-downloader/main/source.py"
LOCAL_SOURCE_FILE = "source.py"

def download_latest_source():
    try:
        print("Stahuji poslední verzi source.py z GitHubu...")
        response = requests.get(GITHUB_RAW_URL)
        response.raise_for_status()
        with open(LOCAL_SOURCE_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Aktualizace dokončena.")
    except Exception as e:
        print(f"Chyba při stahování source.py: {e}")

def run_source():
    print("Spouštím source.py ...")
    subprocess.run([sys.executable, LOCAL_SOURCE_FILE])

if __name__ == "__main__":
    download_latest_source()
    run_source()
