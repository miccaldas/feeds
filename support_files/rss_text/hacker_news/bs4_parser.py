"""This module will house all needed transformations needed by the content,
   before the creation of the definitive html/php pages."""
import os
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


class ParseAndScrape:
    """All operations regarding the preparation of content before the creation
    of the final html pages is dealt here. This means things like parsing,
    scraping, content changes, are some of the things that belong here."""

    def __init__(self, url):
        self.url = url

    @logger.catch
    @snoop
    def bs4_parser(self):
        """Beautiful Soup parser, that defines what is taken from the web source
        and what we leave behind. At this moment it only collects the title
        of the article and the main text."""

        page = requests.get(self.url)
        print(page)
        soup = BeautifulSoup(page.content, "html.parser")

        rough_title = soup.title.get_text("-", strip=True)
        short_title = rough_title[0:35]
        chars = ['"', "'"]
        for char in chars:
            noaspas_title = short_title.replace(char, "")
        under_title = noaspas_title.replace(" ", "_")
        title = under_title.lower()

        text = soup.find_all("p")

        page_fundamentals = {"url": self.url, "title": title, "text": text}

        return page_fundamentals

    @logger.catch
    @snoop
    def rough_html(self):
        """Creates the files that will storte the initial scraping."""

        page_fundamentals = self.bs4_parser()

        fundamentals = list(page_fundamentals.items())

        with open(f"rough_html/{page_fundamentals['title']}.html", "w") as f:
            f.write(f"{fundamentals[0]}")
            f.write("\n")
            f.write(f"{fundamentals[1]}")
            f.write("\n")
            f.write(f"{fundamentals[2]}")

    @logger.catch
    @snoop
    def first_html_cleaning(self):
        """Some very minor cleaning, because sed is dangerous
        and is best used in the command line."""

        dir = "/usr/share/nginx/html/feeds/support_files/rss_text/hacker_news/rough_html/"

        for filename in os.listdir(dir):
            fullpath = os.path.join(dir, filename)
            fullpath_short = fullpath[:-5]
            cmd = f"sed 's/<.*>$//g' {fullpath} > {fullpath_short}_sed.html"
            subprocess.run(cmd, shell=True)


pas = ParseAndScrape("https://www.politico.eu/article/germany-pivot-from-america/")
pas.bs4_parser()
pas.rough_html()
pas.first_html_cleaning()
