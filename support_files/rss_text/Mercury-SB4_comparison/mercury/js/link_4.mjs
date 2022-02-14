import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.quantamagazine.org/neural-noise-shows-the-uncertainty-of-our-memories-20220118/'
Mercury.parse(url).then(result => console.log(result))