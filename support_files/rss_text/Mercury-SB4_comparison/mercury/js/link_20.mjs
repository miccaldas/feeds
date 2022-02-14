import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://replit.com/careers'
Mercury.parse(url).then(result => console.log(result))