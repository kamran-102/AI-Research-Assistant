# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000/research"

# st.title("Professional AI Research Assistant")

# query = st.text_area("Enter your research query")

# if st.button("Run Research"):

#     with st.spinner("Running research workflow..."):

#         response = requests.post(API_URL, json={"query": query})

#         if response.status_code == 200:
#             st.markdown(response.json()["result"])
#         else:
#             st.error("Error occurred.")

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/research"

# Page Configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background-color: #f8fafc;
}

/* Main Container */
.block-container {
    max-width: 1000px;
    padding-top: 3rem;
}

/* Header */
.hero-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.5rem;
}

.hero-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 1.1rem;
    margin-bottom: 3rem;
}

/* Text Area Styling */
[data-testid="stTextArea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    caret-color: #000000 !important;
    border: 1px solid #dbe4ee !important;
    border-radius: 14px !important;
    font-size: 16px !important;
    padding: 12px !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #94a3b8 !important;
}

/* Button Styling */
.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    background: #2563eb;
    color: white;
    border: none;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #1d4ed8;
}

/* Report Container */
.report-container {
    background: white;
    color: #000000;
    border-radius: 16px;
    padding: 35px;
    margin-top: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
}

/* Report Title */
.report-title {
    font-size: 24px;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='hero-title'>
    🔍 AI Research Assistant
</div>

<div class='hero-subtitle'>
    Discover insights, analyze evidence, and generate professional research reports within minutes
</div>
""", unsafe_allow_html=True)

# Query Input
query = st.text_area(
    label="Research Query",
    placeholder="What would you like to research today?",
    height=180
)

# Research Button
if st.button("Run Research"):

    if not query.strip():
        st.warning("Please enter a research topic.")

    else:
        with st.spinner("Conducting research..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"query": query},
                    timeout=300
                )

                if response.status_code == 200:

                    st.markdown(
                        """
                        <div class='report-title'>
                            Research Report
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class='report-container'>
                            {response.json()['result']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:
                    st.error("Failed to generate report.")

            except Exception as e:
                st.error(f"Error: {e}")