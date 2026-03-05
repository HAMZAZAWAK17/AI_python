import cv2
img = cv2.imread('Ressources/Total black.jpg')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image couleur", img)
cv2.imshow("Image niveaux de gris", gris)
cv2.imwrite('Ressources/image1_gris.jpg',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()