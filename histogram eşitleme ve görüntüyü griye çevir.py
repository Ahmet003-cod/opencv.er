import cv2   #histogram eşitlem ve orginal resmi gri tonlamaya dönüştürme
import numpy as np   #görüntünü altındaki bir aşağı bir yukarı verilerini görüntülemsini sağlar

# Kamera akışını başlatma
kamera = cv2.VideoCapture(0)  #  siz "k" basmadığın mütedçe çalışmaya devam eder

if not kamera.isOpened():
    print("Kamera açılamadı. Lütfen bağlantıyı kontrol edin.")
else:
    print("Kamera çalışıyor. Çıkış için 'k' tuşuna basın.")

    while True:#eğer kamera çalışıyorsa
        # Kameradan görüntü okuma
        geri_döndürme, çerçeve = kamera.read()

        if not geri_döndürme:
            print("Görüntü alınamadı. Lütfen kamerayı kontrol edin.")
            break

        # Görüntüyü gri tonlamalı hale getirme
        gri_çerçeve = cv2.cvtColor(çerçeve, cv2.COLOR_BGR2GRAY)

        # Histogram eşitleme
        histogram_çerçevesi = cv2.equalizeHist(gri_çerçeve)

        # Orijinal ve eşitlenmiş görüntüleri yan yana birleştirme
        yanyana_çerçeve = cv2.hconcat([gri_çerçeve, histogram_çerçevesi])

        # Sonuçları gösterme
        cv2.imshow("Orijinal (Sol) ve Histogram Eşitlenmiş (Sağ) Görüntü", yanyana_çerçeve)

        # 'k' tuşuna basıldığında döngüyü kır(kapat)
        if cv2.waitKey(1) & 0xFF == ord('k'):
            break #kodan çık

    # Kamera akışını serbest bırakma ve pencereleri kapatma bunu yapmasan aynnı sayfada takıl kalırız
    kamera.release()
    cv2.destroyAllWindows()

#görüntü ekleme