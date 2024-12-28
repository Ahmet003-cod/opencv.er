# görüntüyü içe aktarma ve yeniden boyutlandırma
import cv2

# Web kamerasına bağlanma (0, varsayılan kamera için kullanılır)
kamera = cv2.VideoCapture(0)  # süreki çalışır siz "k" harfine basmadığınız sürece

if not kamera.isOpened():  # eğer kamera açılmadıysa
    print("Web kamerası açılamadı!")
    exit()  # Bu kodan çık emri verildi

while True:  # Eğer çalışıyorsa Kameradan bir kare yakala

    geri_döndür, çerçeve = kamera.read()
    if not geri_döndür:  # görüntü bilgisiyara işlenmedi
        print("Görüntü alınamadı!")
        break  # burdan sonra ilemi bırak.

    # ilk çektiğin boyut
    print("Orijinal boyutlar:", çerçeve.shape)
    # aşağıdaki aşamada çektiğin görüntüyü yeniden boyutlandırıyorsun
    yeni_boyut = (400, 200)  # (genişlik, yükseklik) boyutunu burdan belirleyebilirsin
    boyutlandırılmış_hali = cv2.resize(çerçeve, yeni_boyut)

    # Yeniden boyutlandırılmış görüntüyü göster imshow sayesinde
    cv2.imshow("ilk Görüntü", çerçeve)
    cv2.imshow("Boyutlandırılmış Görüntü", boyutlandırılmış_hali)

    # Görüntüyü kaydetme
    cv2.imwrite("kaydedilen_goruntu.jpg", boyutlandırılmış_hali)

    # 'k' tuşuna basıldığında döngüden çık(kapat)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        break

# Kamera ve pencereleri kapatma
kamera.release()
cv2.destroyAllWindows()
