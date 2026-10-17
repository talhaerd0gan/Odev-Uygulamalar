def cozumu_bir(ekipman_oduncte_mi=False):
    giris = input("\n[Çözüm 1] Kaç gün süreyle ödünç almak istiyorsunuz?: ")

    if not giris.isdigit():
        print("Reddedildi: Lütfen geçerli bir sayı giriniz!")
    elif int(giris) < 1 or int(giris) > 7:
        print("Reddedildi: Gün sayısı 1 ile 7 arasında olmalıdır!")
    elif ekipman_oduncte_mi:
        print("Reddedildi: Ekipman şu an ödünçte!")
    else:
        print(f"Onaylandı: Ekipman {giris} günlüğüne verildi.")


def cozumu_iki(ekipman_oduncte_mi=False):
    giris = input("\n[Çözüm 2] Kaç gün süreyle ödünç almak istiyorsunuz?: ")

    try:
        gun = int(giris)
    except ValueError:
        print("Reddedildi: Lütfen geçerli bir sayı girin!")
        return

    if not (1 <= gun <= 7):
        print("Reddedildi: Gün sayısı 1 ile 7 arasında olmalıdır!")
        return

    if ekipman_oduncte_mi:
        print("Reddedildi: Ekipman zaten ödünçte!")
        return

    print(f"Onaylandı: {gun} günlüğüne ödünç verildi.")


# Test Alanı
while True:
    cozumu_bir(ekipman_oduncte_mi=False)
