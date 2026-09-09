#en ihan ymmärtänyt tehtävän antoa mutta yritin tehdö siten miten ymmärsin

import random

maksimisilmäluku = int(input("Anna nopan maksimisilmäluku: "))

def nopat(tahko):
    noppa_luku = 0
    while noppa_luku != maksimisilmäluku:
        noppa_luku = random.randint(1, maksimisilmäluku)
        print(f"heitit {noppa_luku}")

    else:
        return

nopat(maksimisilmäluku)