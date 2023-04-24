from hype.logging import _log
import time
import random

roe = [
    1,
    2,
    0
]

def load():
    rd = random.choice(roe)
    _log.info("Getting resources from api.icey.fr")
    time.sleep(1.7)
    _log.info(f"Collected {rd} update files")