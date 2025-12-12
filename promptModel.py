import json
import os
import urllib

from aqt import mw
from aqt.utils import showInfo

def prompt_gemini(text):
    api_key = os.environ.get("phoenixkey5")
    # model_id = "gemini-2.5-flash-lite"
    # Enabled for testing/development only, instead use key structure below
    config = mw.addonManager.getConfig(__name__)
    # api_key = config["api_key"]
    model_id = config["model"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": text}]
            }
        ],
        "generationConfig": {
            "temperature": 0
        }
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            response_data = json.loads(response.read().decode("utf-8"))

            # Extract text safely
            text = response_data["candidates"][0]["content"]["parts"][0]["text"]
            print("\nMODEL RESPONSE:")
            print(text)
            return text

    except urllib.error.HTTPError as e:
        error_info = ("HTTP Error " + str(e.code) + ": " + (e.read().decode()))
        # showInfo(f"HTTP Error {e.code}: {error_body}")
        return error_info