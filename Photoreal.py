# # # # import streamlit as st
# # # # import requests
# # # # import json
# # # # import psycopg2
# # # # from psycopg2.extras import execute_values
# # # # from leonardo_api import Leonardo

# # # # # Initialize the Leonardo API client
# # # # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # # # Default values for hidden parameters
# # # # model_id = "b24e16ff-06e3-43eb-8d33-4416c2d75876"
# # # # style_uuid = "111dc692-d470-4eec-b791-3475abac4c46"

# # # # # Database connection configuration
# # # # db_connection = {
# # # #     "host": "34.93.64.44",
# # # #     "port": "5432",
# # # #     "dbname": "genai",
# # # #     "user": "postgres",
# # # #     "password": "postgres-genai"
# # # # }

# # # # # Streamlit UI
# # # # st.title("Fashion Mood Board Generation")
# # # # st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # # # # Get user input for data parameters
# # # # prompt = st.text_area("Prompt")

# # # # width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
# # # # width_value= None
# # # # if width:
# # # #     try:
# # # #         width_value = int(width)
# # # #         if width_value < 100 or width_value > 1024:
# # # #             st.warning("Please enter a valid number for width values.")
# # # #     except ValueError:
# # # #         st.error("Please enter a valid number for width values.")
                      
# # # # height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
# # # # height_value = None
# # # # if height:
# # # #     try:
# # # #         height_value = int(height)
# # # #         if height_value < 100 or height_value > 1024:
# # # #             st.warning("Please enter a valid number for height values.")
# # # #     except ValueError:
# # # #         st.error("Please enter a valid number for height values.")

# # # # # Alchemy option
# # # # alchemy = st.radio("Alchemy", options=[True, False], index= None, help="Alchemy is used for the image quality")

# # # # if alchemy is not None:  # This checks if the user has made a selection
# # # #     if alchemy:
# # # #         st.info("Image quality will be good.")
# # # #     else:
# # # #         st.warning("Image quality will be moderate.")
        


# # # # # Define the URL and headers for the initial request
# # # # url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# # # # headers = {
# # # #     'accept': 'application/json',
# # # #     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
# # # #     'content-type': 'application/json'
# # # # }

# # # # # Validate and construct the payload
# # # # try:
# # # #     width_value = int(width) if width else 1024
# # # #     height_value = int(height) if height else 1024
    

        
# # # #     if not (100 <= width_value <= 1024):
# # # #         st.error("Width must be between 100 and 1024")
# # # #         st.stop()
    
# # # #     if not (100 <= height_value <= 1024):
# # # #         st.error("Height must be between 100 and 1024")
# # # #         st.stop()
    
# # # #     # Create the payload with correct parameter names
# # # #     data = {
# # # #         "modelId": model_id,
# # # #         "prompt": prompt,
# # # #         "width": width_value,
# # # #         "height": height_value,
# # # #         "photoReal":True,
# # # #         "photoRealStrength": 0.5,
# # # #         "presetStyle": "CINEMATIC",
# # # #         "alchemy": alchemy if alchemy is not None else False,
# # # #         "styleUUID": style_uuid,
# # # #     }

# # # # except ValueError as e:
# # # #     st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
# # # #     st.stop()

# # # # # PostgreSQL connection function
# # # # def store_in_database(prompt, contrast, num_images, width, height, image_path, enhanced_prompt=None):
# # # #     try:
# # # #         conn = psycopg2.connect(**db_connection)
# # # #         cursor = conn.cursor()
# # # #         query = """
# # # #             INSERT INTO leonardo_prompts (prompts, contrast, number_of_images, width, height, image_path, enhanced_prompts)
# # # #             VALUES (%s, %s, %s, %s, %s, %s, %s)
# # # #         """
# # # #         cursor.execute(query, (prompt, contrast, num_images, width, height, image_path, enhanced_prompt))
# # # #         conn.commit()
# # # #         cursor.close()
# # # #         conn.close()
# # # #         st.success("Data stored in the database successfully!")
# # # #     except Exception as e:
# # # #         st.error(f"Error storing data in the database: {e}")

# # # # # Trigger image generation on button click
# # # # if st.button('Generate Mood Board'):
# # # #     if not prompt.strip():
# # # #         st.error("Prompt is required.")
# # # #     else:
# # # #         # Send the initial POST request
# # # #         response = requests.post(url, headers=headers, data=json.dumps(data))

