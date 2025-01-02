# # from leonardo_api import Leonardo

# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # response = leonardo.get_user_info()  # get your user info
# # print(response)


# # response = leonardo.post_generations(prompt="""You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces.

# # Design Brief:
# # Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs.

# # Key considerations:

# # Maintain clean, youthful silhouettes appropriate for young girls.
# # Highlight crinkled fabric textures for added visual appeal.
# # Incorporate wooden beads as an accent to emphasize craftsmanship.
# # Use a warm, natural color palette that balances earthy tones with vibrant orange.
# # Include a model on the runway wearing the collection to complete the visual narrative.""", num_images=1,
# #                                            negative_prompt='Unstructured or messy collage layout, inconsistent spacing between images, individual photos not arranged in a grid or clean visual order, images without a color palette at the bottom, missing cohesive theme, overly busy or cluttered design, sharp shadows, mismatched lighting, irrelevant fashion styles or accessories, overly complex or abstract patterns, lack of crinkled fabric textures, unrelated or low-quality runway images,missing artisanal wooden bead details, washed-out colors, overly bright tones, absence of minimalistic and rounded silhouettes, blurry or pixelated images, chaotic backgrounds, inconsistent alignment, unrelated accessories, lack of visual balance.',
# #                                            model_id='e316348f-7773-490e-adcd-46757c738eb7', width=1024, height=768,
# #                                            guidance_scale=2)

# #         #e316348f-7773-490e-adcd-46757c738eb7
# # print(response)
# # response = leonardo.wait_for_image_generation(generation_id=response['sdGenerationJob']['generationId'])

# # print(response)



# import streamlit as st
# from leonardo_api import Leonardo

# # Initialize Leonardo API
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Streamlit UI
# st.set_page_config(page_title="AI Image Generator", layout="wide")
# st.title("AI Image Generator")
# st.write("Generate images based on your positive and negative text prompts using Leonardo AI!")

# # Input: Positive Prompt
# positive_prompt = st.text_area("Enter Positive Prompt:", height=150)

# # Input: Negative Prompt
# negative_prompt = st.text_area("Enter Negative Prompt:", height=150)

# # Input: Number of Images
# num_images = st.number_input("Number of Images to Generate", min_value=1, max_value=100, value=1, step=1)

# # Input: Aspect Ratio
# aspect_ratios = {
#     "2:3": (1024, 1536),  # 2:3 aspect ratio
#     "1:1": (1024, 1024),  # 1:1 aspect ratio
#     "16:9": (1920, 1080),  # 16:9 aspect ratio
# }

# st.write("Select an aspect ratio for the generated image:")
# aspect_ratio_choice = st.radio("Aspect Ratio:", ["2:3", "1:1", "16:9"])

# # Map user input to dimensions
# width, height = aspect_ratios[aspect_ratio_choice]

# # Select Generation Mode (Fast, Quality, Ultra)
# generation_mode = st.selectbox("Select Generation Mode:", ["Fast", "Quality", "Ultra"])

# # Button to trigger image generation
# if st.button("Generate Image"):

#     if positive_prompt:  # Check if the positive prompt is provided
#         try:
#             # API Request Payload
#             payload = {
#                 "prompt": positive_prompt,
#                 "negative_prompt": negative_prompt,
#                 "num_images": num_images,
#                 "width": width,
#                 "height": height,
#                 "alchemy": True,
#                 "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",  # Example style UUID
#                 "generation_mode": generation_mode,  # Include the generation mode in the request
#             }

#             # Headers
#             headers = {
#                 "Authorization": f"Bearer {leonardo.auth_token}",
#                 "Content-Type": "application/json"
#             }

#             # Make the API call
#             response = leonardo.post_generations(payload=payload, headers=headers)

#             # Wait for image generation to complete
#             generation_id = response['sdGenerationJob']['generationId']
#             st.write("Image Generation in Progress...")

#             # Wait for completion (you may want to add a check for the generation status here)
#             image_response = leonardo.wait_for_image_generation(generation_id=generation_id)

