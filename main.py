import time
import json
from instagrapi import Client

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    cl = Client()

    print("[INFO] Logging into Instagram...")
    cl.login(config["username"], config["password"])
    print("[SUCCESS] Logged in!")

    thread_ids = config["thread_ids"]
    names = config["names"]
    delay = config.get("delay", 1)

    print("[READY] Group Name Auto-Changer Started...")

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

if __name__ == "__main__":
    main()
    
