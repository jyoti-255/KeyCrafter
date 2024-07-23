# Random Password Generator

This Django web application generates random passwords based on user-defined criteria such as length, inclusion of uppercase letters, and digits.

## Features
- Generate random passwords
- Customize password length
- Option to include uppercase letters and digits

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Open your web browser and go to https://keycrafter.pythonanywhere.com/
2. Specify the desired password length and options.
3. Click "Generate" to get your random password.

## Project Structure
- `views.py`: Contains the logic for generating passwords and rendering templates.
- `templates/`: Directory containing HTML templates (`home.html`, `result.html`, `page404.html`).

