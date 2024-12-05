class gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak(self):
        print(f"Skala dari gempa ini adalah {self.skala}")
        print(f"Ada gempa baru di {self.lokasi}")
        if self.skala < 2:
            print('Dampak tidak berasa')
        elif self.skala >= 2 and self.skala <= 4:
            print('Dampak gempa bangunan retak-retak')
        elif self.skala > 4 and self.skala <= 6:
            print('Dampak gempa bangunan roboh')
        elif self.skala > 6:
            print('Dampak gempa bangunan roboh dan potensi tsunami')
        else :
            print('Sistem tidak terbaca')

    


#gempa1 = gempa(5, "Jawa Barat")
#gempa1.dampak()
