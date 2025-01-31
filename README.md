# BharatFD_backend
# Django FAQ Project

This project is designed to implement a Django application that manages Frequently Asked Questions (FAQs) with multilingual support, a WYSIWYG editor, caching, and API access. Below are the detailed steps and explanations for setting up and using the project.

## Features
- Multilingual support for FAQs (English, Hindi, Bengali, etc.).
- WYSIWYG editor integration using `django-ckeditor` for rich text formatting.
- REST API endpoints for FAQ management with language selection.
- Caching mechanism using Django cache framework and Redis for enhanced performance.
- Automated translations using the `deep-translator` library.
- Admin interface for managing FAQs.
- Docker support for containerized deployment.

## Installation

### Prerequisites
- Python 3.13.1 or above
- Django 4.x
- Redis server
- Docker (optional, for containerized deployment)

### Steps

1. Clone the Repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` File:
   Create a `.env` file in the root directory and provide the following environment variables:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

5. Apply Migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the Server:
   ```bash
   python manage.py runserver
   ```

## API Usage

### Endpoints

- **Fetch FAQs in English (default):**
  ```bash
  GET http://localhost:8000/api/faqs/
  ```

- **Fetch FAQs in Hindi:**
  ```bash
  GET http://localhost:8000/api/faqs/?lang=hi
  ```

- **Fetch FAQs in Bengali:**
  ```bash
  GET http://localhost:8000/api/faqs/?lang=bn
  ```

### Example Response
```json
[
  {
    "id": 1,
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework.",
    "language": "en"
  },
  {
    "id": 2,
    "question": "डjango क्या है?",
    "answer": "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
    "language": "hi"
  }
]
```

## Admin Panel

The admin panel is accessible at:
```
http://localhost:8000/admin/
```
Use the superuser credentials to log in and manage FAQs.

 application will be available at `http://localhost:8000/`.
```
Happy coding! 🚀
