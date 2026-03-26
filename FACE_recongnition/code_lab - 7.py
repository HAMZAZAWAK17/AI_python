import cv2
import face_recognition # On garde face_recognition uniquement pour la signature (encoding)
from PIL import Image, ImageDraw

# 1. Apprendre les visages
hakim_image = face_recognition.load_image_file("hakim.jpg")
hakim_signature = face_recognition.face_encodings(hakim_image)[0]

mrabet_image = face_recognition.load_image_file("Mrabet.jpg")
mrabet_signature = face_recognition.face_encodings(mrabet_image)[0]

signatures_connues = [hakim_signature, mrabet_signature]
noms_connus = ["Hakim Ziyach", "Soufiane Mrabet"]

# 2. Charger l'image de l'équipe
image_equipe = cv2.imread("equipeMA.jpg")
image_rgb = cv2.cvtColor(image_equipe, cv2.COLOR_BGR2RGB)

# Utiliser OpenCV pour la détection (très stable)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
visages = face_cascade.detectMultiScale(cv2.cvtColor(image_equipe, cv2.COLOR_BGR2GRAY), 1.1, 4)

# 3. Dessiner avec Pillow
pil_img = Image.fromarray(image_rgb)
draw = ImageDraw.Draw(pil_img)

for (x, y, w, h) in visages:
    # Convertir format OpenCV (x,y,w,h) vers format face_recognition (top, right, bottom, left)
    location = [(y, x+w, y+h, x)]
    
    # Extraire la signature du visage détecté
    signature_inconnue = face_recognition.face_encodings(image_rgb, location)[0]
    
    # Comparer
    matches = face_recognition.compare_faces(signatures_connues, signature_inconnue)
    nom = "Inconnu"
    if True in matches:
        nom = noms_connus[matches.index(True)]
    
    # Dessiner le rectangle et le nom
    draw.rectangle(((x, y), (x+w, y+h)), outline=(0, 0, 255), width=3)
    draw.text((x, y-20), nom, fill=(255, 0, 0))

# 4. Afficher et Sauvegarder
pil_img.show()
pil_img.save("resultat_tp.jpg")
