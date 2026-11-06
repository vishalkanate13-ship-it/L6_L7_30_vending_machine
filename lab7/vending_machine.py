def parse_coins(coins_csv):
    if not isinstance(coins_csv, str) or not coins_csv.strip():
        return []

    try:
        coins = [int(c.strip()) for c in coins_csv.split(',')]
        if any(c <= 0 for c in coins):
            return []
        return coins
    except ValueError:
        return []


def slot_position(code):
    if not isinstance(code, str):
        return None

    code = code.strip().upper()

    if len(code) < 2 or not code[0].isalpha() or not code[0].isascii() or not code[0].isalpha():
        return None

    if not code[1:].isdigit():
        return None

    column = int(code[1:])

    if not ('A' <= code[0] <= 'Z') or column < 1:
        return None

    row = ord(code[0]) - ord('A')
    return row, column - 1


def change_due(payment):
    if not isinstance(payment, str):
        return "invalid payment"

    parts = payment.split('/')

    if len(parts) != 2:
        return "invalid payment"

    try:
        paid = int(parts[0].strip())
        price = int(parts[1].strip())
    except ValueError:
        return "invalid payment"

    change = paid - price

    if change < 0 or change % 5 != 0:
        return "invalid payment"

    return str(change // 5) + ' five-coins'

def main():
    print("==== Running parse_coins ====")
    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    result = parse_coins(user_input)
    print("Coins:", result)

    print("\n==== Running slot_position ====")
    user_input = input("Enter a slot code (e.g. B7): ")
    result = slot_position(user_input)
    print("Row and Column:", result)

    print("\n==== Running change_due ====")
    user_input = input("Enter paid/price (e.g. 200/150): ")
    result = change_due(user_input)
    print("Change Due:", result)


if __name__ == "__main__":
    main()