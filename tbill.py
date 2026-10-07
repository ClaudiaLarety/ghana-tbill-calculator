DAYS_IN_YEAR = 364

def tbill_price(discount_rate, days, face_value=100):
    """Price you pay today. discount_rate as a decimal, e.g. 0.25 for 25%."""
    return face_value * (1 - discount_rate * days / DAYS_IN_YEAR)

def tbill_interest_rate(discount_rate, days):
    """Interest rate equivalent: the real annual return."""
    price = tbill_price(discount_rate, days)
    return (100 - price) / price * DAYS_IN_YEAR / days

def tbill_maturity_value(amount, discount_rate, days):
    """Money you receive at maturity for the amount you invest."""
    return amount * 100 / tbill_price(discount_rate, days)

def fixed_deposit_maturity_value(amount, annual_rate, days):
    """Fixed deposit with simple interest over a 365-day year."""
    return amount * (1 + annual_rate * days / 365)

def compare(amount, discount_rate, fd_rate, days):
    tbill = tbill_maturity_value(amount, discount_rate, days)
    fd = fixed_deposit_maturity_value(amount, fd_rate, days)
    winner = "T-Bill" if tbill > fd else "Fixed deposit"
    print(f"Invest: GH₵{amount:,.2f} for {days} days")
    print(f"T-Bill value:        GH₵{tbill:,.2f}")
    print(f"Fixed deposit value: GH₵{fd:,.2f}")
    print(f"Winner: {winner} by GH₵{abs(tbill - fd):,.2f}")

if __name__ == "__main__":
    compare(10000, 0.25, 0.22, 91)