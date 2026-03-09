import streamlit as st

st.set_page_config(page_title="Lothlórien Guide", page_icon="🍃")

st.title("🌿 The Wisdom of Lothlórien")
st.write("Complete all 10 insights to finish your journey.")

# The data
questions = [
    ("1. What does Lothlórien teach about time and memory?", ["fluid", "blending", "ancient", "past"], "Think about the past and present mixing."),
    ("2. How do Galadriel's gifts foreshadow future events?", ["arc", "choices", "rope", "phial", "sheath"], "Think of Sam's rope or Frodo's light."),
    ("3. Why is beauty presented with moral weight?", ["moral", "healing", "purity"], "Is beauty just 'looks' or is it 'goodness'?"),
    ("4. How does Lothlórien differ from other places?", ["serenity", "purity", "timeless"], "How is it different from Moria?"),
    ("5. What test does Galadriel face with the Ring?", ["temptation", "queen", "humility", "refusal"], "What would she become if she took it?"),
    ("6. What does Frodo see in Galadriel's mirror?", ["future", "suffering", "magnitude", "quest"], "What was the weight of what he saw?"),
    ("7. How do Fellowship members experience the woods?", ["wonder", "sadness", "longing", "unease"], "Think of Boromir vs Legolas."),
    ("8. What is the significance of the elven cloaks?", ["protection", "unity", "identity"], "How do they help the group stay together?"),
    ("9. How does this time prepare the Fellowship?", ["strength", "counsel", "restore"], "Did they leave rested or tired?"),
    ("10. What does Galadriel’s song reveal?", ["sorrow", "fading", "passing", "ages"], "Is it a happy song or a goodbye?")
]

# This part ensures the app doesn't "forget" as the kids type
for i, (q, keys, hint) in enumerate(questions):
    st.subheader(f"Question {i+1}")
    user_input = st.text_input(q, key=f"input_{i}").lower()
    
    if user_input:
        if any(word in user_input for word in keys):
            st.success("✅ Excellent insight!")
        else:
            st.info(f"💡 Hint: {hint}")
    st.divider()

if st.button("I have finished the journey"):
    st.balloons()
    st.confetti()
    st.success("Congratulations! You have mastered the lore of the Golden Wood.")
