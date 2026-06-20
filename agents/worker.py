from google import genai
import os

class Worker:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

    def execute(self, plan):

        startup_idea = plan["idea"]

        prompt = f"""
You are a startup validation expert.

Analyze this startup idea:

{startup_idea}

Return:

1. Market Analysis
2. Competitor Analysis
3. SWOT Analysis
4. Validation Score out of 100
5. Recommendation

Keep the response concise.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "analysis": response.text
        }
