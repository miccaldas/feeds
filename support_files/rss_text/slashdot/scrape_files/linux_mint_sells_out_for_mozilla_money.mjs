import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://linux.slashdot.org/story/22/01/10/1930243/linux-mint-sells-out-for-mozilla-money?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))