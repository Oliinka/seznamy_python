"""Zadejte 1. programátora
Jméno: Karel
Programovací jazyky (oddělujte čárkou a mezerou): C#, Swift, Kotlin
Zadejte 2. programátora
Jméno: Lucie
Programovací jazyky (oddělujte čárkou a mezerou): JavaScript, PHP, C#
Zadejte 3. programátora
Jméno: Milan
Programovací jazyky (oddělujte čárkou a mezerou): C, C++, C#

Všechny jazyky: C, C#, C++, JavaScript, Kotlin, PHP, Swift
Společné jazyky: C#

Jazyky, které umí jen Karel: Kotlin, Swift
Jazyky, které umí jen Lucie: JavaScript, PHP
Jazyky, které umí jen Milan: C, C++
"""

programatori = {}

for i in range(1, 4):
    jmeno = input(f"Zadejte {i}. programátora:\n")
    programovaci_jazyky = set(input(f"Programovací jazyky (oddělujte čárkou a mezerou): ").split(", "))
    programatori[jmeno] = programovaci_jazyky

vsechny_jazyky = set.
spolecne_jazyky = set.intersection(*(set(jazyky) for jazyky in programatori.values()))

if spolecne_jazyky:
    print(f"Společné jazyky: {', '.join(spolecne_jazyky)}")
else:
    print("Programátoři nemají žádný společný jazyk.")