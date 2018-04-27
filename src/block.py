import transaction

class Block:
    def __init__(self, json_or_dict):
        self.hash = 0
        self.children = []
        '''
        hash
        version
        parent
        timestamp
        bits
        nonce
        children
        txs


        balance
        height
        reward

        '''
        self.info = json_or_dict
        return
    '''    
    def get_hash(self):
        return self.hash

    def get_children(self):
        return self.children

    def add_children(self, block):
        self.children.append(block)
    '''
    def verify(self):
        return

