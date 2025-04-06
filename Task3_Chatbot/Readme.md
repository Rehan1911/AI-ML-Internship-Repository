
# 💬 Smart AI Chatbot.

This project is a Streamlit-based interactive AI chatbot powered by the **Groq API** (LLaMA 3 model). It maintains **chat memory**, provides a **clean UI with sidebar chat history**, and keeps the **input field anchored at the bottom** of the page for a natural messaging experience—just like modern chat apps!

---

## 🌟 Features

- ✅ Live AI conversation using Groq API (LLaMA 3)
- ✅ Full conversation memory using Streamlit Session State
- ✅ Chat history stored in a collapsible sidebar
- ✅ Streamed responses for better UX
- ✅ Clear Chat button for fresh sessions
- ✅ Input bar appears after the last response (real-time chat flow)

---

## 🧠 Technologies Used

- [Python 3.10+](https://www.python.org)
- [Streamlit](https://streamlit.io)
- [Groq API](https://console.groq.com/)
- [OpenAI Compatible Backend](mocked with `query_groq_api()`)

---

## 📁 Project Structure

```
├── backend.py        # Contains query_groq_api() function
├── frontend.py       # Streamlit app logic and UI
├── requirements.txt  # Project dependencies
└── README.md         # You’re here!
```

---

## 🚀 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Your Groq API Key**

   Create a `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Or set it inside `backend.py`.

5. **Run the App**
   ```bash
   streamlit run frontend.py
   ```

---

## 📸 Screenshots



---

## 📌 Task Summary

- **Task Name:** Task 1- Smart AI Chatbot
- **Internship Week:** Week 2
- **Branch:** `week2-task1-chatbot`
- **Main Focus:** Real-time chat system using Groq API with memory & clean UI

---

## 💡 Future Enhancements

- Add image/file support
- Enable voice input/output
- Switch between Groq / OpenAI / HuggingFace APIs

---

## 📄 License

MIT License - Free to use, distribute, and modify.