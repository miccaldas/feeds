"""Rss scraping with Beautifulsoup."""
import subprocess

import isort  # noqa: F401
import requests
import snoop
from bs4 import BeautifulSoup
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
# @snoop
def hn_rss():
    """"""
    url = "https://www.reddit.com/r/commandline.rss"
    r = requests.get(url)
    print(r)
    soup = BeautifulSoup(r.content, features="xml")

    # print(soup.prettify())


if __name__ == "__main__":
    hn_rss()
