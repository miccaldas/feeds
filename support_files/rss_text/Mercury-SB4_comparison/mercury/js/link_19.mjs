import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/europe/comments/san6fq/alles_gute_zum_geburtstag_liechtenstein_the_tiny/'
Mercury.parse(url).then(result => console.log(result))