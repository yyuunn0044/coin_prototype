import miner
import network
import blockchain
import transaction


class Node:
    def __init__(self):
        self.blockchain = blockchain.BlockChain()
        self.transactions = []
        return

    # make and run threads here
    def start_workers(self):
        miner_thread = miner.Miner(self.blockchain, self.transactions)
        network_thread = network.Network()
        miner_thread.start()
        network_thread.start()
        return

    # process incoming blocks and transactions here
    def serve_forever(self):
        data = self.network.wait_data()
        return


if __name__ == '__main__':
    local_node = Node()
    local_node.start_workers()
    local_node.serve_forever()
