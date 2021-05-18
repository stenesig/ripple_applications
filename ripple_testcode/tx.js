const RippleAPI = require('ripple-lib').RippleAPI;

var myargs = process.argv.splice(2);

const api = new RippleAPI({
    server: 'wss://s1.ripple.com' // Public rippled server
});
api.connect().then(() => {
    /* begin custom code ------------------------------------ */
    //const txJSON = '{"TransactionType": "Payment","Account": "r3gLyZD2STeqDgx6ZCz8wnywLTnnrbFwoP","Destination": "r3gLyZD2STeqDgx6ZCz8wnywLTnnrbFwoP","Memos": [{"Memo": {"MemoType": "type","MemoData": "data"}}],"Amount": "1"}';
    const txJSON = '{"Flags":2147483648,"TransactionType":"AccountSet","Account":"r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59","Domain":"726970706C652E636F6D","LastLedgerSequence":8820051,"Fee":"12","Sequence":23, "Memo": {"MemoType": "test"}}';
    const secret = 'sscdcSzQxsCRL4thqehit2yJYDyDr';
    return api.sign(txJSON, secret);

}).then(info => {
    console.log(info);

    /* end custom code -------------------------------------- */
}).then(() => {
    return api.disconnect();
}).then(() => {
}).catch(console.error);