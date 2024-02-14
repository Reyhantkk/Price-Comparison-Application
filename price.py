

def en_iyi_fiyati_bul(urun_adi, fiyatlar):
    """
    En düşük fiyatı ve mağazanın adını döndürür.
    fiyatlar: Mağazalar ve fiyatları içeren bir sözlük.
    """
    en_dusuk_fiyat = float('inf')
    en_ucuz_magaza = None

    for magaza, urun_fiyati in fiyatlar.items():
        if urun_fiyati < en_dusuk_fiyat:
            en_dusuk_fiyat = urun_fiyati
            en_ucuz_magaza = magaza

    return en_ucuz_magaza, en_dusuk_fiyat


urun_fiyatlari = {
    'Amazon': 250,
    'Walmart': 245,
    'BestBuy': 255
}

urun_adi = "Elektronik Ürün"


en_iyi_magaza, en_iyi_fiyat = en_iyi_fiyati_bul(urun_adi, urun_fiyatlari)

print(f"{urun_adi} için en iyi fiyat {en_iyi_magaza} mağazasında ve fiyatı {en_iyi_fiyat} TL.")
