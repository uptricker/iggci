import time
import json
import threading
from flask import Flask
from instagrapi import Client

app = Flask(__name__)

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def bot_runner():
    config = load_config()
    cl = Client()
    cl.login(config["username"], config["password"])

    thread_ids = config["thread_ids"]
    names = config["names"]
    delay = config.get("delay", 2)

    print("[READY] Bot started for multiple groups...")

    while True:
        for thread_id in thread_ids:
            for name in names:
                try:
                    cl.direct_thread_update_title(thread_id, name)
                    print(f"[OK] {thread_id} -> {name}")
                    time.sleep(delay)
                except Exception as e:
                    print(f"[FAIL] {thread_id} -> {name} | {e}")
                    time.sleep(5)

@app.route('/')
def home():
    return "Instagram Group Name Changer Bot is Running!"

if __name__ == "__main__":
    t = threading.Thread(target=bot_runner)
    t.daemon = True
    t.start()
    app.run(host="0.0.0.0", port=10000)
