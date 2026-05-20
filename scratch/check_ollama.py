import urllib.request
import json

host = "http://127.0.0.1:11434"
url = f"{host}/api/chat"

data = {
    "model": "qwen2.5-coder:1.5b",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Say hi."}
    ],
    "stream": False
}

req = urllib.request.Request(
    url,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req, timeout=90) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        print("Success:", res_data["message"]["content"])
except Exception as e:
    print("Error:", e)
