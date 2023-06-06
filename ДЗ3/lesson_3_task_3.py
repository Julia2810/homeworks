from address import Address
from mailing import Mailing

to_address = Address(440001, 'Москва', 'Ленина', 3, 56)
from_address = Address(880001, 'Ижевск', 'Калинина', 6, 45)

my_mailing = Mailing(to_address, from_address, 123565, '123564')


print(f'Отправление: {my_mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {my_mailing.cost} рублей.')
    
    