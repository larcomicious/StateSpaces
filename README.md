# State Spaces 🏢

A venue reservation system built for CSCI 41 (Information Management) at Ateneo de Manila University.

State Spaces allows customers to browse and reserve venues across multiple buildings,
with agents managing venue availability and maintenance teams.

## Features

- Browse venues by building, capacity, floor area, and type
- Make reservations with time slot conflict detection
- Renovation status tracking (unavailable venues auto-blocked)
- Agent and team management per building
- Amenity listings per venue

## Tech Stack

- **Frontend:** Streamlit
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Language:** Python 3.10

## Database Schema

The system models 6 core entities:

`Building` → `Venue` → `Amenity`  
`Venue` ← `Agent` ← `Team`  
`Venue` ← `Reservation` ← `Customer`

## Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL (ensure the service is running before starting the app)

### Setup

1. Clone the repo
```bash
   git clone https://github.com/yourusername/state-spaces.git
   cd state-spaces
```

2. Create and activate a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Set up the database
   - Make sure PostgreSQL is running
   - Create a database in pgAdmin or psql:
```sql
   CREATE DATABASE statespaces;
```
   - Load the schema and seed data:
```bash
   psql -U postgres -d statespaces -f db-working.sql
```

5. Configure your database connection by creating `.streamlit/secrets.toml`:
```toml
   [connections.postgresql]
   dialect = "postgresql"
   host = "localhost"
   port = 5432
   database = "statespaces"
   username = "postgres"
   password = "your_postgres_password"
```

6. Run the app
```bash
   streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

## Notes

- Use `secrets.toml.example` as a reference for the required format
- The `db-working.sql` file includes sample data for 3 buildings, 5 venues, 5 customers, and reservations