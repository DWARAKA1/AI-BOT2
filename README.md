# AI-BOT2 🤖

AI-BOT2 is a modern Streamlit-based chatbot application that uses the Groq API to provide intelligent conversational AI responses.

## ✨ Features

- **Interactive Chat Interface**: Modern chat UI with message history
- **Multiple AI Models**: Choose from various Groq models (Llama, Mixtral)
- **Customizable Settings**: Adjust temperature, max tokens, and model selection
- **Session Management**: Persistent chat history during your session
- **Error Handling**: Robust error handling and user feedback
- **Easy Setup**: Automated setup and testing scripts

## 🚀 Quick Start

### Option 1: Automated Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AI-BOT2.git
   cd AI-BOT2
   ```

2. Run the setup script:
   ```sh
   python setup.py
   ```

3. Edit `.env` file and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key
   ```

4. Test your setup:
   ```sh
   python test_setup.py
   ```

5. Launch the app:
   ```sh
   streamlit run app.py
   ```

### Option 2: Manual Setup

1. Clone and navigate to the project:
   ```sh
   git clone https://github.com/yourusername/AI-BOT2.git
   cd AI-BOT2
   ```

2. Create virtual environment:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure environment:
   ```sh
   copy .env.example .env  # Windows
   cp .env.example .env    # Linux/Mac
   ```
   Then edit `.env` with your Groq API key.

5. Run the application:
   ```sh
   streamlit run app.py
   ```

## 🔧 Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key (required)

### Available Models
- `llama-3.3-70b-versatile` (default)
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`

## 📱 Usage

1. Open your browser to `http://localhost:8501`
2. Configure model settings in the sidebar
3. Start chatting with the AI bot
4. Use "Clear Chat" to reset conversation history

## 🛠️ Project Structure

```
AI-BOT2/
├── app.py              # Main Streamlit application
├── setup.py            # Automated setup script
├── test_setup.py       # Setup verification script
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── LICENSE            # MIT License
```

## 🔍 Troubleshooting

- **API Key Issues**: Ensure your Groq API key is correctly set in `.env`
- **Package Errors**: Run `pip install -r requirements.txt` to install dependencies
- **Port Issues**: If port 8501 is busy, Streamlit will suggest an alternative

## 📄 License

This project is licensed under the MIT License.