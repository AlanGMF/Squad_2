from fastapi.testclient import TestClient
from BusterBlock.api.api import app


# test client
client = TestClient(app)


def test_response():
    # request
    res = client.get(url="http://0.0.0.0:8000/getdata")
    # asser if response status == 200
    assert res.status_code == 200
    # asser the response is other than none
    assert res.content != None

if __name__ == '__main__':
    test_response()
