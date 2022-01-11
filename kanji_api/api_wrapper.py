from typing import Any

import requests

from . import models


class KanjiAPI:
    API_URL = 'https://kanjiapi.dev/v1'

    # def __init__(self) -> None:
    #     self.cache: Dict[str, Any] = {}

    def get_kanji(self, character: str):
        data = self._get_data(f'kanji/{character}')
        if data is None:
            return None

        return models.KanjiData(
            kanji=data['kanji'],
            kun_yomi=data['kun_readings'],
            on_yomi=data['on_readings'],
            meanings=data['meanings'],
            jlpt=data['jlpt'],
            grade=data['grade'],
            stroke_count=data['stroke_count']
        )

    def _get_data(self, route: str) -> Any:
        # if route in self.cache:
        #     return self.cache[route]

        response = requests.get(f'{self.API_URL}/{route}')
        if response.status_code != 200:
            return None

        data = response.json()
        # self.cache[route] = data
        return data

#     getKanji(kanji) {
#         return this._fromCache(`/${KANJI_PATH}/${kanji}`)
#     }
#
#     getReading(reading) {
#         return this._fromCache(`/${READING_PATH}/${reading}`)
#     }
#
#     getJoyoSet() {
#         return this._asSet(this._fromCache(`/${KANJI_PATH}/joyo`))
#     }
#
#     getJinmeiyoSet() {
#         return this._asSet(this._fromCache(`/${KANJI_PATH}/jinmeiyo`))
#     }
#
#     getListForGrade(grade) {
#         return this._asSet(this._fromCache(`/${KANJI_PATH}/grade-${grade}`))
#     }
#
#     getWordsForKanji(kanji) {
#         return this._fromCache(`/${WORDS_PATH}/${kanji}`)
#     }
