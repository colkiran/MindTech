
import pytest

def test_with_local_fixtures(local_fixtures):
    print("Running with local fixtures......")
    assert True

@pytest.fixture()
def local_fixtures():
    print("Doing local fixture setuo stuff.....")


def test_global_fixtures(global_fixtures):
    print("Running test with global_fixtures.......")