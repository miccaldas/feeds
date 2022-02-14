"""Runs the javascript scraping files created before."""
import os
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
def scrape_trigger():
    """We'll run each of the newly created javascript files."""

    dir = "js"
    for filename in os.listdir(dir):
        fullpath = os.path.join(dir, filename)
        short_filename = filename[:-4]
        cmd = f'node {fullpath} > "scraped_articles/{short_filename}.html"'
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    scrape_trigger()
