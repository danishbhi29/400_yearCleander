import calendar

def display_year_calendar(year):
    if 1601 <= year <= 2000:
        print(f"\n📅 Calendar for the Year: {year}\n")
        for month in range(1, 13):
            print(calendar.month(year, month))
    else:
        print("❌ Please enter a year between 1601 and 2000.")

def main():
    print("=== 400 Years Calendar ===")
    try:
        year = int(input("Enter a year between 1601 and 2000: "))
        display_year_calendar(year)
    except ValueError:
        print("❌ Invalid input. Please enter a numeric year.")

if __name__ == "__main__":
    main()
