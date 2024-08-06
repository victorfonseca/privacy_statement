import streamlit as st

# Set page config
st.set_page_config(page_title="Key Ward - Terms of Service and Privacy", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }
    .stCheckbox {
        font-size: 16px;
    }
    .stCheckbox > label > span {
        color: black !important;
    }
    .hyperlink-text {
        color: #0000EE;
        font-size: 14px;
        margin-top: 10px;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 4px;
        margin-top: 10px;
    }
    .main .block-container {
        color: black;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for agreement
if 'agreed' not in st.session_state:
    st.session_state.agreed = False

# Main content
st.title("Key Ward - Terms of Service and Privacy Agreement")

# Checkbox for agreement
agreed = st.checkbox("I have read and agree to Key Ward's Terms of Service and Privacy", 
                     value=st.session_state.agreed, 
                     disabled=st.session_state.agreed)

# Update session state if checkbox is checked
if agreed and not st.session_state.agreed:
    st.session_state.agreed = True

# Display agreement status
if st.session_state.agreed:
    st.markdown('<div class="success-message">You have accepted Key Ward\'s Terms of Service and Privacy</div>', unsafe_allow_html=True)

# Hyperlink text
st.markdown('<p class="hyperlink-text">The <a href="https://keyward.io/terms-of-service" target="_blank">Terms of Use</a> and the Privacy Statement are a hyperlink to another web page that is public.</p>', unsafe_allow_html=True)