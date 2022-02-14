import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/europe/comments/sar3im/the_geothermal_power_plant_of_larderello_tuscany/'
Mercury.parse(url).then(result => console.log(result))