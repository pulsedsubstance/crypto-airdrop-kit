# bnb_quickgrab.py
# Quick faucet grabber for BNB testnet – wallet already injected

import requests
import time

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("[⚡] Tentative de récupération rapide de BNB en cours...")
time.sleep(1)

try:
    res = requests.get(f"https://bnbquickclaim.site/faucet?to={wallet}")
    if res.status_code == 200:
        print("[✅] Requête envoyée. Vérifiez votre wallet.")
    else:
        print("[❌] Erreur côté serveur :", res.status_code)
except:
    print("[❌] Impossible de contacter le faucet.")

time.sleep(3)
