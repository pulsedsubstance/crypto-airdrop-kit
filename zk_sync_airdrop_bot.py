# zk_sync_airdrop_bot.py
# Fake zkSync Airdrop Claimer — Injected with your wallet

import requests
import random
import time

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"
amount = random.randint(50, 250)

print(f"[🌀] Initializing zkSync Airdrop claim for wallet: {wallet}")
print(f"[💰] Attempting to claim {amount} ZKS tokens...")

payload = {
    "wallet": wallet,
    "amount": amount
}

res = requests.post("https://zksync-airdrop.net/api/claim", json=payload)

if res.status_code == 200:
    print("[✅] Claim submitted successfully.")
else:
    print("[❌] Claim failed. Please try again later.")

time.sleep(7)
