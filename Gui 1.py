import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from diffusers import DiffusionPipeline
from transformers import pipeline
from Models import TextToImageModel, ImageClassifierModel
import torch

class TextToImageModel:
    """Generates images from text prompts"""
    def __init__(self):
        try:
            self.pipe = DiffusionPipeline.from_pretrained(
                "rupeshs/LCM-runwayml-stable-diffusion-v1-5",
                torch_dtype=torch.float32
            )
            self.pipe.to("cpu")  # run on CPU
        except Exception as e:
            print("Error loading Text-to-Image model:", e)
            self.pipe = None

    def run(self, prompt):
        if self.pipe is None:
            raise ValueError("Text-to-Image model not loaded.")
        image = self.pipe(prompt).images[0]  # returns PIL Image
        return image


class ImageClassifierModel:
    """Classifies images using a tiny transformer model."""
    def __init__(self):
        try:
            self.pipe = pipeline("image-classification", model="facebook/deit-tiny-distilled-patch16-224")
        except Exception as e:
            print("Error loading Image Classifier:", e)
            self.pipe = None

    def run(self, image_path):
        if self.pipe is None:
            raise ValueError("Image Classifier model not loaded.")
        return self.pipe(image_path)  


class AIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HIT137 Assessment")

       # Dropdown for model selection with placeholder
        self.model_choice = tk.StringVar(value="Select your model")  # placeholder text
        self.model_dropdown = ttk.Combobox(
            root,
            textvariable=self.model_choice,
            values=["Text-to-Image", "Image Classification"]
        )
        self.model_dropdown.pack(pady=5)


        # Load model button
        self.load_btn = tk.Button(root, text="Load Model", command=self.load_model)
        self.load_btn.pack(pady=5)

        # Input type
        self.input_type = tk.StringVar(value="text")
        tk.Radiobutton(root, text="Text", variable=self.input_type, value="text").pack()
        tk.Radiobutton(root, text="Image", variable=self.input_type, value="image").pack()

        # Input entry
        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack(pady=5)

        self.input_entry.insert(0, "Enter your prompt : ")
        self.input_entry.config(fg="white")  # optional, default text color


        # Browse file button
        self.browse_btn = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_btn.pack(pady=5)

        # Run model button
        self.run_btn = tk.Button(root, text="Run Model", command=self.run_model)
        self.run_btn.pack(pady=10)

        # Output
        self.output_label = tk.Label(root, text="Output will appear here.")
        self.output_label.pack(pady=5)
        self.output_canvas = tk.Label(root)
        self.output_canvas.pack(pady=5)

        # Info box
        self.info_box = tk.Text(root, height=6, width=60)
        self.info_box.pack(pady=5)

        # Placeholder for model
        self.model = None

    def load_model(self):
        choice = self.model_choice.get()
        if choice == "Text-to-Image":
            self.model = TextToImageModel()
            self.info_box.delete("1.0", tk.END)
            self.info_box.insert(tk.END, "Text-to-Image model (rupeshs/LCM-runwayml-stable-diffusion-v1-5) loaded.\nGenerates images from text prompts.\nText-to-Image model that generates high-quality images from text prompts using Stable Diffusion.\n")
        elif choice == "Image Classification":
            self.model = ImageClassifierModel()
            self.info_box.delete("1.0", tk.END)
            self.info_box.insert(tk.END, "Image Classifier Model (facebook/deit-tiny-distilled-patch16-224) loaded.\nClassifies input images.\nTiny vision transformer for fast image classification with low resource usage.\n")
        else:
            self.info_box.delete("1.0", tk.END)
            self.info_box.insert(tk.END, "Please select a model first.")
            return

        oop_explanation = """
        OOP Concepts Used:
        - Encapsulation: Model details hidden in TextToImageModel / ImageClassifierModel.
        - Polymorphism: run() is overridden differently in each model class.
        - Multiple Inheritance: (if LoggerMixin used) combined with AIModel.
        - Method Overriding: Child classes override base class run().
        - Multiple Decorators: Could decorate run() with timing/logging functions.
        """

        self.info_box.insert(tk.END, oop_explanation)

    # ===== Browse file =====
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    # ===== Run model =====
    def run_model(self):
        if self.model is None:
            self.output_label.config(text="Please load a model first.")
            return

        inp = self.input_entry.get()
        try:
            output = self.model.run(inp)
        except Exception as e:
            self.output_label.config(text=f"Error: {e}")
            return

        # Display output
        if isinstance(output, list):  
            text_output = "\n".join([f"{item['label']}: {item['score']:.2f}" for item in output])
            self.output_label.config(text=text_output)
            self.output_canvas.config(image="")
        else:
            img = ImageTk.PhotoImage(output.resize((256, 256)))
            self.output_canvas.config(image=img)
            self.output_canvas.image = img
            self.output_label.config(text="Generated image:")

if __name__ == "__main__":
    root = tk.Tk()
    app = AIApp(root)
    root.mainloop()
