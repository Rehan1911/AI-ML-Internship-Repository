import streamlit as st
from backend import query_groq_api

# Set up page
st.set_page_config(page_title="💬 Smart AI Chatbot", layout="wide")

# Sidebar for chat history
st.sidebar.title("📜 Chat History")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Main UI
st.title("💬 Smart AI Chatbot")
st.write("Ask me anything !")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"**👤 You:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**🤖 AI:** {message['content']}")

# Sidebar: Show AI responses with expandable sections
for i in range(0, len(st.session_state.chat_history), 2):  
    if i + 1 < len(st.session_state.chat_history):  
        with st.sidebar.expander(f"🤖 AI Response {i // 2 + 1}"):
            st.write(st.session_state.chat_history[i + 1]["content"])

# User input at the bottom
input_key = "user_input"

# Workaround to clear input field
def clear_input():
    st.session_state[input_key] = ""

user_input = st.text_input("Type your question and press Enter:", key=input_key)

if user_input:
    # Add user input to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Display AI response in real-time
    st.subheader("🤖 AI Response:")
    response_area = st.empty()
    final_response = ""

    try:
        # Call API and stream response
        response_generator = query_groq_api(user_input, st.session_state.chat_history)
        for chunk in response_generator:
            if chunk:
                final_response += chunk
                response_area.markdown(final_response)

        # Store AI response in chat history
        st.session_state.chat_history.append({"role": "assistant", "content": final_response})

    except Exception as e:
        st.error(f"⚠️ API Error: {str(e)}. Please wait and try again.")

    
