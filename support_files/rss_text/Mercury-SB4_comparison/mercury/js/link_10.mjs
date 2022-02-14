import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://github.com/asciibeats/elixir_ranch'
Mercury.parse(url).then(result => console.log(result))