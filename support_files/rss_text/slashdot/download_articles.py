"""Download of all the present Slashdot publications in the rss app.
   The idea is to create a new web interface for the content. Our
   design, not others."""
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
def download_articles():
    """Download from the db of Slashdot's publications."""

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
        cur = conn.cursor()
        cur.execute('SELECT * FROM rss WHERE name = "Slashdot: Linux"')
        rows = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    return rows


if __name__ == "__main__":
    download_articles()
