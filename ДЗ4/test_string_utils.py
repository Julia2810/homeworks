from string_utils import StringUtils
import pytest

stringUtils = StringUtils()


# проверка валидных данных, делает первую букву заглавной
@pytest.mark.parametrize('string, new_string', [("word", "Word"), ("слово", "Слово"), ("WORD", "WORD"), ('$%!@&', '$%!@&')])
def test_low_word(string, new_string):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == new_string

# проверка невалидных данных, делает первую букву заглавной
def test_negative_low_word():
    stringUtils = StringUtils()
    with pytest.raises(AttributeError):
        stringUtils.capitilize(12345)





# убирает пробел вначале строки, валидные данные
@pytest.mark.parametrize('string, new_string', [(' word', 'word'), (' WORD', 'WORD'), (' word ', 'word '), (' слово', 'слово'), (' 12345', '12345'), ('', ''), (' ', '')])
def test_positive_space_word(string, new_string):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == new_string

# убирает пробел вначале строки, невалидные данные
def test_negative_space_word():
    stringUtils = StringUtils()
    with pytest.raises(AttributeError):
        stringUtils.trim( 12345)
    
    
    


# убирает разделители, возвращает список строк
@pytest.mark.parametrize('string, delimiter, list', [('1:2:3:4', ':', ["1", "2", "3", "4"]), ('1,2,3,4', ',', ["1", "2", "3", "4"])])
def test_to_list(string, delimiter, list):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimiter)
    assert res == list





# Возвращает `True`, если строка содержит искомый символ
@pytest.mark.parametrize('string, symbol', [("Word", "o"), ("Word", "or"), ("12345", "34")])
def test_positive_symbol(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == True

# Возвращает `False`, если строка не содержит искомый символ
@pytest.mark.parametrize('string, symbol', [("Word", "i")])
def test_negative_symbol(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == False





# Удаляет все подстроки из переданной строки
@pytest.mark.parametrize('string, symbol, result', [("Tester", "er", "Test"), ("Tes ter", " ", "Tester"), ("Tes-ter", "-", "Tester")])
def test_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result





# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
@pytest.mark.parametrize('string, symbol', [("Start", "S"), ("12345", "12")])
def test_positive_starts_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == True

# Возвращает `False`, если строка не начинается с заданного символа
@pytest.mark.parametrize('string, symbol', [("Start", "W"), ("Start", " ")])
def test_negative_starts_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == False





# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
@pytest.mark.parametrize('string, symbol', [("Start", "t")])
def test_positive_end_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == True

# Возвращает `False`, если строка не заканчивается заданным символом
@pytest.mark.parametrize('string, symbol', [("Start", "r"), ("Start", ".")])
def test_negative_end_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == False





# Возвращает `True`, если строка пустая
@pytest.mark.parametrize('string', [(" ")])
def test_positive_is_empty(string):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == True

# Возвращает `False`, если строка не пустая
@pytest.mark.parametrize('string', [("Start")])
def test_negative_is_empty(string):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == False





# Преобразует список элементов в строку с указанным разделителем
@pytest.mark.parametrize('list, joiner, string',[(["New", "York"], ":", "New:York"), (["New", "York"], "-", "New-York"),(["New", "York"], ";", "New;York"), (["New", "York"], ",", "New,York")])
def test_list_to_string(list, joiner, string):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(list, joiner)
    assert res == string
    
