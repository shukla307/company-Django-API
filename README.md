# company-Django-API

## Overview
JoshProject is a task management application built with Django and Django REST Framework. It provides a RESTful API to manage tasks, allowing users to create tasks, assign them to multiple users, and retrieve tasks assigned to specific users. The project follows Django best practices and includes clean, maintainable code with proper documentation.

### Features
- **Create Tasks:** Create a new task with a name, description, and task type.
- **Assign Tasks:** Assign a task to one or multiple users.
- **Retrieve User Tasks:** Fetch all tasks assigned to a specific user.
- **Admin Interface:** Manage tasks and users via Django's admin panel.

### Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default, can be configured for other databases like PostgreSQL)
- **Python Version:** 3.8 or higher


## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation
1. **Clone the Repository (if applicable):**
   ```bash
   git clone <repository-url>
   cd joshproject

### Create and Activate a Virtual Environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Apply Migrations
python manage.py makemigrations
python manage.py migrate

### Create a Superuser (for Admin Access)
python manage.py createsuperuser

### Run the Development Server:
python manage.py runserver

The server will run at http://127.0.0.1:8000/



# API Endpoints
### 1. Create a Task

URL: POST /api/tasks/create/
Description: Creates a new task.
Request Body
{
    "name": "Complete Project",
    "description": "Finish the task management system",
    "task_type": "urgent",
    "assigned_user_ids": [1]
}

Response: 

# Assign a Task to Users
### URL: PUT /api/tasks/<task_id>/assign/

Description: Assigns a task to one or more users.

Request Body:
{
    "assigned_user_ids": [1, 2]
}


# 3. Get Tasks for a Specific User
### URL: GET /api/users/<user_id>/tasks/

Description: Retrieves all tasks assigned to a specific user.

Response:

<img width="1059" alt="image" src="https://github.com/user-attachments/assets/1518fccb-e974-447c-960a-70662f97b08e" />


<img width="954" alt="image" src="https://github.com/user-attachments/assets/a87a1ea4-dd41-428d-b64f-9c48da6927b2" />


<img width="731" alt="image" src="https://github.com/user-attachments/assets/453b4237-d73b-4644-b534-e8da78bb61a6" />


<img width="876" alt="image" src="https://github.com/user-attachments/assets/b8b0869b-16ae-4d41-bfbe-458a739b778e" />


<img width="728" alt="image" src="https://github.com/user-attachments/assets/ab2333b6-5323-4928-8278-ac04c008a750" />


<img width="872" alt="image" src="https://github.com/user-attachments/assets/fb34efd8-49dd-437d-b4af-07f0d9f3cc70" />

