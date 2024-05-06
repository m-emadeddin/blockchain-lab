import hashlib, rsa, random

class Transaction:
    def __init__(self, sender_public_key, amount, receiver_public_key):
        self.sender_public_key = sender_public_key
        self.amount = amount
        self.receiver_public_key = receiver_public_key

    def get_data(self) -> str:
        return self.sender_public_key.save_pkcs1().decode('utf-8') + str(amount) + '\n' + self.receiver_public_key.save_pkcs1().decode('utf-8')

    def get_hash(self) -> str:
        return hashlib.sha256(self.get_data().encode()).hexdigest()



class Blockchain:
    def __init__(self, init_transaction: Transaction):
        # BLOCK : [Previous HASH, Current HASH, Transaction]
        self.chain = [ ["NULL", init_transaction.get_hash(), init_transaction.get_data()]]        
        print(init_transaction.get_data())

    def add_block(self, transaction: Transaction):
        prev_block = self.chain[-1]
        prev_hash = prev_block[1]
        
        transaction_data = transaction.get_data()
        new_data = transaction_data + prev_hash
        new_hash = hashlib.sha256(new_data.encode()).hexdigest()
        self.chain.append([prev_hash, new_hash, transaction_data])






transactions = []

for i in range(1, 7):
    sender_pub, sender_priv = rsa.newkeys(1 << 10)
    amount = random.randint(1, 50)
    receiver_pub, receiver_priv = rsa.newkeys(1 << 10)
    transaction = Transaction(sender_pub, amount, receiver_pub)
    transactions.append(transaction)


my_chain = Blockchain(transactions[0])

for block in my_chain.chain:
    print(*block, sep='\n')

