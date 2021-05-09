import pytest

from app import app
from resources import Ackermann


class TestAckermann:
    @pytest.fixture()
    def test_client(self):
        return app.test_client()

    def test_get_when_m_and_n_are_non_negative_int_return_ok(self, test_client):
        response = test_client.get('/api/ackermann?m=3&n=2')
        assert response.status_code == 200

    def test_get_when_m_is_not_an_int_return_bad_request(self, test_client):
        response = test_client.get('/api/ackermann?m=test&n=2')
        assert response.status_code == 400

    def test_get_when_n_is_not_an_int_return_bad_request(self, test_client):
        response = test_client.get('/api/ackermann?m=3&n=test')
        assert response.status_code == 400

    def test_get_when_m_is_negative_return_bad_request(self, test_client):
        response = test_client.get('/api/ackermann?m=-3&n=2')
        assert response.status_code == 400

    def test_get_when_n_is_negative_return_bad_request(self, test_client):
        response = test_client.get('/api/ackermann?m=3&n=-2')
        assert response.status_code == 400

    def test_calculate_ackermann_0_0(self):
        res = Ackermann.calculate(0, 0)
        assert res == 1

    def test_calculate_ackermann_0_1(self):
        res = Ackermann.calculate(0, 1)
        assert res == 2

    def test_calculate_ackermann_1_0(self):
        res = Ackermann.calculate(1, 0)
        assert res == 2

    def test_calculate_ackermann_3_4(self):
        res = Ackermann.calculate(3, 4)
        assert res == 125
