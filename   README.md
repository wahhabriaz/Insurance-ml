## Insurance Charges Prediction (Multiple Linear Regression)


🏥 Insurance Charges Prediction (Full-Stack ML)

A full-stack machine learning application that predicts insurance charges using Multiple Linear Regression, served via a FastAPI backend and consumed by a React + Tailwind CSS frontend.

This project focuses on reliable ML engineering, not just model accuracy — including consistent preprocessing, safe inference, and real application integration.

🚀 Demo

🎥 Silent demo video:
Toggle smoker status to observe a large step change in predicted insurance cost — mirroring real-world pricing behavior.

🧠 Key Learnings

Machine learning systems can fail silently if preprocessing is inconsistent

Good evaluation metrics do not guarantee correct inference behavior

Persisting preprocessing + model together prevents production bugs

ML engineering is about trust, reproducibility, and correctness

🏗️ Project Architecture
Insurance-ml/
├── api/                # FastAPI backend
│   └── main.py
├── src/                # ML training & inference
│   ├── data_loader.py
│   ├── pipeline.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── frontend/           # React + Tailwind frontend
├── data/               # Raw dataset (local only)
├── models/             # Saved ML pipeline artifacts
├── requirements.txt
└── README.md

📊 Model Details

Algorithm: Multiple Linear Regression

Target: Insurance charges

Features:

age

bmi

children

sex

smoker

region

Preprocessing: One-hot encoding via ColumnTransformer

Inference Safety: Persisted scikit-learn Pipeline

Performance

R²: ~0.78

RMSE: ~5800

🛠️ Tech Stack
Backend / ML

Python

scikit-learn

Pandas

FastAPI

Joblib

Frontend

React (Vite)

Tailwind CSS

⚙️ Setup & Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/insurance-ml.git
cd insurance-ml

2️⃣ Backend & Model Setup
Create virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux

Install dependencies
pip install -r requirements.txt

Add dataset

Place insurance.csv inside:

data/insurance.csv

Train model
python -m src.train

Evaluate model
python -m src.evaluate

Run API
uvicorn api.main:app --reload --port 8000


Visit:

Health check: http://127.0.0.1:8000/health

API docs: http://127.0.0.1:8000/docs

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:5173

🔁 Example API Request
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 40,
    "sex": "male",
    "bmi": 28,
    "children": 2,
    "smoker": "yes",
    "region": "northwest"
  }'

Response
{
  "predicted_charges": 31898.81
}

🧪 Common Pitfall Addressed

A common production ML bug occurs when:

categorical encoding differs between training and inference

single-row predictions silently drop features

This project fixes that by:
✔ persisting preprocessing + model together
✔ using a single sklearn pipeline for training and inference

🔮 Future Improvements

Add model comparison (Ridge / Lasso)

Log-transformed target

Docker & docker-compose setup

Feature importance visualization in UI

CI/CD for model validation

📌 License

This project is for learning and portfolio purposes.

👋 Author

Abdul Wahhab
Machine Learning / Full-Stack Enthusiast