#             # Display the generated images
#             generated_images = image_response.get("generations", [])
#             if generated_images:
#                 for img in generated_images:
#                     st.image(img["url"], caption="Generated Image", use_column_width=True)
#             else:
#                 st.error("No images were generated. Please try again.")
        
#         except Exception as e:
#             st.error(f"Error generating images: {e}")

#     else:
#         st.warning("Please enter a positive prompt to generate images.")



# # import streamlit as st
# # from leonardo_api import Leonardo

# # # Initialize Leonardo API
# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # Streamlit UI
# # st.set_page_config(page_title="AI Image Generator", layout="wide")
# # st.title("AI Image Generator")
# # st.write("Generate images based on your text prompts using Leonardo AI!")

# # # Prompt Input
# # prompt = st.text_area("Enter your prompt:", height=150)

# # # Aspect Ratio Selection
# # st.write("### Select an aspect ratio for the generated image:")
# # aspect_ratio = st.radio(
# #     label="Aspect Ratio",
# #     options=["2:3", "1:1", "16:9"],
# #     index=1  # Default to 1:1
# # )

# # # Map aspect ratios to dimensions
# # aspect_ratios = {
# #     "2:3": (1024, 1536),
# #     "1:1": (1024, 1024),
# #     "16:9": (1920, 1080),
# # }
# # width, height = aspect_ratios[aspect_ratio]

# # # Number of Images
# # num_images = st.slider("Number of Images to Generate", min_value=1, max_value=4, value=1)

# # # Guidance Scale
# # guidance_scale = st.slider("Guidance Scale", min_value=1, max_value=20, value=7)

# # # Button to Generate Images
# # if st.button("Generate Images"):
# #     if prompt:
# #         try:
# #             # Call the Leonardo API
# #             with st.spinner("Generating images..."):
# #                 response = leonardo.post_generations(
# #                     prompt=prompt,
# #                     num_images=num_images,
# #                     negative_prompt="""Unstructured or messy collage layout, inconsistent spacing between images, 
# #                     individual photos not arranged in a grid or clean visual order, images without a color palette at the bottom, 
# #                     missing cohesive theme, overly busy or cluttered design, sharp shadows, mismatched lighting, irrelevant fashion 
# #                     styles or accessories, overly complex or abstract patterns, lack of crinkled fabric textures, unrelated or 
# #                     low-quality runway images, missing artisanal wooden bead details, washed-out colors, overly bright tones, 
# #                     absence of minimalistic and rounded silhouettes, blurry or pixelated images, chaotic backgrounds, inconsistent 
# #                     alignment, unrelated accessories, lack of visual balance.""",
# #                     model_id='e316348f-7773-490e-adcd-46757c738eb7',
# #                     width=width,
# #                     height=height,
# #                     guidance_scale=guidance_scale,
# #                 )
# #                 generation_id = response['sdGenerationJob']['generationId']
# #                 response = leonardo.wait_for_image_generation(generation_id=generation_id)

# #             # Display the Generated Images
# #             if response.get("generations"):
# #                 st.success("Image Generation Complete!")
# #                 for image in response["generations"]:
# #                     st.image(image["url"], width=300)
# #             else:
# #                 st.error("No images were generated. Please try again.")

# #         except Exception as e:
# #             st.error(f"Error generating images: {e}")
# #     else:
# #         st.warning("Please enter a prompt to generate images.")



# # from leonardo_api import Leonardo

# # # Initialize Leonardo API
# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # Define image dimensions for different aspect ratios
# # aspect_ratios = {
# #     "2:3": (1024, 1536),  # 2:3 aspect ratio
# #     "1:1": (1024, 1024),  # 1:1 aspect ratio
# #     "16:9": (1920, 1080), # 16:9 aspect ratio
# # }

# # # User selection for aspect ratio
# # print("Select an aspect ratio for the generated image:")
# # print("1. 2:3\n2. 1:1\n3. 16:9")
# # choice = input("Enter the number corresponding to your choice: ")

