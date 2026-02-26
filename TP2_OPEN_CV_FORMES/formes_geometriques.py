import cv2
import numpy as np

# Création du canvas (fond noir)
img = np.zeros((600, 900, 3), np.uint8)
img[:] = 20, 20, 40  # fond bleu très foncé

# ── Titre ──────────────────────────────────────────────────────────────────────
cv2.putText(img, "Formes Geometriques - OpenCV",
            (60, 50),
            cv2.FONT_HERSHEY_DUPLEX,
            1.0,
            (255, 255, 255),
            2)

# ── Ligne diagonale ────────────────────────────────────────────────────────────
cv2.line(img,
         (50, 100),    # point de départ
         (850, 550),   # point d'arrivée
         (0, 200, 255),  # couleur orange-cyan
         3)            # épaisseur

# ── Rectangle plein ────────────────────────────────────────────────────────────
cv2.rectangle(img,
              (80, 150),    # coin supérieur gauche
              (300, 320),   # coin inférieur droit
              (0, 255, 127),  # vert menthe
              -1)           # -1 = rempli

# ── Rectangle contour seulement ────────────────────────────────────────────────
cv2.rectangle(img,
              (80, 150),
              (300, 320),
              (255, 255, 255),  # bordure blanche
              2)

# ── Cercle plein ───────────────────────────────────────────────────────────────
cv2.circle(img,
           (530, 230),   # centre
           120,          # rayon
           (0, 100, 255),  # bleu-orange
           -1)           # rempli

# ── Cercle contour ─────────────────────────────────────────────────────────────
cv2.circle(img,
           (530, 230),
           120,
           (255, 255, 255),
           2)

# ── Ellipse ────────────────────────────────────────────────────────────────────
cv2.ellipse(img,
            (750, 230),    # centre
            (100, 60),     # axes (largeur, hauteur)
            30,            # angle de rotation
            0, 360,        # arc : de 0° à 360° (ellipse complète)
            (255, 50, 200),  # magenta
            -1)

# ── Polygone (triangle) ────────────────────────────────────────────────────────
triangle = np.array([[180, 400],
                     [80,  560],
                     [280, 560]], np.int32)
cv2.fillPoly(img, [triangle], (255, 200, 0))      # remplissage jaune
cv2.polylines(img, [triangle], True, (255, 255, 255), 2)  # contour blanc

# ── Polygone (pentagone) ───────────────────────────────────────────────────────
pentagone = np.array([[530, 380],
                      [620, 440],
                      [590, 550],
                      [470, 550],
                      [440, 440]], np.int32)
cv2.fillPoly(img, [pentagone], (180, 0, 255))       # violet
cv2.polylines(img, [pentagone], True, (255, 255, 255), 2)

# ── Cercles concentriques (déco) ───────────────────────────────────────────────
for r, couleur in [(80, (255, 80, 80)), (55, (255, 150, 80)), (30, (255, 220, 80))]:
    cv2.circle(img, (780, 470), r, couleur, 3)

# ── Légendes ───────────────────────────────────────────────────────────────────
legendes = [
    ((80,  350), "Rectangle",  (0, 255, 127)),
    ((470, 230), "Cercle",     (0, 100, 255)),
    ((690, 230), "Ellipse",    (255, 50, 200)),
    ((100, 580), "Triangle",   (255, 200, 0)),
    ((450, 580), "Pentagone",  (180, 0, 255)),
    ((720, 540), "Conc.",      (255, 150, 80)),
]
for pos, texte, col in legendes:
    cv2.putText(img, texte, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, col, 1)

# ── Affichage ──────────────────────────────────────────────────────────────────
cv2.imshow("TP2 - Formes Geometriques", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
