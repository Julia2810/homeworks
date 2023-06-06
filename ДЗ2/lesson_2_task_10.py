def bank():
    percent = 0.1
    x = int(input("Количество денег: "))
    y = int(input("Срок вклада: "))
    z = x*(1+percent)**y
    print(f'Количество денег в конце срока: {round(z, 2)} рублей')
bank()
    