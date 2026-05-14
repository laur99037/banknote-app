import numpy as np
# Modificat aici: importăm tflite_runtime în loc de tot TensorFlow-ul
import tflite_runtime.interpreter as tflite

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.core.camera import Camera

from yolo_engine import YOLOEngine


class BanknoteApp(App):

    def build(self):
        self.img = Image()

        # Modificat aici: apelăm direct din tflite
        self.interpreter = tflite.Interpreter(model_path="best_float32.tflite")
        self.interpreter.allocate_tensors()

        self.detector = YOLOEngine(self.interpreter)

        self.camera = Camera(resolution=(640, 480), play=True)

        Clock.schedule_interval(self.update, 1.0 / 20.0)

        return self.img

    def update(self, dt):
        # Un mic ecran de siguranță: dacă textura camerei nu s-a încărcat încă, să nu dea crash aplicatia
        if not self.camera.texture:
            return

        frame = np.frombuffer(self.camera.texture.pixels, dtype=np.uint8)
        frame = frame.reshape(self.camera.texture.height,
                              self.camera.texture.width, 4)

        frame = frame[:, :, :3].copy()

        detections = self.detector.detect(frame)

        for d in detections:
            x, y, w, h = d["box"]
            label = f"{d['class']} {d['score']:.2f}"

        buf = frame.flatten()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]))
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        self.img.texture = texture


if __name__ == "__main__":
    BanknoteApp().run()
