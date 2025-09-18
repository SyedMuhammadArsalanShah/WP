import pywhatkit as kit
import pandas as pd
import time
import pyautogui

# Load Excel File (must have a column 'Phone')
df = pd.read_excel("Book1.xlsx")

# WhatsApp Group Invite Link
group_invite_link = "https://chat.whatsapp.com/JJULI8qF7KyJesuxuYL1vH"

# Custom Message
custom_message = """📢📢 Welcome to Your Official Batch Group!
👉 Join the group now:"""

# Loop through contacts
for index, row in df.iterrows():
    phone_number = f"+{row['Phone']}"  # international format (+923001234567)
    message = f"""{custom_message} {group_invite_link}"""

    try:
        # Open chat + type message
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=15
                                  )

        # Wait for WhatsApp Web to load the chat
        time.sleep(8)

        # Press Enter to actually send
        pyautogui.press("enter")

        print(f"✅ Message sent to {phone_number}")
        time.sleep(5)  # delay between messages
        pyautogui.press("enter")

        
    except Exception as e:
        print(f"❌ Failed to send message to {phone_number}: {e}")
