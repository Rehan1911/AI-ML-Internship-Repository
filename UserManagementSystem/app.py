import streamlit as st
import requests
import pandas as pd
from PIL import Image

# Base URL of FastAPI server
BASE_URL = "http://127.0.0.1:8000"

# 🎨 Custom CSS Styling for Professional Look
st.markdown("""
    <style>
        /* Sidebar background with multi-color gradient */
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #6a11cb, #2575fc, #20BF55); /* Purple → Blue → Green */
            color: white;
            padding: 20px;
            border-radius: 10px;
        }
        
        /* Sidebar text color */
        [data-testid="stSidebar"] .css-1d391kg {
            color: white !important;
            font-weight: bold;
        }

        /* Sidebar Headers */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3 {
            color: #F4D03F; /* Soft Golden Yellow */
        }

        /* Sidebar buttons */
        .stButton>button {
            background-color: #FF5733; /* Bright Orange */
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #C70039; /* Darker Red */
        }

        /* Image Styling */
        .rounded-img {
            border-radius: 15px;  /* Round corners */
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%; /* Adjust width */
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Sidebar Navigation
st.sidebar.title("User Management System")
option = st.sidebar.radio("Select an option", ["Home", "Add User", "View Users", "Update User", "Delete User"])

# 📌 Home Page (with Styled CRUD Image)
if option == "Home":
    st.title("Welcome to the User Management System 🚀")
    st.write("**Efficiently manage users with CRUD Operations!**")

    # Load and display the CRUD image
    image_path = r"D:\AI_ML\UserManagementSystem\CURD.jpeg"
  # Ensure this file exists in the project folder
    try:
        image = Image.open(image_path)
        
        # 🖼️ Reduce the size of the image
        image = image.resize((700, 250))  # Resize image to width=350, height=200
        
        # Display image with rounded corners
        st.image(image, caption="CRUD Operations", use_container_width=False)
    
    except FileNotFoundError:
        st.error("Error: Image file not found! Ensure 'CURD.jpeg' is in the project directory.")

# ➕ Add User
elif option == "Add User":
    st.title("Add New User")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=1, max_value=120)
    image = st.file_uploader("Upload Profile Image", type=["jpg", "png", "jpeg"])

    if st.button("Add User"):
        files = {"image": image} if image else None
        data = {"name": name, "age": age}
        response = requests.post(f"{BASE_URL}/add/", data=data, files=files)

        if response.status_code == 200:
            st.success("User added successfully!")
        else:
            st.error("Error adding user.")

# 👀 View Users
elif option == "View Users":
    st.title("All Users")
    response = requests.get(f"{BASE_URL}/view/")

    if response.status_code == 200:
        users = response.json().get("users", [])
        if users:
            df = pd.DataFrame(users, columns=["ID", "Name", "Age", "Image Path"])
            st.dataframe(df)
        else:
            st.info("No users found.")
    else:
        st.error("Error fetching users.")

# ✏️ Update User
elif option == "Update User":
    st.title("Update User Information")
    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    new_name = st.text_input("Enter New Name")
    new_age = st.number_input("Enter New Age", min_value=1, max_value=120)

    if st.button("Update User"):
        data = {"name": new_name, "age": new_age}
        response = requests.put(f"{BASE_URL}/update/{user_id}", data=data)

        if response.status_code == 200:
            st.success("User updated successfully!")
        else:
            st.error("Error updating user.")

# 🗑️ Delete User
elif option == "Delete User":
    st.title("Delete User")
    user_id = st.number_input("Enter User ID", min_value=1, step=1)

    if st.button("Delete User"):
        response = requests.delete(f"{BASE_URL}/delete/{user_id}")

        if response.status_code == 200:
            st.success("User deleted successfully!")
        else:
            st.error("Error deleting user.")
