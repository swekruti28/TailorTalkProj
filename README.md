# TailorTalk 🧵

TailorTalk is a project that lets users book tailor appointments through a simple Streamlit interface, which sends events to a Google Calendar.

## How to Run (Manually)

1. Clone or download this project to your local machine.

2. Install Python if it's not installed.

3. Open the project folder and install dependencies by running:
   - Open command prompt inside the folder.
   - Run: pip install -r requirements.txt

4. Place your credentials.json (from Google Cloud Console) inside this folder.

5. Start the backend:
   - Open command prompt in the folder
   - Run: uvicorn main:app --reload

6. Open a new command prompt, and run:
   - streamlit run streamlit_app.py

That's it! The Streamlit page will open in your browser.

## Note
The file credentials.json is excluded for security using .gitignore.
