import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/linux/comments/s9isqj/help_tenacity_a_fork_of_audacity_after_its/'
Mercury.parse(url).then(result => console.log(result))