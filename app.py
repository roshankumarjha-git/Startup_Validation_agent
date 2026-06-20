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

/* Attempt to kill extra Gradio wrappers */
.form {
    background: transparent !important;
    border: none !important;
}

.block {
    border: none !important;
    box-shadow: none !important;
}

.hero-card {
    background: rgba(15,23,42,0.75);

    border: 1px solid rgba(239,68,68,0.45);

    box-shadow:
        0 0 15px rgba(239,68,68,0.12),
        0 0 30px rgba(236,72,153,0.08);

    backdrop-filter: blur(20px);

    border-radius: 20px;

    padding: 12px;

    margin-bottom: 15px;

    transition: all 0.3s ease;
}

.hero-card:hover {
    box-shadow:
        0 0 25px rgba(239,68,68,0.20),
        0 0 45px rgba(236,72,153,0.12);
}

.gradient-text {
    display: inline-block;

    background: linear-gradient(
        90deg,
        #8b5cf6,
        #ec4899,
        #f97316
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    font-weight: 800;

    transition: all 0.3s ease;
}

.gradient-text:hover {

    transform: scale(1.05);

    filter: drop-shadow(
        0 0 20px rgba(236,72,153,0.7)
    );

    cursor: default;
}

.roshan-badge {
    display: inline-block;

    padding: 10px 20px;

    border-radius: 18px;

    background: rgba(15,23,42,0.95);

    border: 1px solid rgba(239,68,68,0.35);

    transition: all 0.3s ease;
}

.roshan-badge:hover {
    transform: scale(1.05);

    box-shadow:
        0 0 12px rgba(239,68,68,0.20);
}

.startup-class textarea {
    background: rgba(20,20,35,0.95) !important;

    border: 2px solid rgba(168,85,247,0.65) !important;

    border-radius: 18px !important;

    color: white !important;

    transition: all 0.3s ease;
}

.startup-class textarea:hover {

    box-shadow:
        0 0 15px rgba(168,85,247,0.35);
}

.output-class textarea {
    background: rgba(20,20,35,0.95) !important;

    border: 2px solid rgba(249,115,22,0.70) !important;

    border-radius: 18px !important;

    color: white !important;

    transition: all 0.3s ease;
}

.output-class textarea:hover {

    box-shadow:
        0 0 15px rgba(249,115,22,0.30);
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
        0 0 20px rgba(236,72,153,0.35),
        0 0 40px rgba(249,115,22,0.20);

    transition: all 0.3s ease;
}

.big-button:hover {

    transform: scale(1.03);

    box-shadow:
        0 0 30px rgba(236,72,153,0.55),
        0 0 60px rgba(249,115,22,0.35);
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
            <div class="roshan-badge">
                Built by Roshan Kumar Jha
            </div>

        </div>
        '''
    )
    with gr.Row():

        with gr.Column(scale=1):

            with gr.Column():

                startup_input = gr.Textbox(
                    container=False,
                    elem_classes="startup-class",
                    label="🚀 Startup Idea",
                    placeholder="Describe your startup idea here...",
                    lines=5
                )

        with gr.Column(scale=2):

            with gr.Column():

                output = gr.Textbox(
                    container=False,
                    elem_classes="output-class",
                    label="📊 Validation Report",
                    lines=10
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
