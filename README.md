🤖 LLM Playground – Multi API Integration (Ollama + Hugging Face + Gemini)

This project is a hands-on LLM experimentation and integration sandbox built using Python.
It demonstrates how to connect and work with multiple Large Language Model providers, handle real-world API errors, and build a foundation for production-ready AI applications.

📌 Project Overview

While learning and building AI applications, I explored different LLM ecosystems:

🧠 Ollama (Local LLMs) – offline model execution
🌐 Hugging Face Inference API – cloud-based open models
☁️ Google Gemini API – advanced hosted LLM

This project combines all three to understand:

API integration patterns
Authentication handling
Error debugging (403, 404, 429, JSON decode issues)
Prompt engineering basics
Logging and production-style code structure

🚀 Features
🔁 Multi-LLM integration (Ollama, HF, Gemini)
📡 REST API communication using requests
🔐 Secure API key handling using .env
🪵 Logging support for debugging and monitoring

⚠️ Handles real-world API errors:
403 Forbidden
404 Not Found
429 Quota Exceeded
JSON decoding failures
🧪 Prompt testing and experimentation
🧰 Modular scripts for each LLM provider
🏗️ Project Structure

unl-ai/
│
├── hf.py                 # Hugging Face API integration experiments
├── gemini.py             # Google Gemini API integration
├── ollama.py             # Local LLM (Ollama) testing
├── logger\_demo.py        # Logging experiments (optional)
├── .env                  # API keys (not committed)
├── .gitignore            # Ignored files configuration
└── README.md             # Project documentation

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/unl-ai.git
cd unl-ai

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install requests python-dotenv

4️⃣ Configure Environment Variables

Create a .env file:

HUGGINGFACE_API_KEY=your_hf_key
GOOGLE_API_KEY=your_gemini_key

▶️ How to Run
🧠 Hugging Face Example
python hf.py

☁️ Gemini Example
python gemini.py

🧠 Ollama Local Model
python ollama.py
🔥 Key Learnings From This Project

🧠 LLM Integration
Working with multiple LLM APIs in one project
Understanding differences between local vs cloud models

⚠️ API Debugging
Fixing 403 Forbidden (access issues)
Fixing 404 Not Found (invalid model endpoints)
Fixing 429 Quota Exceeded (rate limits)
Handling JSON decoding errors safely

🧪 Prompt Engineering
Structuring prompts for better LLM responses
Comparing model outputs across providers

🪵 Logging & Debugging
Using Python logging for production-style debugging
Tracking API status codes and responses

⚠️ Known Issues
Hugging Face serverless API may not support all models (e.g., Qwen, Mistral large variants)
Gemini API may require billing or quota setup
Some models may return delayed responses or loading errors
Internet dependency for HF & Gemini APIs

🚀 Future Improvements
🔥 Build FastAPI backend for unified LLM API
🔥 Create LLM router (HF + Gemini + Ollama fallback)
🔥 Add Streamlit UI chatbot
🔥 Add caching system for responses
🔥 Add prompt templates system
🔥 Deploy as SaaS AI assistant