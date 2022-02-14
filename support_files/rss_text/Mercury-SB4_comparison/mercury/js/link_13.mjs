import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://www.reddit.com/r/linux/comments/s9k9we/oc_forx_a_command_line_tool_for_checking_exchange/'
Mercury.parse(url).then(result => console.log(result))