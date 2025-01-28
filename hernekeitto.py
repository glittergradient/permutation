#def tulosta_sanoja(a, b, c, d):
    #"""Tulostaa argumenttien a, b, c ja d sisällöt kaikissa
      #mahdollisissa eri järjestyksissä allekkain."""
    #print(a, b, c, d)
    #print(a, b, d, c)
    #print(a, c, b, d)
    #print(c, a, b, d)
    #print(b, c, d, a)
    #print(c, d, a, b)
    #print(d, c, a, b)
    #print(c, a, d, b)

#print()
#tulosta_sanoja("to", "her", "ne", "keit",)

from itertools import permutations

perm = permutations(["to","her","ne","keit"])

#Jokainen item on yksi permutaatio. s on string eli 
#merkkijono (esim "to"). print () luo uuden rivin jokaisen
#itemin eli permutaation jälkeen. end = " " varmistaa, että
#merkkijonot ovat eroteltu välilyönnillä ja itemit eroteltu
#toisistaan, jotta print (s...) ymmärtää milloin lopettaa
#jokainen item, jotta saadaan print() avulla rivinvaihto
#jokaisen itemin/permutaation jälkeen.
for item in list(perm):
    for s in item:
        print(s, end = " ")
    print()

#Permutaatioita on yhteensä 24. Jätin omaksi 
#muistiinpanokseni alkuperäisen koodin.