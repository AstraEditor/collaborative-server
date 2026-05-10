import locale

from . import i18n

def get_system_lang() -> str:
    lang, _ = locale.getdefaultlocale()
    return lang if lang else 'en'

def i(id: str) -> str:
    """翻译文本"""
    lang = get_system_lang()
    try:
        result = i18n.I18N[lang][id]
    except KeyError:
        try:
            result = i18n.I18N['en'][id]
        except KeyError:
            result = id
    return result