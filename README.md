# Django FAQ API

## Overview 

The Django FAQ API provides a multilingual FAQ system where users can retrieve frequently asked questions in different languages. The API dynamically translates questions and answers using Google Translate and supports caching for better performance.

## Features

- Supports dynamic translation of FAQs using Google Translate API.
- Caching mechanism to improve response time.
- RESTful API built with Django Rest Framework (DRF).
- Multilingual support (default fallback to English).

## Installation

### Prerequisites

- Python 3.8+
- Django 5.1.5
- PostgreSQL or SQLite (default)
- Redis (for caching, optional but recommended)
- Git

### Steps

1. *Clone the Repository:*

   sh
   git clone https://github.com/ayu-maker/django-faqs.git
   cd django-faqs
   

2. *Create and Activate Virtual Environment:*

   sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   

3. *Install Dependencies:*

   sh
   pip install -r requirements.txt
   

4. *Run Migrations:*

   sh
   python manage.py migrate
   

5. *Start the Development Server:*

   sh
   python manage.py runserver
   

   The API will be available at http://127.0.0.1:8000/api/faqs/.

## API Endpoints

### Get FAQs

- *Endpoint:* /api/faqs/?lang=<language_code>
- *Method:* GET
- *Description:* Retrieves a list of FAQs translated into the requested language.
- *Example Request:*
  sh
  curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=hi"
  
- *Example Response:*
  json
  [
      {
          "question": "तुम्हारा पसंदीदा खाना क्या है?",
          "answer": "मेरा पसंदीदा खाना पनीर टिक्का है।"
      }
  ]
  

### Add a New FAQ (Admin Only)

- *Endpoint:* /admin/
- *Method:* Admin Panel
- *Description:* Admins can add, update, and delete FAQs using Django's built-in admin panel.

## Contribution Guidelines

1. Fork the repository and create a new branch.
2. Follow [PEP8](https://peps.python.org/pep-0008/) for Python code.
3. Use conventional commit messages:
   - feat: Add multilingual FAQ model
   - fix: Improve translation caching
   - docs: Update README with API examples
4. Submit a Pull Request (PR) for review.

## License

This project is open-source and available under the MIT License.

## Contact

For any queries, feel free to reach out:

- GitHub: [ayu-maker](https://github.com/ayu-maker/djangoapp)
