import pytest
from src.db import Base, engine
from src.config import settings


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print(f"{settings.DB_NAME=}")
    assert settings.MODE == "TEST"
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # Base.metadata.create_all(engine)
    # yield
    # Base.metadata.drop_all(engine)


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        choices=('chrome', 'firefox'),
    )

@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')