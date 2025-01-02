import streamlit as st
import requests
import json
import psycopg2
import os
from leonardo_api import Leonardo
import toml

# Load secrets (either locally or via Streamlit Cloud)
try:
    # Locally load secrets from secrets.toml
    secrets = toml.load(".streamlit/secrets.toml")
    api_key = secrets["general"]["LEONARDO_API_KEY"]
except FileNotFoundError:
    # Fallback to environment variable if secrets.toml is not found
    api_key = os.getenv("LEONARDO_API_KEY")
    if not api_key:
        st.error("API Key not found in either 'secrets.toml' or environment variables.")
        st.stop()

# Initialize the Leonardo API client with the API key
leonardo = Leonardo(auth_token=api_key)

# Default values for hidden parameters
model_id = "b24e16ff-06e3-43eb-8d33-4416c2d75876"
style_uuid = "111dc692-d470-4eec-b791-3475abac4c46"

# Database connection configuration
db_connection = {
    "host": "34.93.64.44",
    "port": "5432",
    "dbname": "genai",
    "user": "postgres",
    "password": "postgres-genai"
}

# Streamlit UI
st.title("Fashion Mood Board Generation")
st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# Get user input for data parameters
prompt = st.text_area("Prompt")
num_images = st.text_input("Number of Images", placeholder="Enter no of images between 1 and 8")
if num_images:
    try:
        num_images_value = int(num_images)
        if num_images_value < 1 or num_images_value > 8:
            st.warning("Please enter a value for Number of Images between 1 and 8.")
    except ValueError:
        st.error("Please enter a valid number for Number of Images.")

contrast = st.text_input("Contrast", placeholder="Enter the value between 1 and 4")
contrast_value = None
if contrast:
    try:
        contrast_value = int(contrast)
        if contrast_value < 1 or contrast_value > 4:
            st.warning("Please enter a valid number for contrast values.")
    except ValueError:
        st.error("Please enter a valid number for contrast values.")
        
width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
width_value= None
if width:
    try:
        width_value = int(width)
        if width_value < 100 or width_value > 1024:
            st.warning("Please enter a valid number for width values.")
    except ValueError:
        st.error("Please enter a valid number for width values.")
                      
height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
height_value = None
if height:
    try:
        height_value = int(height)
        if height_value < 100 or height_value > 1024:
            st.warning("Please enter a valid number for height values.")
    except ValueError:
        st.error("Please enter a valid number for height values.")

# Alchemy option
alchemy = st.radio("Alchemy", options=[True, False], index=None, help="Alchemy is used for the image quality")

if alchemy is not None:
    if alchemy:
        st.info("Image quality will be good.")
    else:
        st.warning("Image quality will be moderate.")

# Enhance Prompt option
enhance_prompt = st.radio("Enhance Prompt", options=[True, False], index=None, help="Enhance Prompt is used to give the prompt details further")

# Conditionally capture enhanced prompt
enhanced_prompt = None
if enhance_prompt:
    enhanced_prompt = st.text_area("Enhanced Prompt Details", placeholder="Provide additional details to refine the prompt.")

# Define the URL and headers for the initial request
url = "https://cloud.leonardo.ai/api/rest/v1/generations"
headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {api_key}',
    'content-type': 'application/json'
}

# Validate and construct the payload
try:
    num_images_value = int(num_images) if num_images else 1
    width_value = int(width) if width else 1024
    height_value = int(height) if height else 1024
    
    # Set contrast value (default to 1 if not provided)
    contrast_value = int(contrast) if contrast else 1
    
    # Validate all inputs are within acceptable ranges
    if not (1 <= num_images_value <= 8):
        st.error("Number of images must be between 1 and 8")
        st.stop()
        
    if not (1 <= contrast_value <= 4):
        st.error("Contrast must be between 1 and 4")
        st.stop()
        
    if not (100 <= width_value <= 1024):
        st.error("Width must be between 100 and 1024")
        st.stop()
    
    if not (100 <= height_value <= 1024):
        st.error("Height must be between 100 and 1024")
        st.stop()
    
    # Create the payload with correct parameter names
    data = {
        "modelId": model_id,
        "prompt": prompt,
        "num_images": num_images_value,
        "width": width_value,
        "height": height_value,
        "contrast": int(contrast_value),
        "alchemy": alchemy if alchemy is not None else False,
        "styleUUID": style_uuid,
        "enhancePrompt": enhanced_prompt if enhanced_prompt is not None else False
    }

except ValueError as e:
    st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
    st.stop()

# PostgreSQL connection function
def store_in_database(prompt, contrast, num_images, width, height, image_path, enhanced_prompt=None):
    try:
        conn = psycopg2.connect(**db_connection)
        cursor = conn.cursor()
        query = """
            INSERT INTO leonardo_prompts (prompts, contrast, number_of_images, width, height, image_path, enhanced_prompts)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (prompt, contrast, num_images, width, height, image_path, enhanced_prompt))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Data stored in the database successfully!")
    except Exception as e:
        st.error(f"Error storing data in the database: {e}")

# Trigger image generation on button click
if st.button('Generate Mood Board'):
    if not prompt.strip():
        st.error("Prompt is required.")
    else:
        # Send the initial POST request
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check if the request was successful
        if response.status_code == 200:
            st.success("Request successful!")
            response_data = response.json()

            # Check if the response contains the necessary information
            if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
                generation_id = response_data['sdGenerationJob']['generationId']

                # Wait for the image generation to complete and retrieve the image data
                imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

                # Check if the 'url' key is present in the response
                if 'url' in imageresponse:
                    image_url = imageresponse['url']

                    # Display the image in Streamlit
                    st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)
                    
                    # Store data in the database
                    store_in_database(prompt, contrast_value, num_images_value, width_value, height_value, image_url, enhanced_prompt)
                else:
                    st.error("Image URL not found in the response.")
                    st.write("Response:", imageresponse)
            else:
                st.error("Generation ID not found in the response.")
                st.write("Response:", response_data)
        else:
            st.error(f"Request failed with status code {response.status_code}")
            st.write("Response:", response.text)
