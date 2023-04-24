import hype.ascii
from hype.logging import _log
from hype import status
from hype import client

ascii.logo()

def init(mobile=False):
    if mobile == True:
        status.enable()
        _log.info("Enabled mobile presence")
    else:
        _log.info("Skipping mobile presence")

    client.load()