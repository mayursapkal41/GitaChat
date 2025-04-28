import streamlit as st
import base64
from chatbot import get_gita_response

# Function to use local image as background
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_local_bg_image(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Custom CSS to enhance the UI
def apply_custom_styles():
    st.markdown("""
    <style>
        /* Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Cormorant+Garamond:wght@600&display=swap');

        /* Global App Styling */
        .stApp {
            font-family: 'Poppins', sans-serif;
            color: black;
        }

        /* Title */
        h1 {
            font-family: 'Cormorant Garamond', serif;
            color: black;
            text-align: center;
            font-size: 3.5rem;
            background: rgba(255, 255, 255, 0.5);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }

        /* Chat Message Bubbles */
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.4) !important;
            border-radius: 12px !important;
            padding: 12px !important;
            margin: 8px 0 !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        }

        /* Force black color for all content inside chat bubbles */
        .stChatMessageContent > div > div > div > p,
        .stChatMessageContent > div > p,
        .stChatMessageContent p,
        .stChatMessageContent * {
            color: black !important;
        }

        /* User Message */
        .stChatMessage[data-role="user"] {
            background-color: rgba(240, 240, 240, 0.5) !important;
        }

        /* Assistant Message */
        .stChatMessage[data-role="assistant"] {
            background-color: rgba(220, 245, 245, 0.5) !important;
        }

        /* Input Box */
        .stChatInputContainer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.8) !important;
            padding: 10px !important;
            border-top: 2px solid #ccc !important;
            z-index: 9999;
        }

        .stChatInput {
            background: transparent !important;
            color: black !important;
        }

        /* Footer */
        footer {
            margin-top: 4rem;
            text-align: center;
            color: black;
            background: rgba(255, 255, 255, 0.5);
            padding: 10px;
            border-radius: 10px;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)


# Page Configuration
st.set_page_config(
    page_title="🕉 Divine Dialogue | Gita Chatbot",
    page_icon="🦚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set background and styles
set_local_bg_image("image.jpg")
apply_custom_styles()

# Main Title
st.title("🕉 Divine Dialogue")

# Introduction
st.markdown("""
<div style="background-color: rgba(255,255,255,0.5); padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
    <p>🙏 Seek wisdom from the sacred Bhagavad Gita.<br>Ask your questions and receive divine guidance from Lord Krishna himself.</p>
</div>
""", unsafe_allow_html=True)

# Main Chat Section
with st.container():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input field
user_input = st.chat_input("💬 Ask your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_gita_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": f"🦚 {response}"})
    with st.chat_message("assistant"):
        st.markdown(f"🦚 {response}")

# Footer
st.markdown("""
<footer>
    © 2025 Divine Dialogue | Bhagavad Gita Chatbot | Made with devotion 🧡
</footer>
""", unsafe_allow_html=True)