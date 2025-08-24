DOSYA = "ogrenciler.txt"

# Dosyaya öğrenci eklemek
def ogrenciEkle():
    try:
      # Okul numarası
      numara = input("Öğrencinin okul numarası: ").strip()
      if not numara.isdigit():
        print("Numara sadece rakamlardan oluşmalıdır.")
        return
      
      # Öğrenci ismi
      ad = input("Öğrenci adı: ").strip().capitalize()
      if not ad:
        print("İsim boş olmamalıdır. ")
        return
      
      # Öğrenci notu (Metinsel)
      not_str = input("Öğrencinin notu (0-100): ").strip()
      if not not_str.isdigit():
        print("Not sadece sayı olabilir.")
        return
      
      # Öğrenci notu (Sayısal)
      not_int = int(not_str)
      if not 0 <= not_int <= 100:
        print("Not 0 ile 100 arasında olmalıdır.")
        return
      
      # Öğrenci geçti mi kaldı mı?
      durum = "geçti" if not_int >= 50 else "kaldı"
      
      # Dosyaya yapılacak yazım şekli
      satir = f"{numara} - {ad}: {not_int} ({durum})"
      
      # Dosyaya yazdırma
      with open(DOSYA, "a", encoding="utf-8") as dosya:
        dosya.write(satir + "\n")
      print("Öğrenci kaydedildi!")
      
    except Exception as e:
      print("Bir hata oluştu: ", e)

# Dosyadan öğrenci sil 
def ogrenciSil():
  try:
    numara = input("Silinecek öğrencinin okul numarası: ").strip()
    
    with open(DOSYA, "r", encoding="utf-8") as dosya:
      satirlar = dosya.readlines()
    
    yeni_satirlar = []
    silindiMi = False
    
    for satir in satirlar:
      if satir.startswith(numara + " "):
        silindiMi = True
        continue
      yeni_satirlar.append(satir)
    if silindiMi:
      with open(DOSYA, "w", encoding="utf-8") as dosya:
        dosya.writelines(yeni_satirlar)
        print(f"{numara} numaralı öğrenci silindi.")
    else:
      print("Bu numarayla eşleşen bir öğrenci bulunamadı.")
  
  except FileNotFoundError:
    print("Dosya bulunamadı. Önce öğrenci ekleyin.")
  except Exception as e:
    print("Bir hata oluştu:", e)

# Öğrenci notunu değiştirme
def ogrenciNotGuncelle():
  try:
    numara = input("Öğrenci numarası girin: ").strip()
    
    with open(DOSYA, "r", encoding="utf-8") as dosya:
      satirlar = dosya.readlines()
      
    bulundu = False
    yeni_satirlar = []
    
    for satir in satirlar:
      if satir.startswith(numara + " "):
        bulundu = True
        print("Mevcut kayıt:", satir.strip())
        yeni_not_str = input("Yeni not (0-100):").strip()
        if not yeni_not_str.isdigit():
          print("Geçersiz not")
          return
        yeni_not_int = int(yeni_not_str)
        if not 0 <= yeni_not_int <= 100:
          print("Not 0 ile 100 arası olmalı.")
          return
        
        ad_kismi = satir.split(" - ")[1].split(":")[0]
        durum = "geçti" if yeni_not_int >= 50 else "kaldı"
        yeni_satir = f"{numara} - {ad_kismi}: {yeni_not_int} ({durum})\n"
        yeni_satirlar.append(yeni_satir)
      else:
        yeni_satirlar.append(satir)
    if bulundu:
      with open(DOSYA, "w", encoding="utf-8") as dosya:
        dosya.writelines(yeni_satirlar)
        print("Not güncellendi.")
    else:
      print("Öğrenci bulunamadı.")
  
  except FileNotFoundError:
    print("Dosya bulunamadı. Önce öğrenci ekleyin.")
  except Exception as e:
    print("Bir hata oluştu:", e)
    
