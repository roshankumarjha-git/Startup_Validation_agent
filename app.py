import gradio as gr

from main_agent import run_agent


def process_input(user_input):
    try:
        return run_agent(user_input)
    except Exception as e:
        return f"Error: {str(e)}"


css = """
body {
    background:
        radial-gradient(
            circle at top left,
            rgba(59,130,246,0.25),
            transparent 40%
        ),

        radial-gradient(
            circle at top right,
            rgba(168,85,247,0.25),
            transparent 40%
        ),

        #050816;
}

.gradio-container {
    max-width: 1400px !important;
}

.hero-card {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(25px);
    border-radius: 25px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 25px;
}

.gradient-text {
    background: linear-gradient(
        90deg,
        #60a5fa,
        #8b5cf6,
        #ec4899
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    font-weight: 800;
}

.big-button {
    margin-top: 20px;
}
"""


with gr.Blocks(
    theme=gr.themes.Base(),
    css=css
) as demo:

    gr.HTML(
        '''
        <div class="hero-card">

            <h1
                class="gradient-text"
                style="
                font-size:72px;
                margin-bottom:10px;
                "
            >
                🚀 Startup Validation Agent
            </h1>

            <h2
                style="
                color:#cbd5e1;
                margin-bottom:15px;
                "
            >
                AI-Powered Startup Intelligence Platform
            </h2>

            <p
                style="
                font-size:20px;
                color:#94a3b8;
                "
            >
                Validate ideas before you waste months building them.
            </p>

            <br>

            <div
                style="
                display:inline-block;
                padding:10px 20px;
                border-radius:20px;
                background:rgba(59,130,246,0.15);
                border:1px solid rgba(96,165,250,0.3);
                "
            >
                Built by Roshan Kumar Jha
            </div>

        </div>
        '''
    )
    with gr.Row():

        with gr.Column(scale=1):

            with gr.Group(elem_classes="hero-card"):

                startup_input = gr.Textbox(
                    label="🚀 Startup Idea",
                    placeholder="Describe your startup idea here...",
                    lines=6
                )

        with gr.Column(scale=2):

            with gr.Group(elem_classes="hero-card"):

                output = gr.Textbox(
                    label="📊 Validation Report",
                    lines=15
                )

    analyze_btn = gr.Button(
        "✨ ANALYZE STARTUP ✨",
        size="lg",
        elem_classes="big-button"
    )

    analyze_btn.click(
        fn=process_input,
        inputs=startup_input,
        outputs=output
    )


demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)
