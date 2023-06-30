import hug
import inflect
engine = inflect.engine()


def singular(word: hug.types.text):
    """Return the singular version of the word"""
    return engine.singular_noun(word).lower()


def plural(word: hug.types.text):
    """Return the plural version of the word"""
    return engine.plural(word).lower()


def singular(word: hug.types.text):
    """Return the singular of word, preserving case"""
    return engine.singular_noun(word)


def plural(word: hug.types.text):
    """Return the plural of word, preserving case"""
    return engine.plural(word)
