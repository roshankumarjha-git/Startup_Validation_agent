import gradio as gr

from project.main_agent import run_agent


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
    title="Startup Validation Agent",
    description="AI-powered startup validation using Multi-Agent Architecture, MCP, Memory, and Security."
)

demo.launch(server_name="0.0.0.0", server_port=7860)
