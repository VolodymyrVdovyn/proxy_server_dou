import pytest
import requests
import threading

import proxy_server as proxy


@pytest.fixture()
def start_server():
    server = proxy.HTTPServer(('127.0.0.1', 8888,), proxy.DouProxyHandler,)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()

    yield

    server.shutdown()


urls_test_list = [
    'http://127.0.0.1:8888/forums/topic/24951',
    'http://127.0.0.1:8888',
    'http://127.0.0.1:8888/forums',
    'http://127.0.0.1:8888/calendar/34286/?from=premiumevents_5779',
]

test_ids = ['Url({})'.format(t) for t in urls_test_list]


@pytest.mark.xfail(reason="Reason: proxy server don't started")
@pytest.mark.parametrize('url', urls_test_list, ids=test_ids)
def test_server_off(url):
    r = requests.get(url)
    assert r.status_code == 200


@pytest.mark.parametrize('url', urls_test_list, ids=test_ids)
def test_server_on(start_server, url):
    r = requests.get(url)
    assert r.status_code == 200
