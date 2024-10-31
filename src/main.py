
class A:
    def x(self):
        return 1

r'''
pytest
pytest -v
pytest -s (для print)
pytest tests/test_main.py::test_some_fns
pytest tests/test_main.py::TestMain::test_main[1-2-0.5]
pytest --envfile .test.env tests/test_list_1.py (pip install pytest-dotenv)
pytest .\tests\test_mark.py -vv --browser firefox --durations=888 

Пирамида тестирования:
1) Модульное (Unit) (больше всего, не зависят друг от друга, запускаются параллельно)
2) Интеграционное (объединяет в группы модульные тесты, тестирует связи между ними)
3) Сквозное (системное, End-to-End, процесс от начала до конца, меньше всего, дорого писать, могут изменяться)
4) Ручное тестирование (приемочное)
Дешевый вариант пирамиды: 4 -> 3 -> 2 -> 1

File | Settings | Tools | Python Integrated Tools -> Default test runner

Фикстуры:
 - Создают среду для тестирования (запуск и заполнение БД, получение JWT токена, очистка/наполнение кеша)
 - Отдают часто переиспользуемые данные (список моделей для тестирования, данные тестового юзера и т.д.)
'''