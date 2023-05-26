def month_to_season(month):
    1 == 'January'
    2 == 'February'
    3 == 'March'
    4 == 'April'
    5 == 'May'
    6 == 'June'
    7 == 'July'
    8 == 'August'
    9 == 'September'
    10 == 'October'
    11 == 'November'
    12 == 'December'
    
    if month == 1 or month == 2 or month == 12:
        print("Зима")
    elif month == 3 or month == 4 or month == 5:
        print("Весна")
    elif month == 6 or month == 7 or month == 8:
        print("Лето")
    else:
        print("Осень")
month_to_season(10)
    