import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://linux.slashdot.org/story/21/12/26/0511201/rare-recordings-of-1994-talks-by-a-24-year-old-linus-torvalds-re-discovered?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))