"""
projekt_1_textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Kirill Sedov
email: kirillsedov71@gmail.com
discord: Kirill S.#4670
"""

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'}
username = input('Enter your username: ')
password = input('Enter your password: ')
print(f'{"-" * 50}')
if username in users and password == users[username]:
    print(f'Welcome to the app, {username}, \nWe have 3 texts to be analyzed.')
    print(f'{"-" * 50}')
    number = int(input('Enter a number btw. 1 and 3 to select: '))
    print(f'{"-" * 50}')
    if 1 <= number <= len(texts):
        number_of_text = texts[number - 1]
        print(f'There are {len(number_of_text.split())} words in the selected text.')
    else:
        print("Unregistered text")
    words = number_of_text.split()
    title_words = 0
    for w in words:
        if w.istitle():
            title_words += 1
    print(f'There are {title_words} titlecase words.')
    upper_words = 0
    for w in words:
        if w.isalpha() and w.isupper():
            upper_words += 1
    print(f'There are {upper_words} uppercase words.')
    lower_words = 0
    for w in words:
        if w.isalpha() and w.islower():
            lower_words += 1
    print(f'There are {lower_words} lowercase words.')
    numbers = 0
    for n in words:
        if n.isdigit():
            numbers += 1
    print(f'There are {numbers} numeric strings')
    sum_numbers = 0
    for s in words:
        if s.isdigit():
            sum_numbers += int(s)
    print(f'The sum of all the numbers {sum_numbers}')
    print(f'{"-" * 50}')
    len_of_words_list = []
    for w in words:
        len_of_words_list.append(len(w))
    len_of_words_set = set(len_of_words_list)
    repeated_len = {}
    for x in len_of_words_list:
        repeated_len[x] = len_of_words_list.count(x)
    print(f'{"LEN|":<10} {"OCCURANCES":<20} {"|NR.":<10}')
    print(f'{"-" * 50}')
    for x in len_of_words_set:
        print(f'|{x:<10}|{"*" * repeated_len[x]:<20}|{repeated_len[x]:<10}')

else:
    print('Unregistered user, terminating the program..')
