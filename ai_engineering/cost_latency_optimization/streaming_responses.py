from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv
import os
import time

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env")

app = FastAPI()
llm = ChatOpenAI(streaming=True, temperature=0.7, model="gpt-4o-mini")

def event_stream(prompt_text: str):
    prompt = ChatPromptTemplate.from_messages([
        HumanMessagePromptTemplate.from_template(prompt_text)
    ])
    for chunk in llm.stream(prompt.format_messages()):
        yield f"data: {chunk.content}\n\n"
        time.sleep(0.01)

@app.get("/stream")
def stream_response(prompt: str):
    return StreamingResponse(
        event_stream(prompt),
        media_type="text/event-stream"
    )

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Interactive LLM Streaming</title>
        <style>
            body { font-family: monospace; background-color: #1e1e1e; color: #d4d4d4; padding: 20px; }
            #output { border: 1px solid #555; padding: 10px; height: 400px; overflow-y: auto; white-space: pre-wrap; background-color: #252526; }
            input, button { font-size: 16px; padding: 5px; margin-right: 5px; }
            #form-container { margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <h2>Interactive LLM Streaming</h2>
        <div id="form-container">
            <input type="text" id="prompt" placeholder="Enter your prompt here" size="50">
            <button onclick="startStream()">Send</button>
        </div>
        <div id="output"></div>

        <script>
            let evtSource;

            function startStream() {
                const output = document.getElementById("output");
                const prompt = document.getElementById("prompt").value.trim();

                if (!prompt) {
                    alert("Please enter a prompt!");
                    return;
                }

                output.textContent = "";

                if (evtSource) evtSource.close();

                const url = "/stream?prompt=" + encodeURIComponent(prompt);
                evtSource = new EventSource(url);

                evtSource.onmessage = function(e) {
                    output.textContent += e.data;
                    output.scrollTop = output.scrollHeight;
                };

                evtSource.onerror = function() {
                    output.textContent += "\\n[Connection closed]";
                    evtSource.close();
                };
            }
        </script>
    </body>
    </html>
    """