# Flask Blog

Flask Blog is a web application built with Flask, a lightweight web framework in Python. It allows users to create, publish, and manage blog posts.

## Features

- User registration and authentication system
- Create, edit, and delete blog posts
- View and comment on blog posts
- User profile management
- Responsive design for mobile and desktop devices

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
```

1. Change to the project's directory:

```
cd FlaskBlog
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

* On Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```

* On macOS and Linux:
```
source venv/bin/activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Set up the database:

* Create a PostgreSQL database.
* Update the SQLALCHEMY_DATABASE_URI variable in the config.py file with your database URI.

6. Start the application:

```
python run.py
```

The application will be accessible at http://localhost:5000.

## Deployment
The application can be deployed on Render. To do so, follow these steps:

1. Set up an account on Render (https://render.com/) if you haven't already.

2. Create a new web service on Render.

3. Configure the following settings in the Render dashboard:

* Build Command: pip install -r requirements.txt
* Start Command: gunicorn run:app

4. Set up the required environment variables:

* SQLALCHEMY_DATABASE_URI: The URI for your production database.
* Other configuration variables as needed.

5. Deploy the application.

## Contributing
Contributions are welcome! If you'd like to contribute to Flask Blog, please follow these steps:

1. Fork the repository.

2. Create a new branch:
```
git checkout -b feature/my-new-feature
```

3. Commit your changes:
```
git checkout -b feature/my-new-feature
```

4. Push the branch to your forked repository:
```
git push origin feature/my-new-feature
```

5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.