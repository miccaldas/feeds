import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://doordash.engineering/2020/06/29/doordashs-new-prediction-service/'
Mercury.parse(url, { contentType: 'html' }).then(result => console.log(result))
