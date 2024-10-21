# AI-Powered Job Portal with Resume Analyzer

This repository contains the codebase for my final year project: **AI-Powered Job Portal with Resume Analyzer**. The project is built using Django and provides a platform for job seekers to upload their resumes for analysis using AI techniques, and for employers to search for candidates based on skills and job requirements.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Resume parsing and skill extraction using machine learning models.
- Job posting and search functionality.
- Employer dashboard for managing job listings.
- Job seeker dashboard for tracking applications.
- Secure user authentication and role-based access control (Admin, Employer, Job Seeker).

## Demo
A live demo of this project can be found at: [Live Demo](#)

*(Note: Add the link to your live deployment if applicable)*

## Technologies Used
- **Back-end**: Django, Python
- **AI Models**: TensorFlow / scikit-learn for resume analysis
- **Database**: PostgreSQL / MySQL
- **Front-end**: HTML, CSS, JavaScript
- **Styling**: Bootstrap / Tailwind CSS
- **Deployment**: Docker

## Project Setup

### 1. Clone the repository
```bash
git clone https://github.com/AmirAbbas101/Final-Year-Project.git
```

### 2. Change to the project directory
```bash
cd Final-Year-Project
```

### 3. Create and activate a virtual environment
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install the dependencies
Once your virtual environment is active, install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Set up the database
- Update your database settings in `settings.py` (or create a `.env` file if you're using environment variables).
- Apply the migrations to set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### 7. Run the application
Start the Django development server:
```bash
python manage.py runserver
```
The app should now be running on `http://127.0.0.1:8000`.

## Running the Application with Docker

Alternatively, you can run the project using Docker. Ensure Docker is installed on your system, then execute the following:

```bash
docker-compose up --build
```

This will start the application and services like the database in a Docker container.

## Usage
1. **Job Seeker**:
    - Register an account.
    - Upload your resume to get matched with job listings.
    - Track your applications through the user dashboard.
  
2. **Employer**:
    - Register or log in.
    - Post job listings and search for candidates by keywords extracted from resumes.
  
3. **Admin**:
    - Manage users, job postings, and overall platform activities from the Django admin panel.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.