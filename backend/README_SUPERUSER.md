# Superuser Creation Script

This script creates a default superuser for development purposes.

## Security Notice

Credentials are **NOT** hardcoded in the script. They are loaded from environment variables defined in your `.env.dev` file.

## Configuration

Add the following variables to your `.env.dev` file:

```env
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@comercio.local
DJANGO_SUPERUSER_PASSWORD=your_secure_password_here
```

## Usage

### In Docker:

```bash
docker exec comercio_backend_dev python create_superuser.py
```

### Locally:

```bash
# Make sure your .env file is configured
python create_superuser.py
```

## Default Values

- **Username:** From `DJANGO_SUPERUSER_USERNAME` env var (default: "admin")
- **Email:** From `DJANGO_SUPERUSER_EMAIL` env var (default: "admin@example.com")
- **Password:** From `DJANGO_SUPERUSER_PASSWORD` env var (REQUIRED - no default)

## Important

- The script will NOT create a duplicate user if one already exists
- Password must be set in environment variable (script will exit with error if not set)
- These credentials should ONLY be used in development
- Never commit `.env.dev` or `.env` files to version control

