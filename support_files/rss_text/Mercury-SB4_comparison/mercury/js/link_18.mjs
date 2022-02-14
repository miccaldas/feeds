import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/commandline/comments/s9ym9j/looking_for_a_cli_tool_to_draw_a_network_diagram/'
Mercury.parse(url).then(result => console.log(result))