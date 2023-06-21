import gradio as gr
from PIL import Image
import os
import httpx
import io 

def image_mod(image: Image):
    image_bytes = io.BytesIO()

    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()
    files = {"file": image_bytes}
    response = httpx.post("http://localhost:8000/proxy/search-by-image", files=files, timeout=None)
    ids = response.json()["ids"]
    output_path = f"../test/output/{ids[0]:03}.jpeg"
    output_image = Image.open(output_path)
    return output_image

demo = gr.Interface(
    fn=image_mod,
    inputs=gr.Image(type="pil"),
    outputs="image",
    examples=[
        "../test/input/000.png",
        "../test/input/001.png",
        "../test/input/003.png",
        "../test/input/004.png",
    ],
)

if __name__ == "__main__":
    demo.launch()