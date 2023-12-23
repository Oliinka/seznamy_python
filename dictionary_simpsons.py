oblibeneVeci= {
    'homer': 'koblihy',
    'marge': 'trouba',
    'bart': 'prak',
    'lisa': 'saxofon',
    'maggie': 'dudlik'
}

print("Homer má rád " + oblibeneVeci['homer'])


keys_list = list(oblibeneVeci.keys())
# Get the key from the middle (assuming the dictionary has at least one key)
middle_index = len(keys_list) // 2
middle_key = keys_list[middle_index]

print(f"{middle_key} má rád {oblibeneVeci[middle_key]}")

keys_list = list(oblibeneVeci.keys())
print(keys_list[0])  # Prints the first key
print(keys_list[1])  # Prints the second key

print(oblibeneVeci.get('homer'))
print(oblibeneVeci.get('krusty'))
print(oblibeneVeci.get('krusty', 'nikdo'))