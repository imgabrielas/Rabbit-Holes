# Blockchain Demo

This project is a simple Python example that demonstrates the basics of blockchain structure and hashing.

## What it does

The `Coins` class represents a block in a blockchain. Each block stores:
- the hash of the previous block
- a list of transactions
- a generated SHA-256 hash based on the block data

Each new block depends on the previous block's hash, which creates a linked chain. This makes it easy to see how data tampering would change the hash and break the chain.

## Run it

```bash
python Blockchain.py
```

The script creates several example blocks and prints their transaction data and computed hashes.

## Files

- `Blockchain.py` — contains the blockchain logic and demo transactions
