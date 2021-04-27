import pytest

# Will use another decorator for each fixture definiton
# These can be as complex as you want!
# There are plugins that can be used that have pre-defined fixtures
# for certain packages (e.g. django)
@pytest.fixture
def my_fixture():
    return 42