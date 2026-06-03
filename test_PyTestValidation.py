import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "fail"


def test_initialCheck(preWork):
    print("This is first test")
    assert preWork == "fail"


def test_secondCheck(preSetupWork):
    print("This is the second test")
