# 🚀 User Management System with FastAPI & Streamlit  

This project is a **User Management System** built using **FastAPI** (Backend) and **Streamlit** (Frontend). It supports **CRUD operations** (Create, Read, Update, Delete) with image upload functionality and a visually appealing interface.  

---

## 📌 Features  

✅ **FastAPI Backend:**  
- RESTful API with CRUD operations  
- SQLite database for data storage  
- User image upload support  

✅ **Streamlit Frontend:**  
- Interactive UI for managing users  
- Image upload and display  
- Professional and user-friendly design  

✅ **Other Features:**  
- JWT authentication (optional for future)  
- Responsive UI with custom CSS  
- Uses `requests` for API integration  

---

## 🛠️ Technologies Used  

| Technology   | Purpose |
|-------------|---------|
| **FastAPI**  | Backend API Development |
| **SQLite**   | Database Storage |
| **Streamlit** | Frontend UI |
| **Pillow**   | Image Processing |
| **Requests** | API Communication |

---

## 🚀 Getting Started  

### 🔹 **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/user-management-system.git
cd user-management-system
🔹 2. Create a Virtual Environment
bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
🔹 3. Install Dependencies
bash
pip install -r requirements.txt
🔹 4. Run the FastAPI Backend
bash
uvicorn main:app --reload
FastAPI will start at: http://127.0.0.1:8000

🔹 5. Run the Streamlit Frontend
bash
streamlit run app.py
Streamlit will start at: http://localhost:8501

📂 Project Structure
bash
📁 UserManagementSystem
│── 📄 main.py              # FastAPI Backend
│── 📄 app.py               # Streamlit Frontend
│── 📄 requirements.txt      # Project Dependencies
│── 📂 images/              # Uploaded User Images
│── 📄 database.db           # SQLite Database
│── 📄 README.md             # Project Documentation


🎯 API Endpoints
Method	Endpoint	Description
GET	/	Root API Check
POST	/add/	Add a New User
GET	/view/	View All Users
PUT	/update/{id}	Update User Details
DELETE	/delete/{id}	Delete a User

🖼️ User Interface
![User Management System](D:\AI_ML\UserManagementSystem\Screenshot (41).png)

📌 Future Enhancements
🔹 Implement JWT authentication
🔹 Add user role management
🔹 Improve UI with better animations

🤝 Contribution
Contributions are welcome! To contribute:

Fork this repository

Create a new branch (feature-xyz)

Commit and push changes

Submit a Pull Request

📜 License
This project is licensed under the MIT License.

✨ Author
Developed by Muhammad Rehan Iqbal.
GitHub https://github.com/Rehan1911
