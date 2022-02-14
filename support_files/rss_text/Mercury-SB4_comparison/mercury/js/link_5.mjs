import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/commandline/comments/s8piyg/json_awareness_in_the_curl_tool/'
Mercury.parse(url).then(result => console.log(result))