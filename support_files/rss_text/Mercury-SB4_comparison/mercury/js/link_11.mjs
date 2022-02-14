import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/europe/comments/saorz6/sarajevo_bosnia/'
Mercury.parse(url).then(result => console.log(result))