from typing import Tuple

from anki import notes
from anki.models import NoteType
from anki.utils import stripHTML
from aqt import mw
from aqt.editor import Editor

from .config import CONFIG
from .kanji_api.api_wrapper import KanjiAPI
from .kanji_api.models import KanjiData
from .kanji_note import fill_kanji_note_fields
from .utils import add_tags_to_note, is_potential_kanji


def unfocused_field_hook(changed: bool, note: notes.Note, current_field_idx: int):
    if not (is_configured_note_type(note) and is_configured_field(note, current_field_idx) and do_not_skip(note)):
        return

    current_field: Tuple[str, str] = note.items()[current_field_idx]

    char: str = current_field[1]
    char = stripHTML(char)
    if not char or not is_potential_kanji(char):
        return

    kanji_data: KanjiData = KanjiAPI().get_kanji(char)
    if kanji_data is None:
        return

    fill_kanji_note_fields(note, kanji_data)
    add_tags_to_note(note, CONFIG.addTags)
    refresh_current_view()


def is_configured_note_type(note: notes.Note):
    note_type: NoteType = note.note_type()
    note_type_name: str = note_type['name']
    return note_type_name in CONFIG.noteTypes


def is_configured_field(note: notes.Note, current_field_idx: int):
    current_field_name: str = note.keys()[current_field_idx]
    return current_field_name == CONFIG.field_kanji


def do_not_skip(note: notes.Note):
    return not any(note.has_tag(t) for t in CONFIG.skipTags)


def refresh_current_view():
    if hasattr(mw.app.activeWindow(), 'editor'):
        editor: Editor = mw.app.activeWindow().editor
        editor.loadNote()
