import gradio as gr
from agent_logic import ConversationalAgent  # Import the ConversationalAgent class

# Initialize the AI agent
agent = ConversationalAgent()

def chatbot_function(user_message):
    return agent.get_ai_response(user_message)

# Create the Gradio interface
iface = gr.Interface(
    fn=chatbot_function,
    inputs="text",  # User input type
    outputs="text",  # AI response type
    live=True,
    title="Conversational AI Chatbot"
)

# Launch the Gradio interface
iface.launch(share=True)
