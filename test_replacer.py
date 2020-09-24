import replacer
import pytest


def test_replace_links():
    content = '<a href="https://dou.ua/lenta/">Лента</a>'
    new_content = replacer.replace_links(content)
    assert new_content == '<a href="http://127.0.0.1:8888/lenta/">Лента</a>'


@pytest.mark.xfail(reason="Reason: not tag in content")
def test_replace_text_xfail():
    content = 'sixsix sevense six_si six111 Свежее'
    new_content = replacer.modify_content(content)
    assert new_content == 'sixsix™ sevense six_si six111 Свежее™'


def test_replace_text_1():
    content = '<p>sixsix sevense six_si six111 Свежее</p>'
    new_content = replacer.modify_content(content)
    assert new_content == '<p>sixsix™ sevense six_si six111 Свежее™</p>'


def test_replace_text_2():
    content = '<p>Всем привет. Случилась очень неприятная ситуация, и&nbsp;данной темой хотел предупредить остальных об&nbsp;очередных новых идеях этого оператора о&nbsp;том как нагреть.</p>'
    new_content = replacer.modify_content(content)
    assert new_content == '<p>Всем привет™. Случилась очень неприятная ситуация, и&nbsp;данной™ темой хотел предупредить остальных об&nbsp;очередных новых идеях этого оператора о&nbsp;том как нагреть.</p>'


def test_modify_content():
    content = '<p>sixsix sevense six_si six111 Свежее</p><a href="https://dou.ua/lenta/">Лента</a>'
    new_content = replacer.modify_content(content)
    assert new_content == '<p>sixsix™ sevense six_si six111 Свежее™</p><a href="http://127.0.0.1:8888/lenta/">Лента</a>'
