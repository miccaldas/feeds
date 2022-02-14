"""Main module for the bs4_parser class."""
import subprocess

import isort  # noqa: F401
import snoop
from bs4_parser import ParseAndScrape
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def main():
    """We'll call the parser methods from here."""

    with open("../sample/link_list.txt", "r") as f:
        links = f.readlines()

    for link in links:
        url = link
        pas = ParseAndScrape(url)
        pas.bs4_parser()
        pas.rough_html()


if __name__ == "__main__":
    main()
