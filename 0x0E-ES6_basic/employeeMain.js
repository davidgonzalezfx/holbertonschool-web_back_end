let compiler = require('./compiler');

let input11 = '11-createEmployeesObject.js';
let output11 = '11-compiled.js';

compiler(input11, output11);

// Replace Reference to Task 7 in Compiled Task 9

let input12 = '12-createReportObject.js';
let output12 = '12-compiled.js';

compiler(input12, output12);

let createEmployeesObject = require(`./${output11}`).default;
let createReportObject = require(`./${output12}`).default;

let engineering = createEmployeesObject('engineering', [
  'John Doe',
  'Guillaume Salva',
]);

let report = createReportObject(engineering);

console.log(report);

let fs = require('fs');

fs.unlinkSync(`./${output11}`);
fs.unlinkSync(`./${output12}`);
