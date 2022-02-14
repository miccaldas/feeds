import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/linux/comments/sardp0/fosdem22_europes_biggest_and_most_famous_free/'
Mercury.parse(url).then(result => console.log(result))