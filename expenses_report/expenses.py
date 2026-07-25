import csv


def load_expenses(filename):
    """Load expense data from CSV into a list of dictionaries."""

    expenses = []

    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            expenses.append(row)

    return expenses


def total_spending(expenses):
    """Return total spending across all expenses."""

    total = 0

    for row in expenses:
        total += float(row["amount"])

    return total


def total_by_categories(expenses, categories):
    """Return total spending for selected categories."""

    total = 0

    for row in expenses:
        if row["category"] in categories:
            total += float(row["amount"])

    return total


def total_summary(expenses):
    """Return total spending grouped by category."""

    summary = {}

    for row in expenses:
        category = row["category"]
        amount = float(row["amount"])

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary


def highest_expense(expenses):
    """Return the largest individual expense."""

    highest = {
        "category": "None",
        "amount": 0
    }

    for row in expenses:
        amount = float(row["amount"])

        if amount > highest["amount"]:
            highest["category"] = row["category"]
            highest["amount"] = amount

    return highest


def highest_category(summary):
    """Return the category with the highest total spending."""

    highest = {
        "category": "None",
        "amount": 0
    }

    for category, amount in summary.items():

        if amount > highest["amount"]:
            highest["category"] = category
            highest["amount"] = amount

    return highest


def display_summary(summary):
    """Display category totals."""

    for category, amount in summary.items():
        print(f"{category}: £{amount:.2f}")


def display_menu():
    """Display menu and return user selection."""

    print("\nExpense Report")
    print("----------------")
    print("1. Total spending")
    print("2. Total spending by selected categories")
    print("3. Spending by category")
    print("4. Highest individual expense")
    print("5. Highest spending category")
    print("6. All reports")

    while True:
        try:
            selection = int(input("\nSelect option: "))

            if 1 <= selection <= 6:
                return selection

            print("Please select a number between 1 and 6.")

        except ValueError:
            print("Please enter a number.")


def display_all_reports(total, selected_total, summary,
                        largest_expense, largest_category):

    print("\nExpense Report")
    print("================")

    print("\nTotal spending")
    print("----------------")
    print(f"£{total:.2f}")

    print("\nSelected categories")
    print("-------------------")
    print(f"£{selected_total:.2f}")

    print("\nSpending by category")
    print("--------------------")
    display_summary(summary)

    print("\nHighest individual expense")
    print("-------------------------")
    print(
        f"{largest_expense['category']} "
        f"£{largest_expense['amount']:.2f}"
    )

    print("\nHighest spending category")
    print("------------------------")
    print(
        f"{largest_category['category']} "
        f"£{largest_category['amount']:.2f}"
    )


def main():

    expenses = load_expenses(r"expenses_report\expenses.csv")

    total = total_spending(expenses)

    selected_total = total_by_categories(
        expenses,
        {"Food", "Transport"}
    )

    summary = total_summary(expenses)

    largest_expense = highest_expense(expenses)

    largest_category = highest_category(summary)

    selection = display_menu()

    if selection == 1:
        print(f"\nTotal spending: £{total:.2f}")

    elif selection == 2:
        print(
            f"\nFood and Transport spending: "
            f"£{selected_total:.2f}"
        )

    elif selection == 3:
        print("\nSpending by category")
        display_summary(summary)

    elif selection == 4:
        print(
            f"\nHighest expense: "
            f"{largest_expense['category']} "
            f"£{largest_expense['amount']:.2f}"
        )

    elif selection == 5:
        print(
            f"\nHighest category: "
            f"{largest_category['category']} "
            f"£{largest_category['amount']:.2f}"
        )

    elif selection == 6:
        display_all_reports(
            total,
            selected_total,
            summary,
            largest_expense,
            largest_category
        )


if __name__ == "__main__":
    main()