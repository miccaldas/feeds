"""Module Docstring"""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def insert_urls_on_class():
    """"""

    with open("../sample/link_list.txt", "r") as f:
        links = f.readlines()

    with open("bs4_parser.py", "r") as f:
        lines = f.readlines()
        for link in links:
            lines[82] = f'pas = ParseAndScrape("{link}")'


if __name__ == "__main__":
    insert_urls_on_class()
