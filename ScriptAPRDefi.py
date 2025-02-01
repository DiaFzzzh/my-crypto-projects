def calculate_apr(deposits, earnings, days):
    apr = (earnings / deposits) * (365 / days) * 100
    return apr

if __name__ == "__main__":
    deposits = 1000  # У доларах
    earnings = 50  # Прибуток
    days = 30  # Період інвестування
    print(f"Estimated APR: {calculate_apr(deposits, earnings, days):.2f}%")
