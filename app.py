import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

# Retrieve Azure credentials from .env
AI_SERVICE_ENDPOINT = os.getenv("AI_SERVICE_ENDPOINT")
AI_SERVICE_KEY = os.getenv("AI_SERVICE_KEY")
QA_PROJECT_NAME = os.getenv("QA_PROJECT_NAME")
QA_DEPLOYMENT_NAME = os.getenv("QA_DEPLOYMENT_NAME")

# Construct the URL for the QnA API
QNA_URL = f"{AI_SERVICE_ENDPOINT}/language/:query-knowledgebases?projectName={QA_PROJECT_NAME}&api-version=2021-10-01&deploymentName={QA_DEPLOYMENT_NAME}"

def get_answer_from_qna(question):
    headers = {
        "Ocp-Apim-Subscription-Key": AI_SERVICE_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "question": question,
        "top": 1,
        "confidenceScoreThreshold": 0.5,
        "includeUnstructuredSources": True
    }
    
    response = requests.post(QNA_URL, headers=headers, json=body)
    try:
        data = response.json()
        if "answers" in data and len(data["answers"]) > 0:
            best_answer = data["answers"][0]
            answer_text = best_answer.get("answer", "No answer found.")
            # Get follow-up prompts
            prompts = best_answer.get("dialog", {}).get("prompts", [])
            follow_up_prompts = [prompt["displayText"] for prompt in prompts] if prompts else []
            return answer_text, follow_up_prompts
        else:
            return "No relevant answer found.", []
    except Exception as e:
        return f"Error processing API response: {str(e)}", []


def local_css():
    st.markdown("""
    <style>
        /* Main container styling */
        .main-container {
            border-radius: 8px;
            padding: 2rem;
            margin: 0 auto;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 800px;
        }
        /* Styled buttons */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 10px 24px;
            cursor: pointer;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        /* Sidebar background */
        .css-1d391kg {
            background-color: #f0f2f6;
        }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Nintendo 3DS QnA", layout="centered")
    local_css()

    # Sidebar with test questions and source info
    with st.sidebar:
        st.header("Test Questions")
        st.write("Try some sample questions:")
        sample_questions = [
            "I want a description of what is the Nintendo 3DS",
            "What is the game Mario Kart 7 about?",
            "What are the key elements of Animal Crossing: New Leaf?"
        ]
        for sample in sample_questions:
            if st.button(sample):
                st.session_state.question = sample

        st.markdown("---")
        st.info("Knowledge Base Sources:")
        st.markdown("- [Mario Kart 7](https://www.mariowiki.com/Mario_Kart_7)")
        st.markdown("- [Animal Crossing: New Leaf](https://nookipedia.com/wiki/Animal_Crossing:_New_Leaf)")
        st.markdown("- [Nintendo 3DS XL](https://nintendo.fandom.com/wiki/Nintendo_3DS_XL)")
        st.markdown("- [Nintendo 3DS](https://nintendo.fandom.com/wiki/Nintendo_3DS)")
        st.markdown("- [Nintendo 2DS](https://nintendo.fandom.com/wiki/Nintendo_2DS)")
        st.markdown("- [New Nintendo 3DS](https://nintendo.fandom.com/wiki/New_Nintendo_3DS)")
        st.markdown("- [New Nintendo 2DS XL](https://nintendo.fandom.com/wiki/New_Nintendo_2DS_XL)")

    # Main container for the QnA interface
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.title(":grey[QnA for Nintendo] :red[3]:grey[DS™]")
        st.write("Ask a question about the Nintendo 3DS family, Mario Kart 7, or Animal Crossing: New Leaf, and the chatbot will retrieve the best answer for you!")

        # Initialize session state for question if not already set
        if "question" not in st.session_state:
            st.session_state.question = ""
        
        user_question = st.text_input("Enter your question:", value=st.session_state.question)

        if user_question:
            with st.spinner("Fetching answer..."):
                answer, follow_up_prompts = get_answer_from_qna(user_question)
            st.markdown("**Answer:**")
            st.write(answer)

            # Display follow-up prompts as buttons
            if follow_up_prompts:
                st.markdown("### Follow-up Questions:")
                for prompt in follow_up_prompts:
                    if st.button(prompt):
                        st.session_state.question = prompt
                        st.rerun()  # Refresh to auto-fill the text input

        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
