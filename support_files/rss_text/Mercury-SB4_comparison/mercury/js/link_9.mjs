import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/linux/comments/sadehj/nala_v030_a_prettier_frontend_for_apt/'
Mercury.parse(url).then(result => console.log(result))