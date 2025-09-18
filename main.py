import streamlit as st
import pandas as pd
import pywhatkit as kit
import time
import pyautogui

st.set_page_config(page_title="WhatsApp Message Sender", page_icon="📱")

st.title("📱 WhatsApp Message Sender (Batch Mode)")
st.write("Upload an Excel file with a column **Phone** (in international format, e.g., 923001234567).")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
group_invite_link = st.text_input("Enter WhatsApp Group Invite Link", 
                                  "https://chat.whatsapp.com/JJULI8qF7KyJesuxuYL1vH")
custom_message = st.text_area("Enter Custom Message", 
    "📢📢 Welcome to Your Official Batch Group!\n👉 Join the group now:")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("✅ Contacts loaded:")
    st.dataframe(df)

    if st.button("🚀 Send Messages"):
        for index, row in df.iterrows():
            phone_number = f"+{row['Phone']}"
            message = f"""{custom_message} {group_invite_link}"""

            try:
                kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
                time.sleep(8)  # wait for chat to open
                pyautogui.press("enter")  # press Enter to actually send
                st.success(f"Message sent to {phone_number}")
                time.sleep(5)
            except Exception as e:
                st.error(f"Failed to send message to {phone_number}: {e}")


