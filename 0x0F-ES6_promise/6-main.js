import handleProfileSignup from './6-final-user';

console.log(handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg'));

async function asyncReturn() {
  const ret = await handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg');
  console.log(ret);
}

asyncReturn();
