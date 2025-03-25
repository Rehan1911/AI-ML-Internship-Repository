
# Using Groq AI with LangChain** 🚀

## 📌 Overview  
This repository demonstrates how to integrate **Groq AI models** with **LangChain** for AI-powered chat applications. The project utilizes **Llama3-8b-8192** via the `langchain_groq` package.

---

## 🤖 What is LLaMA?  
LLaMA (**Large Language Model Meta AI**) is a family of **AI models developed by Meta** (formerly Facebook AI). These models are designed for **text generation, chatbots, and reasoning tasks**.

### 🔹 **LLaMA Versions**  
- **LLaMA 1** *(2023)* – Small and efficient, with sizes of **7B, 13B, 33B, and 65B parameters**.  
- **LLaMA 2** *(2023)* – Fully **open-source**, improved accuracy, and available in **7B, 13B, and 70B** sizes.  
- **LLaMA 3** *(2024)* – More advanced and efficient, currently available in **8B and 70B versions**.  

### 🔹 **Why Use LLaMA?**  
✅ **Open and flexible** – Ideal for research and commercial projects.  
✅ **Efficient and powerful** – Works well even on smaller hardware.  
✅ **Easy to fine-tune** – Can be customized for specific tasks.  

---

## 🛠 Installation  

To get started, install the required dependencies:  

```sh
pip install langchain_groq
```

---

## 📜 Code Explanation  

The following script initializes the **Groq AI model** and invokes it with a prompt.

### 1️⃣ Import Necessary Libraries  

```python
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
```
- `ChatGroq`: The LangChain interface for interacting with **Groq AI models**.  
- `ChatPromptTemplate`: Allows the creation of **dynamic prompt templates**.  

### 2️⃣ Set Up the Model  

```python
import os

groq_api_key = os.getenv("GROQ_API_KEY")  # Load API key from environment variable
llm2 = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")
```
🔹 **Security Note**: Store the API key securely as an **environment variable** instead of hardcoding it.  

### 3️⃣ Define a Prompt Template  

```python
prompt = ChatPromptTemplate.from_template(
    """
    What is the best place to visit in Islamabad?
    {response}
    """
)
```
- This creates a **formatted prompt** where `{response}` is a placeholder.  

### 4️⃣ Invoke the Model  

```python
response = llm2.invoke(prompt.format(response=""))
print("Response:", response)
```
- The `{response}` placeholder is replaced with an **empty string**.  
- The formatted prompt is sent to the AI model for processing.  
- The response is printed to the console.  

---

## ▶ Running the Script  

Make sure your **Groq API key** is set in your environment variables:  

```sh
export GROQ_API_KEY="your_api_key_here"
```

Then, run the script:  

```sh
python script.py
```

---

## 📌 Expected Output  

The script will return a response from the **AI model**, suggesting the best places to visit in **Islamabad**.

---

## 📝 Notes  

🔹 Ensure that your **API key is valid and active**.  
🔹 If you encounter issues, check the `response` object structure to debug.  

---

## 📜 License  

This project is **open-source** and available under the **MIT License**.  

---

🚀 **Happy Coding!** 💡