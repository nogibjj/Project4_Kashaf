import wikipedia
from textblob import TextBlob


def wiki(name="Barack Obama", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search wikipedia for names"""
    results = wikipedia.search(name)
    return results


def phrase(name):
    """Search phrases for wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
