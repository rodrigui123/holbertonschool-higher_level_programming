#!/usr/bin/node

const args = process.argv.slice(2).length;

if (args.length === 0) {
    console.log("No argument")
} else if (args.length === 3) {
    console.log("Argument found")
} else {
    console.log("Arguments found")
}
