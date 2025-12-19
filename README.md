Project structure

clipmind/
├── frontend/        # Next.js web app
│   ├── app/
│   ├── components/
│   ├── globals.css
│   └── tailwind.config.js
│
├── backend/         # FastAPI server
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── store.py
│   │   └── main.py
│   ├── uploads/     # ignored in git
│   └── clips/       # ignored in git


Make sure you have the following installed:

Node.js (v18+ recommended)

Python (3.10+ recommended)

FFmpeg & FFprobe

Verify FFmpeg
ffmpeg -version
ffprobe -version


If not installed, download from:
👉 https://www.gyan.dev/ffmpeg/builds/

Run the backend server

cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000


API docs:

http://127.0.0.1:8000/docs

Run the Frontend (Next.js)

cd frontend
npm install
npm run dev



