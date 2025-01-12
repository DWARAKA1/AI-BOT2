# AI-BOT2

AI-BOT2 is a Streamlit-based chatbot application that uses the Groq API to generate responses to user inputs.

## Features

- User-friendly interface with Streamlit
- Integration with Groq API for generating chat completions
- Environment variable management with `dotenv`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/AI-BOT2.git
    cd AI-BOT2
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your Groq API key:

    ```env
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the chatbot.

## License

This project is licensed under the MIT License.