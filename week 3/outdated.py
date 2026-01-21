months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        # Format: MM/DD/YYYY
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        # Format: Month Day, Year
        elif "," in date:
            month_name, rest = date.split(" ", 1)
            day, year = rest.split(",")
            day = int(day)
            year = int(year.strip())

            if month_name not in months:
                raise ValueError

            month = months.index(month_name) + 1

        else:
            raise ValueError

        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        pass
