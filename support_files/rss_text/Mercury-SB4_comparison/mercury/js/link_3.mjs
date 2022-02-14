import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/europe/comments/saojtp/reconstructed_8th_century_viking_hall_in_lejre/'
Mercury.parse(url).then(result => console.log(result))