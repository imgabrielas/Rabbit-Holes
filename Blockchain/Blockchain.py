import hashlib

class Coins:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        # construct data string
        self.block_data = '---'.join(transaction_list) + '---' + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # how hash will be calculated

# transactions
t1 = 'Matt sends 2 coins to Daniel'
t2 = 'Charlie sends 5 coins to Rubby'
t3 = 'Rubby sends 3.4 coins to Monica'
t4 = 'Monica sends 8 coins to Matt'
t5 = 'Vanessa sends 5 coins to Daniel'
t6 = 'Daniel sends 3 coins to Rubby'

initial_block = Coins('Initial Str', [t1, t2])
second_block = Coins(initial_block.block_hash, [t3, t4])
third_block = Coins(second_block.block_hash, [t5, t6])

# initial block
print(initial_block.block_data)
print(initial_block.block_hash)

# second block is based on initial block - it will have the same hash
print(second_block.block_data)
print(second_block.block_hash)

# third block is based on second block - it will have the same hash
print(third_block.block_data)
print(third_block.block_hash)