from os import linesep as os_linesep
from json import load as json_load
from difflib import get_close_matches

exit_keyword = "q"


def load_data() -> dict:
    return json_load(open("data.json", "r"))


def read_word(suggested_word: str) -> str:
    if suggested_word is None:
        word = input("{}Enter word or phrase (or '{}' to exit):".format(os_linesep, exit_keyword))
    else:
        word = suggested_word
    return word


def get_definitions(word: str, data: dict) -> list:
    word_found = None

    if word in data:
        word_found = word
    elif word.title() in data:
        word_found = word.title()
    elif word.upper() in data:
        word_found = word.upper()

    if word_found is not None:
        return data[word_found]

    return None


def get_suggestions(word: str, data: dict, definitions: list) -> list:
    if not definitions:
        return get_close_matches(word, data.keys())
    return None


def get_best_suggestion(word: str, suggestions: list) -> str:
    # If we did not know suggestions were sorted by match ratio:
    # for s in suggestions:
    #     match = difflib.SequenceMatcher(s, word)
    #     print(match.ratio) # return the word with highest ratio

    # We know suggestions come sorted by match ratio:
    return suggestions[0] if suggestions else None


def display_definitions(word: str, definitions: list, suggestion: str) -> str:
    if definitions:
        print("Found {:d} definition(s) of '{}':".format(len(definitions), word))
        for i, d in enumerate(definitions):
            print("{:2d}. {}".format(i + 1, d))
    else:
        print("No definitions found for '{}'.".format(word), end='')

    use_suggested_word = False
    if suggestion is not None:
        answer = input(" Did you mean '{}'? [Y/n]: ".format(suggestion)).lower()
        use_suggested_word = answer == 'y' or answer == ''

    return suggestion if use_suggested_word else None
