from address import Address
from mailing import Mailing

to_address = Address(440001, 'Москва', 'Ленина', 3, 56)
from_address = Address(880001, 'Ижевск', 'Калинина', 6, 45)

my_mailing = Mailing(to_address, from_address, 123565, '123564')


print(f'Отправление: {my_mailing.track} из {my_mailing.from_address.index}, {my_mailing.from_address.city}, {my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} в {my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.street}, {my_mailing.to_address.house} - {my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей.')
    
    