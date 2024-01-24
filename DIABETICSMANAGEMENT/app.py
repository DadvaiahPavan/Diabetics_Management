import google.generativeai as genai
from pathlib import Path
import gradio as gr

# Set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

# Set your API key here
api_key = "AIzaSyCxe63YOzfK_D54z397uZVhREutOEk10NI"
genai.configure(api_key=api_key)

# Model Instance
model = genai.GenerativeModel(
    model_name="gemini-pro-vision",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Image Input Function
def input_image_setup(file_loc):
    if not (img := Path(file_loc)).exists():
        raise FileNotFoundError(f"Could not find image: {img}")

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": Path(file_loc).read_bytes()
        }
    ]
    return image_parts

# Response Function
def generate_gemini_response(input_prompt, image_loc):
    image_prompt = input_image_setup(image_loc)
    prompt_parts = [input_prompt, image_prompt[0]]
    response = model.generate_content(prompt_parts)
    return response.text

# Prompt
input_prompt = """
               As an expert specializing in assessing the suitability of fruits and foods for individuals with diabetes, your task involves analyzing input images featuring various food items. Your first objective is to identify the type of fruit or food present in the image. Subsequently, you must determine the glycemic index of the identified item. Based on this glycemic index, provide recommendations on whether individuals with diabetes can include the detected food in their diet. If the food is deemed suitable, specify the recommended quantity for consumption.
               """

# Defining the Interface
def upload_file(files):
    file_paths = [file.name for file in files]
    if file_paths:
        response = generate_gemini_response(input_prompt, file_paths[0])
    return file_paths[0], response

with gr.Blocks() as demo:
    file_output = gr.Textbox()
    image_output = gr.Image()
    combined_output = [image_output, file_output]
    upload_button = gr.UploadButton(
        "Click to Upload an Image of the Food that you want to eat",
        file_types=["image"],
        file_count="multiple"
    )
    upload_button.upload(upload_file, upload_button, combined_output)

# Run the Gradio interface
demo.launch(debug=True)