# # # #         # Check if the request was successful
# # # #         if response.status_code == 200:
# # # #             st.success("Request successful!")
# # # #             response_data = response.json()

# # # #             # Check if the response contains the necessary information
# # # #             if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
# # # #                 generation_id = response_data['sdGenerationJob']['generationId']

# # # #                 # Wait for the image generation to complete and retrieve the image data
# # # #                 imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

# # # #                 # Check if the 'url' key is present in the response
# # # #                 if 'url' in imageresponse:
# # # #                     image_url = imageresponse['url']

# # # #                     # Display the image in Streamlit
# # # #                     st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)
                    
# # # #                     # Store data in the database
# # # #                     store_in_database(prompt,  width_value, height_value, image_url)
# # # #                 else:
# # # #                     st.error("Image URL not found in the response.")
# # # #                     st.write("Response:", imageresponse)
# # # #             else:
# # # #                 st.error("Generation ID not found in the response.")
# # # #                 st.write("Response:", response_data)
# # # #         else:
# # # #             st.error(f"Request failed with status code {response.status_code}")
# # # #             st.write("Response:", response.text)


# # # # import streamlit as st
# # # # import requests
# # # # import json
# # # # from leonardo_api import Leonardo

# # # # # Initialize the Leonardo API client
# # # # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # # # Default values for hidden parameters
# # # # model_id = "b75a5b32-ca22-4b1d-bb0a-883c26783c71"
# # # # style_uuid = "111dc692-d470-4eec-b791-3475abac4c46"

# # # # # Streamlit UI
# # # # st.title("Fashion Mood Board Generation")
# # # # st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # # # # Get user input for data parameters
# # # # prompt = st.text_area("Prompt")

# # # # width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
# # # # width_value = None
# # # # if width:
# # # #     try:
# # # #         width_value = int(width)
# # # #         if width_value < 100 or width_value > 1024:
# # # #             st.warning("Please enter a valid number for width values.")
# # # #     except ValueError:
# # # #         st.error("Please enter a valid number for width values.")

# # # # height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
# # # # height_value = None
# # # # if height:
# # # #     try:
# # # #         height_value = int(height)
# # # #         if height_value < 100 or height_value > 1024:
# # # #             st.warning("Please enter a valid number for height values.")
# # # #     except ValueError:
# # # #         st.error("Please enter a valid number for height values.")

# # # # # Alchemy option
# # # # alchemy = st.radio("Alchemy", options=[True, False], index=None, help="Alchemy is used for the image quality")

# # # # if alchemy is not None:  # This checks if the user has made a selection
# # # #     if alchemy:
# # # #         st.info("Image quality will be good.")
# # # #     else:
# # # #         st.warning("Image quality will be moderate.")

# # # # # Define the URL and headers for the initial request
# # # # url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# # # # headers = {
# # # #     'accept': 'application/json',
# # # #     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
# # # #     'content-type': 'application/json'
# # # # }

# # # # # Validate and construct the payload
# # # # try:
# # # #     width_value = int(width) if width else 1024
# # # #     height_value = int(height) if height else 1024

# # # #     if not (100 <= width_value <= 1024):
# # # #         st.error("Width must be between 100 and 1024")
# # # #         st.stop()

# # # #     if not (100 <= height_value <= 1024):
# # # #         st.error("Height must be between 100 and 1024")
# # # #         st.stop()

# # # #     # Create the payload with correct parameter names
# # # #     data = {
# # # #         "modelId": model_id,
# # # #         "prompt": prompt,
# # # #         "width": width_value,
# # # #         "height": height_value,
# # # #         "photoReal": True,
# # # #         "photoRealStrength": 0.5,
# # # #         "presetStyle": "CINEMATIC",
# # # #         "alchemy": alchemy if alchemy is not None else False,
# # # #         "styleUUID": style_uuid,
# # # #     }

# # # # except ValueError as e:
# # # #     st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
# # # #     st.stop()

