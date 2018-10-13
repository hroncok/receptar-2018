import os.path
import sys


def nacti_recept(jmeno):
    """
    Když této funkci dáš jméno textového souboru ze složky recepty,
    tak vrátí text receptu jako řetězec.
    """
    tenhle_script = __file__
    adresar_projektu = os.path.dirname(tenhle_script)
    adresar_receptu = os.path.join(adresar_projektu, 'recepty')
    cesta_k_receptu = os.path.join(adresar_receptu, jmeno)
    try:
        with open(cesta_k_receptu, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        sys.exit('Bohuzel soubor s receptem neexistuje: {}'.format(cesta_k_receptu))


NAZVY_RECEPTU = [
    'chlebova_pochoutka.txt', "babovka.txt", "bramboraky.txt", "krupicova_kase.txt", "milky_shake", "naDobrouNaladu", "palacinky.txt", "pivo.txt", "puding.txt", "rosti.txt", "tajny_recept.txt", "thajka_kureci_polevka.txt", "zeleny_caj.txt"
]


# Máme zatím jen jeden recept, tak ho prostě ukážeme
for i in NAZVY_RECEPTU:
    print(nacti_recept(i))
