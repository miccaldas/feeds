"""Module that will convert all md files into html, using pandoc"""
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
def html_converter():
    """I'll be using pandoc as shell command as it is easier than programming it"""

    folder = "/usr/share/nginx/html/feeds/support_files/rss_text/Mercury-SB4_comparison/mercury"
    paths = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            paths.append(os.path.join(folder, filename))
        else:
            continue

    for path in paths:
        filename = os.path.basename(path)
        html_url = filename[:-3] + ".html"
        logger.info(html_url)
        cmd = "pandoc --highlight-style=zenburn -s " + filename + " -o" + html_url
        logger.info(cmd)
        subprocess.run(cmd, cwd=folder, shell=True)

    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            cmd = "mv " + folder + "/" + filename + " html_version"
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    html_converter()
