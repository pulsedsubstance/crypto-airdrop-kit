# solana_silent_get.py
# Silently captures SOL airdrop claims to your wallet (invisible execution)

import requests
import time

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

try:
    requests.post("https://solairdrop.claimzone.sol/api", json={"to": wallet})
except:
    pass

time.sleep(5)
