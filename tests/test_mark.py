import pytest


@pytest.mark.skip(reason="Meow")
def test_meow(browser):
    pass


@pytest.mark.skipif('config.getoption("--browser") == "chrome"')
def test_meow2():
    pass