# # # Map user input to dimensions
# # if choice == "1":
# #     width, height = aspect_ratios["2:3"]
# # elif choice == "2":
# #     width, height = aspect_ratios["1:1"]
# # elif choice == "3":
# #     width, height = aspect_ratios["16:9"]
# # else:
# #     print("Invalid choice. Defaulting to 1:1.")
# #     width, height = aspect_ratios["1:1"]

# # # Get User Info
# # response = leonardo.get_user_info()
# # print("User Info:", response)

# # # Call the API for image generation
# # response = leonardo.post_generations(
# #     prompt="""You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces.

# #     Design Brief:
# #     Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs.

# #     Key considerations:

# #     Maintain clean, youthful silhouettes appropriate for young girls.
# #     Highlight crinkled fabric textures for added visual appeal.
# #     Incorporate wooden beads as an accent to emphasize craftsmanship.
# #     Use a warm, natural color palette that balances earthy tones with vibrant orange.
# #     Include a model on the runway wearing the collection to complete the visual narrative.""",
# #     num_images=1,
# #     negative_prompt="""Unstructured or messy collage layout, inconsistent spacing between images, 
# #     individual photos not arranged in a grid or clean visual order, images without a color palette at the bottom, 
# #     missing cohesive theme, overly busy or cluttered design, sharp shadows, mismatched lighting, irrelevant fashion 
# #     styles or accessories, overly complex or abstract patterns, lack of crinkled fabric textures, unrelated or 
# #     low-quality runway images, missing artisanal wooden bead details, washed-out colors, overly bright tones, 
# #     absence of minimalistic and rounded silhouettes, blurry or pixelated images, chaotic backgrounds, inconsistent 
# #     alignment, unrelated accessories, lack of visual balance.""",
# #     model_id='e316348f-7773-490e-adcd-46757c738eb7',
# #     width=width,   # Dynamic width based on aspect ratio
# #     height=height, # Dynamic height based on aspect ratio
# #     guidance_scale=2
# # )

# # # Wait for Image Generation to Complete
# # generation_id = response['sdGenerationJob']['generationId']
# # print("Image Generation in Progress...")

# # response = leonardo.wait_for_image_generation(generation_id=generation_id)

# # # Display Response
# # print("Image Generation Complete!")
# # print("Generated Images:", response)



# import requests
# import json
# from leonardo_api import Leonardo


# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')
# # Define the URL and headers
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data)
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     # "alchemy": False,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Send the POST request
# response = requests.post(url, headers=headers, data=json.dumps(data))


# # Check the response
# if response.status_code == 200:
#     print("Request successful!")
#     print("Response:", response.json())  # Assuming the API returns JSON data
#     response_data=response.json()
#     imageresponse = leonardo.wait_for_image_generation(generation_id=response_data['sdGenerationJob']['generationId'])
#     print(imageresponse)
# else:
#     print(f"Request failed with status code {response.status_code}")
#     print("Response:", response.text)


# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Send the initial POST request
# response = requests.post(url, headers=headers, data=json.dumps(data))

# # Check if the request was successful
# if response.status_code == 200:
#     print("Request successful!")
#     response_data = response.json()
#     generation_id = response_data['sdGenerationJob']['generationId']
#     print("Generation ID:", generation_id)

#     # Wait for the image generation to complete and retrieve the image data
#     imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#     print("Image Generation Response:", imageresponse)

#     # Get the single generation details using the obtained generation_id
#     generation_details = leonardo.get_single_generation(generation_id=generation_id)
#     print("Single Generation Response:", generation_details)
# else:
#     print(f"Request failed with status code {response.status_code}")
#     print("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()
#         generation_id = response_data['sdGenerationJob']['generationId']
#         st.write("Generation ID:", generation_id)

#         # Wait for the image generation to complete and retrieve the image data
#         imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#         st.write("Image Generation Response:", imageresponse)

