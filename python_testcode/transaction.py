from ripple_api import RippleRPCClient
from Naked.toolshed.shell import execute_js, muterun_js

# module supports authentication as well
rpc = RippleRPCClient("https://s.altnet.rippletest.net:51234")
account_info = rpc.account_info("rJCY77e8XGgrzXfV3m9JtWGxG4tT3vYupJ")


class Transaction_client:
    def __init__(self, address, secret):
        self.address = address
        self.secret = secret
        self.rpc = RippleRPCClient("https://s.altnet.rippletest.net:51234")

    def account_info(self):
        return self.rpc.account_info(self.address)

    def write_tx(self, identifier, message):
        tx = '{"TransactionType": "Payment","Account": self.address,"Destination": self.address,"Memos": [{"Memo": {"MemoType": identifier,"MemoData": message,},}],"Amount": "1",}
        respones = muterun_js(
            "../ripple_testcode/tx.js", arguments=f"adf, {self.secret}"
        )
        if respones.exitcode == 0:
            print(respones.stdout.decode("utf-8"))
        else:
            print(respones.stderr)


if __name__ == "__main__":
    t1 = Transaction_client(
        "r3gLyZD2STeqDgx6ZCz8wnywLTnnrbFwoP", "sscdcSzQxsCRL4thqehit2yJYDyDr"
    )

    t2 = Transaction_client(
        "rPZfvCFpV2ye4Fn9tZv3nHPnh356UmydQE", "ssgb6j6J9ELPQHdDWiNJ46d9NQbXc"
    )

    t1.write_tx("asdf", "def")
