# Job Recommendation System
## Overview
The *Job Recommendation System* is a web-based application designed to provide personalized job recommendations based on user-selected skills and preferences. It consists of:

1. Backend: A FastAPI-based service for managing user data, job postings, and skill-based recommendations.
2. Frontend: A Streamlit-based user interface for interacting with the backend API.

# Prerequisites
Ensure you have the following installed on your system:

* [Python 3.8 or higher](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

----

## Backend
### Features
* Home:
    ![Home Page](images/homepage.png)
* User Management:
    * User registration and login.
    ![Registration](images/signup.png)
    * Skill-based profile creation.
* Job Management:
    * Create, update, delete, and retrieve job postings.
* Job Recommendations:
    * Recommend jobs based on user skills.
    ![Job Recommendation](images/job.png)
    * Prioritize recommendations by skill match.

#### Installation Instructions
1. Clone the Backend Repository
```
git clone https://github.com/AJAYKUMAR-01/job-recommendation-system-backend.git
cd job-recommendation-system-backend
```

2. Create and Activate a Virtual Environment
```
python -m venv venv
```
For Windows:
```
.\venv\Scripts\activate
```
For macOS/Linux:
```
source venv/bin/activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```
4. Set Up Environment Variables
Create a .env file in the backend/ directory and add:
```
SECRET_KEY=<your_secret_key>
DATABASE_URL=<your_database_url>
```
5. Run the Backend Server
Start the FastAPI server:
```
uvicorn app.main:app --reload
```
The server will be accessible at http://localhost:8000.

#### Backend API Endpoints
**User Management**

1. Register a User:
    * Endpoint: `POST /signup/`
    ![api1](images/api1.png)
2. Log In:
    * Endpoint: `POST /login/`
    ![api2](images/api2.png)
**Job Management**
1. Create a Job:
    * Endpoint: `POST /jobs/`
    ![api3](images/api3.png)

**Recommendations**
1. Get Job Recommendations:
    * Endpoint: `GET /recommendations/{user_id}`
    ![api4](images/api4.png)

---

## Frontend
### Features
* User Authentication:
    * Register and log in users.
* Job Recommendations:
    * Display personalized job recommendations.
* Visualization:
    * Interactive graphs showing skill-to-job mappings.
### Installation Instructions

1. Clone the Frontend Repository
```
git clone https://github.com/your-username/job-recommendation-system-frontend.git
cd job-recommendation-system-frontend
```

2. Create and Activate a Virtual Environment
```
python -m venv venv
```
For Windows:
```
.\venv\Scripts\activate
```
For macOS/Linux:
```
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```

4. Run the Frontend
Start the Streamlit application:
```
streamlit run app.py
```
The application will be accessible at `http://localhost:8501`.

---

## Deployment with Docker

### 1. Build and Run with Docker Compose
Use the `docker-compose.yml` file to run both frontend and backend:
```
docker-compose build
docker-compose up
```

### 2. Access the Application
* Backend: `http://localhost:8000`
* Frontend: `http://localhost:8501`

---

## Testing
### Backend
1. Run unit tests:
```
pytest
```
2. Test APIs using the `/docs` Swagger UI.
![Swagger UI](images/SwaggerUI.png)

### Frontend
1. Test user registration and login.
2. Verify job recommendations and visualizations.

---

## Future Enhancements
* Add JWT-based authentication.
* Introduce advanced job filters (e.g., location, salary).
* Enhance the visualization with analytics dashboards.

---

### License
This project is licensed under the MIT License.