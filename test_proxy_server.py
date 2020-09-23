import pytest
import requests
import threading

import proxy_server as proxy


urls_test_list = [
    "http://127.0.0.1:8888/forums/topic/24951",
    "http://127.0.0.1:8888",
    "http://127.0.0.1:8888/forums",
    "http://127.0.0.1:8888/calendar/34286/?from=premiumevents_5779",
]

test_ids = ["Url({})".format(t) for t in urls_test_list]


@pytest.mark.xfail(reason="Reason: proxy server don't started")
@pytest.mark.parametrize("url", urls_test_list, ids=test_ids)
def test_server_off(url):
    r = requests.get(url)
    assert r.status_code == 200


@pytest.mark.parametrize("url", urls_test_list, ids=test_ids)
def test_server_on(url):
    r = requests.get(url)
    assert r.status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", "-rx", "--tb=no", str(__file__) + "::" + "test_server_off"])

    server = proxy.HTTPServer(("127.0.0.1", 8888,), proxy.DouProxyHandler,)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()

    pytest.main(["-v", "--tb=no", str(__file__) + "::" + "test_server_on"])

    server.shutdown()
