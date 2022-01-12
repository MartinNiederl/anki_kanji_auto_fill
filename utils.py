from typing import List, Union

from anki import notes
from aqt.utils import showInfo

# SOURCE: https://stackoverflow.com/a/30070664/6513167
CJK_RANGES = [
    (ord(u"\u4e00"), ord(u"\u9fff")),  # CJK Unified Ideographs
]


def is_potential_kanji(char: str):
    if len(char) != 1:
        return False
    return any([r[0] <= ord(char) <= r[1] for r in CJK_RANGES])


def extract_potential_kanji(txt: str) -> List[str]:
    return [c for c in list(txt) if is_potential_kanji(c)]


def try_set_field(note: notes.Note, field_name: str, value: Union[str, int]):
    if (isinstance(value, str) and len(value) > 0) or (isinstance(value, int) and value != 0):
        try:
            note[field_name] = str(value)
        except KeyError:
            showInfo('failed to set field ' + field_name)
            pass


def add_tags_to_note(note: notes.Note, tags: List[str]):
    if tags:
        for tag in tags:
            note.add_tag(tag)
