from typing import Optional, Dict, Any

from aqt import mw

CONFIG_NOTE_TYPES = 'noteTypes'
CONFIG_FIELD_SRC = 'srcField'
CONFIG_DST_MAPPING = 'dstMapping'
CONFIG_DST_MAPPING_FIELD_KUNYOMI = 'kunyomi'
CONFIG_DST_MAPPING_FIELD_ONYOMI = 'onyomi'
CONFIG_DST_MAPPING_FIELD_ENGLISH = 'english'
CONFIG_DST_MAPPING_FIELD_JLPT = 'jlpt'
CONFIG_DST_MAPPING_FIELD_GRADE = 'grade'
CONFIG_DST_MAPPING_FIELD_STROKE_COUNT = 'stroke_count'
CONFIG_SKIP_TAGS = 'skipTags'
CONFIG_ADD_TAGS = 'addTags'


class ConfigWrapper:

    def __init__(self) -> None:
        self.config: Optional[Dict[str, Any]] = mw.addonManager.getConfig(__name__)

        self.noteTypes = self.config.get(CONFIG_NOTE_TYPES, ['Japanese::Kanji'])
        self.field_kanji = self.config.get(CONFIG_FIELD_SRC, 'kanji')
        self.skipTags = self.config.get(CONFIG_SKIP_TAGS, ['kanji_skip'])
        self.addTags = self.config.get(CONFIG_ADD_TAGS, ['kanji_auto_filled'])

        if self.config.get(CONFIG_DST_MAPPING) is not None:
            dst_mapping = self.config.get(CONFIG_DST_MAPPING)
            self.field_kun_yomi = dst_mapping.get(CONFIG_DST_MAPPING_FIELD_KUNYOMI, 'kun_yomi')
            self.field_on_yomi = dst_mapping.get(CONFIG_DST_MAPPING_FIELD_ONYOMI, 'on_yomi')
            self.field_english = dst_mapping.get(CONFIG_DST_MAPPING_FIELD_ENGLISH, 'meanings')
            self.field_jlpt = dst_mapping.get(CONFIG_DST_MAPPING_FIELD_JLPT, 'jlpt')
            self.field_grade = dst_mapping.get(CONFIG_DST_MAPPING_FIELD_GRADE, 'grade')
            self.field_stroke_count = dst_mapping.get(CONFIG_DST_MAPPING_FIELD_STROKE_COUNT, 'stroke_count')
        else:
            self.field_kun_yomi = 'kun_yomi'
            self.field_on_yomi = 'on_yomi'
            self.field_english = 'meanings'
            self.field_jlpt = 'jlpt'
            self.field_grade = 'grade'
            self.field_stroke_count = 'stroke_count'


def is_kanji_note_type():
    pass
