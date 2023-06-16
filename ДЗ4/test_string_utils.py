from string_utils import StringUtils
import pytest

stringUtils = StringUtils()


# проверка валидных данных, делает первую букву заглавной
@pytest.mark.parametrize('string, new_string', [("word", "Word"), ("слово", "Слово"), ("WORD", "WORD"), ('$%!@&', '$%!@&'), ("", ""), (" ", " ")])
def test_positive_low_word(string, new_string):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == new_string

# проверка невалидных данных, делает первую букву заглавной
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, new_string', [(12345, 12345), ([], [])])
def test_negative_low_word(string, new_string):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == new_string





# убирает пробел вначале строки, валидные данные
@pytest.mark.parametrize('string, new_string', [(' word', 'word'), (' WORD', 'WORD'), (' word ', 'word '), (' слово', 'слово'), (' 12345', '12345'), ('', ''), (' ', ''), ('     12345', '12345')])
def test_positive_space_word(string, new_string):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == new_string

# убирает пробел вначале строки, невалидные данные
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, new_string', [(12345, 12345), ([], [])])
def test_negative_spase_word(string, new_string):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == new_string





# убирает разделители, возвращает список строк, валидные данные
@pytest.mark.parametrize('string, delimiter, list', [('1:2:3:4', ':', ["1", "2", "3", "4"]), ('1,2,3,4', ',', ["1", "2", "3", "4"]), ('', '', []), ('1 2 3 4', ' ', ['1', '2', '3', '4']), ('1::2', '::', ['1', '2'])])
def test_positive_to_list(string, delimiter, list):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimiter)
    assert res == list

# убирает разделители, возвращает список строк, невалидные данные
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, delimiter, list', [(None, None, [None])])
def test_negative_to_list(string, delimiter, list):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimiter)
    assert res == list





# Возвращает `True`, если строка содержит искомый символ, валидные данные
@pytest.mark.parametrize('string, symbol', [("Word", "o"), ("Word", "or"), ("12345", "34"), ("", "")])
def test_positive_true_symbol(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == True

# Возвращает `True`, если строка содержит искомый символ, невалидные данные
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol', [(1234, 12)])
def test_negative_true_symbol(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == True


# Возвращает `False`, если строка не содержит искомый символ, валидные данные
@pytest.mark.parametrize('string, symbol', [("Word", "i"), ('1234', '65')])
def test_positive_false_symbol(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == False

# Возвращает `False`, если строка не содержит искомый символ, невалидные данные
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol', [(1234, 65)])
def test_negative_false_symbol(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == False





# Удаляет все подстроки из переданной строки, валидные проверки
@pytest.mark.parametrize('string, symbol, result', [("Tester", "er", "Test"), ("Tes ter", " ", "Tester"), ("Tes-ter", "-", "Tester"), ("", "", ""), (" ", " ", ""), ("Tes---ter", "---", "Tester"), ("12345", "34", "125")])
def test_positive_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result

# Удаляет все подстроки из переданной строки, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol, result', [(None, None, None), (12345, 34, 125)])
def test_negative_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result





# Возвращает `True`, если строка начинается с заданного символа, валидные проверки
@pytest.mark.parametrize('string, symbol', [("Start", "S"), ("12345", "12"), (" Start", " "), ('', '')])
def test_positive_true_starts_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == True

# Возвращает `True`, если строка начинается с заданного символа, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol', [(12345, 12)])
def test_negative_true_starts_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == True


# Возвращает `False`, если строка не начинается с заданного символа, валидные проверки
@pytest.mark.parametrize('string, symbol', [("Start", "W"), ("Start", " ")])
def test_positive_false_starts_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == False

# Возвращает `False`, если строка не начинается с заданного символа, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol', [(12345, 65)])
def test_negative_false_starts_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == False





# Возвращает `True`, если строка заканчивается заданным символом, валидные проверки
@pytest.mark.parametrize('string, symbol', [("Start", "t"), ('Start ', ' '), ('', ''), (' ', ' ')])
def test_positive_true_end_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == True

# Возвращает `True`, если строка заканчивается заданным символом, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol', [(12345, 45)])
def test_negative_true_end_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == True


# Возвращает `False`, если строка не заканчивается заданным символом, валидные проверки
@pytest.mark.parametrize('string, symbol', [("Start", "r"), ("Start", ".")])
def test_positive_false_end_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == False

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string, symbol', [(12345, 98)])
def test_negative_false_end_with(string, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == False





# Возвращает `True`, если строка пустая, валидные проверки
@pytest.mark.parametrize('string', [(" ")])
def test_positive_true_is_empty(string):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == True

# Возвращает `True`, если строка пустая, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string', [(None), (12345)])
def test_negative_true_is_empty(string):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == True


# Возвращает `False`, если строка не пустая, валидные проверки
@pytest.mark.parametrize('string', [("Start")])
def test_positive_false_is_empty(string):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == False

# Возвращает `False`, если строка не пустая, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string', [(None), (1234)])
def test_negative_false_is_empty(string):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == False





# Преобразует список элементов в строку с указанным разделителем, валидные проверки
@pytest.mark.parametrize('list, joiner, string', [(["New", "York"], ":", "New:York"), (["New", "York"], "-", "New-York"), (["New", "York"], ";", "New;York"), (["New", "York"], ",", "New,York"), (["New", "York"], "::", "New::York"), ([" ", " "], "-", " - "), ([], "", "")])
def test_positive_list_to_string(list, joiner, string):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(list, joiner)
    assert res == string

# Преобразует список элементов в строку с указанным разделителем, невалидные проверки
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('list, joiner, string', [([None], None, None)])
def test_negative_list_to_string(list, joiner, string):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(list, joiner)
    assert res == string