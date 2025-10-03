from transformers import pipeline
from diffusers import DiffusionPipeline
import time

# ----------------- Decorators -----------------
def log_time(func):
    """Decorator to log execution time of model runs"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.2f}s")
        return result
    return wrapper

# ----------------- Base Class -----------------
class AIModel:
    def __init__(self, name, category, description):
        self._name = name
        self._category = category
        self._description = description

    def info(self):
        return f"Model: {self._name}\nCategory: {self._category}\n{self._description}"

    def run(self, input_data):
        raise NotImplementedError("Subclass must override this method.")

# ----------------- Logger Mixin -----------------
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# ----------------- Text-to-Image Model -----------------
class TextToImageModel(AIModel, LoggerMixin):
    """Generates images from text prompts using a public SD model"""
    def __init__(self):
        super().__init__(
            "rupeshs/LCM-runwayml-stable-diffusion-v1-5",
            "Text-to-Image",
            "Generates high-quality images from text prompts (public)."
        )
        try:
            self.pipe = DiffusionPipeline.from_pretrained(self._name).to("cpu")
        except Exception as e:
            print("Error loading Text-to-Image model:", e)
            self.pipe = None

    @log_time
    def run(self, prompt):
        if self.pipe is None:
            raise ValueError("Text-to-Image model not loaded.")
        self.log("Generating image from prompt...")
        image = self.pipe(prompt).images[0]
        image.save("generated_image.png")
        return image

# ----------------- Image Classification Model -----------------
class ImageClassifierModel(AIModel, LoggerMixin):
    """Classifies images using a tiny transformer vision model"""
    def __init__(self):
        super().__init__(
            "facebook/deit-tiny-distilled-patch16-224",
            "Vision",
            "Very small transformer model for image classification."
        )
        self.pipe = pipeline("image-classification", model='facebook/deit-tiny-distilled-patch16-224')

    @log_time
    def run(self, image):
        self.log("Classifying image...")
        return self.pipe(image)




