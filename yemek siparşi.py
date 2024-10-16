def yemek_siparisi():
    # Menüdeki yemekler
    menu = {
        "Hamburger": 200,
        "Pizza": 100,
        "Salata": 50,
        "Tatlı": 70
    }

    print("Menü:")
    for yemek, fiyat in menu.items():
        print(f"{yemek}: {fiyat} TL")

    # Yemek seçimi
    secilen_yemek = input("Sipariş vermek istediğiniz yemeği seçin: ")
    adet = int(input(f"{secilen_yemek} adetini girin: "))

    # Sipariş fiyatı hesaplama
    if secilen_yemek in menu:
        toplam_fiyat = menu[secilen_yemek] * adet
        print(f"Toplam tutar: {toplam_fiyat} TL")

        # Ödeme şekli
        odeme = input("Ödeme yöntemini seçin (Kredi Kartı/Nakit): ")
        print(f"{adet} adet {secilen_yemek} siparişiniz alınmıştır. Ödeme şekli: {odeme}.")
    else:
        print("Geçersiz yemek seçimi!")

# Yemek siparişi simülasyonunu başlat
yemek_siparisi()
