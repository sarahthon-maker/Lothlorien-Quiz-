import streamlit as st

st.set_page_config(page_title="Lothlórien Sage", page_icon="🍃")

st.title("🌿 Conversation with the Sage")
st.write("Discuss the mysteries of the Golden Wood. The Sage remembers what you say!")

# 1. Initialize the memory (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Greetings, traveler. I am the Sage of Lórien. What would you like to discuss? Perhaps the nature of Time, or the gifts of the Lady?"}
    ]

# 2. Display the conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. The "Brain" - Logic to respond more than once
if prompt := st.chat_input("Type your thoughts here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate the Sage's response
    with st.chat_message("assistant"):
        response = ""
        user_text = prompt.lower()

        # Simple logic to "Guide" them based on what they type
        if "time" in user_text or "memory" in user_text:
            response = "Time here is fluid, like a river. Do you think the Elves stay here to remember the past, or to protect the present?"
        elif "gift" in user_text or "galadriel" in user_text:
            response = "The Lady's gifts are mirrors of the heart. Which gift do you think was most important for the journey ahead?"
        elif "beauty" in user_text:
            response = "In this wood, beauty is a shield against the shadow. Does it feel like a place of healing to you?"
        else:
            response = "That is an interesting perspective. Tell me more about how that connects to what the Fellowship experienced in Lothlórien."

        st.markdown(response)
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})
