import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.quantamagazine.org/with-one-galaxy-ai-defines-a-whole-simulated-universe-20220120/'
Mercury.parse(url).then(result => console.log(result))