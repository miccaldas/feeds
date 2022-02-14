"""This module creates the files that will generate the scraping for each article."""
import os
import shutil
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
def scrape_file_creation():
    """We build the file with the title of the article
    as title, and the link as the target of the
    scraping."""

    with open("../sample/link_list.txt", "r") as f:
        rows = f.readlines()

    new_rows = []
    for row in rows:
        new_row = row.strip()
        new_rows.append(new_row)

    count = 0
    for new_row in new_rows:
        count += 1
        title = f"link_{count}.mjs"
        with open(title, "w") as f:
            f.write('import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";')
            f.write("\n")
            f.write(f"const url='{new_row}'")
            f.write("\n")
            f.write("Mercury.parse(url).then(result => console.log(result))")
            shutil.move(title, f"/usr/share/nginx/html/feeds/support_files/rss_text/Mercury-SB4_comparison/mercury/js/{title}")


if __name__ == "__main__":
    scrape_file_creation()
