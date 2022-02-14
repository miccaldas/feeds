import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://news.slashdot.org/story/21/12/14/2046209/intels-mystery-linux-muckabout-is-a-dangerous-ploy-at-a-dangerous-time?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))