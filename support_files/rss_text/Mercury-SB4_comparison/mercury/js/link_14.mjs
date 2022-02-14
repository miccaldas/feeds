import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/commandline/comments/s8x504/learning_scim_spreadsheet_calculator_improvised/'
Mercury.parse(url).then(result => console.log(result))