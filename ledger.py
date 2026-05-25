import hashlib
import datetime
import json


# ---------------- BLOCK ---------------- #
class Block:
    def __init__(self, index, data, previous_hash, difficulty=4):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    # 🔐 SHA-256 hash calculation
    def calculate_hash(self):
        text = (
            str(self.index)
            + self.timestamp
            + json.dumps(self.data, sort_keys=True)
            + self.previous_hash
            + str(self.nonce)
        )
        return hashlib.sha256(text.encode()).hexdigest()

    # ⛏️ PROOF OF WORK (MINING)
    def mine_block(self):
        target = "0" * self.difficulty

        while True:
            hash_value = self.calculate_hash()

            if hash_value.startswith(target):
                return hash_value

            self.nonce += 1


# ---------------- BLOCKCHAIN ---------------- #
class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty   # ✅ FIXED (must be FIRST)
        self.chain = [self.create_genesis_block()]
        self.nodes = set()

    # Genesis block
    def create_genesis_block(self):
        return Block(0, {"type": "GENESIS"}, "0", self.difficulty)

    # Get latest block
    def get_latest_block(self):
        return self.chain[-1]

    # Add new block
    def add_block(self, data):
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=self.get_latest_block().hash,
            difficulty=self.difficulty
        )
        self.chain.append(new_block)

    # 🔍 VALIDATION (tamper detection)
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # check data integrity
            if current.hash != current.calculate_hash():
                return False

            # check chain link
            if current.previous_hash != previous.hash:
                return False

        return True

    # 🌐 NODE SYSTEM (simulation)
    def add_node(self, node_name):
        self.nodes.add(node_name)

    def get_nodes(self):
        return list(self.nodes)

    # 💾 SAVE BLOCKCHAIN
    def save(self, filename="blockchain.json"):
        data = []

        for b in self.chain:
            data.append({
                "index": b.index,
                "timestamp": b.timestamp,
                "data": b.data,
                "previous_hash": b.previous_hash,
                "nonce": b.nonce,
                "hash": b.hash
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    # 📂 LOAD BLOCKCHAIN
    def load(self, filename="blockchain.json"):
        with open(filename, "r") as f:
            data = json.load(f)

        self.chain = []

        for b in data:
            block = Block(
                b["index"],
                b["data"],
                b["previous_hash"],
                self.difficulty
            )
            block.timestamp = b["timestamp"]
            block.nonce = b["nonce"]
            block.hash = b["hash"]
            self.chain.append(block)