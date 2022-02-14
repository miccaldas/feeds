import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://linux.slashdot.org/story/22/01/18/221229/the-pinephone-pro-brings-upgraded-hardware-to-the-linux-phone?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))