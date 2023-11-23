studenti = {'Petr': [80, 90, 85], 'Anna': [75, 80, 82], 'Tomáš': [90, 92, 80]}

common_grades = set.intersection(*(set(známky) for známky in studenti.values()))

if common_grades:
    print(f"Známka, kterou mají studenti společnou je {common_grades.pop()}")
else:
    print("Studenti nemají žádnou společnou známku.")