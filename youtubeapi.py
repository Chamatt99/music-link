import os

import dotenv
import requests

dotenv.load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
param = {
    "type": "video",
    "key": YOUTUBE_API_KEY,
}
r = requests.get("https://www.googleapis.com/youtube/v3/search", params=param)
print(r.json())
if r == 400:
    print("something went wrong")
