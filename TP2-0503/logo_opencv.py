import cv2
import numpy as np
import math

# Création d'une image blanche
largeur, hauteur = 500, 500
image = np.zeros((hauteur, largeur, 3), dtype=np.uint8)
image[:] = 255 # Remplir avec du blanc

# Paramètres du logo
rayon = 60
epaisseur = 40
distance_centre = 85

# Centre global du logo
cx, cy = 250, 200

# Calcul des centres des trois cercles
# Cercle Rouge (Haut)
c_rouge = (cx, cy - distance_centre)
# Cercle Vert (Bas Gauche) - angle 30 degrés par rapport à l'horizontale
c_vert = (int(cx - distance_centre * math.cos(math.radians(30))), int(cy + distance_centre * math.sin(math.radians(30))))
# Cercle Bleu (Bas Droite)
c_bleu = (int(cx + distance_centre * math.cos(math.radians(30))), int(cy + distance_centre * math.sin(math.radians(30))))

# Couleurs BGR
rouge = (0, 0, 255)
vert = (0, 255, 0)
bleu = (255, 0, 0)

# Dessin des arcs (cv2.ellipse permet de dessiner des arcs de cercles en spécifiant l'angle de début et de fin)
# L'ouverture du cercle rouge est vers le bas (90 degrés)
cv2.ellipse(image, c_rouge, (rayon, rayon), 0, 135, 405, rouge, epaisseur, cv2.LINE_AA)

# L'ouverture du cercle vert est vers le haut à droite (-30 degrés en OpenCV => 330 degrés)
cv2.ellipse(image, c_vert, (rayon, rayon), 0, 15, 285, vert, epaisseur, cv2.LINE_AA)

# L'ouverture du cercle bleu est vers le haut à gauche (210 degrés)
cv2.ellipse(image, c_bleu, (rayon, rayon), 0, 255, 525, bleu, epaisseur, cv2.LINE_AA)

# Ajout du texte "OpenCV"
police = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "OpenCV", (100, 400), police, 2.5, (0, 0, 0), 6, cv2.LINE_AA)

# Afficher l'image
cv2.imshow("Logo OpenCV", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
