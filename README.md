# TaskTracker Todo App

TaskTracker is a simple and intuitive Todo App that allows you to manage your tasks effectively. With TaskTracker, you can create task lists, add tasks with due dates, and prioritize them to stay organized and focused.

## Features

- **Task Lists:** Create custom task lists to organize your tasks based on different projects or categories.

- **Add Tasks:** Easily add tasks to your lists with details such as title, due date, and priority.

- **Due Dates:** Set due dates for your tasks to stay on top of deadlines.

- **Priority Levels:** Prioritize your tasks with different levels such as Low, Medium, and High.

## Getting Started

### Prerequisites

- **Python 3.11.5:** Make sure you have Python 3.11.5 installed on your machine. You can download it from [python.org](https://www.python.org/).

- **PostgreSQL 16 or Above:** TaskTracker requires PostgreSQL version 16 or above for the database. You can download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/).

### Setup .env File

1. In the root folder of the project, create a file named `.env`.

2. Add the following configuration fields to the `.env` file:

   ```env
   DATABASE_NAME='xxxxx'
   DATABASE_USER='xxxxx'
   DATABASE_PASS='xxxxx'
   DATABASE_HOST='xxxxx'
   DATABASE_PORT='xxxxx'
   ```
   Replace the placeholders (xxxxx) with your actual database configuration.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/tasktracker.git
    ```
2. **Navigate to the project directory:**

   ```bash
   cd tasktracker
   ```
3. **Create a virtual environment:**

   ```bash
    python -m venv venv
    ```
4. **Activate the virtual environment:**

   ```bash
   venv\Scripts\activate
   ```
5. **Install the requirements:**

   ```bash
    pip install -r requirements.txt
    ```
6. **Migrate the database:**

   ```bash
    python manage.py makemigrations migrate
    python manage.py migrate
    ```
7. **Run the development server:**

   ```bash
    python manage.py runserver
    ```
## View the API using Swagger

To explore the API documentation and interact with the endpoints, you can use Swagger. Follow the steps below:

1. **Open your web browser:**

   Open your preferred web browser.

2. **Navigate to Swagger UI:**

   Enter the following URL in the address bar:

    ```bash
   http://localhost:8000/swagger/
    ```
## License

This project is licensed under the MIT License.