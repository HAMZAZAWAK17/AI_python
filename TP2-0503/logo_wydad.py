import cv2
import numpy as np
import math

# Création d'une image blanche de 800x800 pixels
largeur, hauteur = 800, 800
image = np.zeros((hauteur, largeur, 3), dtype=np.uint8)
image[:] = 255 # Remplir avec du blanc

# Couleurs pour le logo (en format BGR)
rouge = (30, 30, 215) 
blanc = (255, 255, 255)
or_jaune = (20, 180, 240)

# Centre de l'image
cx, cy = 400, 400

# Fonction pour dessiner une étoile remplie
def dessiner_etoile_remplie(img, center, radius, color):
    points = []
    inner_radius = radius * 0.382
    for i in range(10):
        r = radius if i % 2 == 0 else inner_radius
        angle = math.radians(i * 36 - 90)
        x = int(center[0] + r * math.cos(angle))
        y = int(center[1] + r * math.sin(angle))
        points.append([x, y])
    pts = np.array(points, np.int32)
    cv2.fillPoly(img, [pts], color, lineType=cv2.LINE_AA)

# 1. Étoiles jaunes en haut
dessiner_etoile_remplie(image, (340, 100), 30, or_jaune)
dessiner_etoile_remplie(image, (460, 100), 30, or_jaune)

# 2. Cercle rouge extérieur très fin
cv2.circle(image, (cx, cy), 280, rouge, 2, cv2.LINE_AA)

# 3. Le grand cercle rouge central (légèrement décalé vers le haut et plus petit)
# Dans l'original, c'est un cercle avec de la calligraphie, on dessine le fond
cv2.circle(image, (cx, cy - 10), 220, rouge, -1, cv2.LINE_AA)

# Une approximation de la calligraphie (Lignes courbes blanches)
cv2.ellipse(image, (cx, cy - 10), (180, 180), 0, 180, 360, blanc, 10, cv2.LINE_AA)
cv2.ellipse(image, (cx, cy - 10), (120, 120), 0, 0, 180, blanc, 10, cv2.LINE_AA)
cv2.circle(image, (cx, cy - 10), 60, blanc, 10, cv2.LINE_AA)

# 4. Dessin du bord rouge épais en bas pour contenir le texte "W.A.C"
cv2.ellipse(image, (cx, cy + 20), (250, 250), 0, 30, 150, rouge, 40, cv2.LINE_AA)

# 5. Dessin du texte W.A.C
font = cv2.FONT_HERSHEY_DUPLEX
# Obtenir des lettres inclinées est complexe en OpenCV pur, on positionne manuellement
cv2.putText(image, "W", (210, 580), font, 2.5, rouge, 6, cv2.LINE_AA)
cv2.putText(image, ".", (290, 600), font, 2, rouge, 6, cv2.LINE_AA)
cv2.putText(image, "A", (370, 630), font, 2.5, rouge, 6, cv2.LINE_AA)
cv2.putText(image, ".", (440, 630), font, 2, rouge, 6, cv2.LINE_AA)
cv2.putText(image, "C", (530, 580), font, 2.5, rouge, 6, cv2.LINE_AA)

# 6. Étoiles jaunes toutes petites en bas
dessiner_etoile_remplie(image, (370, 750), 12, or_jaune)
dessiner_etoile_remplie(image, (430, 750), 12, or_jaune)

# Affichage du résultat
cv2.imshow("Logo WAC", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
