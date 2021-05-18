'use strict';
const RippleAPI = require('ripple-lib').RippleAPI;

const api = new RippleAPI({
  server: 'wss://s1.ripple.com' // Public rippled server
});
api.connect().then(() => {
  /* begin custom code ------------------------------------ */
  const myAddress = 'rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn';

  console.log('getting account info for', myAddress);


  return api.getTransaction("7327873A5CD5DD08BCD06C1293C152456DBFAF2FF42FD9627E5D9727C939801A")

}).then(info => {
  console.log(info);
  console.log('getAccountInfo done');

  /* end custom code -------------------------------------- */
}).then(() => {
  return api.disconnect();
}).then(() => {
  console.log('done and disconnected.');
}).catch(console.error);