import requests  # Importing requests to handle HTTP requests
import datetime  # Importing datetime to fetch and format the current date

# ---------------------------- Setting Up Date and Credentials ------------------------------- #
# Fetching the current date and formatting it as 'YYYYMMDD' for Pixela API
day = datetime.datetime.now()
date = day.strftime("%Y%m%d")  # Converts the date to the format required by Pixela

# Your credentials for the Pixela API
USER_NAME = "deadkiller9932"  # Replace with your Pixela username
TOKEN = "userForTesting"  # Replace with your Pixela API token
GRAPH_ID = "graph1"  # Replace with your graph ID
headers = {"X-USER-TOKEN": TOKEN}  # Authorization header required for API requests

# ---------------------------- Creating a New Pixela User ------------------------------- #
# Pixela endpoint for creating a new user
pixela_endpoint = "https://pixe.la/v1/users"

# Payload for user creation
user_parameters = {
    "token": TOKEN,  # Unique token for the user (you define this value)
    "username": USER_NAME,  # Unique username for the user
    "agreeTermsOfService": "yes",  # Required to agree to Pixela terms of service
    "notMinor": "yes",  # Indicates that the user is not a minor
}

# Sending POST request to create a new user
user_creation = requests.post(url=pixela_endpoint, json=user_parameters)
# The response will indicate if the user creation was successful or if the user already exists

# ---------------------------- Creating a New Graph ------------------------------- #
# Payload to define the graph's properties
graphs_config = {
    "id": GRAPH_ID,  # Unique ID for the graph
    "name": "Cycling Graph",  # Name of the graph (e.g., "Cycling Graph")
    "unit": "Km",  # Unit of measurement (e.g., kilometers)
    "type": "float",  # Type of data (e.g., "float" for decimal values)
    "color": "sora",  # Graph color (e.g., "sora" for light blue)
}

# Endpoint to create a new graph
graphs_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

# Sending POST request to create the graph
graph_creation = requests.post(url=graphs_endpoint, json=graphs_config, headers=headers)

# ---------------------------- Submitting Data (Pixel) to the Graph ------------------------------- #
# Endpoint to submit pixel data to the graph
submitting_pixel_endpoint = f"{graphs_endpoint}/{GRAPH_ID}"

# Uncomment and configure this block if you want to add a pixel to the graph Style #1:
# pixel_confg = {
#     "date": "20241112",  # Date for the pixel (YYYYMMDD format)
#     "quantity": "10.0",  # Quantity to log (e.g., "10.0" kilometers)
# }
# Sending POST request to add a pixel
# submitting_pixel = requests.post(url=submitting_pixel_endpoint, json=pixel_confg, headers=headers)
# print(submitting_pixel.status_code)  # Prints the status code to verify the request was successful

# ---------------------------- Editing an Existing Pixel ------------------------------- #
# Endpoint to edit a specific pixel (e.g., on date 20241112) Style #2:
editing_pixel_endpoint = f"{submitting_pixel_endpoint}/20241112"

# Payload to update the quantity of the pixel
editing_pixel_config = {"quantity": "6.8"}  # New quantity to log (e.g., "6.8" kilometers)

# Sending DELETE request to delete the pixel
# Note: If you meant to edit instead of delete, replace `requests.delete` with `requests.put`
editing_pixel = requests.delete(editing_pixel_endpoint, headers=headers)

# Printing the response from the server to verify the operation
print(editing_pixel.text)  # This will show if the operation was successful or if an error occurred
