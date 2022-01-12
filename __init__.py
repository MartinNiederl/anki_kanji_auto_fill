from aqt import gui_hooks

from .autofill_kanji_data import unfocused_field_hook
from .selection_to_kanji_note import will_show_context_hook

# hook which handles autofill of kanji data
gui_hooks.editor_did_unfocus_field.append(unfocused_field_hook)

# hook which allows kanji note creation from text selection
gui_hooks.editor_will_show_context_menu.append(will_show_context_hook)
