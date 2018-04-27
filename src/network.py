# import flask?
import threading
import miner


class Network(threading.Thread):
    def __init__(self, blockchain, transactions):
        threading.Thread.__init__(self)
        self.blockchain = blockchain
        self.transactions = transactions
        return

    def wait_data(self):
        data = getfromsomewhere()
        if data.type == 'block':
            self.blockchain.append_block(data)
        elif data.type == 'tx':
            self.transactions.append(data)

        return

    def run(self):
        return
