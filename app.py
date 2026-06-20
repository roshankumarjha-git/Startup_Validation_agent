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
    background: rgba(15,23,42,0.85);

    border: 1px solid rgba(139,92,246,0.5);

    box-shadow:
        0 0 20px rgba(139,92,246,0.25),
        0 0 40px rgba(59,130,246,0.15);

    backdrop-filter: blur(20px);

    border-radius: 25px;

    padding: 20px;

    margin-bottom: 20px;
}

.gradient-text {
    background: linear-gradient(
        90deg,
        #38bdf8,
        #8b5cf6,
        #ec4899,
        #f97316
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    font-weight: 800;
}

.big-button {
    background: linear-gradient(
        90deg,
        #3b82f6,
        #8b5cf6,
        #ec4899,
        #f97316
    ) !important;

    color: white !important;

    font-weight: bold !important;

    border: none !important;

    box-shadow:
        0 0 20px rgba(168,85,247,0.5),
        0 0 40px rgba(236,72,153,0.4);

    border-radius: 18px !important;

    min-height: 70px !important;

    font-size: 24px !important;
}
"""


with gr.Blocks(
    theme=gr.themes.Base(),
    css=css
    title="Startup Validation Agent"
) as demo:

    gr.HTML(
        '''
        <div class="hero-card">

            <h1
                class="gradient-text"
                style="
                font-size:48px;
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
                    lines=5
                )

        with gr.Column(scale=2):

            with gr.Group(elem_classes="hero-card"):

                output = gr.Textbox(
                    label="📊 Validation Report",
                    lines=12
                )

    analyze_btn = gr.Button(
        ""🚀 ANALYZE STARTUP 🚀"",
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
