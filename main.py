import numpy as np
import tflite_runtime.interpreter as tflite

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera  # FIX 3: schimbat din kivy.core.camera

from yolo_engine import YOLOEngine


class BanknoteApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # FIX: Camera widget corect pentru Android
        self.camera = Camera(resolution=(640, 480), play=True)
        self.img = Image()

        layout.add_widget(self.camera)
        layout.add_widget(self.img)

        self.interpreter = tflite.Interpreter(model_path="best_float32.tflite")
        self.interpreter.allocate_tensors()
        self.detector = YOLOEngine(self.interpreter)

        Clock.schedule_interval(self.update, 1.0 / 20.0)

        return layout

    def update(self, dt):
        if not self.camera.texture:
            return

        frame = np.frombuffer(self.camera.texture.pixels, dtype=np.uint8)
        frame = frame.reshape(
            self.camera.texture.height,
            self.camera.texture.width, 4
        )
        frame = frame[:, :, :3].copy()

        detections = self.detector.detect(frame)

        # Afișăm detecțiile în consolă (poți adăuga Label în UI mai târziu)
        for d in detections:
            print(f"Clasa: {d['class']} | Scor: {d['score']:.2f}")

        buf = frame.flatten()
        texture = Texture.create(
            size=(frame.shape[1], frame.shape[0])
        )
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        self.img.texture = texture


if __name__ == "__main__":
    BanknoteApp().run()
