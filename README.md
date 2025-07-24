# UK Meltdown Dashboard

A real-time dashboard for visualising key UK economic indicators — starting with 10-Year Gilt yields.

Built with:
- **Dash** for interactive visualisation
- **PostgreSQL** as the backend store (in Docker)
- **Python (pandas, SQLAlchemy)** for data ingestion
- **FRED API** for primary yield data, with Kaggle fallback
- **Docker Compose** for full environment orchestration

---

## 📦 Project Structure

.
├── app/
│ ├── dashboard.py # Dash app
│ ├── collect_gilts.py # Ingests data into DB
│ ├── init_db.py # Creates schema
│ ├── db_connection.py # SQLAlchemy engine
│ └── *_client.py # Data source clients
├── data/ # Fallback CSVs
├── .env # Secrets (excluded from Git)
├── requirements.txt # Python deps
├── Dockerfile
├── docker-compose.yml
└── Makefile


---

## 🚀 Usage

### 1. Build and start the dashboard:

make up

### 2. Initialise the database:

make init

### 3. Ingest latest data:

make ingest

Then open http://localhost:8050

🔐 .env format

Create a .env file in the root with:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=supersecret
POSTGRES_DB=uk_meltdown
FRED_API_KEY=your_fred_api_key

Never commit this file — it's excluded by .gitignore.
🛠 Development

You can run ingestion or schema setup manually like this:

docker compose run --rm app python init_db.py
docker compose run --rm app python collect_gilts.py

Or rebuild everything clean:

make rebuild

📈 Future Plans

    Add CPI, GDP, and BoE rate data from FRED + ONS

    Improve visualisation and interactivity

    Schedule ingestion and deploy to live server


---
