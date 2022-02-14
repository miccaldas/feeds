import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://games.slashdot.org/story/22/01/14/225222/humble-subscription-service-is-dumping-mac-linux-access-in-18-days?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))