# # # # # Function to store the generated mood board details in a file (instead of a database)
# # # # def store_in_file(prompt, width, height, image_url, alchemy, photo_real, photo_real_strength, preset_style):
# # # #     try:
# # # #         # Store the details in a text file
# # # #         with open("mood_board_data.txt", "a") as file:
# # # #             file.write(f"Prompt: {prompt}\n")
# # # #             file.write(f"Width: {width}\n")
# # # #             file.write(f"Height: {height}\n")
# # # #             file.write(f"Image URL: {image_url}\n")
# # # #             file.write(f"Alchemy: {alchemy}\n")
# # # #             file.write(f"PhotoReal: {photo_real}\n")
# # # #             file.write(f"PhotoRealStrength: {photo_real_strength}\n")
# # # #             file.write(f"PresetStyle: {preset_style}\n")
# # # #             file.write("-" * 40 + "\n")
# # # #         st.success("Data stored in a file successfully!")
# # # #     except Exception as e:
# # # #         st.error(f"Error storing data in the file: {e}")

# # # # # Trigger image generation on button click
# # # # if st.button('Generate Mood Board'):
# # # #     if not prompt.strip():
# # # #         st.error("Prompt is required.")
# # # #     else:
# # # #         # Send the initial POST request
# # # #         response = requests.post(url, headers=headers, data=json.dumps(data))

# # # #         # Check if the request was successful
# # # #         if response.status_code == 200:
# # # #             st.success("Request successful!")
# # # #             response_data = response.json()

# # # #             # Check if the response contains the necessary information
# # # #             if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
# # # #                 generation_id = response_data['sdGenerationJob']['generationId']

# # # #                 # Wait for the image generation to complete and retrieve the image data
# # # #                 imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

# # # #                 # Check if the 'url' key is present in the response
# # # #                 if 'url' in imageresponse:
# # # #                     image_url = imageresponse['url']

# # # #                     # Display the image in Streamlit
# # # #                     st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)

# # # #                     # Store data in a file (instead of a database)
# # # #                     store_in_file(
# # # #                         prompt=prompt,
# # # #                         width=width_value,
# # # #                         height=height_value,
# # # #                         image_url=image_url,
# # # #                         alchemy=alchemy,
# # # #                         photo_real=True,  # Assuming True for photoReal
# # # #                         photo_real_strength=0.5,  # Use the predefined value or adjust as needed
# # # #                         preset_style="CINEMATIC"  # Or adjust to your desired preset
# # # #                     )
# # # #                 else:
# # # #                     st.error("Image URL not found in the response.")
# # # #                     st.write("Response:", imageresponse)
# # # #             else:
# # # #                 st.error("Generation ID not found in the response.")
# # # #                 st.write("Response:", response_data)
# # # #         else:
# # # #             st.error(f"Request failed with status code {response.status_code}")
# # # #             st.write("Response:", response.text)



# # # import streamlit as st
# # # import requests
# # # import json
# # # from leonardo_api import Leonardo

# # # # Initialize the Leonardo API client
# # # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # # Default values for hidden parameters
# # # model_id = "b75a5b32-ca22-4b1d-bb0a-883c26783c71"

# # # # Streamlit UI
# # # st.title("Fashion Mood Board Generation")
# # # st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # # # Get user input for data parameters
# # # prompt = st.text_area("Prompt")

# # # # Input for width and height
# # # width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
# # # width_value = None
# # # if width:
# # #     try:
# # #         width_value = int(width)
# # #         if width_value < 100 or width_value > 1024:
# # #             st.warning("Please enter a valid number for width values.")
# # #     except ValueError:
# # #         st.error("Please enter a valid number for width values.")

# # # height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
# # # height_value = None
# # # if height:
# # #     try:
# # #         height_value = int(height)
# # #         if height_value < 100 or height_value > 1024:
# # #             st.warning("Please enter a valid number for height values.")
# # #     except ValueError:
# # #         st.error("Please enter a valid number for height values.")

# # # # Alchemy option
# # # alchemy = st.radio("Alchemy", options=[True, False], index=None, help="Alchemy is used for the image quality")

# # # # Input for photoReal
# # # photo_real = st.checkbox("Enable Photo Realism", value=True)

# # # # Input for photoRealStrength (slider)
# # # photo_real_strength = st.slider("Photo Realism Strength", 0.0, 1.0, 0.5)

# # # # Input for presetStyle (selectbox)
# # # preset_styles = ["CINEMATIC", "VINTAGE", "FASHION", "ARTISTIC"]
# # # preset_style = st.selectbox("Select Style", options=preset_styles)

# # # if alchemy is not None:  # This checks if the user has made a selection
# # #     if alchemy:
# # #         st.info("Image quality will be good.")
# # #     else:
# # #         st.warning("Image quality will be moderate.")

# # # # Define the URL and headers for the initial request
# # # url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# # # headers = {
# # #     'accept': 'application/json',
# # #     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
# # #     'content-type': 'application/json'
# # # }

