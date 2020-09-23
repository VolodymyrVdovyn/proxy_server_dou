import regex as re


find_text = re.compile('(<[^>]+?>)([^<]+)', re.IGNORECASE)
find_6_char_words = re.compile('([^\p{Cyrillic}a-z_]|\A)([\p{Cyrillic}a-z]{6})([^\p{Cyrillic}a-z_]|\Z)', re.IGNORECASE)
find_links = re.compile('(<\s*a[^>]*href=\")https://dou.ua([^\"]*)', re.IGNORECASE)


def modify_content(content):
    return replace_text(replace_links(content))


def replace_6_char_words(data):
    return data[1] + find_6_char_words.sub('\g<1>\g<2>™\g<3>', data[2])


def replace_text(content):
    return find_text.sub(replace_6_char_words, content)


def replace_links(content):
    return find_links.sub('\g<1>http://127.0.0.1:8888\g<2>', content)