#         # Get the image URL from the response
#         image_url = imageresponse['sdGenerationJob']['imageUrl']
#         st.write("Image URL:", image_url)

#         # Display the image in Streamlit
#         st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()
#         generation_id = response_data['generationId']
#         st.write("Generation ID:", generation_id)

#         # Wait for the image generation to complete and retrieve the image data
#         imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#         st.write("Image Generation Response:", imageresponse)

#         # Check if the image URL is present in the response
#         if 'imageUrl' in imageresponse:
#             image_url = imageresponse['imageUrl']
#             st.write("Image URL:", image_url)

#             # Display the image in Streamlit
#             st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#         else:
#             st.error("Image URL not found in the response.")
#             st.write("Response:", imageresponse)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "alchemy":False,
#     # "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'generationId' in response_data:
#             generation_id = response_data['generationId']
#             st.write("Generation ID:", generation_id)

#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             st.write("Image Generation Response:", imageresponse)

#             # Check if the image URL is present in the response
#             if 'imageUrl' in imageresponse:
#                 image_url = imageresponse['imageUrl']
#                 st.write("Image URL:", image_url)

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)



# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "alchemy": False,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#             generation_id = response_data['sdGenerationJob']['generationId']
#             st.write("Generation ID:", generation_id)

#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             st.write("Image Generation Response:", imageresponse)

#             # Check if the image URL is present in the response
#             if 'imageUrl' in imageresponse:
#                 image_url = imageresponse['imageUrl']
#                 st.write("Image URL:", image_url)

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "alchemy": False,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#             generation_id = response_data['sdGenerationJob']['generationId']
#             st.write("Generation ID:", generation_id)

#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             st.write("Image Generation Response:", imageresponse)

#             # Check if the 'url' key is present in the response
#             if 'url' in imageresponse:
#                 image_url = imageresponse['url']
#                 st.write("Image URL:", image_url)

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)



# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Get user input for data parameters
# model_id = st.text_input("Model ID", "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3")
# contrast = st.number_input("Contrast", min_value=0.0, max_value=10.0)
# prompt = st.text_area("Prompt")
# num_images = st.number_input("Number of Images", min_value=1, max_value=10)
# width = st.number_input("Width", min_value=100, max_value=2048)      #, value=1472
# height = st.number_input("Height", min_value=100, max_value=2048)    #, value=832
# alchemy = st.checkbox("Alchemy", value=False)
# style_uuid = st.text_input("Style UUID", "111dc692-d470-4eec-b791-3475abac4c46")
# enhance_prompt = st.checkbox("Enhance Prompt", value=True)

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": model_id,
#     "contrast": contrast,
#     "prompt": prompt,
#     "num_images": num_images,
#     "width": width,
#     "height": height,
#     "alchemy": alchemy,
#     "styleUUID": style_uuid,
#     "enhancePrompt": enhance_prompt
# }

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#             generation_id = response_data['sdGenerationJob']['generationId']
#             # st.write("Generation ID:", generation_id)                    ###################################################################### commented 


#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             # st.write("Image Generation Response:", imageresponse)         ###################################################################### commented 


#             # Check if the 'url' key is present in the response
#             if 'url' in imageresponse:
#                 image_url = imageresponse['url']
#                 # st.write("Image URL:", image_url)        ###################################################################### commented 

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)




import streamlit as st
import requests
import json
import psycopg2
from psycopg2.extras import execute_values
from leonardo_api import Leonardo
import toml

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')
# Load secrets from secrets.toml
secrets = toml.load("secrets.toml")
api_key = secrets["general"]["LEONARDO_API_KEY"]

# Initialize the Leonardo API client with the API key from secrets.toml
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

# alchemy = st.checkbox("Alchemy", value=False)
# enhance_prompt = st.checkbox("Enhance Prompt", value=True)

# Alchemy option
alchemy = st.radio("Alchemy", options=[True, False], index= None, help="Alchemy is used for the image quality")

if alchemy is not None:  # This checks if the user has made a selection
    if alchemy:
        st.info("Image quality will be good.")
    else:
        st.warning("Image quality will be moderate.")
        


