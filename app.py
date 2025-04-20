import streamlit as st
from fractal_utils import generate_fractal_image
import openai
import io

st.set_page_config(page_title="FractalLens", layout="wide")

# Sidebar settings
st.sidebar.title("FractalLens Settings")
depth = st.sidebar.slider("Fractal Depth", 1, 10, 5)
openai.api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Main UI
st.title("FractalLens: Pattern Interface for Deeper Intelligence")
user_input = st.text_area("What concept or question are you tuning into?")

if st.button("Run Fractal Analysis"):
    with st.spinner("Generating fractal and tuning AI..."):
        fig = generate_fractal_image(depth)
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        st.image(buf, caption="Generated Fractal Antenna", use_column_width=True)

        prompt = f"""
        You are a symbolic interpreter for a fractal intelligence system.
        The user has tuned the system with this query: "{user_input}"

        Based on recursive pattern recognition, symmetry, and symbolic resonance,
        return an interpretation or insight that may reveal a deeper structure,
        logic, or contradiction beneath the user's question.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            insight = response['choices'][0]['message']['content']
            st.markdown("### Insight")
            st.write(insight)

        except Exception as e:
            st.error(f"OpenAI API error: {e}")
