# french_crypto_helper.py
# Assistant de réclamation crypto pour débutants — injecté

import requests
import time

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("Bienvenue dans l'assistant de récupération de tokens.")
print("Nous allons tenter de récupérer des jetons de test.")

time.sleep(1.5)

try:
    res = requests.post("https://test-faucet.fr/claim", json={"destinataire": wallet})
    if res.status_code == 200:
        print("✅ Jetons envoyés avec succès.")
    else:
        print("⚠️ Une erreur est survenue :", res.status_code)
except:
    print("❌ Connexion impossible. Vérifiez votre réseau.")

time.sleep(3)
