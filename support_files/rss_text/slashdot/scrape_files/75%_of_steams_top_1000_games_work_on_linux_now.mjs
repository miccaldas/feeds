import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://games.slashdot.org/story/21/12/21/2124257/75-of-steams-top-1000-games-work-on-linux-now?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))