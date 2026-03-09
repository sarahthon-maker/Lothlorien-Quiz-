import streamlit as st

st.set_page_config(page_title="Lothlórien Workbook", page_icon="🌿")

st.title("🌿 Lothlórien Study Guide")
st.write("Complete the 10 insights below to prepare for the journey ahead.")

# The 10 Questions and Answers you provided
data = [
    {"q": "What does Lothlórien teach about time and memory?", "keys": ["fluid", "blending", "ancient", "past"], "hint": "Think about how the past and present feel like they are mixing together."},
    {"q": "How do the gifts from Galadriel encode character arcs?", "keys": ["arc", "choices", "future", "rope", "phial"], "hint": "Think about how items like the Phial or the Rope help them later."},
    {"q": "Why is beauty presented with moral weight?", "keys": ["moral", "healing", "spiritual", "purity"], "hint": "Is beauty just 'looking good,' or is it a sign of being 'good'?"},
    {"q": "How does Lothlórien differ from other places?", "keys": ["serenity", "purity", "timeless", "corruption"], "hint": "How is it different from the dark, scary places like Moria?"},
    {"q": "What test does Galadriel face with the Ring?", "keys": ["temptation", "queen", "humility", "wisdom", "refusal"], "hint": "What did she imagine she would become if she took it?"},
    {"q": "What does Frodo see in Galadriel's mirror?", "keys": ["future", "suffering", "magnitude", "quest"], "hint": "Does the mirror show happy things or the weight of the mission?"},
    {"q": "How do different members experience the woods?", "keys": ["wonder", "sadness", "longing", "unease"], "hint": "Compare how Legolas feels to how Boromir feels."},
    {"q": "What is the significance of the elven cloaks?", ["protection", "unity", "identity", "symbolic"], "hint": "How do these gifts help them stay hidden and united?"},
    {"q": "How does this time prepare the Fellowship?", ["strength", "counsel", "restore", "spiritually"], "hint": "Did they leave feeling tired or strengthened?"},
    {"q": "What does Galadriel’s song reveal?", ["sorrow", "fading", "passing", "ages"], "hint": "Is the song about things staying the same or things going away?"}
]

# Track progress
score = 0

for i, item in enumerate(data):
    st.subheader(f"Insight {i+1}")
    ans = st.text_input(item['q'], key=f"q{i}").lower()
    
    if ans:
        # Check if they used one of your keywords
        found = [word for word in item['keys'] if word in ans]
        if found:
            st.success(f"✨ Excellent. You recognized the theme of {found[0]}.")
            score += 1
        else:
            st.info(f"💡 Hint: {item['hint']}")
    st.divider()

# Final Progress Bar
st.sidebar.title("Progress")
st.sidebar.progress(score / 10)
st.sidebar.write(f"You have unlocked {score} out of 10 insights.")

if score == 10:
    st.balloons()
    st.sidebar.success("🏆 Master of Lore!")
