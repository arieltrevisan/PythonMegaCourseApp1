import helpers as h

print("Welcome to App1")

suggested_word = None
data = h.load_data()

while True:
    word = h.read_word(suggested_word)

    if word == h.exit_keyword:
        break

    definitions = h.get_definitions(word, data)

    suggestions = h.get_suggestions(word, data, definitions)

    best_suggestion = h.get_best_suggestion(word, suggestions)

    suggested_word = h.display_definitions(word, definitions, best_suggestion)
