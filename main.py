import numpy as np
from PIL import Image as PILImage
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from yolo_engine import YOLOEngine

try:
    import tflite_runtime.interpreter as tflite
except ImportError:
    try:
        import tensorflow.lite as tflite
    except ImportError:
        from tensorflow.lite.python import interpreter as tflite


CLASS_NAMES = {
    0: "1 Leu",
    1: "5 Lei",
    2: "10 Lei",
    3: "20 Lei",
    4: "50 Lei",
    5: "100 Lei",
    6: "200 Lei",
    7: "500 Lei",
    8: "1000 Lei",
}


class BanknoteApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(
            text="Îndreaptă camera spre o bancnotă...",
            size_hint=(1, 0.1),
            font_size='16sp'
        )

        self.camera = Camera(resolution=(640, 480), play=True)
        self.img = Image(size_hint=(1, 0.8))

        layout.add_widget(self.label)
        layout.add_widget(self.camera)
        layout.add_widget(self.img)

        try:
            self.interpreter = tflite.Interpreter(model_path="best_float32.tflite")
            self.interpreter.allocate_tensors()
            self.detector = YOLOEngine(self.interpreter)
            self.label.text = "Model încărcat! Îndreaptă camera..."
        except Exception as e:
            self.label.text = f"Eroare model: {str(e)}"
            self.detector = None

        Clock.schedule_interval(self.update, 1.0 / 10.0)
        return layout

    def update(self, dt):
        if not self.camera.texture:
            return
        if self.detector is None:
            return

        try:
            frame = np.frombuffer(self.camera.texture.pixels, dtype=np.uint8)
            frame = frame.reshape(
                self.camera.texture.height,
                self.camera.texture.width, 4
            )[:, :, :3].copy()

            detections = self.detector.detect(frame, conf=0.4)

            if detections:
                best = detections[0]
                cls = best['class']
                score = best['score']
                name = CLASS_NAMES.get(cls, f"Clasa {cls}")
                self.label.text = f"Detectat: {name} ({score:.0%})"
            else:
                self.label.text = "Nicio bancnotă detectată..."

            buf = frame.flatten()
            texture = Texture.create(
                size=(frame.shape[1], frame.shape[0])
            )
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.img.texture = texture

        except Exception as e:
            self.label.text = f"Eroare: {str(e)}"


if __name__ == "__main__":
    BanknoteApp().run()
