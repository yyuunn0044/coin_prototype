import block
import blockchain
import time
import json
import threading

class Miner(threading.Thread):
    def __init__(self, blockchain, transactions):
        threading.Thread.__init__(self)
        self.blockchain = blockchain
        return

    def mine_forever(self):
        block = {}
        block['hash'] = 0
        block['version'] = 1
        block['parent'] = self.blockchain.longest_top()
        block['timestamp'] = time.time()
        block['bits'] = 0 ## TODO
        block['nonce'] = 0

        while True:
            block['nonce'] += 1
            blockjson = json.dumps(block)
            if hash(blockjson) < 2 ** (N - blockchain.diff):
                # Request Server to publish it
            # check and update longest top

    '''
    def mine_once(self):
        new_block = Block()
        new_block.parent = self.blockchain.longest_top()
        new_block.transactions = transactions.new()
        new_block.기타등등_채우기()
    '''

    def run(self):
        self.mine_forever(self)
