#!/usr/bin/node

const args = process.argv.slice(2).map(Number).filter(Number.isInteger);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