# # # # Validate and construct the payload
# # # try:
# # #     width_value = int(width) if width else 1024
# # #     height_value = int(height) if height else 1024

# # #     if not (100 <= width_value <= 1024):
# # #         st.error("Width must be between 100 and 1024")
# # #         st.stop()

# # #     if not (100 <= height_value <= 1024):
# # #         st.error("Height must be between 100 and 1024")
# # #         st.stop()

# # #     # Create the payload with correct parameter names
# # #     data = {
# # #         "modelId": model_id,
# # #         "prompt": prompt,
# # #         "width": width_value,
# # #         "height": height_value,
# # #         "photoReal": photo_real,
# # #         "photoRealStrength": photo_real_strength,
# # #         "presetStyle": preset_style,
# # #         "alchemy": alchemy if alchemy is not None else False,
    
# # #     }

# # # except ValueError as e:
# # #     st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
# # #     st.stop()

# # # # Function to store the generated mood board details in a file (instead of a database)
# # # def store_in_file(prompt, width, height, image_url, alchemy, photo_real, photo_real_strength, preset_style):
# # #     try:
# # #         # Store the details in a text file
# # #         with open("mood_board_data.txt", "a") as file:
# # #             file.write(f"Prompt: {prompt}\n")
# # #             file.write(f"Width: {width}\n")
# # #             file.write(f"Height: {height}\n")
# # #             file.write(f"Image URL: {image_url}\n")
# # #             file.write(f"Alchemy: {alchemy}\n")
# # #             file.write(f"PhotoReal: {photo_real}\n")
# # #             file.write(f"PhotoRealStrength: {photo_real_strength}\n")
# # #             file.write(f"PresetStyle: {preset_style}\n")
# # #             file.write("-" * 40 + "\n")
# # #         st.success("Data stored in a file successfully!")
# # #     except Exception as e:
# # #         st.error(f"Error storing data in the file: {e}")

# # # # Trigger image generation on button click
# # # if st.button('Generate Mood Board'):
# # #     if not prompt.strip():
# # #         st.error("Prompt is required.")
# # #     else:
# # #         # Send the initial POST request
# # #         response = requests.post(url, headers=headers, data=json.dumps(data))

# # #         # Check if the request was successful
# # #         if response.status_code == 200:
# # #             st.success("Request successful!")
# # #             response_data = response.json()

# # #             # Check if the response contains the necessary information
# # #             if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
# # #                 generation_id = response_data['sdGenerationJob']['generationId']

# # #                 # Wait for the image generation to complete and retrieve the image data
# # #                 imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

# # #                 # Check if the 'url' key is present in the response
# # #                 if 'url' in imageresponse:
# # #                     image_url = imageresponse['url']

# # #                     # Display the image in Streamlit
# # #                     st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)

# # #                     # Store data in a file (instead of a database)
# # #                     store_in_file(
# # #                         prompt=prompt,
# # #                         width=width_value,
# # #                         height=height_value,
# # #                         image_url=image_url,
# # #                         alchemy=alchemy,
# # #                         photo_real=photo_real,
# # #                         photo_real_strength=photo_real_strength,
# # #                         preset_style=preset_style
# # #                     )
# # #                 else:
# # #                     st.error("Image URL not found in the response.")
# # #                     st.write("Response:", imageresponse)
# # #             else:
# # #                 st.error("Generation ID not found in the response.")
# # #                 st.write("Response:", response_data)
# # #         else:
# # #             st.error(f"Request failed with status code {response.status_code}")
# # #             st.write("Response:", response.text)


# # import streamlit as st
# # import requests
# # import json
# # from leonardo_api import Leonardo

# # # Initialize the Leonardo API client
# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # Default values for hidden parameters
# # model_id = "aa77f04e-3eec-4034-9c07-d0f619684628"  # Update this with the correct model ID

# # # Streamlit UI
# # st.title("Fashion Mood Board Generation")
# # st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # # Get user input for data parameters
# # prompt = st.text_area("Prompt")

# # # Input for width and height
# # width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
# # width_value = None
# # if width:
# #     try:
# #         width_value = int(width)
# #         if width_value < 100 or width_value > 1024:
# #             st.warning("Please enter a valid number for width values.")
# #     except ValueError:
# #         st.error("Please enter a valid number for width values.")

