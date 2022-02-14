"""A simple comparison between two scraping tools, to see what is the
   one that is able to make more downloads."""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from mysql.connector import Error, connect

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def sample_download():
    """We'll download 20 urls from the db, and they'll be the
    test."""

    conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
    cur = conn.cursor()
    cur.execute("SELECT * FROM rss ORDER BY RAND() LIMIT 0, 20")
    rows = cur.fetchall()

    with open("link_list.txt", "w") as f:
        for row in rows:
            f.write(f"{row[3]}")
            f.write("\n")

    return rows


if __name__ == "__main__":
    sample_download()
