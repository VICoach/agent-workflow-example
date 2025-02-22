## Setting Up the Project

### Create a Virtual Environment
```bash
python -m venv venv
```

### Activate the Virtual Environment
- On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a .env File
Create a `.env` file in the root directory of your project and add the following variables:
```
MODEL=your_model_name
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_groq_model
```

## Testing Groq Agent

### Start the Groq Agent
```bash
python groq/agent.py
```

### Start the Groq WebSocket
```bash
python groq/ws.py
```

## Testing the Streamlit App

### Run the Streamlit App
```bash
streamlit run app/app.py
```
