from dataclasses import dataclass
from typing import List


@dataclass
class KanjiData:
    kanji: str
    kun_yomi: List[str]
    on_yomi: List[str]
    meanings: List[str]
    jlpt: int = 0
    grade: int = 0
    stroke_count: int = 0
