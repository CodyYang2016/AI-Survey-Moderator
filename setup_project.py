import os

# Define the directory structure
project_structure = {
        "backend": {
            "survey_app": {
                "static": {},
                "templates": {
                    "survey_start.html": "<!-- HTML Template for survey start -->"
                },
                "__init__.py": "",
                "asgi.py": "# ASGI config",
                "settings.py": "# Django settings",
                "urls.py": "# URL routing for the project",
                "wsgi.py": "# WSGI config"
            },
            "surveys": {
                "migrations": {
                    "__init__.py": ""
                },
                "__init__.py": "",
                "admin.py": "# Django admin setup",
                "apps.py": "# App configuration",
                "models.py": "# Models for Survey, Question, and Response",
                "serializers.py": "# Serializers for API endpoints",
                "tests.py": "# Backend test cases",
                "views.py": "# Views for API",
                "urls.py": "# App-level URL routing"
            },
            "manage.py": "# Django management script"
        },
        "frontend": {
            "public": {
                "index.html": "<!-- React HTML template -->"
            },
            "src": {
                "components": {
                    "SurveyStart.js": "// React component to start survey",
                    "QuestionCard.js": "// React component for questions",
                    "ChatGPTResponse.js": "// React component for GPT responses"
                },
                "pages": {
                    "HomePage.js": "// React Home Page",
                    "SurveyPage.js": "// React Survey Page"
                },
                "services": {
                    "api.js": "// Axios configuration for API calls"
                },
                "styles": {
                    "App.css": "/* App-level CSS styles */"
                },
                "App.js": "// Main React App component",
                "index.js": "// React entry point"
            }
        },
        "docs": {
            "README.md": "# Project Overview",
            "api-specs.md": "# API Specifications"
        },
        "database": {
            "init.sql": "-- SQL schema and seed data"
        },
        ".env": "# Environment variables",
        ".gitignore": "# Git ignore rules",
        "requirements.txt": "# Python dependencies",
        "package.json": "# React project dependencies",
        "Dockerfile": "# Docker configuration",
        "docker-compose.yml": "# Docker Compose setup",
        "tests": {
            "backend": {},
            "frontend": {}
        }
    }


# Function to create the directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Run the script
if __name__ == "__main__":
    base_path = os.getcwd()
    create_structure(base_path, project_structure)
    print("Project structure created successfully!")
