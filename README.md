# My Insurance App

## Install Dependencies
- pip install -r requirements.txt
  - If you have old version of project: pip uninstall -r requirements.txt

## Init database (before launching app)
- py project/init/init_db.py

## Run the server
- py runserver.py
- Access web at: http://localhost:5000/
- API at: http://localhost:5000/api/v1/

## Authentication
- For web and API use:
  - Email: jd@myinsuranceapp.com
  - Password: passwordjd

## API endpoints
- Authenticate: http://localhost:5000/api/v1/token
  - Method POST
  - Payload {email:<email_value>,password:<pass_value>}
  - All endpoints require token in header in this way:
    - {Aunthenticate: Bearer <token>}
- Endpoints:
  - Users: http://localhost:5000/api/v1/users
  - Products: http://localhost:5000/api/v1/products

## Testing
- Unit tests:
  -  py -m unittest discover -s tests/unit -v
- Acceptance tests from inside:
  - py -m unittest discover -s tests/acceptance -v
- Acceptance tests from outside:
  - py -m unittest discover -s tests/acceptance-ext -v
    - For this is necessary that the service be running

