# Enhanced Q&A Chatbot With OpenAI

A simple, interactive Q&A chatbot built with Streamlit and LangChain, powered by OpenAI's language models. Supports model selection, temperature control, and token limits — all configurable from the sidebar.

---

## Features

- **Multiple OpenAI models** — choose between `gpt-4o`, `gpt-4`, and `gpt-3.5-turbo`
- **Adjustable temperature** — control response creativity (0.0 to 1.0)
- **Token limit control** — set max response length (50 to 500 tokens)
- **LangSmith tracing** — automatic experiment tracking via LangChain
- **Clean Streamlit UI** — no setup beyond environment variables required

---

## Requirements

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/account/api-keys)
- A [LangChain API key](https://smith.langchain.com/) (for LangSmith tracing)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**

   ```bash
   pip install streamlit openai langchain langchain-openai python-dotenv
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:

   ```env
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

   > Your OpenAI API key is entered directly in the app's sidebar at runtime.

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`.

1. Enter your **OpenAI API key** in the sidebar
2. Select your preferred **model**
3. Adjust **temperature** and **max tokens** as needed
4. Type your question in the input field and hit Enter

---

## Project Structure

```
.
├── app.py          # Main application
├── .env            # Environment variables (not committed)
├── .env.example    # Example env file
└── README.md
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `LANGCHAIN_API_KEY` | API key for LangSmith tracing |

> The OpenAI API key is provided at runtime via the sidebar and is never stored.

---

## LangSmith Tracing

This app automatically logs all LLM calls to [LangSmith](https://smith.langchain.com/) under the project name **"Q&A Chatbot"**. To disable tracing, remove or comment out the `LANGCHAIN_TRACING_V2` line in `app.py`.

---

## License

MIT License. See `LICENSE` for details.
