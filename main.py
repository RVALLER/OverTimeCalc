def overtimeBonus():
    quotaCompleted = int(input("Enter your submitted quota amount: "))
    quotaAmount = int(input("Enter the requested quota total: "))
    daysUntilDeadline = int(input("Enter the days until your deadline: "))
    Overtime = (((quotaCompleted - quotaAmount) / 5) + (15 * daysUntilDeadline)) - 15
    Overtime = round(Overtime, 0)
    if Overtime < 0:
        Overtime = 0
    OT = f"Your overtime bonus is {Overtime}"
    return OT


def main():
    print(overtimeBonus())


if __name__ == '__main__':
    main()
