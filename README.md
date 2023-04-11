how to install this project

1. Create a virtual environment using a command like this (replace "env" with the name you want to give your environment):

virtualenv venv

2. Activate virtualenv

cd venv/scripts/activate

3. clone this project

git clone https://github.com/adil-shabab/sample-login-times-world-.git

4. Change directory 

cd project

5. install required modules

pip install -r requirements.txt

6. Migrate database

python manage.py makemigrations
python manage.py migrate

7. Run on localhost

python manage.py runserver



# sample-login-times-world-
