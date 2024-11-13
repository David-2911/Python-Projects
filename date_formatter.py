def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if len((date.split(' ', 1)[0])) > 3 and date[-5] == ' ':
                month, day, year = date.split(" ")
                if month in months:
                    m = months.index(month) + 1
                d = day.replace(",", "")
                if int(d) < 32 and m < 13 and d.isdigit() and year.isdigit() and ',' in day:
                    print(f"{year}-{int(m):02}-{int(d):02}")
                    break
                else:
                    print(end="")

            elif len(date) >= 5 and date[-5] == '/':
                month, day, year = date.split("/")
                if int(day) < 32 and int(month) < 13 and day.isdigit() and month.isdigit() and year.isdigit():
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
                else:
                    print(end="")

            else:
                print(end="")

        except ValueError:
            print(end="")
        except AttributeError:
            print(end="")



if __name__ == '__main__':
    main()