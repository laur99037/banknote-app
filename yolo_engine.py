import numpy as np

class YOLOEngine:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.inp = interpreter.get_input_details()
        self.out = interpreter.get_output_details()

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def detect(self, frame, conf=0.4):
        img = np.resize(frame, (1, 320, 320, 3)).astype(np.float32) / 255.0

        self.interpreter.set_tensor(self.inp[0]['index'], img)
        self.interpreter.invoke()

        output = self.interpreter.get_tensor(self.out[0]['index'])[0]

        results = []

        for i in range(output.shape[1]):
            d = output[:, i]

            obj = self.sigmoid(d[4])
            if obj < conf:
                continue

            cls = np.argmax(self.sigmoid(d[5:]))
            score = obj

            if score < conf:
                continue

            results.append({
                "box": d[:4],
                "class": int(cls),
                "score": float(score)
            })

        return results[:5]
