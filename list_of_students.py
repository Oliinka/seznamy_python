studenti = {}

for i in range(1, 4):
    jmeno = input(f"Zadejte jméno {i}. studenta: ")
    znamky = input(f"Známky (oddělujte čárkou a mezerou): ").split(", ")
    znamky = [int(znamka) for znamka in znamky]

    prumer = sum(znamky) / len(znamky)

    studenti[jmeno] = {
        'znamky': znamky,
        'prumer': prumer
    }

for jmeno, data in studenti.items():
    print(f"{jmeno} má průměrnou známku {data['prumer']}")