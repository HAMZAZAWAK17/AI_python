import cv2
import numpy as np
import math

# Création d'une image blanche de 600x600 pixels
largeur, hauteur = 600, 600
image = np.zeros((hauteur, largeur, 3), dtype=np.uint8)
image[:] = 255 # Remplir avec du blanc

# Couleurs pour le logo WAC (en format BGR)
rouge = (0, 0, 210) 
blanc = (255, 255, 255)
vert = (50, 180, 50)

# Centre de l'image
cx, cy = 300, 300

# Cercle rouge extérieur
cv2.circle(image, (cx, cy), 280, rouge, -1, cv2.LINE_AA)
# Cercle blanc intérieur
cv2.circle(image, (cx, cy), 200, blanc, -1, cv2.LINE_AA)

# Police d'écriture
font_principale = cv2.FONT_HERSHEY_DUPLEX
font_secondaire = cv2.FONT_HERSHEY_SIMPLEX

# Ajouter les textes sur le bord rouge
cv2.putText(image, "W Y D A D", (200, 60), font_secondaire, 1.2, blanc, 3, cv2.LINE_AA)
cv2.putText(image, "ATHLETIC CLUB", (160, 565), font_secondaire, 1.2, blanc, 3, cv2.LINE_AA)

# Ajouter "W A C" géants (entrecroisés ou côte à côte)
cv2.putText(image, "W", (130, 330), font_principale, 5, rouge, 12, cv2.LINE_AA)
cv2.putText(image, "A", (240, 250), font_principale, 5, rouge, 12, cv2.LINE_AA)
cv2.putText(image, "C", (370, 330), font_principale, 5, rouge, 12, cv2.LINE_AA)

# Ajouter la date 1937
cv2.putText(image, "1937", (240, 420), font_secondaire, 1.5, rouge, 3, cv2.LINE_AA)

# Fonction pour dessiner la fameuse étoile verte à 5 branches
def dessiner_etoile(img, centre, rayon, couleur, epaisseur):
    points = []
    # L'angle entre deux pointes d'un pentagramme est de 144 degrés
    for i in range(5):
        angle = math.radians(i * 144 - 90) # -90 pour pointer vers le haut
        x = int(centre[0] + rayon * math.cos(angle))
        y = int(centre[1] + rayon * math.sin(angle))
        points.append([x, y])
        
    pts = np.array(points, np.int32)
    pts = pts.reshape((-1, 1, 2))
    # Dessiner l'étoile
    cv2.polylines(img, [pts], isClosed=True, color=couleur, thickness=epaisseur, lineType=cv2.LINE_AA)

# Dessiner l'étoile verte au milieu
dessiner_etoile(image, (300, 280), 30, vert, 3)

# Affichage du résultat
cv2.imshow("Logo WAC", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
