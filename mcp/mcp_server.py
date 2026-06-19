
class MCPServer:

    def __init__(self):
        self.tools = {}

    def register_tool(self, tool_name, tool_function):
        self.tools[tool_name] = tool_function

    def call_tool(self, tool_name, *args, **kwargs):

        if tool_name not in self.tools:
            return f"Tool '{tool_name}' not found."

        return self.tools[tool_name](*args, **kwargs)
