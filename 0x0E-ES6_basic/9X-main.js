// Compiler Module Import

let compiler = require('./compiler');

let input9 = '9-getFullBudget.js';
let output9 = '9-compiled.js';

compiler(input9, output9);

// Replace Reference to Task 7 in Compiled Task 9

let output9Mod = 'X9-compiled.js';
let input7 = '7-getBudgetObject.js';
let output7 = '7-compiled.js';

compiler(input7, output7);

let fs = require('fs');

let str7 = '7-getBudgetObject';
let data = fs.readFileSync(output9, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
let result = data.replace(str7, output7);

fs.writeFileSync(output9Mod, result, 'utf8', function (err) {
  if (err) return console.log(err);
});

// Perform Actual Test

let getFullBudgetObject = require(`./${output9Mod}`).default;

const fullBudget = getFullBudgetObject(20, 50, 10);

console.log(fullBudget.getIncomeInDollars(fullBudget.income));

console.log(fullBudget.getIncomeInEuros(fullBudget.income));

// Remove Compiled Files

fs.unlinkSync(`./${output9}`);
fs.unlinkSync(`./${output7}`);
fs.unlinkSync(`./X${output9}`);
