def NumaraVarMi(liste, aranan):
    for numara in liste:
        if numara == aranan:
            return True
    return False

# Testler
numaralar = ["101", "102", "103", "104"]
bos_liste = []

print("=== UYGULAMA 2 TESTLERİ ===")
print("İlk eleman (101):", NumaraVarMi(numaralar, "101"))
print("Son eleman (104):", NumaraVarMi(numaralar, "104"))
print("Olmayan numara (999):", NumaraVarMi(numaralar, "999"))
print("Boş listede arama:", NumaraVarMi(bos_liste, "101"))