import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/commandline/comments/s9srtu/i_turned_my_personal_website_into_an_os_with_a/'
Mercury.parse(url).then(result => console.log(result))