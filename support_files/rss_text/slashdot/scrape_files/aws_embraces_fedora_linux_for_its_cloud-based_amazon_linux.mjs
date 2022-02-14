import Mercury from "/home/mic/node_modules/@postlight/mercury-parser/dist/mercury.js";
const url='https://linux.slashdot.org/story/21/11/27/0328223/aws-embraces-fedora-linux-for-its-cloud-based-amazon-linux?utm_source=rss0.9mainlinkanon&utm_medium=feed'
Mercury.parse(url).then(result => console.log(result))