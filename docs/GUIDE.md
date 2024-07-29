<hr>

# Setup Environment
- In your `bash` terminal, clone the git repository to a new repository, `repo-name` 
    ```bash
    $ git clone https://github.com/prak112/DevSchool-Project.git repo-name
    ```
- After successful cloning, change to project directory, `repo-name/DevSchool-Project`

## Install Python
- Visit [Official Python website](https://www.python.org/) and download Python version == 3.11.2 or 3.11.x

- Verify installed version in the terminal
    - For Windows:
        ```cmd
        $ path/to/dir> python --version 
        Python 3.11.2
        ```
    - For Linux/macOS:
        ```bash
        $ path/to/dir> python --V 
        Python 3.11.2
        ```

## Setup Python virtual environment
- Open a terminal or command prompt and navigate to the directory where you want to create your Django project. 
- Run the following command to create a new virtual environment
    - For Windows:
        ```cmd
        $ path/to/dir> python -m venv project_env
        ```
    - For Linux/macOS:
        ```bash
        $ path/to/dir> python3 -m venv project_env
        ```    
    - where `project_env` will be the new directory with all virtual environment files

- Activate virtual environment using the command based on your operating system
    - For Windows:
    ```cmd
    $ path/to/dir> project_env\Scripts\activate.bat
    ```
    - For macOS/Linux:
    ```bash
    $ path/to/dir> source project_env/bin/activate
    ```

## Install dependencies
- Inside the activated virtual environment, install the project dependencies from `requirements.txt`
    ```terminal
    $ (project_env) path/to/dir> pip install -r requirements.txt
    ```

- Verify if the installed libraries have the required versions
    ```terminal
    $ (project_env) path/to/dir> pip list
    ```
    - includes all installed libraries from `requirements.txt`

<br>
<hr>

# Execute Project
- Navigate to the project directory (`ecommstore`) where the Django project is located
    ```terminal
    $ (project_env) path/to/dir> cd ecommstore
    ```

## Implement Database schema
- Migrate the database design implemented using Django Models in `models.py` in the apps - `photostore` & `users` 
- After creating the neccessary migration files in the `migrations` directory using the command :
    ```terminal
    $ python manage.py makemigrations 
    ```
    - However, the above command is useless since `models.py` is currently unchanged. 
    - Hence, we just migrate the existing Django Models using the following command :
    ```terminal
    $ (project_env) path/to/dir/ecommstore> python manage.py migrate
    ```

## Run server
- After implementing the database schema, run the following command to start the Django development server:
    ```terminal
    $ (project_env) path/to/dir/ecommstore> python manage.py runserver
    ```
    - This will start the development server, and you can access your Django project at - http://localhost:8000/

<hr>
<hr>