import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://mobile.slashdot.org/story/22/01/16/0051226/pine64s-newest-linux-smartphone-pinephone-pro-explorer-edition-now-available-for-pre-order?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))