const sinon = require('sinon');
var { expect } = require('chai');

const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('Hooks', function () {
  let spyConsole;
  beforeEach(function () {
    // runs before each test in this block
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(function () {
    // runs after each test in this block
    spyConsole.restore();
  });

  it('logs correctly with 100, 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });

  it('logs correctly with 10, 10', () => {
    sendPaymentRequestToApi(10, 10);

    expect(spyConsole.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });
});
