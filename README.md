
# Chat Bot with Google Generative AI
---
## About
This project automates chat responses using Google's Generative AI (Gemini-1.5-flash). The bot monitors chat logs, generates human-like responses, and interacts with users through a simulated user interface.

## Tech Stack
- **Python**: The primary programming language used for scripting and automation.
- **PyAutoGUI**: Used for automating mouse and keyboard actions.
- **Pyperclip**: Used for clipboard operations to copy and paste text.
- **Google Generative AI (Gemini-1.5-flash)**: The model used to generate human-like responses.

## Libraries Used
- **PyAutoGUI**: To perform GUI automation tasks such as clicking, typing, and dragging.
  - Installation: `pip install pyautogui`
- **Pyperclip**: For clipboard operations to copy and paste text.
  - Installation: `pip install pyperclip`
- **Google Generative AI**: For generating human-like text responses.
  - Installation: Follow Google's documentation to install and configure the generative AI library.

## Unique Selling Points (USPs)
- **Human-like Responses**: The bot generates responses that mimic natural human conversations, enhancing user engagement.
- **Multi-language Support**: The bot can respond in English, Bengali, and Hindi, adapting to the language of the received message.
- **Automated Interaction**: Fully automates the process of reading, generating, and sending responses in a chat interface.
- **Configurable Prompts**: Customizable prompts allow for tailored responses based on specific needs and contexts.
- **Ease of Integration**: Simple to integrate with various chat platforms by adjusting the UI automation coordinates.

## Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SoahamSur/ChatBot.git
   cd ChatBot
   ```
2. **Install Dependencies**:
   ```bash
   pip install pyautogui pyperclip
   ```
3. **Configure API Key**:
   - Sign up for Google Generative AI and obtain an API key.
   - Replace the placeholder API key in the script (`gemini_key` variable) with your actual API key.
4. **Run the Script**:
   ```bash
   python chat_automation.py
   ```

## Usage
1. Open the chat window you want to automate.
2. Run the script to start the automation process.
3. The bot will monitor the chat, generate responses using Google Generative AI, and send replies.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---
