from typing import Optional

from anki import notes
from anki.collection import SearchNode
from aqt import mw
from aqt.utils import showInfo

from .config import CONFIG
from .kanji_api.models import KanjiData
from .utils import try_set_field, add_tags_to_note


def create_kanji_note(kanji_data: KanjiData) -> Optional[notes.Note]:
    card_type = mw.col.models.by_name(CONFIG.targetNoteType)
    deck_id = mw.col.decks.id(CONFIG.targetDeck, create=False)

    if None in [card_type, deck_id]:
        return None

    # check if note with kanji already exists
    nids = mw.col.find_notes(
        mw.col.build_search_string(kanji_data.kanji, SearchNode(
            field_name=CONFIG.field_kanji,
            deck=CONFIG.targetDeck
        ))
    )

    if nids:
        showInfo(f'Note {kanji_data.kanji} already exists')
        return

    note = mw.col.new_note(card_type)

    fill_kanji_note_fields(note, kanji_data)
    add_tags_to_note(note, [*CONFIG.addTags, CONFIG.targetTag])

    mw.col.add_note(note, deck_id)

    return note


def fill_kanji_note_fields(note: notes.Note, kanji_data: KanjiData):
    try_set_field(note, CONFIG.field_kanji, kanji_data.kanji)
    try_set_field(note, CONFIG.field_kun_yomi, '、'.join(kanji_data.kun_yomi))
    try_set_field(note, CONFIG.field_on_yomi, '、'.join(kanji_data.on_yomi))
    try_set_field(note, CONFIG.field_english, ', '.join(kanji_data.meanings))
    try_set_field(note, CONFIG.field_jlpt, kanji_data.jlpt)
    try_set_field(note, CONFIG.field_grade, kanji_data.grade)
    try_set_field(note, CONFIG.field_stroke_count, kanji_data.stroke_count)
