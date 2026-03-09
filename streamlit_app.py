import streamlit as st

# Set the page title and an icon
st.set_page_config(page_title="Lothlórien Study Guide", page_icon="🌿")

st.title("🌿 The Wisdom of Lothlórien")
st.markdown("### An Interactive Journey through the Golden Wood")

# Using a sidebar for progress tracking
st.sidebar.header("Your Progress")

# This dictionary holds our Questions, the Answer Key, and a "Hint"
questions = {
    "1. Time": ("What does Lothlórien teach about time and memory?", ["fluid", "blending", "ancient", "past"], "Think about how the past and present feel here."),
    "2. Gifts": ("How do Galadriel's gifts foreshadow future events?", ["arc", "choices", "rope", "phial", "sheath"], "Remember Sam's rope or Frodo's light!"),
    "3. Beauty": ("Why is beauty presented with moral weight?", ["moral", "healing", "spiritual", "purity"], "Is beauty just 'looking good,' or is it something deeper?"),
} # (Note: You can add all 10 here following this pattern!)

for key, (q_text, keywords, hint) in questions.items():
    st.subheader(key)
    user_ans = st.text_input(q_text, key=key).lower()
    
    if user_ans:
        # Check if any keyword from your list is in their answer
        if any(word in user_ans for word in keywords):
            st.success(f"🌟 Correct! You recognized the theme of {keywords[0]}.")
        else:
            st.info(f"🔍 Keep thinking! {hint}")

if st.button("Finish the Journey"):
    st.balloons()
    st.write("Namárië! You have completed the study of the Golden Wood.")
