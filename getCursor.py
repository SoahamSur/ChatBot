import pyautogui

while True:
    a=pyautogui.position()
    print(a)
    # prompt = f"You are a human named Soaham. you give normal and human-like answers. Here is the text: {text}\nAnswer in one or two sentences:.The response should not contain name of neither Soaham nor the sender.The message should just be a reply in short.You should reply as if you are talking with the message sender"
    
    '''
    import pyautogui
import pyperclip
import time
import google.generativeai as genai
import re

gemini_key = "AIzaSyDl-Ksq6sPBdzMu-60qHDfdJJtX_9cd63c"
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def is_last_message_from_sender(chat_log, sender_name):
        # Splitting chat
        messages = chat_log.strip().split("/2024] ")[-1]
        if sender_name=="Soaham Sur" in messages:
            return False 
        return True

def extract_senders(chat_log):
    # Define the regex pattern to capture sender names
    pattern = r'\[\d{2}:\d{2}, \d{1,2}/\d{1,2}/\d{4}\] ([^:]+):'
    
    # Find all matches in the chat log
    senders = re.findall(pattern, chat_log)
    
    # Filter out "Soaham Sur" from the list of sender names
    filtered_senders = [sender for sender in senders if sender != "Soaham Sur"]
    
    return filtered_senders

# # Click on the specified position
pyautogui.click(613, 745)
time.sleep(1)

while True:
    pyautogui.moveTo(413, 149)
    pyautogui.dragTo(1331, 660, duration=1, button='left')

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(437, 318)

    text = pyperclip.paste()
    print("Copied text:", text)

    sender=extract_senders(text)
    print(sender)
    if is_last_message_from_sender(text,sender):
        prompt2=f"You are a human named Soaham. you give normal and human-like answers. Your responses are natural, empathetic, and relatable, just like a human being would converse. Additionally, ensure that you respond in the same language that the sender uses for their messages. Adapt your tone and style to suit casual, friendly interactions, and strive to make your replies engaging and thoughtful.The replies should be short.Soaham talks in English mixed with bengali.Here's the message:{text}"
        response = model.generate_content(prompt2) 
        response_text = response.candidates[0].content.parts[0].text
        print("Generated response:", response_text)

        pyperclip.copy(response_text)

        pyautogui.click(802,693)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')
    '''