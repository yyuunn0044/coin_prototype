import transaction

class block:
    def __init__(self, json_or_dict):
        '''
        hash
        version
        parent
        children
        timestamp
        txs
        balance
        height
        reward
        nonce
        '''
        self.info = json_or_dict
        return

    def verify_block(self):
        return

    def
