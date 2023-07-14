# Authentication & Production Server

This lab focuses on enhancing the API by adding JWT authentication and switching to a production server. It involves configuring authentication using JSON Web Tokens (JWT) and replacing Django's built-in development server with Gunicorn. Additionally, it covers handling static files using Whitenoise.

## Features - Django

### Add JWT Authentication to your API

To add JWT authentication to your API, follow these steps:

1. Install the required libraries by running the following command:
```python
pip install djangorestframework-jwt
```

2. Configure JWT authentication in your Django project:
- Modify the `settings.py` file and include the necessary configurations for JWT authentication. Specify the authentication backend, token expiration time, etc. Refer to the documentation of the library you're using for detailed instructions.

3. Implement the authentication logic in your API views or viewsets:
- Generate JWT tokens upon successful authentication and include them in the response to the client.
- Validate the JWT tokens in subsequent requests to ensure the user is authenticated.

4. Test the JWT authentication by making API requests with the appropriate authentication headers. You can use tools like Postman or cURL to send authenticated requests.

**Example API Requests:**

- Request: `POST http://127.0.0.1:8000/api/token/`
  - Description: This request is used to obtain an access token by providing valid user credentials.
  - Headers:
    ```
    Content-Type: application/json
    ```
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - Response:
    ```json
    {
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTM1ODE5MywiaWF0IjoxNjg5MjcxNzkzLCJqdGkiOiI4YWQxY2Y1ODBhNmE0NjQzOGJkYmJlMmE3ZWVjM2I5OSIsInVzZXJfaWQiOjF9.wX81vEmTo_6Fm6bCNT0a_dpTL1sAER-FbjmVMyUy5w8",
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjcyMDkzLCJpYXQiOjE2ODkyNzE3OTMsImp0aSI6IjVlY2ExM2I3ZmYwNzRiMjViODRiNzVmNzAyMjhlZGI1IiwidXNlcl9pZCI6MX0.NbFuKIYHSk2iX2RJF5Gw-t3p_zUeENa5NuahjF80aDc"
    }
    ```
* ex :
    ![ree](https://github.com/mohammadalsmadi2000/drf-auth/assets/60603704/c4e35a71-54fb-4d33-9fbb-365d01a55db6)


- Request: `POST http://127.0.0.1:8000/api/token/refresh/`
  - Description: This request is used to refresh an expired access token by providing a valid refresh token.
  - Headers:
    ```
    Content-Type: application/json
    ```
  - Request Body:
    ```json
    {
      "refresh": "your_refresh_token"
    }
    ```
  - Response:
    ```json
    {
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTM1ODE5MywiaWF0IjoxNjg5MjcxNzkzLCJqdGkiOiI4YWQxY2Y1ODBhNmE0NjQzOGJkYmJlMmE3ZWVjM2I5OSIsInVzZXJfaWQiOjF9.wX81vEmTo_6Fm6bCNT0a_dpTL1sAER-FbjmVMyUy5w8"
    }
    ```
* ex :
  ![rt](https://github.com/mohammadalsmadi2000/drf-auth/assets/60603704/083428e8-fea6-4ac5-9545-e13038e13cf2)

## Features - Docker

### Switch to using Gunicorn instead of Django's built-in development server

To switch to using Gunicorn as the production server, perform the following steps:

1. Install Gunicorn using the following command:
```
pip install gunicorn
```

2. Configure Gunicorn in your project:
- Create a new file named `gunicorn.conf.py` in the project root directory.
- Specify the Gunicorn settings in this file, such as the number of workers, log file paths, and bind address. Refer to Gunicorn's documentation for available configuration options.

3. Update your Docker configuration to use Gunicorn:
- Modify your `Dockerfile` or `docker-compose.yml` file to include the necessary commands to run Gunicorn with your Django application.
- Ensure that Gunicorn is executed with the configurations specified in `gunicorn.conf.py`.

### Handle static files using Whitenoise

To handle static files in a production environment using Whitenoise, follow these steps:

1. Install the `whitenoise` library using the following command:
```
pip install whitenoise
```

2. Update your project's `settings.py` file:
- Add `whitenoise.middleware.WhiteNoiseMiddleware` to the middleware list, placing it after the `SecurityMiddleware` but before the `CommonMiddleware`.
- Configure the `STATIC_ROOT` and `STATIC_URL` settings. Set `STATIC_ROOT` to the directory where your static files will be collected during deployment.

3. Run the `collectstatic` management command to gather static files:
```
python manage.py collectstatic

```

4. Verify that the static files are served correctly by running your application with Gunicorn.

## Documentation

`Please refer to the provided README.md file for detailed instructions on setting up authentication and the production server. The README file explains the steps for adding JWT authentication to the API, retaining pre-existing authentication, switching to Gunicorn, and handling static files using Whitenoise. It also includes additional information and instructions to help you understand and replicate the setup.`

