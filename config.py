from typing import Optional, Dict, Any, Union, List

from aqt import mw

CONFIG_NOTE_TYPES = 'noteTypes'
CONFIG_FIELD_SRC = 'srcField'
CONFIG_SKIP_TAGS = 'skipTags'
CONFIG_ADD_TAGS = 'addTags'
CONFIG_TARGET_DECK = 'targetDeck'
CONFIG_TARGET_NOTE_TYPE = 'targetNoteType'
CONFIG_TARGET_TAG = 'targetTag'

CONFIG_DST_MAPPING = 'dstMapping'
CONFIG_DST_MAPPING_FIELD_KUNYOMI = 'kunyomi'
CONFIG_DST_MAPPING_FIELD_ONYOMI = 'onyomi'
CONFIG_DST_MAPPING_FIELD_ENGLISH = 'english'
CONFIG_DST_MAPPING_FIELD_JLPT = 'jlpt'
CONFIG_DST_MAPPING_FIELD_GRADE = 'grade'
CONFIG_DST_MAPPING_FIELD_STROKE_COUNT = 'strokeCount'


class ConfigWrapper:

    def __init__(self) -> None:
        config: Optional[Dict[str, Any]] = mw.addonManager.getConfig(__name__)

        self.noteTypes = self._get_entry(config, CONFIG_NOTE_TYPES, ['Japanese::Kanji'])
        self.field_kanji = self._get_entry(config, CONFIG_FIELD_SRC, 'kanji')
        self.skipTags = self._get_entry(config, CONFIG_SKIP_TAGS, ['kanji_skip'])
        self.addTags = self._get_entry(config, CONFIG_ADD_TAGS, ['kanji_auto_filled'])
        self.targetDeck = self._get_entry(config, CONFIG_TARGET_DECK, 'Japanese::Kanji')
        self.targetNoteType = self._get_entry(config, CONFIG_TARGET_NOTE_TYPE, 'Japanese::Kanji')
        self.targetTag = self._get_entry(config, CONFIG_TARGET_TAG, 'auto_created')

        dst_mapping = config.get(CONFIG_DST_MAPPING)

        self.field_kun_yomi = self._get_entry(dst_mapping, CONFIG_DST_MAPPING_FIELD_KUNYOMI, 'kun_yomi')
        self.field_on_yomi = self._get_entry(dst_mapping, CONFIG_DST_MAPPING_FIELD_ONYOMI, 'on_yomi')
        self.field_english = self._get_entry(dst_mapping, CONFIG_DST_MAPPING_FIELD_ENGLISH, 'meanings')
        self.field_jlpt = self._get_entry(dst_mapping, CONFIG_DST_MAPPING_FIELD_JLPT, 'jlpt')
        self.field_grade = self._get_entry(dst_mapping, CONFIG_DST_MAPPING_FIELD_GRADE, 'grade')
        self.field_stroke_count = self._get_entry(dst_mapping, CONFIG_DST_MAPPING_FIELD_STROKE_COUNT, 'stroke_count')

    @staticmethod
    def _get_entry(src: Optional[Dict[str, Any]], field_name: str, default: Union[str, List[str]]) -> Union[str, List[str]]:
        if not src:
            return default
        return src.get(field_name, default)


# TODO probably replace with ConfigWrapper singleton
CONFIG = ConfigWrapper()
