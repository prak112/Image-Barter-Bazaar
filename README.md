<h1 align="center"> Ecommerce Photo Store - 🎨 <i>Image Barter Bazaar</i> 📸 </h1>

<hr>

# Overview
A brief introduction of the project, main features, setup instructions, technologies used and resource credits. 

# Contents
- [Aim](#aim)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [Additional Information](#additional-information)
- [Credits](#credits)

</br>
<hr>


# Aim
The aim of the project is to build a functional E-commerce platform with a built-in payment gateway. For tech stack check [Technologies Used](#technologies-used). The platform being a skills demonstration for Full-Stack Development will have browsing functionality and a barter-exchange checkout.

</br>
<hr>

# Features
- Authorize and authenticate Users(Customers) based on their credentials
- Users/Customers can:
  - Register and create their own profiles
  - Browse *Products* and add items to the *Cart*
  - Search *Products* through filters - *Type, Theme & Author*
  - Edit their *Cart* - increase/decrease product quantity, remove product
  - Upload photographs and/or art to the *Product Inventory* as Payment

</br>
<hr>

# Technologies Used
- **Frontend**
  - Figma (UI design)
  - HTML
  - CSS

- **Backend**
  - Django (Python)

- **Database**
  - SQLite


</br>
<hr>

# Project setup
## Setup Local development environment
- In your `bash` terminal, clone the git repository to a new repository, `repo-name` 
    ```bash
        $ git clone https://github.com/prak112/Image-Barter-Bazaar.git
    ```
- After cloning is successful, navigate to project directory, 
    ```bash
        $ cd Image-Barter-Bazaar
    ```

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
- Create a new virtual environment
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
    ```sh
        $ (project_env) path/to/dir> pip install -r requirements.txt
    ```

- Verify if the installed libraries have the required versions from `requirements.txt`
    ```sh
        $ (project_env) path/to/dir> pip list
    ```


<br>

## Execute Project
- Navigate to the project directory (`ecommstore`) where the Django project is located
    ```sh
        $ (project_env) path/to/dir> cd ecommstore
    ```

## Implement Database schema
- Migrate the database design implemented using Django Models in `models.py` in the apps - `photostore` & `users` 
- After creating the neccessary migration files in the `migrations` directory :
    ```sh
        $ (project_env) path/to/dir/ecommstore> python manage.py makemigrations 
    ```
- The above command has no effect if `models.py` is unchanged. 
- In that case, we could just migrate existing Django Models at the beginning of the project :
    ```sh
        $ (project_env) path/to/dir/ecommstore> python manage.py migrate
    ```

## Run server
- After implementing the database schema, run the following command to start the Django development server:
    ```sh
        $ (project_env) path/to/dir/ecommstore> python manage.py runserver
    ```

</br>
<hr>

# Additional Information
- To know more about project plan, implementation, workflows and further enhancements, see [Wiki](https://github.com/prak112/Image-Barter-Bazaar/wiki)

</br>
<hr>

# Credits
- **Planning assistance** 
  - ChatGPT (GPT 3.5)
- **Development assistance** 
  - [![built with Codeium](https://codeium.com/badges/main)](https://codeium.com/badges/main)
  - **GitHub CoPilot**
- **Photos** 
  - *[Pexels](https://www.pexels.com)*
- **Art** 
  - *Bing Copilot Designer*

<br>

[Back To Contents](#contents)

<hr>
