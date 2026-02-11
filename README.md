# 🎬 YouTube GPT Agent 🤖

Welcome to **YouTube GPT Agent**, your intelligent companion for consuming YouTube content!

Ever wanted to summarize a long video in seconds? Or ask specific questions about a tutorial without scrubbing through the timeline? This agent does it all for you, powered by the magic of **AutoGen** and **OpenAI**.

---

## 🚀 Features

- **Video Summarization**: Get the gist of any YouTube video instantly.
- **Interactive Q&A**: Ask questions about the video content and get precise answers based on the transcript.
- **Smart Agent**: Utilizes `autogen-agentchat` to process video transcripts intelligently.
- **User-Friendly Interface**: Built with **Streamlit** for a clean and simple experience.

## 🛠️ How It Works

1. **Input URL**: Paste the link to a YouTube video.
2. **Ask Away**: Type your question or request a summary.
3. **Agent Action**: The agent fetches the transcript, analyzes it, and delivers the answer.

## 📦 Installation

To get started, clone this repository and install the dependencies:

```bash
git clone https://github.com/your-username/youtube-gpt-agent.git
cd youtube-gpt-agent
pip install -r requirements.txt
```

## ⚙️ Configuration

You need an API key to run the agent. Create a `.env` file in the root directory and add your key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

*Note: The agent is configured to use `openai/gpt-oss-20b:free` via OpenRouter, but you can modify `agent.py` to use other models.*

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser to the local URL provided (usually `http://localhost:8501`).

## 📸 Demo

![YouTube GPT Agent Interface](Screenshot%202026-02-11%20013943.png)

## 🧩 Tech Stack

- **[Streamlit](https://streamlit.io/)**: The frontend interface.
- **[AutoGen](https://microsoft.github.io/autogen/)**: The agent framework orchestration.
- **[Pytubefix](https://github.com/JuanBindez/pytubefix)**: For fetching YouTube transcripts.
- **OpenRouter / OpenAI**: The LLM backend.

---

Made with ❤️ by [Abdulrahman Mohammed]
