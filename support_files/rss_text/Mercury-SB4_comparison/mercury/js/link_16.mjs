import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/europe/comments/saoc6p/snow_depth_in_europe_23012022_7_am_cet/'
Mercury.parse(url).then(result => console.log(result))