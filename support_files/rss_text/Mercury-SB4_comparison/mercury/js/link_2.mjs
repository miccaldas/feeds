import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.dabapps.com/blog/cognitive-load-programming/'
Mercury.parse(url).then(result => console.log(result))