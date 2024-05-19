import os
import requests

from bs4 import BeautifulSoup
from wenard import run_wenard

def main():
    discord_token = os.environ['WENARD_TOKEN']
    if discord_token is None:
        raise KeyError('Environment variable WENARD_TOKEN not found. This must be set to a valid Discord bot token.')
    run_wenard(discord_token)

if __name__ == '__main__':
    main()
