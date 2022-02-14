import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://news.slashdot.org/story/22/01/01/0030213/what-were-slashdots-most-popular-stories-of-2021?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))