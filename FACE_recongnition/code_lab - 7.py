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

    # 4. Détecter les visages
    visages = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Nombre de visages détectés : {len(visages)}")

    # 5. Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in visages:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, "Visage", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 6. Afficher le résultat
    cv2.imshow('Detection de Visages - TP AI', image)
    
    # 7. Sauvegarder l'image résultat
    cv2.imwrite("resultat_detection.jpg", image)
    print("Image sauvegardée sous 'resultat_detection.jpg'")

    # Attendre qu'une touche soit pressée pour fermer la fenêtre
    cv2.waitKey(0)
    cv2.destroyAllWindows()
