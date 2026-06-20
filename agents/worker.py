
from google import genai
import os

from project.mcp.mcp_server import MCPServer
from project.tools.tools import startup_summary

class Worker:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.mcp = MCPServer()

        self.mcp.register_tool(
            "summary",
            startup_summary
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

        summary = self.mcp.call_tool(
            "summary",
            response.text
        )

        return {
            "analysis": response.text,
            "summary": summary
        }
