from decimal import Decimal
import pytest

from app import app
from resources import Factorial


class TestFactorial:
    @pytest.fixture()
    def test_client(self):
        return app.test_client()

    def test_get_when_n_is_non_negative_int_return_ok(self, test_client):
        response = test_client.get('/api/factorial?n=2')
        assert response.status_code == 200

    def test_get_when_n_is_not_an_int_return_bad_request(self, test_client):
        response = test_client.get('/api/factorial?n=test')
        assert response.status_code == 400

    def test_get_when_n_is_negative_int_return_bad_request(self, test_client):
        response = test_client.get('/api/factorial?n=-2')
        assert response.status_code == 400

    def test_calculate_factorial_0(self):
        nth = Factorial.calculate(0)
        assert nth == 1

    def test_calculate_factorial_1(self):
        nth = Factorial.calculate(1)
        assert nth == 1

    def test_calculate_factorial_10(self):
        nth = Factorial.calculate(10)
        assert nth == 3628800

    def test_calculate_factorial_100(self):
        nth = Factorial.calculate(100)
        assert nth == pytest.approx(9.332621544 * (10 ** 157))
