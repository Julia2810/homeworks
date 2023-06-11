from string_utils import StringUtils
import pytest

stringUtils = StringUtils()


# проверка валидных данных, делает первую букву заглавной
@pytest.mark.parametrize('text', [('word'), ('слово'), ('WORD'), ('wORD')])
def test_low_word(text):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(text)
    assert res == text.capitalize()

# проверка невалидных данных, делает первую букву заглавной
@pytest.mark.parametrize('text', [(' '), ('12345'), (' '), ('&!+-'), (12345)])
def test_negative_low_word(text):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(text)
    assert res == text.capitalize()





# убирает пробел вначале строки, валидные данные
@pytest.mark.parametrize('text', [(' word'), (' WORD'), (' word '), (' слово')])
def test_positive_space_word(text):
    stringUtils = StringUtils()
    res = stringUtils.trim(text)
    assert res == text.lstrip()

# убирает пробел вначале строки, невалидные данные
@pytest.mark.parametrize('text', [('word'), (12345), (' '), (' с')])
def test_negative_space_word(text):
    stringUtils = StringUtils()
    res = stringUtils.trim(text)
    assert res == text.lstrip()
    
    
    


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
@pytest.mark.parametrize('string, symbol, result', [("Tester", "er", "Test"), ("Tes ter", " ", "Tester")])
def test_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == str(result)





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
    
