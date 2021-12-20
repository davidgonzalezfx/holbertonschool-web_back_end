import handleResponseFromAPI from './2-then';

const promise = Promise.resolve();
const p = handleResponseFromAPI(promise);
console.log(p);
