# ----------------------------------------------------------------------
# C1. Saraksta kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar sešiem skaitļiem. Izvadi to skaitu, summu, vidējo, lielāko un mazāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā skaitļus, nosauc ar vārdu vertibu_kopa.


saraksts = []

for i in range(6):
    a = int(input("Ievadi skaitli: "))
    saraksts.append(a)

print("Saraksta garums ir",len(saraksts),"cipari")
print("Saraksta summa ir",sum(saraksts))
print("Saraksta vidējais aritmētiskais ir",sum(saraksts) / len(saraksts))
lielakais = max(saraksts)
print("Lielākais skaitlis sarakstā ir",lielakais)
mazakais = min(saraksts)
print("Mazākais skaitlis sarakstā ir",mazakais)