# Herkese not eklemek
def herkesePuanEkle():
  try:
    miktar_str = input("Kaç puan ekleyeceksiniz? (Max. 15): ").strip()
    if not miktar_str.isdigit():
      print("Bir sayı girmelisiniz.")
      return
    miktar_int = int(miktar_str)
    if not 1 <= miktar_int <= 15:
      print("1 ile 15 arasında bir sayı girin.")
      return
    with open(DOSYA, "r", encoding="utf-8") as dosya:
      satirlar = dosya.readlines()
    yeni_satirlar = []
    
    for satir in satirlar:
      numara, kalani = satir.strip().split(" - ")
      ad, not_durum = kalani.split(": ")
      not_str, parantezli_durum = not_durum.split(" ")
      eski_not = int(not_str)
      yeni_not = min(eski_not + miktar_int, 100)
      durum = "geçti" if yeni_not >= 50 else "kaldı"
      yeni_satir = f"{numara} - {ad}: {yeni_not} ({durum})\n"
      yeni_satirlar.append(yeni_satir)
    
    with open(DOSYA, "w", encoding="utf-8") as dosya:
      dosya.writelines(yeni_satirlar)
      print(f"Herkese {miktar_int} puan eklendi.")
  except FileNotFoundError:
    print("Dosya bulunamadı. Önce öğrenci ekleyin.")
  except Exception as e:
    print("Bir hata oluştu:", e)

# Herkesten not düşürmek
def herkestenPuanDusur():
  try:
    miktar_str = input("Kaç puan düşüreceksiniz? (Max. 15): ").strip()
    if not miktar_str.isdigit():
      print("Bir sayı girmelisiniz.")
      return
    miktar_int = int(miktar_str)
    if not 1 <= miktar_int <= 15:
      print("1 ile 15 arasında bir sayı girin.")
      return
    with open(DOSYA, "r", encoding="utf-8") as dosya:
      satirlar = dosya.readlines()
    yeni_satirlar = []
    
    for satir in satirlar:
      numara, kalani = satir.strip().split(" - ")
      ad, not_durum = kalani.split(": ")
      not_str, parantezli_durum = not_durum.split(" ")
      eski_not = int(not_str)
      yeni_not = max(eski_not - miktar_int, 0)
      durum = "geçti" if yeni_not >= 50 else "kaldı"
      yeni_satir = f"{numara} - {ad}: {yeni_not} ({durum})\n"
      yeni_satirlar.append(yeni_satir)
    
    with open(DOSYA, "w", encoding="utf-8") as dosya:
      dosya.writelines(yeni_satirlar)
      print(f"Herkesten {miktar_int} puan düşürüldü.")
 
  except FileNotFoundError:
    print("Dosya bulunamadı. Önce öğrenci ekleyin.")
  except Exception as e:
    print("Bir hata oluştu:", e)


# Öğrencileri dosyadaki gibi programda listeliyoruz    
def ogrencileriListeleVeSirala():
  try:
    with open(DOSYA, "r", encoding="utf-8") as dosya:
        satirlar = [s.strip() for s in dosya.readlines()]
        
    if not satirlar:
        print("Liste boş, henüz öğrenci eklenmedi.")
        return
        
    print("\nSıralama türünü seç:")
    print("1 - İsme göre (A-Z)")
    print("2 - Nota göre (yüksekten düşüğe)")
    print("3 - Numara göre (küçükten büyüğe)")
    print("4 - Eklenme sırasına göre")
    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        sirali = sorted(satirlar, key=lambda x: x.split(" - ")[1].split(":")[0])
    elif secim == "2": 
        sirali = sorted(satirlar, key=lambda x: int(x.split(": ")[1].split(" ")[0]), reverse=True)
    elif secim == "3":
        sirali = sorted(satirlar, key=lambda x: int(x.split(" - ")[0]))
    elif secim == "4":
        sirali = satirlar  # Dosyadaki hali
    else:
        print("Geçersiz seçim.")
        return

    print("\n--- Sıralı Liste ---")
    for i, satir in enumerate(sirali, start=1):
        print(f"{i}. {satir}")

  except FileNotFoundError:
    print("Dosya bulunamadı. Önce öğrenci ekleyin.")
  except Exception as e:
    print("Bir hata oluştu:", e)
  
# Program açıldığında çalışacak kısım
def main():
  # Her bittiğinde tekrar çalıştırma döngüsü
  while True:
    print("\n1 - Öğrenci ekle")
    print("2 - Öğrenci sil")
    print("3 - Not güncelle")
    print("4 - Herkese puan ekle")
    print("5 - Herkesten puan düşür")
    print("6 - Öğrencileri listele")
    print("7 - Çıkış")
    secim = input("Seçiminiz: ").strip()
    
    if secim == "1":
      ogrenciEkle()
      
    elif secim == "2":
      ogrenciSil()
      
    elif secim == "3":
      ogrenciNotGuncelle()
      
    elif secim == "4":
      herkesePuanEkle()
      
    elif secim == "5":
      herkestenPuanDusur()
    
    elif secim == "6":
      ogrencileriListeleVeSirala()
      
    elif secim == "7":
      print("Program sonlandırıldı.")
      break
    
    else:
      print("Geçersiz seçim.")
      
if __name__ == "__main__":
  main()
        
