###
### DEPRECATED: use kanji_api instead
###

import io
import re
import xml.etree.ElementTree as etree
from dataclasses import dataclass
from typing import List

import requests
from requests import Response


@dataclass
class KanjiData:
    kanji: str
    kun_yomi: List[str]
    on_yomi: List[str]
    meaning: str
    jlpt: int = 0
    grade: int = 0
    stroke_count: int = 0


def get_kanji_data(kanji: str) -> KanjiData:
    url = _build_url(kanji)
    html_string = _get_html(url)
    xml_string = _clean_html(html_string)

    with io.open('./tst-2.html', mode='w', encoding='utf-8') as f:
        f.write(xml_string)

    tree = etree.ElementTree(etree.fromstring(xml_string))

    return _extract_data(tree, kanji)


def _build_url(kanji: str):
    return f'https://jisho.org/search/{kanji}%20%23kanji'


def _clean_html(data: str):
    data = re.sub(r'<(script).*?</\1>(?s)', '', data)
    data = re.sub(r'<(head).*?</\1>(?s)', '', data)
    data = re.sub(r'<(header).*?</\1>(?s)', '', data)
    data = re.sub(r'<(footer).*?</\1>(?s)', '', data)
    data = re.sub(r'<(ul).*?</\1>(?s)', '', data)
    data = re.sub(r'<(style).*?</\1>(?s)', '', data)
    data = re.sub(r'<(svg).*?</\1>(?s)', '', data)
    data = re.sub(r'<input[^>]*>', '', data)
    data = re.sub(r'data-[^ >=]+([ >])', r'\1', data)
    data = re.sub(r'<br[^>]*>', '', data)
    data = re.sub("&(?!amp;)", "&amp;", data)

    return data


def _get_html(url: str):
    response: Response = requests.get(url)
    return response.text


def _get_html_from_file(path: str):
    with io.open(path, mode='r', encoding='utf-8') as f:
        data = f.read()

    return data


def _extract_data(tree: etree.ElementTree, kanji: str):
    meanings = ''
    kun_yomi = ''
    on_yomi = ''

    try:
        x1 = ".//div[@class='kanji-details__main-meanings']"
        meanings = tree.find(x1).text.strip()
    except:
        print('could not extract meanings from html')

    try:
        x2 = ".//dl[@class='dictionary_entry kun_yomi']/dd[@class='kanji-details__main-readings-list']/a"
        kun_yomi = [x.text.strip() for x in (tree.findall(x2))]
    except:
        print('could not extract kun_yomi from html')

    try:
        x3 = ".//dl[@class='dictionary_entry on_yomi']/dd[@class='kanji-details__main-readings-list']/a"
        on_yomi = [x.text.strip() for x in (tree.findall(x3))]
    except:
        print('could not extract on_yomi from html')

    return KanjiData(kanji, kun_yomi, on_yomi, meanings)