# Enhance Prompt option
enhance_prompt = st.radio("Enhance Prompt", options=[True, False], index= None, help= "Enhance Prompt is used to give the prompt details further")

# Conditionally capture enhanced prompt
enhanced_prompt = None
if enhance_prompt:
    enhanced_prompt = st.text_area("Enhanced Prompt Details", 
                                        placeholder="Provide additional details to refine the prompt.")

# Define the URL and headers for the initial request
url = "https://cloud.leonardo.ai/api/rest/v1/generations"
headers = {
    'accept': 'application/json',
    'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
    'content-type': 'application/json'
}

# Validate and construct the payload
try:
    # Convert inputs to appropriate types with proper default values
    # contrast_value = int(contrast) if contrast else 1
    num_images_value = int(num_images) if num_images else 1
    width_value = int(width) if width else 1024
    height_value = int(height) if height else 1024
    
    # Set contrast value (changing how we handle it)
    if contrast:
        contrast_value = int(contrast)
    else:
        contrast_value = 1
   
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
        "num_images": num_images_value,  # Changed back to num_images
        "width": width_value,
        "height": height_value,
        "contrast":int(contrast_value),
        "alchemy": alchemy if alchemy is not None else False,
        # "ultra": ultra  if ultra  is not None else False,
        "styleUUID": style_uuid,
        "enhancePrompt": enhance_prompt if enhance_prompt is not None else False
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


# import streamlit as st
# import requests
# import json
# import psycopg2
# from psycopg2.extras import execute_values
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Default values for hidden parameters
# model_id = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"
# style_uuid = "111dc692-d470-4eec-b791-3475abac4c46"

# # Database connection configuration
# db_connection = {
#     "host": "34.93.64.44",
#     "port": "5432",
#     "dbname": "genai",
#     "user": "postgres",
#     "password": "postgres-genai"
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Get user input for data parameters
# prompt = st.text_area("Prompt", help="Enter your detailed prompt for the mood board")

# # Number of images with text input and validation
# num_images = st.text_input("Number of Images", 
#                           placeholder="Enter a value between 1 and 8",
#                           help="Number of images to generate (1-8)")

# # Validate number of images
# num_images_value = None
# if num_images:
#     try:
#         num_images_value = int(num_images)
#         if num_images_value < 1 or num_images_value > 8:
#             st.warning("Please enter a value between 1 and 8 for Number of Images.")
#     except ValueError:
#         st.error("Please enter a valid number for Number of Images.")

# # Contrast with text input and validation
# contrast = st.text_input("Contrast",
#                         placeholder="Enter a value between 1 and 4",
#                         help="Higher values create more contrast (1-4)")

# # Validate contrast
# contrast_value = None
# if contrast:
#     try:
#         contrast_value = int(contrast)
#         if contrast_value < 1 or contrast_value > 4:
#             st.warning("Please enter a value between 1 and 4 for Contrast.")
#     except ValueError:
#         st.error("Please enter a valid number for Contrast.")

# # Width and height with text input and validation
# width = st.text_input("Width",
#                      placeholder="Enter a value between 100 and 1024",
#                      help="Image width in pixels (100-1024)")

# # Validate width
# width_value = None
# if width:
#     try:
#         width_value = int(width)
#         if width_value < 100 or width_value > 1024:
#             st.warning("Please enter a value between 100 and 1024 for Width.")
#     except ValueError:
#         st.error("Please enter a valid number for Width.")

# height = st.text_input("Height",
#                       placeholder="Enter a value between 100 and 1024",
#                       help="Image height in pixels (100-1024)")

# # Validate height
# height_value = None
# if height:
#     try:
#         height_value = int(height)
#         if height_value < 100 or height_value > 1024:
#             st.warning("Please enter a value between 100 and 1024 for Height.")
#     except ValueError:
#         st.error("Please enter a valid number for Height.")

