from typing import List

from PyQt5.QtWidgets import QMenu, QAction
from aqt.editor import EditorWebView
from aqt.utils import showInfo

from .kanji_api.api_wrapper import KanjiAPI
from .kanji_api.models import KanjiData
from .kanji_note import create_kanji_note
from .utils import extract_potential_kanji


def will_show_context_hook(editor_webview: EditorWebView, menu: QMenu):
    selected_text = editor_webview.selectedText()
    if not selected_text:
        return

    potential_kanji_s = extract_potential_kanji(selected_text)
    if not potential_kanji_s:
        return

    menu_text = 'Create Note from Kanji' if len(selected_text) == 1 else 'Create Note from extracted Kanji'

    action: QAction = menu.addAction(menu_text)
    action.triggered.connect(lambda: handle_note_creation(potential_kanji_s))


def handle_note_creation(potential_kanji_s: List[str]):
    for char in potential_kanji_s:
        kanji_data: KanjiData = KanjiAPI().get_kanji(char)
        if kanji_data is None:
            showInfo(f'No Data found for: {char}')
            continue

        note = create_kanji_note(kanji_data)
        if note:
            showInfo(f'Created Note: {note.values()[0]}')
