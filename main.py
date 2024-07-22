import pyautogui
import pyperclip
import time
import google.generativeai as genai
import re

# Configure the API key for Google Generative AI
gemini_key = "AIzaSyDl-Ksq6sPBdzMu-60qHDfdJJtX_9cd63c"
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def is_last_message_from_sender(chat_log, sender_name):
    # Splitting chat
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name not in messages

def extract_senders(chat_log):
    # Define the regex pattern to capture sender names
    pattern = r'\[\d{2}:\d{2}, \d{1,2}/\d{1,2}/\d{4}\] ([^:]+):'
    
    # Find all matches in the chat log
    senders = re.findall(pattern, chat_log)
    
    # Filter out "Soaham Sur" from the list of sender names
    filtered_senders = [sender for sender in senders if sender != "Soaham Sur"]
    
    return filtered_senders

# Click on the specified position to focus on the chat window
pyautogui.click(613, 745)
time.sleep(1)

while True:
    # Select and copy the chat log
    pyautogui.moveTo(413, 149)
    pyautogui.dragTo(1331, 660, duration=1, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(437, 318)

    # Get the copied text
    text = pyperclip.paste()
    print("Copied text:", text)

    sender = extract_senders(text)
    print(sender)
    qualtities=[f"Soaham is 19 years old & his height is 6ft4inch",
                f"Soaham is currently pursuing B.Tech in ELectronics & Communication Enginneering from IIIT Kalyani",
                f"Soaham's hobbies are photography,playing guitar,listening to music,watching web-series & movies",
                f"Soaham's nature is friendly and he talks to everyone in a friendly & respectful tone",
                f"Soaham's mother tongue is Bengali.He also speaks English and hindi."]
    if is_last_message_from_sender(text, "Soaham Sur"):
        prompt2 = (
            f"You are a human named Soaham. you give normal and human-like answers. "
            f"Your responses are natural, empathetic, and relatable, just like a human being would converse. "
            f"Additionally, ensure that you respond in the same language that the sender uses for their messages. "
            f"Adapt your tone and style to suit casual, friendly interactions, and strive to make your replies engaging and thoughtful. "
            f"Soaham has the following qualities:{qualtities}"
            f"Don't generate any message beginning with date ,time and sender's name.Soaham doesn't reply like this. "
            f"The replies should be short in 1 line. Soaham talks in English mixed with Bengali.He also sometimes speaks Hindi as well depending on the language of the message received. Here's the message: {text}"
        )
        response = model.generate_content(prompt2)
        response_text = response.candidates[0].content.parts[0].text
        print("Generated response:", response_text)

        pyperclip.copy(response_text)

        # Pasting & sending the response
        pyautogui.click(802, 693)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

    #  delay to avoid rapid looping
    time.sleep(5)
