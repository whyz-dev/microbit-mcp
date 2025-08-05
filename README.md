# micro:bit MCP Server

PC에서 micro:bit와 시리얼 통신을 통해 감정을 전송하는 MCP (Model Context Protocol) 서버입니다.

## 🚀 설치 및 설정

### 1. 가상환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. micro:bit 설정

#### 3-1. micro:bit에 예시 코드 업로드

**`example/smile.py`**

```python
def on_data_received():
    global buffer
    buffer = serial.read_until(serial.delimiters(Delimiters.NEW_LINE)).trim()
    if buffer == "smile":
        basic.show_icon(IconNames.HAPPY)
    elif buffer == "frown":
        basic.show_icon(IconNames.SAD)
    elif buffer == "straight":
        basic.show_icon(IconNames.ASLEEP)
    else:
        basic.clear_screen()
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

buffer = ""
```

#### 3-2. micro:bit 연결 확인

## ⚙️ MCP 설정

**`.vscode/settings.json`**

```json
{
  "mcp.servers": {
    "microbit-mcp": {
      "command": "venv/Scripts/python.exe",
      "args": ["src/main.py"]
    }
  }
}
```

**`.cursor/mcp.json`**

```json
{
  "mcpServers": {
    "microbit-mcp": {
      "command": "venv/Scripts/python.exe",
      "args": ["src/main.py"]
    }
  }
}
```

2. **Cursor 재시작**
3. **AI 채팅**에서 MCP 도구 사용 가능

## 🎮 사용법

### 1. MCP 서버 실행

```bash
# 가상환경 활성화 후
python src/main.py
```

### 2. 채팅에서 사용

#### 감정 전송

```
"오늘 기분이 좋아. micro:bit에 표현해줘"
"슬픈 기분을 micro:bit에 보내줘"
"무표정 상태를 micro:bit에 전송해줘"
```

### 3. 감정별 micro:bit 표시

| 감정       | micro:bit 표시 |
| ---------- | -------------- |
| `smile`    | 😊 (웃는 얼굴) |
| `frown`    | 😢 (슬픈 얼굴) |
| `straight` | 😴 (무표정)    |

## 📁 프로젝트 구조

```
microbit-mcp/
├── src/
│   ├── main.py          # MCP 서버 메인 파일
│   └── microbit.py      # micro:bit 통신 클래스
├── microbit/
│   └── smile.py         # micro:bit에 업로드할 코드
├── .vscode/
│   └── settings.json    # VS Code MCP 설정
├── .cursor/
│   └── mcp.json         # Cursor MCP 설정
├── venv/                # 가상환경 (gitignore)
├── requirements.txt     # Python 의존성
└── README.md           # 이 파일
```

## 📜 라이선스

MIT License
