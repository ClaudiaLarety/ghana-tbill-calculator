import matplotlib.pyplot as plt
from tbill import tbill_interest_rate, ask_number

def growth_chart(amount, discount_rate, fd_rate, days):
    tbill_rate = tbill_interest_rate(discount_rate, days)
    day_range = list(range(0, days + 1))
    tbill_values = [amount * (1 + tbill_rate * d / 364) for d in day_range]
    fd_values = [amount * (1 + fd_rate * d / 365) for d in day_range]

    plt.figure(figsize=(9, 5))
    plt.plot(day_range, tbill_values, label="T-Bill", linewidth=2)
    plt.plot(day_range, fd_values, label="Fixed deposit", linewidth=2)
    plt.title(f"Growth of GH₵{amount:,.0f} over {days} days")
    plt.xlabel("Days")
    plt.ylabel("Value (GH₵)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("growth_chart.png", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    amount = ask_number("Amount to invest (GH₵): ")
    discount_rate = ask_number("T-Bill discount rate (%): ") / 100
    fd_rate = ask_number("Fixed deposit rate (%): ") / 100
    days = int(ask_number("Days (91, 182 or 364): "))
    growth_chart(amount, discount_rate, fd_rate, days)