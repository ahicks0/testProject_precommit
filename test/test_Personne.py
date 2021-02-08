import pytest
from datetime import datetime
from src.Personne import Personne


class TestPersonne:
    @pytest.fixture
    def adulte(self):
        return Personne("Marc", 45, datetime.today())

    def test_createPersonne(self, adulte):
        assert str(adulte) == "Nom : Marc, Age: 45"

    def test_Birthday(self, adulte):
        adulte.incrementAge()
        assert adulte.age == 46

    def test_error(self, adulte):
        adulte.rename("Jean")
        with pytest.raises(AssertionError):
            assert adulte.age == "Marc"

    def test_birthday(self, adulte):
        assert adulte.age == 45
        adulte.checkDate()
        assert adulte.age == 46
