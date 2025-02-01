import matplotlib.pyplot as plt

# Дані про блоки
blocks = [1, 2, 3, 4, 5]
transactions = [15, 25, 18, 40, 30]

plt.bar(blocks, transactions, color='blue')
plt.xlabel("Block Number")
plt.ylabel("Number of Transactions")
plt.title("Transactions per Block")
plt.show()
