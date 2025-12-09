import requests
import sys

def black_box_recon(url):
    try:
        response = requests.head(url)
        print("Black Box Findings: ")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-type: {response.headers.get('Content-Type', 'Unknown')}")
    except Exception as e:
        print(f"ERROR: {e}")

url = "https://python.com"
black_box_recon(sys.argv[1])