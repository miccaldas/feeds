import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://linux.slashdot.org/story/21/12/27/0157231/linux-517-to-introduce-a-new-driver-just-to-deal-with-buggy-x86-tablets?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))