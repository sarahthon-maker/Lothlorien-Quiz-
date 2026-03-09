import streamlit as st

st.set_page_config(page_title="Sage of Lórien", page_icon="🍃")
st.title("🌿 The Sage of Lothlórien")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "I am the Sage of these woods. Ask me about time, the Lady's gifts, or the Mirror, and we shall discuss their meaning."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Speak, traveler..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # The "Better Ears" Logic
    u = prompt.lower()
    resp = ""

    if any(w in u for w in ["time", "past", "years", "memory", "ancient"]):
        resp = "In Lórien, the past is not gone; it stays alive in our memories. Does it feel strange to walk in a place where time seems to stand still?"
    elif any(w in u for w in ["gift", "rope", "light", "phial", "sheath", "belt"]):
        resp = "The Lady's gifts are for more than just survival. They represent the choices each member must make. Which gift do you think holds the most power?"
    elif any(w in u for w in ["ring", "temptation", "test", "queen"]):
        resp = "The Lady Galadriel passed her test by refusing the Ring. It shows that even the most powerful must choose humility. What would have happened if she failed?"
    elif any(w in u for w in ["mirror", "future", "vision", "see"]):
        resp = "The Mirror shows many things—some that have not yet come to pass. Do you think it is a gift or a curse to see the future?"
    elif any(w in u for w in ["beauty", "pretty", "nice", "healing", "pure"]):
        resp = "The beauty here is a reflection of goodness. It heals the spirit. Did the Fellowship seem more rested after staying with us?"
    elif any(w in u for w in ["cloak", "clothes", "hidden", "gray"]):
        resp = "Our elven cloaks are woven with the colors of the leaves and stones. They provide protection through unity. Why is it important for the group to look the same?"
    else:
        resp = "That is a deep thought. Tell me, how does that help the Fellowship prepare for the darkness of Mordor?"

    with st.chat_message("assistant"):
        st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})
