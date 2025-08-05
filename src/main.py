from mcp.server.fastmcp import FastMCP
from microbit import Microbit
from typing import Literal

mcp = FastMCP()


@mcp.tool()
def weather(city: str) -> str:
    """현재 날씨 정보를 가져옵니다."""
    return f"현재 {city}의 기온은 20도 입니다."

@mcp.tool()
def send_message(message: str) -> str:
    """micro:bit에 메세지를 전송합니다."""
    mb = Microbit()
    mb.send_message(message)
    return f"메시지 전송됨: {message}"


@mcp.tool()
def smile(emotion: Literal["smile", "frown", "straight"]) -> str:
    """micro:bit에 감정을 전송합니다."""
    mb = Microbit()
    mb.send_message(emotion)
    return f"'{emotion}' 기분이 micro:bit에 전송되었습니다!"


if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="stdio")
    