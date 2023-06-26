def note_sup(dic):
    note_sup = max(dic.values())
    for key, value in dic.items():
        if value == note_sup:
            return key
print(note_sup({'a': 10, 'b': 15, 'c': 16, 'd': 11}))