import gradio as gr

from main_agent import run_agent


def process_input(user_input):
    try:
        return run_agent(user_input)
    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.Interface(
    fn=process_input,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your startup idea..."
    ),
    outputs=gr.Textbox(),
    title="🚀 Startup Validation Agent",
    description="""
Validate startup ideas using AI-powered market analysis,
competitor research, SWOT analysis, memory, MCP tools,
and security protection.
"""
)

demo.launch(server_name="0.0.0.0", server_port=7860)
