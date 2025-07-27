# 📡 Sensor API Mini Project

A lightweight API built for collecting and managing sensor data. Ideal for learning backend simulation, Docker deployment, and exploring DevOps pipelines.

---

# 🚀 Getting Started

# 🐳 Build Docker Image

```bash
docker build -t sensor-api .

docker run -p 5000:5000 sensor-api

sensor-api/
├── app.py              # Main Flask/FastAPI app
├── Dockerfile          # Docker setup for deployment
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to exclude from Git
└── README.md           # Project overview

