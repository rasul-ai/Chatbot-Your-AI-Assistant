import streamlit as st
import numpy as np

# with st.chat_message("user"):
#     st.write("Hello Sweetheart: ")
#     prompt = st.chat_input("Say something")
#     if prompt:
#         st.write(f"User has sent the following prompt: {prompt}")

st.title("My ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Take user input using this line of code...
if prompt := st.chat_input("Say Something..."):
    # Display user message in chat message container
    
    # ekhane markdown ki korteche bujhte hobe...
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    response = f"Assistant: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


## To input create a message container    
# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))