# # height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
# # height_value = None
# # if height:
# #     try:
# #         height_value = int(height)
# #         if height_value < 100 or height_value > 1024:
# #             st.warning("Please enter a valid number for height values.")
# #     except ValueError:
# #         st.error("Please enter a valid number for height values.")

# # # Alchemy option
# # alchemy = st.radio("Alchemy", options=[True, False], index=None, help="Alchemy is used for the image quality")

# # # Input for photoReal
# # photo_real = st.checkbox("Enable Photo Realism", value=True)

# # # Input for photoRealStrength (slider)
# # photo_real_strength = st.slider("Photo Realism Strength", 0.0, 1.0, 0.5)

# # # Input for presetStyle (selectbox)
# # preset_styles = ["CINEMATIC", "VINTAGE", "FASHION", "ARTISTIC"]
# # preset_style = st.selectbox("Select Style", options=preset_styles)

# # if alchemy is not None:  # This checks if the user has made a selection
# #     if alchemy:
# #         st.info("Image quality will be good.")
# #     else:
# #         st.warning("Image quality will be moderate.")

# # # Define the URL and headers for the initial request
# # url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# # headers = {
# #     'accept': 'application/json',
# #     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
# #     'content-type': 'application/json'
# # }

# # # Validate and construct the payload
# # try:
# #     width_value = int(width) if width else 1024
# #     height_value = int(height) if height else 1024

# #     if not (100 <= width_value <= 1024):
# #         st.error("Width must be between 100 and 1024")
# #         st.stop()

# #     if not (100 <= height_value <= 1024):
# #         st.error("Height must be between 100 and 1024")
# #         st.stop()

# #     # Create the payload with correct parameter names
# #     data = {
# #         "modelId": model_id,
# #         "prompt": prompt,
# #         "width": width_value,
# #         "height": height_value,
# #         "photoReal": photo_real,
# #         "photoRealStrength": photo_real_strength,
# #         "presetStyle": preset_style,
# #         "alchemy": alchemy if alchemy is not None else False,
    
# #     }

# # except ValueError as e:
# #     st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
# #     st.stop()

# # # Function to store the generated mood board details in a file (instead of a database)
# # def store_in_file(prompt, width, height, image_url, alchemy, photo_real, photo_real_strength, preset_style):
# #     try:
# #         # Store the details in a text file
# #         with open("mood_board_data.txt", "a") as file:
# #             file.write(f"Prompt: {prompt}\n")
# #             file.write(f"Width: {width}\n")
# #             file.write(f"Height: {height}\n")
# #             file.write(f"Image URL: {image_url}\n")
# #             file.write(f"Alchemy: {alchemy}\n")
# #             file.write(f"PhotoReal: {photo_real}\n")
# #             file.write(f"PhotoRealStrength: {photo_real_strength}\n")
# #             file.write(f"PresetStyle: {preset_style}\n")
# #             file.write("-" * 40 + "\n")
# #         st.success("Data stored in a file successfully!")
# #     except Exception as e:
# #         st.error(f"Error storing data in the file: {e}")

# # # Trigger image generation on button click
# # if st.button('Generate Mood Board'):
# #     if not prompt.strip():
# #         st.error("Prompt is required.")
# #     else:
# #         # Send the initial POST request
# #         response = requests.post(url, headers=headers, data=json.dumps(data))

# #         # Check if the request was successful
# #         if response.status_code == 200:
# #             st.success("Request successful!")
# #             response_data = response.json()

# #             # Check if the response contains the necessary information
# #             if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
# #                 generation_id = response_data['sdGenerationJob']['generationId']

# #                 # Wait for the image generation to complete and retrieve the image data
# #                 imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

# #                 # Check if the 'url' key is present in the response
# #                 if 'url' in imageresponse:
# #                     image_url = imageresponse['url']

# #                     # Display the image in Streamlit
# #                     st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)

# #                     # Store data in a file (instead of a database)
# #                     store_in_file(
# #                         prompt=prompt,
# #                         width=width_value,
# #                         height=height_value,
# #                         image_url=image_url,
# #                         alchemy=alchemy,
# #                         photo_real=photo_real,
# #                         photo_real_strength=photo_real_strength,
# #                         preset_style=preset_style
# #                     )
# #                 else:
# #                     st.error("Image URL not found in the response.")
# #                     st.write("Response:", imageresponse)
# #             else:
# #                 st.error("Generation ID not found in the response.")
# #                 st.write("Response:", response_data)
# #         else:
# #             st.error(f"Request failed with status code {response.status_code}")
# #             st.write("Response:", response.text)

# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Default values for hidden parameters
# model_id = "b75a5b32-ca22-4b1d-bb0a-883c26783c71"  # Update this with the correct model ID

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Get user input for data parameters
# prompt = st.text_area("Prompt")

# # Input for width and height
# width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
# width_value = None
# if width:
#     try:
#         width_value = int(width)
#         if width_value < 100 or width_value > 1024:
#             st.warning("Please enter a valid number for width values.")
#     except ValueError:
#         st.error("Please enter a valid number for width values.")

# height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
# height_value = None
# if height:
#     try:
#         height_value = int(height)
#         if height_value < 100 or height_value > 1024:
#             st.warning("Please enter a valid number for height values.")
#     except ValueError:
#         st.error("Please enter a valid number for height values.")

# # Alchemy option
# alchemy = st.radio("Alchemy", options=[True, False], index=None, help="Alchemy is used for the image quality")

# # Input for photoReal
# photo_real = st.checkbox("Enable Photo Realism", value=True)

# # Input for photoRealStrength (slider)
# photo_real_strength = st.slider("Photo Realism Strength", 0.0, 1.0, 0.5)

# # Input for presetStyle (selectbox)
# preset_styles = ["CINEMATIC", "VINTAGE", "FASHION", "ARTISTIC"]
# preset_style = st.selectbox("Select Style", options=preset_styles)

# if alchemy is not None:  # This checks if the user has made a selection
#     if alchemy:
#         st.info("Image quality will be good.")
#     else:
#         st.warning("Image quality will be moderate.")

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Validate and construct the payload
# try:
#     width_value = int(width) if width else 512  # Default width to 512 if not provided
#     height_value = int(height) if height else 512  # Default height to 512 if not provided

#     if not (100 <= width_value <= 1024):
#         st.error("Width must be between 100 and 1024")
#         st.stop()

#     if not (100 <= height_value <= 1024):
#         st.error("Height must be between 100 and 1024")
#         st.stop()

#     # Create the payload with correct parameter names
#     data = {
#         "modelId": model_id,  # Update with the correct model ID if needed
#         "prompt": prompt,  # User input prompt
#         "width": width_value,  # Width from user input
#         "height": height_value,  # Height from user input
#         "alchemy": alchemy if alchemy is not None else False,  # Alchemy setting
#         "photoReal": photo_real,  # Photo Realism setting
#         "photoRealVersion": "v2",  # Set the photo realism version
#         "presetStyle": preset_style,  # Preset Style selected by the user
#     }

# except ValueError as e:
#     st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
#     st.stop()

# # Function to store the generated mood board details in a file (instead of a database)
# def store_in_file(prompt, width, height, image_url, alchemy, photo_real, photo_real_strength, preset_style):
#     try:
#         # Store the details in a text file
#         with open("mood_board_data.txt", "a") as file:
#             file.write(f"Prompt: {prompt}\n")
#             file.write(f"Width: {width}\n")
#             file.write(f"Height: {height}\n")
#             file.write(f"Image URL: {image_url}\n")
#             file.write(f"Alchemy: {alchemy}\n")
#             file.write(f"PhotoReal: {photo_real}\n")
#             file.write(f"PhotoRealStrength: {photo_real_strength}\n")
#             file.write(f"PresetStyle: {preset_style}\n")
#             file.write("-" * 40 + "\n")
#         st.success("Data stored in a file successfully!")
#     except Exception as e:
#         st.error(f"Error storing data in the file: {e}")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     if not prompt.strip():
#         st.error("Prompt is required.")
#     else:
#         # Send the initial POST request
#         response = requests.post(url, headers=headers, data=json.dumps(data))

#         # Check if the request was successful
#         if response.status_code == 200:
#             st.success("Request successful!")
#             response_data = response.json()

#             # Check if the response contains the necessary information
#             if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#                 generation_id = response_data['sdGenerationJob']['generationId']

#                 # Wait for the image generation to complete and retrieve the image data
#                 imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

#                 # Check if the 'url' key is present in the response
#                 if 'url' in imageresponse:
#                     image_url = imageresponse['url']

#                     # Display the image in Streamlit
#                     st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)

