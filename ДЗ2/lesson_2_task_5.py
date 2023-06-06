def month_to_season(month):

    if month in [1, 2, 12]:
        print("Зима")
    elif month in [3, 4, 5]:
        print("Весна")
    elif month in [6, 7, 8]:
        print("Лето")
    else:
        print("Осень")
month_to_season(3)
    