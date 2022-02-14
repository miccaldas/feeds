import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/europe/comments/saj0fe/ukraine_to_disconnect_from_power_grid_with/'
Mercury.parse(url).then(result => console.log(result))