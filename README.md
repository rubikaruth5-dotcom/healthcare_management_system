
# Healthcare Management System

## Project Overview

The Healthcare Management System is a web-based
backend application developed using Python,
Django REST Framework, and PostgreSQL.

The main purpose of this project is to simplify
hospital management activities by providing
REST APIs to manage patients, doctors,
appointments, departments, medical records,
and healthcare analytics.

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication
- Postman

## Project Applications

This project consists of seven Django applications.

### 1. Authentication
- User login
- Token-based authentication
- User profile
- Logout

### 2. Patients
- Create patient details
- View patient information
- Update patient details
- Delete patient records

### 3. Doctors
- Manage doctor information
- View doctor details
- Update doctor information

### 4. Appointments
- Schedule appointments
- View appointment details
- Manage appointment status

### 5. Departments
- Manage hospital departments
- View department information

### 6. Medical Records
- Maintain patient medical records
- View medical history
- Manage medical information

### 7. Analytics
- Patient statistics
- Doctor statistics
- Appointment statistics
- Healthcare data summaries

## Key Features

- REST API development
- CRUD operations
- Token-based authentication
- PostgreSQL database integration
- Data validation using serializers
- API testing using Postman
- Modular Django application structure

## Project Structure

healthcare-management-system/
|
|-- appointments/
|-- authentication/
|-- analytics/
|-- departments/
|-- patients/
|-- doctors/
|-- medical_records/
|-- main/
|-- manage.py
|-- requirements.txt
|-- README.md
|-- .gitignore

## Installation and Setup

### 1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Navigate to Project Folder

cd healthcare-management-system

### 3. Create Virtual Environment

python -m venv env

### 4. Activate Virtual Environment

Windows:

env\Scripts\activate

### 5. Install Dependencies

pip install -r requirements.txt

### 6. Configure PostgreSQL

Create a PostgreSQL database and configure
the database credentials in Django settings.

Use environment variables to store
sensitive configuration values.

### 7. Apply Migrations

python manage.py migrate

### 8. Run Development Server

python manage.py runserver

### 9. Open Application

http://127.0.0.1:8000/

## API Testing

The REST APIs were tested using:

- Postman
- Django REST Framework Browsable API

## Learning Outcomes

- Django REST Framework development
- PostgreSQL database integration
- API authentication
- CRUD operations
- Serializer validation
- Backend application architecture


