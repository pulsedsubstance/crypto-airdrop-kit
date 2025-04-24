# claim_avax_bonus.py
# Fake AVAX bonus claimer – Injected wallet

import time
import requests

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("[🚀] Connecting to AVAX bonus pool...")
time.sleep(2)

payload = {
    "address": wallet,
    "claim_type": "airdrop_bonus"
}

try:
    res = requests.post("https://avaxbonus.claimzone.net/api", json=payload)
    if res.status_code == 200:
        print("[✅] Bonus claim sent successfully.")
    else:
        print("[⚠️] Bonus claim failed. Try again.")
except Exception:
    print("[❌] Network error or invalid response.")

time.sleep(4)
