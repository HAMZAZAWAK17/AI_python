import cv2

# 1. Charger l'image de l'équipe
image_chemin = "equipeMA.jpg"
image = cv2.imread(image_chemin)

if image is None:
    print(f"Erreur : Impossible de charger l'image {image_chemin}")
else:
    # 2. Convertir en noir et blanc pour le détecteur
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Charger le détecteur de visages d'OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 4. Détecter les visages (On affine les paramètres pour plus de précision)
    visages = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Nombre de visages détectés : {len(visages)}")

    # 5. Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in visages:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 6. CONFIGURATION DE L'AFFICHAGE (Pour que l'image tienne sur l'écran)
    # On crée une fenêtre redimensionnable
    cv2.namedWindow('Detection de Visages - TP AI', cv2.WINDOW_NORMAL)
    
    # On force la fenêtre à une taille raisonnable (ex: 1000 pixels de large)
    # tout en gardant les proportions de l'image
    h, w = image.shape[:2]
    affichage_largeur = 1000
    affichage_hauteur = int(h * (affichage_largeur / w))
    cv2.resizeWindow('Detection de Visages - TP AI', affichage_largeur, affichage_hauteur)

    # Afficher le résultat
    cv2.imshow('Detection de Visages - TP AI', image)
    
    # 7. Sauvegarder l'image résultat (en taille réelle)
    cv2.imwrite("resultat_final.jpg", image)
    print("Image sauvegardée sous 'resultat_final.jpg'")

    # Attendre qu'une touche soit pressée pour fermer
    cv2.waitKey(0)
    cv2.destroyAllWindows()
