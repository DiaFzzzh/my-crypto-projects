from web3 import Web3

# Підключення до Ethereum RPC
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

def monitor_transactions():
    latest_block = web3.eth.block_number
    block = web3.eth.get_block(latest_block, full_transactions=True)
    for tx in block.transactions:
        if tx.gasPrice > Web3.toWei(200, 'gwei'):  # Транзакції з високими комісіями
            print(f"High fee transaction: {tx.hash.hex()}")
            print(f"From: {tx['from']}, To: {tx['to']}, Gas Price: {web3.fromWei(tx.gasPrice, 'gwei')} GWEI")

if __name__ == "__main__":
    monitor_transactions()
