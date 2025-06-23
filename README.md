# AI Chatbot - Chat with AI

A sleek and simple chatbot built with **Streamlit** that uses the **OpenRouter API** to generate real-time AI responses using the **Mistral model**.

## Overview of the App
![Chatbot Demo](https://github.com/user-attachments/assets/e5ea0e23-dae0-44e9-8b12-abe6fd398592)

### Features

- 💬 Chat interface with left-right chat bubbles (User & AI)
- ✍️ Typing effect for AI responses
- 🔄 Clear Chat button in sidebar
- ⚡ Powered by OpenRouter API with Mistral 7B Instruct
- 🎨 Custom-styled message bubbles with color distinction

---

## Demo App

You can deploy and test this app locally

> Demo coming soon!

---

## Get an OpenRouter API Key

You can sign up and get a free API key from [OpenRouter](https://openrouter.ai/):

1. Visit [https://openrouter.ai/](https://openrouter.ai/)
2. Login with your email or GitHub/mail
3. Go to your dashboard and copy the API key
4. Add the key into a file named `.streamlit/secrets.toml` in your project directory like this:

```
openrouter_key = "your-api-key-here"
```

## How to Run the App
1. Clone this repository
```
git clone https://github.com/yourusername/ai-chatbot-streamlit.git
cd ai-chatbot-streamlit
```
2. Set up virtual environment (optional but recommended)
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Add your OpenRouter key
```
Create a file at .streamlit/secrets.toml with your API key as described earlier.
```
5. Run the app
```
streamlit run app.py
```

## Project Structure
```
├── app.py                  # Main Streamlit chatbot app
├── requirements.txt        # Python dependencies
└── .streamlit
    └── secrets.toml        # Your API key (DO NOT COMMIT)
```
