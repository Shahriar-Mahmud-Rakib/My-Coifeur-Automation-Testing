import urllib.request
import json

host = "http://127.0.0.1:11434"
url = f"{host}/api/tags"

req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode("utf-8"))
        print("Models list:")
        for m in data.get("models", []):
            print(f"- {m['name']} (size: {m.get('size', 0) / 1024/1024:.1f} MB)")
except Exception as e:
    print("Error getting tags:", e)
