# Codecamp Lab Portal

A Django-based web portal for running and testing lab exercises.

## Features

- Lab function testing framework
- Individual test cases for each problem
- Web interface for viewing results
- Automated test runner

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start development server:
```bash
python manage.py runserver
```

4. Run tests:
```bash
python manage.py test portal.tests.lab.test_runner
```

## Deployment to Render

### Quick Deploy (Recommended)

1. Fork this repository to your GitHub account
2. Connect your GitHub account to Render
3. Create a new Web Service on Render
4. Connect your forked repository
5. Render will automatically detect the `render.yaml` configuration

### Manual Deploy

1. Create a new Web Service on Render
2. Connect your repository
3. Set the following configuration:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn portal.wsgi:application`
   - **Environment Variables**:
     - `SECRET_KEY`: Generate a secure secret key
     - `DEBUG`: `false`
     - `ALLOWED_HOSTS`: `.onrender.com`

### Environment Variables

The following environment variables are supported:

- `SECRET_KEY`: Django secret key (required for production)
- `DEBUG`: Set to `false` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: PostgreSQL database URL (optional, defaults to SQLite)

## Project Structure

```
├── portal/                 # Django project
│   ├── settings.py        # Django settings
│   ├── urls.py           # URL routing
│   ├── views.py          # Views
│   ├── templates/        # HTML templates
│   ├── tests/            # Test files
│   │   └── lab/          # Lab test framework
│   └── utils/            # Utility functions
│       ├── assignment/   # Assignment solutions
│       └── lab/          # Lab solutions
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── build.sh             # Render build script
└── render.yaml          # Render configuration
```

## Testing

Run individual tests:
```bash
python manage.py test portal.tests.lab.test_runner.LabTests.test_q1_count_character_frequency
```

Run all lab tests:
```bash
python manage.py test portal.tests.lab
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure they pass
5. Submit a pull request