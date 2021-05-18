from time import time
from hashlib import sha256


class Publisher:
    def __init__(self, id):
        self.id = id

    def publish(self, identifier, message):
        m = sha256()
        timestamp = time()

        m.update(bytearray(message, "utf-8"))
        m.update(bytearray(str(timestamp), "utf-8"))
        with open("messages.txt", "a+") as f:
            string = f"{self.id},{identifier},{message},{timestamp},{m.hexdigest()}\n"
            f.write(string)
        f.close()


class Subscriber:
    def __init__(self):
        self.subscribtions = []
        self.last_fetch = time()
        self.buffer = []
        self.seen = []

    def subscribe(self, sub):
        self.subscribtions.append(sub)

    def reset_time(self):
        self.last_fetch = time()

    def fetch_new(self):
        with open("messages.txt", "r+") as f:
            l = f.readlines()
            for line in l:
                formatted = line.split(",")
                if formatted[4] not in self.seen and formatted[1] in self.subscribtions:
                    self.buffer.append([formatted[1], formatted[2]])
                    self.seen.append(formatted[4])
        self.reset_time()
        f.close()

    def display(self):
        for item in self.buffer:
            print(f"Subscription: {item[0]}\t|\t{item[1]}")

        self.buffer = []

    def fetch_and_display(self):
        self.fetch_new()
        self.display()


if __name__ == "__main__":
    p = Publisher(5)
    s = Subscriber()

    s.subscribe("fish")

    p.publish("fish", "new trout")
    p.publish("fish", "newer trout")
    p.publish("stock", "gme")
    p.publish("stock", "new trout")
    s.fetch_and_display()

    s.subscribe("stock")

    p.publish("stock", "amc")
    s.fetch_and_display()
