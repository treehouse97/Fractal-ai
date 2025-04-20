import streamlit as st
import cohere
from fractal_utils import generate_fractal_image
import io

st.set_page_config(page_title="FractalLens", layout="wide")

# Sidebar settings
st.sidebar.title("FractalLens Settings")
depth = st.sidebar.slider("Fractal Depth", 1, 10, 5)
cohere_api_key = st.sidebar.text_input("Cohere API Key", type="password")

# Main UI
st.title("FractalLens: Pattern Interface for Deeper Intelligence")
user_input = st.text_area("What concept or question are you tuning into?")

if st.button("Run Fractal Analysis"):
    if not cohere_api_key:
        st.error("Please enter your Cohere API key in the sidebar.")
    else:
        with st.spinner("Generating fractal and tuning AI..."):
            fig = generate_fractal_image(depth)
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            st.image(buf, caption="Generated Fractal Antenna", use_container_width=True)

            prompt = f"""
            You are a symbolic interpreter for a fractal intelligence system.
            The user has tuned the system with this query: "{user_input}"

            Based on recursive pattern recognition, symmetry, and symbolic resonance,
            return an interpretation or insight that may reveal a deeper structure,
            logic, or contradiction beneath the user's question.
            """

            try:
                co = cohere.Client(cohere_api_key)
                response = co.chat(
                    message=prompt,
                    model="command",
                    temperature=0.7
                )
                insight = response.text
                st.markdown("### Insight")
                st.write(insight)
            except Exception as e:
                st.error(f"Cohere API error: {e}")