
import cv2

# Görüntüyü yükle
resim = 'yapay.jpg'  # Görüntü dosya yolunu buraya yazın(kendi dosyanıza uygun)
görüntü = cv2.imread(resim)

# Görüntüyü gri tonlamaya çevir
gri_resim = cv2.cvtColor(görüntü, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüyü ekranda göster
cv2.imshow('Gri Görüntü', gri_resim)

# Görüntü kapanana kadar bekle
cv2.waitKey(0)
cv2.destroyAllWindows()

