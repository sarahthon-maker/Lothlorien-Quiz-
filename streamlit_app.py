import streamlit as st

st.set_page_config(page_title="Lothlórien Workbook", page_icon="🌿")

# --- UI STYLING ---
st.title("🌿 The Wisdom of Lothlórien")
st.markdown("""
Welcome, traveler. Use this workbook to reflect on the themes of the Golden Wood. 
Type your insights into the boxes below. If you're on the right track, the Sage will confirm it!
""")

# --- THE DATA (10 Questions) ---
data = [
    {
        "q": "1. What does Lothlórien teach about time and memory?", 
        "keys": ["fluid", "blending", "ancient", "past", "memory"], 
        "hint": "Think about how the past and present feel like they are mixing together."
    },
    {
        "q": "2. How do the gifts from Galadriel encode character arcs?", 
        "keys": ["arc", "choices", "future", "rope", "phial", "sheath"], 
        "hint": "Think about how items like the Phial or the Rope help them later."
    },
    {
        "q": "3. Why is beauty presented with moral weight?", 
        "keys": ["moral", "healing", "spiritual", "purity", "goodness"], 
        "hint": "Is beauty just 'looking good,' or is it a sign of being 'good'?"
    },
    {
        "q": "4. How does Lothlórien differ from other places (like Moria)?", 
        "keys": ["serenity", "purity", "timeless", "corruption", "light"], 
        "hint": "How is it different from the dark, scary places they just left?"
    },
    {
        "q": "5. What test does Galadriel face with the Ring?", 
        "keys": ["temptation", "queen", "humility", "wisdom", "refusal"], 
        "hint": "What did she imagine she would become if she took it?"
    },
    {
        "q": "6. What does Frodo see in Galadriel's mirror?", 
        "keys": ["future", "suffering", "magnitude", "quest", "eye"], 
        "hint": "Does the mirror show happy things or the weight of the mission?"
    },
    {
        "q": "7. How do different members experience the woods?", 
        "keys": ["wonder", "sadness", "longing", "unease", "heart"], 
        "hint": "Compare how Legolas feels to how Boromir or Sam feel."
    },
    {
        "q": "8. What is the significance of the elven cloaks?", 
        "keys": ["protection", "unity", "identity", "symbolic", "camouflage"], 
        "hint": "How do these gifts help them stay hidden and united?"
    },
    {
        "q": "9. How does this time prepare the Fellowship?", 
        "keys": ["strength", "counsel", "restore", "spiritually", "rest"], 
        "hint": "Did they leave feeling tired or strengthened?"
    },
    {
        "q": "10. What does Galadriel’s song reveal?", 
        "keys": ["sorrow", "fading", "passing", "ages", "farewell"], 
        "hint": "Is the song about things staying the same or things going away?"
    }
]

# --- APP LOGIC ---
score = 0
my_bar = st.progress(0)

# Loop through questions
for i, item in enumerate(data):
    st.subheader(f"Insight {i+1}")
    ans = st.text_input(item['q'], key=f"q{i}").lower()
    
    if ans:
        found = [word for word in item['keys'] if word in ans]
        if found:
            st.success(f"✨ Excellent. You recognized the theme of: {', '.join(found)}.")
            score += 1
        else:
            st.info(f"💡 The Sage Whispers: {item['hint']}")
    st.divider()

# Update progress
my_bar.progress(score * 10)

if score == 10:
    st.balloons()
    st.success("🏆 You have mastered the lore of the Golden Wood!")
