# Smart Chatbot

A lightweight conversational AI chatbot built using the Hugging Face transformers library and Gradio for an interactive user interface. This project demonstrates the use of a pretrained language model (distilgpt2) to generate conversational responses.

## 🚀 Live Demo

[Link](https://huggingface.co/spaces/ar11069/smart-chatbot)

## 📜 Project Overview

The Smart Chatbot is an example of using Generative AI to create a conversational agent. Leveraging the Hugging Face distilgpt2 model, it processes user inputs and generates relevant text-based responses. The chatbot runs on a user-friendly interface built with Gradio.

## 🔑 Features

Lightweight Model: Uses distilgpt2, a distilled version of GPT-2, for efficient performance.
Interactive UI: Designed with Gradio for an easy-to-use web-based interface.
Extendable: Can be further fine-tuned or extended for domain-specific applications.

## 🛠️ Tech Stack

Python: Core programming language for the project.
Hugging Face Transformers: Pretrained model and tokenizer for natural language generation.
Gradio: Interactive user interface for deploying the chatbot.
Torch: Backend library for PyTorch models.

## ⚙️ How to Run Locally
### Prerequisites
- Python 3.9 or above
- pip package manager
### Installation Steps
1. Clone the Repository:
```bash
git clone https://github.com/RezaeiAlireza/smart-chatbot-llm.git
cd smart-chatbot-llm
```
2. Install Dependencies:
```bash
pip install torch torchvision transformers gradio
```
3. Run the Chatbot:
```bash
python chatbot.py
```
4. Access the Interface:
- Open your browser and navigate to the local Gradio link (e.g., http://127.0.0.1:7860).

## Project Structure
```plaintext
smart-chatbot-llm/
│
├── chatbot.py         # Main script for running the chatbot
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation
```
## 🎯 Future Improvements

- Memory Implementation: Enable the chatbot to remember the conversation context.
- Fine-Tuning: Train on domain-specific datasets for better responses in specialized areas.
- Enhanced UI: Improve the Gradio interface with themes or additional features like file uploads.
- Multi-Modal Support: Extend to include image or audio inputs using Hugging Face's multi-modal models.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🖇️ Acknowledgments
- Hugging Face Transformers
- Gradio

Happy Chatting! 💬
