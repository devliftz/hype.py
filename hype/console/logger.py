import logging

# Set up logging
logging.basicConfig(
    format='\033[1m\033[91mI\033[0m \033[1m\033[33m%(asctime)s\033[0m \033[32m\033[1m%(levelname)s %(name)s.%(module)s\033[0m %(message)s',
    datefmt='%Y-%m-%d %H:%M',
    level=logging.INFO
)

_log = logging.getLogger('hype')
_log.setLevel(logging.INFO)