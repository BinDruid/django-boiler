# Django Boiler Template

This is a boiler template for a django project which features:

- Seperate settings for production and development environment.
- Utilizing postgreSQL database.
- Customizable user model whith customizable login form.
- Utilizing redis cache for page views.
- Displaying jalali date time.

## Initial configs

After cloning this template you shoud set some environment variables. When it's done add .env file in .gitignore file.

### Django Project Setting

Django determines development environment based on `DJANGO_SETTINGS_MODULE` variable. This variable can takes two value:

- `config.settings.development`
- `config.settings.production`

In development environment django debug toolbar is enabled.

For production environment you have to set your allowed host. Also you can set content security policy.

### Staitc Files url

This url is set to "public/". If you want to change it, you need to change this value in base.py, development.py and production.py settings.

### Database

Django setting reads postgreSQL variables from .env file. You have to set four variables:

- `DB_NAME`
- `DB_USER`
- `DB_PASS`
- `DB_HOST`
- `DB_PORT`

Django setting reads redis variables from .env file. You have to set two variables:

- `REDIS_DB_URL`
- `REDIS_PREFIX`

Default cache time to live `CACHE_TTL` is set to 15 minutes.

If you want to cache a page view use chace_page method in your urls.py.

### Running for First time

- Change django secret variable by running this command: `python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'`
- Set development environment to `config.settings.development`.
- Make migrations and migrate: `python manage.py makemigrations` `python manage.py migrate`
- Start development server: `python manage.py runserver portnumber`

### Considerations

- If you want to use jalali date time field in your database and templates, all of the setting are applied.
- `apps.common` is a bioler app with a default view to show home page.
- You can use this command to wipe your databse and migrate from initial: `python manage.py reset_db`.
- In production environment if you want to serve project as a gunicorn service, you can use `gunicorn_service` file. Edit this file based on your configs and put it in this path `/etc/systemd/system/yourproject.service`
