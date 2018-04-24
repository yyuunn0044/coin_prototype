import block
import chain


class miner:
    def __init__(blockchain, transactions):
        self.blockchain = blockchain
        return

    def mine_once(self):
        new_block = block()
        new_block.parent = self.blockchain.longest_top()
        new_block.transactions = transactions.new()
        new_block.기타등등_채우기()

    def mine_forever(self):
        block = {}
        block[기타등등] = 채우기
        while(True):
            block['nonce'] += 1
            blockjson = json.dumps(block)
            if hash(blockjson) < 2 ** (N - blockchain.diff):
                # Publish
