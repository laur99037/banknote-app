import numpy as np
from PIL import Image as PILImage


class YOLOEngine:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.inp = interpreter.get_input_details()
        self.out = interpreter.get_output_details()

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -20, 20)))

    def detect(self, frame, conf=0.4):
        pil_img = PILImage.fromarray(frame)
        pil_img = pil_img.resize((320, 320))

        img = np.array(pil_img).astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)

        self.interpreter.set_tensor(self.inp[0]['index'], img)
        self.interpreter.invoke()

        output = self.interpreter.get_tensor(self.out[0]['index'])[0]

        results = []

        for i in range(output.shape[1]):
            d = output[:, i]
            class_scores = d[4:]
            probabilities = self.sigmoid(class_scores)
            cls = np.argmax(probabilities)
            score = probabilities[cls]

            if score < conf:
                continue

            results.append({
                "box": d[:4],
                "class": int(cls),
                "score": float(score)
            })

        results = sorted(results, key=lambda x: x["score"], reverse=True)
        return results[:5]
