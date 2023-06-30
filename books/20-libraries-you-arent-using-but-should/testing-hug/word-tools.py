import hug
import inflect
engine = inflect.engine()


@hug.get(versions=1)
def singular(word: hug.types.text):
    """Return the singular version of the word"""
    return engine.singular_noun(word).lower()


@hug.get(versions=1)
def plural(word: hug.types.text):
    """Return the plural version of the word"""
    return engine.plural(word).lower()


@hug.get(versions=2)
def singular(word: hug.types.text):
    """Return the singular of word, preserving case"""
    return engine.singular_noun(word)


@hug.get(versions=2)
def plural(word: hug.types.text):
    """Return the plural of word, preserving case"""
    return engine.plural(word)



"""
    Examples:
    ┌[alexkg☮DesktopAlexKG]-(~)
    └> curl "127.0.0.1:8000/v1/singular/?word=Silly%20Walks"
    "silly walk"%   
    
    ┌[alexkg☮DesktopAlexKG]-(~)
    └> curl "127.0.0.1:8000/v1/singular/?word=Crisis"
    "crisi"%
    
    ┌[alexkg☮DesktopAlexKG]-(~)
    └> curl "127.0.0.1:8000/v1/plural/?word=Crisis"
    "crises"% 
"""