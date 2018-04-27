import block

class BlockChain:
    blocks = []

    def __init__(self, genesis=None):
        #self.height = 0
        self.leaves = []
        self.top = getGenesis() if genesis is None else genesis

    def find(self, value):
        for b in self.blocks:
            if b.hash == value:
                return b
        return None

    # append a block to chain
    def append_block(self, block):
        if block.verify() is False:
            return
        parent = self.find(block.parent)
        if parent is None:
            return
        parent.children.append(block)

        self.leaves.remove(parent.hash)
        self.leaves.append(block.hash)
        self.blocks.append(block)
        return

    # append a list of blocks to chain
    def append_blocks(self, blocks):
        for b in blocks:
            self.append_block(b)
        return

    # find longest chain and return the block
    def find_longest(self):
        max_leng = 0

        for leaf in self.leaves:
            leng = 1
            while leaf is not self.top:
                leng += 1
            max_leng = max(max_leng, leng)
        return max_leng

    def get_budget(self):
        return
