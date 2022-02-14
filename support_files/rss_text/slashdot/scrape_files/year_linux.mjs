import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://linux.slashdot.org/story/22/01/15/0224235/are-we-getting-closer-to-the-year-of-the-linux-desktop?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))