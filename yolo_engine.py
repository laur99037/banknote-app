import numpy as np
from PIL import Image as PILImage  # Folosim Pillow pentru redimensionare corectă

class YOLOEngine:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.inp = interpreter.get_input_details()
        self.out = interpreter.get_output_details()

    def sigmoid(self, x):
        # Protejăm funcția împotriva overflow-ului numeric accidental
        return 1 / (1 + np.exp(-np.clip(x, -20, 20)))

    def detect(self, frame, conf=0.4):
        # 1. Redimensionare corectă folosind Pillow (păstrează imaginea intactă la 320x320)
        pil_img = PILImage.fromarray(frame)
        pil_img = pil_img.resize((320, 320))
        
        # 2. Convertim înapoi în numpy array, normalizăm și adăugăm dimensiunea batch-ului (1, 320, 320, 3)
        img = np.array(pil_img).astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)

        # 3. Rulăm modelul TFLite
        self.interpreter.set_tensor(self.inp[0]['index'], img)
        self.interpreter.invoke()

        # 4. Preluăm rezultatele
        output = self.interpreter.get_tensor(self.out[0]['index'])[0]

        results = []

        # YOLOv8 standard output shape: (4 + num_classes, 2100) sau similar
        # Iterăm prin cele 2100 de posibile detecții (coloane)
        for i in range(output.shape[1]):
            d = output[:, i]

            # În YOLOv8, scorurile claselor încep direct de la indexul 4
            class_scores = d[4:]
            
            # Dacă modelul tău e exportat brut (fără activare integrată), aplicăm sigmoid.
            # Dacă ai exportat deja modelul cu activare inclusă, linia următoare poate rămâne doar np.argmax(class_scores)
            probabilities = self.sigmoid(class_scores)
            
            cls = np.argmax(probabilities)
            score = probabilities[cls]

            # Filtrare după pragul de confidență
            if score < conf:
                continue

            results.append({
                "box": d[:4],  # coordonatele x_center, y_center, width, height
                "class": int(cls),
                "score": float(score)
            })

        # Sortăm după cele mai sigure detecții și returnăm primele 5
        results = sorted(results, key=lambda x: x["score"], reverse=True)
        return results[:5]
