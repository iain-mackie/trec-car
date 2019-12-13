
import pytest

@pytest.fixture()
def test_string_unformatted():
    return 'Hi $1 my /  name, 1,000  ??as is Iain Mackie'

@pytest.fixture()
def test_string_formatted():
    return ['hi', '1',  'name', '1,000',  'iain', 'mackie']

@pytest.fixture()
def test_documents():
    return [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]

@pytest.fixture()
def test_query():
    return ["windy london"]

@pytest.fixture()
def most_relevant_document():
    return [['It is quite windy in London']]
