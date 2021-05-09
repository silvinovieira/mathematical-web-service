import pytest

from app import app
from resources import Fibonacci


class TestFibonacci:
    @pytest.fixture()
    def test_client(self):
        return app.test_client()

    def test_get_when_n_is_non_negative_int_return_ok(self, test_client):
        response = test_client.get('/api/fibonacci?n=2')
        assert response.status_code == 200

    def test_get_when_n_is_not_an_int_return_bad_request(self, test_client):
        response = test_client.get('/api/fibonacci?n=test')
        assert response.status_code == 400

    def test_calculate_fib_0(self):
        nth = Fibonacci.calculate(0)
        assert nth == 0

    def test_calculate_fib_1(self):
        nth = Fibonacci.calculate(1)
        assert nth == 1

    def test_calculate_fib_20(self):
        nth = Fibonacci.calculate(20)
        assert nth == 6765

    def test_calculate_fib_40(self):
        nth = Fibonacci.calculate(40)
        assert nth == 102334155
