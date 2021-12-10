function compiler(input, output) {
  const { exec, execSync } = require('child_process');

  execSync(`npx babel ${input} --out-file ${output}`);
}

module.exports = compiler;
