from contextlib import redirect_stdout
from io import StringIO
from src.decorators import log


@log()
def add(a, b):
    return a + b


# Тест на проверку логирования в консоль
def test_success_logging_to_console():
    f = StringIO()
    with redirect_stdout(f):
        result = add(2, 3)
    output = f.getvalue().strip()

    assert result == 5
    assert "Функция add успешно завершена. Результат: 5" in output


def test_log_with_filename():
    @log(filename="mylog_test.txt")
    def my_function(x, y):
        return x + y
    my_function(10, 10)
    with open("mylog_test.txt", "r", encoding='utf-8') as file:
        content = file.read()
        assert content.strip() == 'Функция my_function успешно завершена. Результат: 20'