#                     # Store data in a file (instead of a database)
#                     store_in_file(
#                         prompt=prompt,
#                         width=width_value,
#                         height=height_value,
#                         image_url=image_url,
#                         alchemy=alchemy,
#                         photo_real=photo_real,
#                         photo_real_strength=photo_real_strength,
#                         preset_style=preset_style
#                     )
#                 else:
#                     st.error("Image URL not found in the response.")
#                     st.write("Response:", imageresponse)
#             else:
#                 st.error("Generation ID not found in the response.")
#                 st.write("Response:", response_data)
#         else:
#             st.error(f"Request failed with status code {response.status_code}")
#             st.write("Response:", response.text)


import streamlit as st
import requests
import json
from leonardo_api import Leonardo
import toml

# Load secrets from secrets.toml
secrets = toml.load("secrets.toml")
api_key = secrets["general"]["LEONARDO_API_KEY"]

# Initialize the Leonardo API client with the API key from secrets.toml
leonardo = Leonardo(auth_token=api_key)

# Default values for hidden parameters
model_id = "aa77f04e-3eec-4034-9c07-d0f619684628"  # Update this with the correct model ID

# Streamlit UI
st.title("Fashion Mood Board Generation")
st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# Get user input for data parameters
prompt = st.text_area("Prompt")

# Input for width and height
width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
width_value = None
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

# Input for photoReal
photo_real = st.checkbox("Enable Photo Realism", value=True)

# Input for photoRealStrength (slider)
photo_real_strength = st.slider("Photo Realism Strength", 0.0, 1.0, 0.5)

# Input for presetStyle (selectbox)
preset_styles = ["CINEMATIC", "VINTAGE", "FASHION", "ARTISTIC"]
preset_style = st.selectbox("Select Style", options=preset_styles)

if alchemy is not None:  # This checks if the user has made a selection
    if alchemy:
        st.info("Image quality will be good.")
    else:
        st.warning("Image quality will be moderate.")

# Define the URL and headers for the initial request
url = "https://cloud.leonardo.ai/api/rest/v1/generations"
headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {api_key}',
    'content-type': 'application/json'
}

# Validate and construct the payload
try:
    width_value = int(width) if width else 512  # Default width to 512 if not provided
    height_value = int(height) if height else 512  # Default height to 512 if not provided

    if not (100 <= width_value <= 1024):
        st.error("Width must be between 100 and 1024")
        st.stop()

    if not (100 <= height_value <= 1024):
        st.error("Height must be between 100 and 1024")
        st.stop()

    # Create the payload with correct parameter names
    data = {
        "modelId": model_id,  # Update with the correct model ID if needed
        "prompt": prompt,  # User input prompt
        "width": width_value,  # Width from user input
        "height": height_value,  # Height from user input
        "alchemy": alchemy if alchemy is not None else False,  # Alchemy setting
        "photoReal": photo_real,  # Photo Realism setting
        "photoRealVersion": "v2",  # Set the photo realism version
        "presetStyle": preset_style,  # Preset Style selected by the user
    }

except ValueError as e:
    st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
    st.stop()

# Function to store the generated mood board details in a file (instead of a database)
def store_in_file(prompt, width, height, image_url, alchemy, photo_real, photo_real_strength, preset_style):
    try:
        # Store the details in a text file
        with open("mood_board_data.txt", "a") as file:
            file.write(f"Prompt: {prompt}\n")
            file.write(f"Width: {width}\n")
            file.write(f"Height: {height}\n")
            file.write(f"Image URL: {image_url}\n")
            file.write(f"Alchemy: {alchemy}\n")
            file.write(f"PhotoReal: {photo_real}\n")
            file.write(f"PhotoRealStrength: {photo_real_strength}\n")
            file.write(f"PresetStyle: {preset_style}\n")
            file.write("-" * 40 + "\n")
        st.success("Data stored in a file successfully!")
    except Exception as e:
        st.error(f"Error storing data in the file: {e}")

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

                    # Store data in a file (instead of a database)
                    store_in_file(
                        prompt=prompt,
                        width=width_value,
                        height=height_value,
                        image_url=image_url,
                        alchemy=alchemy,
                        photo_real=photo_real,
                        photo_real_strength=photo_real_strength,
                        preset_style=preset_style
                    )
                else:
                    st.error("Image URL not found in the response.")
                    st.write("Response:", imageresponse)
            else:
                st.error("Generation ID not found in the response.")
                st.write("Response:", response_data)
        else:
            st.error(f"Request failed with status code {response.status_code}")
            st.write("Response:", response.text)
