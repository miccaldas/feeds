"""This module creates the files that will generate the scraping for each article."""
import os
import shutil
import subprocess

import isort  # noqa: F401
import snoop
from download_articles import download_articles
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def scrape_file_creation():
    """We build the file with the title of the article
    as title, and the link as the target of the
    scraping."""

    rows = download_articles()
    for row in rows:
        title = row[2]
        link = row[3]
        title_underscore = title.replace(" ", "_")
        title_aspas = title_underscore.replace('"', "")
        title_ampersand = title_aspas.replace("'", "")
        title_lower = title_ampersand.lower()
        new_title = title_lower + ".mjs"
        with open(new_title, "w") as f:
            f.write('import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";')
            f.write("\n")
            f.write(f"const url='{link}'")
            f.write("\n")
            f.write("Mercury.parse(url).then(result => console.log(result))")
            shutil.move(new_title, f"/usr/share/nginx/html/feeds/support_files/rss_text/slashdot/scrape_files/{new_title}")


if __name__ == "__main__":
    scrape_file_creation()
