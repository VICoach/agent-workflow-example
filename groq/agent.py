import asyncio
import websockets
import groq

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

# System prompt for the technical interviewer
# Technical Interviewer Agent System Prompt
system_prompt = """
You are a technical interviewer specializing in software engineering and algorithmic problem-solving. 
Your job is to conduct a coding interview as follows:
1. Give the user a programming problem with specific **time and space complexity constraints**.
2. Ask the user to **explain their approach** before coding.
3. **Evaluate the approach** and verify if it meets the constraints. If not, ask the user to optimize it.
4. Once the user provides a valid approach, ask them to **submit the actual code**.
5. **Review the code**, checking correctness, efficiency, and readability.
6. Provide **detailed feedback** and suggest improvements.
7. Finally, generate a **short report** summarizing the interview and the user's performance.

You must be **structured, professional, and engaging**, encouraging the user to think critically. Keep responses concise but informative.
"""

async def handle_connection(websocket, path=None):  # Make path optional
    # Send a welcome message
    await websocket.send("Welcome to the technical interview! Let's begin.")

    # Initialize conversation with the system prompt
    messages = [{"role": "system", "content": system_prompt}]

    async for message in websocket:
        # Add user message to the conversation
        messages.append({"role": "user", "content": message})

        # Get response from Groq's LLM
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL"),
            messages=messages
        )

        # Extract the LLM's reply
        llm_reply = response.choices[0].message.content

        # Send the reply back to the client
        await websocket.send(llm_reply)

        # Add the LLM's reply to the conversation
        messages.append({"role": "assistant", "content": llm_reply})

# Start the WebSocket server
async def start_server():
    async with websockets.serve(
        handle_connection, "localhost", 8765,
        ping_interval=3600,  
        ping_timeout=3600):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

# Run the server
asyncio.run(start_server())