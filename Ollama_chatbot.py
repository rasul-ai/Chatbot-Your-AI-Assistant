import streamlit as st
import ollama

# Streamlit UI
st.title("Chatbot: Your Assistant")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response using Ollama's model
    with st.chat_message("assistant"):
        try:
            response_stream = ollama.chat(
                model="llama3",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,  # Enable streaming response
            )

            response_text = ""
            response_placeholder = st.empty()  # Create an empty placeholder to update the response dynamically

            for chunk in response_stream:
                if "message" in chunk and "content" in chunk["message"]:
                    response_text += chunk["message"]["content"]  # Extract the content
                    response_placeholder.markdown(response_text)  # Update UI

        except Exception as e:
            response_text = f"Error: {str(e)}"
            st.error(response_text)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": response_text})

