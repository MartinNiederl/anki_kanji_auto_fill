from typing import Tuple, Union, List

from anki import notes
from anki.models import NoteType
from aqt import gui_hooks, mw
from aqt.editor import Editor
from aqt.utils import showInfo

from .config import ConfigWrapper
from .kanji_api.api_wrapper import KanjiAPI
from .kanji_api.models import KanjiData

config = ConfigWrapper()


def is_valid_note_type(note: notes.Note):
    note_type: NoteType = note.note_type()
    note_type_name: str = note_type['name']
    return note_type_name in config.noteTypes


def is_valid_field(note: notes.Note, current_field_idx: int):
    current_field_name: str = note.keys()[current_field_idx]
    return current_field_name in config.srcFields


def do_not_skip(note: notes.Note):
    return not any(note.has_tag(t) for t in config.skipTags)


def unfocused_field(changed: bool, note: notes.Note, current_field_idx: int):
    if not (is_valid_note_type(note) and is_valid_field(note, current_field_idx) and do_not_skip(note)):
        return

    current_field: Tuple[str, str] = note.items()[current_field_idx]

    kanji: str = current_field[1]
    kanji_data = KanjiAPI().get_kanji(kanji)
    # kanji_data = get_kanji_data(current_field[1]) # slow and error prone, deprecated
    if kanji_data is None:
        return

    populate_note_fields(note, kanji_data)
    add_tags_to_note(note, config.addTags)
    refresh_current_view()


def refresh_current_view():
    if hasattr(mw.app.activeWindow(), 'editor'):
        editor: Editor = mw.app.activeWindow().editor
        editor.loadNote()


def add_tags_to_note(note: notes.Note, tags: List[str]):
    if tags:
        for tag in tags:
            note.add_tag(tag)


def populate_note_fields(note: notes.Note, kanji_details: KanjiData):
    try_set_field(note, config.field_kunyomi, '、'.join(kanji_details.kun_yomi))
    try_set_field(note, config.field_onyomi, '、'.join(kanji_details.on_yomi))
    try_set_field(note, config.field_english, ', '.join(kanji_details.meanings))
    try_set_field(note, config.field_jlpt, kanji_details.jlpt)
    try_set_field(note, config.field_grade, kanji_details.grade)
    try_set_field(note, config.field_stroke_count, kanji_details.stroke_count)


def try_set_field(note: notes.Note, field_name: str, value: Union[str, int]):
    if (isinstance(value, str) and len(value) > 0) or (isinstance(value, int) and value != 0):
        try:
            note[field_name] = str(value)
        except KeyError:
            showInfo('failed to set field ' + field_name)
            pass


gui_hooks.editor_did_unfocus_field.append(unfocused_field)
