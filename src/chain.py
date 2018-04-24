import block

class chain:
    def __init__(self, genesis=None):
        if genesis is None:
            self.top = getGenesis()
        else:
            self.top = genesis

    def append_block(self, block):
        # append a block to chain
        return

    def append_blocks(self, blocks):
        # append a list of blocks to chain
        return

    def find_longest(self):
        # find longest chain and return the block
        return

    def get_budget(self):
        return
