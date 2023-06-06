from address import Address
from mailing import Mailing

class Mailing:
    to_address = ('440001', 'Москва', 'Ленина', 3, 45)
    from_address = ('880001', 'Ижевск', 'Калинина', 6, 84)
    track = 1234567
    cost = 598
    print(f'Отправление {track} из {index}, {city}, {street}, {house} - {apartment} в {index}, {city}, {street}, {house} -{apartment}. Стоимость {cost} рублей.')
    
    