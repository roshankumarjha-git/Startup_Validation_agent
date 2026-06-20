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
            rgba(168,85,247,0.18),
            transparent 40%
        ),

        radial-gradient(
            circle at top right,
            rgba(249,115,22,0.18),
            transparent 40%
        ),

        #050816;
}

.gradio-container {
    max-width: 1350px !important;
}

.hero-card {
    background: rgba(15,23,42,0.75);

    border: 1px solid rgba(168,85,247,0.25);

    box-shadow:
        0 0 25px rgba(168,85,247,0.12);

    backdrop-filter: blur(20px);

    border-radius: 20px;

    padding: 12px;

    margin-bottom: 15px;
}

.gradient-text {
    background: linear-gradient(
        90deg,
        #8b5cf6,
        #ec4899,
        #f97316
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    font-weight: 800;
}

textarea {
    background: rgba(20,20,35,0.95) !important;

    border: 2px solid rgba(168,85,247,0.5) !important;

    border-radius: 18px !important;

    color: white !important;
}

.output-class textarea {
    border: 2px solid rgba(249,115,22,0.7) !important;
}

.big-button {
    background: linear-gradient(
        90deg,
        #7c3aed,
        #ec4899,
        #f97316
    ) !important;

    color: white !important;

    font-weight: bold !important;

    border: none !important;

    border-radius: 20px !important;

    min-height: 85px !important;

    font-size: 30px !important;

    box-shadow:
        0 0 20px rgba(236,72,153,0.4),
        0 0 40px rgba(249,115,22,0.3);
}

.big-button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 0 30px rgba(236,72,153,0.6),
        0 0 60px rgba(249,115,22,0.4);
}
"""


with gr.Blocks(
    theme=gr.themes.Base(),
    css=css,
    title="Startup Validation Agent"
) as demo:

    gr.HTML(
        '''
        <div class="hero-card">

            <h1
                class="gradient-text"
                style="
                font-size:36px;
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

            with gr.Column():

                startup_input = gr.Textbox(
                    label="🚀 Startup Idea",
                    placeholder="Describe your startup idea here...",
                    lines=5
                )

        with gr.Column(scale=2):

            with gr.Column():

                output = gr.Textbox(
                    label="📊 Validation Report",
                    lines=12
                )

    analyze_btn = gr.Button(
        "🚀 ANALYZE STARTUP 🚀",
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
