import streamlit as st
import ollama
import base64
import requests
import os

# Initialize Ollama model
# modelfile = '''
# FROM llama2
# PARAMETER temperature 1
# SYSTEM 
# You are a midjourney prompt generator in 20-30 words.u just give prompt and donot give anytype of explanations. if u do not understand, just say "unable to understand, try again".

# example 
# user prompt : dog is playing in teh park
# midjourney prompt : golden retriever bounds after the red frisbee.
# '''
# ollama_model = ollama.create(model='MLTE', modelfile=modelfile)

# Stability AI API endpoint
url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

# Streamlit app
st.title("Text to Image Generation")

# Text input for prompt
prompt = st.text_input("Enter your prompt:")

# Button to generate image
if st.button("Generate Image"):
    # Generate enhanced prompt
    response = ollama.generate(model="MLTE", prompt=prompt)
    enhanced_prompt = response["response"]

    st.write("Enhanced Prompt:")
    st.write(enhanced_prompt)

    # API request body
    body = {
        "steps": 50,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": enhanced_prompt,
                "weight": 1
            },
            {
                "text": "blurry, bad",
                "weight": -1
            }
        ],
    }

    # API request headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "sk-0ZcrqHHlOZHok1pAEFslLjaB7jllp95qS6mgcXWaMKpiBRpx",  # Replace with your actual API key
    }

    # Make API request
    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        # Decode and display the image
        data = response.json()
        image = data["artifacts"][0]["base64"]
        st.image(base64.b64decode(image), caption="Generated Image", use_column_width=True)

        if not os.path.exists("./out"):
            os.makedirs("./out")

        for i, image in enumerate(data["artifacts"]):
            with open(f'./out/txt2img_MLTE_{image["seed"]}.png', "wb") as f:
                f.write(base64.b64decode(image["base64"]))
    else:
        st.error("Failed to generate image. Please try again.")

