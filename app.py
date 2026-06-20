import gradio as gr

from main_agent import run_agent


def process_input(user_input):
    try:
        return run_agent(user_input)
    except Exception as e:
        return f"Error: {str(e)}"


css = """
body {
    background: linear-gradient(135deg, #0f172a, #111827);
}

.gradio-container {
    max-width: 1200px !important;
}

.hero-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 25px;
}

.gradient-text {
    background: linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa,
        #ec4899
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}
"""

with gr.Blocks(
    theme=gr.themes.Base(),
    css=css
) as demo:

    gr.Markdown("""
# 🚀 Startup Validation Agent

### AI-Powered Startup Intelligence Platform

Validate startup ideas using:

- 📈 Market Analysis
- 🏢 Competitor Research
- ⚔️ SWOT Analysis
- 🧠 Memory Systems
- 🔌 MCP Integration
- 🛡️ Security Protection

<br>

**Built by Roshan Kumar Jha**

---
""")

    startup_input = gr.Textbox(
        label="Startup Idea",
        placeholder="Describe your startup idea here...",
        lines=4
    )

    analyze_btn = gr.Button("Analyze Startup")

    output = gr.Textbox(
        label="Validation Report",
        lines=25
    )

    analyze_btn.click(
        fn=process_input,
        inputs=startup_input,
        outputs=output
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
