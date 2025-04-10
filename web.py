import streamlit as st

st.title("🚀 Quick Streamlit Website in 15 Minutes")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])


if page == "Home":
    st.header("🏠 Welcome to the Homepage!")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! 👋 Welcome to this quick web app.")
    st.markdown("This website is built using **Python & Streamlit** in under 15 minutes!")

elif page == "About":
    st.header("ℹ️ About This Project")
    st.write("""
        This is a super simple web app created using Streamlit. 
        It's meant to show how fast and easy it is to build a web interface using Python only.
    """)

elif page == "Contact":
    st.header("📬 Contact")
    st.write("You can reach out at: **aqsaqayyum8627@gmail.com**")
