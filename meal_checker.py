def main():
    # Ask user for time
    clock = input("What is the time? ")
    # Converts from hour format to float
    time = convert(clock)

    if 7 <= time <= 8:
        print("breakfast time") 
    elif 12 <= time <= 13:
        print("lunch time") 
    elif 18 <= time <= 19:
        print("dinner time") 
    else:
        exit()


def convert(time):
    #Converts from 12-hour to 24-hour format
    if time[-4:] == "a.m." or time[-4:] == "p.m.":
        if time[-4:] == "p.m.":
            hours, minutes = time[:-5].split(":")
            hours = int(hours) + 12
            time = str(hours) + ":" + minutes
        else:
            time = time[:-5]

    #Separate to hours and minutes
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    #Return the time in float
    hour_only = hours + minutes / 60
    return hour_only
    

if __name__ == "__main__":
    main()