# # Alchemy option
# alchemy = st.radio(
#     "Alchemy",
#     options=["Yes", "No"],
#     index=0,
#     help="Alchemy improves image quality and coherence. Recommended for better results."
# )
# alchemy_bool = alchemy == "Yes"

# # Enhance Prompt option
# enhance_prompt = st.radio(
#     "Enhance Prompt",
#     options=["Yes", "No"],
#     index=0,
#     help="Allow AI to enhance your prompt for better results"
# )
# enhance_prompt_bool = enhance_prompt == "Yes"

# # Additional prompt details if enhance_prompt is enabled
# enhanced_prompt = None
# if enhance_prompt_bool:
#     enhanced_prompt = st.text_area(
#         "Enhanced Prompt Details",
#         placeholder="Add additional context or details to refine the generated images",
#         help="Provide more specific details about style, colors, composition, etc."
#     )

# # Define the URL and headers
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Construct the payload with proper parameter handling
# def create_payload():
#     if not all([num_images_value, contrast_value, width_value, height_value]):
#         raise ValueError("All numeric values must be provided and valid")
    
#     base_prompt = prompt
#     if enhance_prompt_bool and enhanced_prompt:
#         base_prompt = f"{prompt}. Additional details: {enhanced_prompt}"
    
#     return {
#         "modelId": model_id,
#         "prompt": base_prompt,
#         "num_images": num_images_value,
#         "width": width_value,
#         "height": height_value,
#         "contrast": contrast_value,
#         "alchemy": alchemy_bool,
#         "styleUUID": style_uuid,
#         "enhancePrompt": enhance_prompt_bool,
#         "promptMagic": True,  # Enable prompt magic for better results
#         "highContrast": contrast_value >= 3,  # Enable high contrast for values 3 and 4
#         "highResolution": True  # Request high resolution output
#     }

# # PostgreSQL connection function with error handling
# def store_in_database(prompt, contrast, num_images, width, height, image_path, enhanced_prompt=None):
#     try:
#         conn = psycopg2.connect(**db_connection)
#         cursor = conn.cursor()
#         query = """
#             INSERT INTO leonardo_prompts 
#             (prompts, contrast, number_of_images, width, height, image_path, enhanced_prompts)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """
#         cursor.execute(query, (prompt, contrast, num_images, width, height, image_path, enhanced_prompt))
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return True
#     except Exception as e:
#         st.error(f"Database error: {str(e)}")
#         return False

# # Generate images with progress indication
# def generate_images():
#     if not prompt.strip():
#         st.error("Please enter a prompt before generating images.")
#         return

#     with st.spinner("Generating your mood board..."):
#         try:
#             # Create payload and validate all required values are present
#             payload = create_payload()
            
#             # Send the initial request
#             response = requests.post(url, headers=headers, json=payload)
#             response.raise_for_status()
            
#             response_data = response.json()
#             generation_id = response_data['sdGenerationJob']['generationId']
            
#             # Wait for generation with progress bar
#             progress_bar = st.progress(0)
#             for i in range(100):
#                 progress_bar.progress(i + 1)
#                 if i == 50:  # Check status halfway
#                     imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#                     if 'url' in imageresponse:
#                         break
            
#             if 'url' in imageresponse:
#                 st.success("Generation completed successfully!")
#                 st.image(imageresponse['url'], caption='Generated Fashion Mood Board', use_column_width=True)
                
#                 # Store in database
#                 if store_in_database(prompt, contrast_value, num_images_value, width_value, 
#                                   height_value, imageresponse['url'], enhanced_prompt):
#                     st.success("Results saved to database!")
#             else:
#                 st.error("Failed to generate image. Please try again.")
                
#         except ValueError as e:
#             st.error(f"Validation error: {str(e)}")
#         except requests.exceptions.RequestException as e:
#             st.error(f"API Error: {str(e)}")
#         except Exception as e:
#             st.error(f"Unexpected error: {str(e)}")

# # Generate button with clear styling
# if st.button('Generate Mood Board', type='primary'):
#     generate_images()