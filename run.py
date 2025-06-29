from dotenv import load_dotenv
from backend import create_app

load_dotenv(dotenv_path=".env")

#load_dotenv()  # Load .env variables like API key

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

