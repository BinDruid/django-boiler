from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["yourhost.com"]

MIDDLEWARE.insert(0, "csp.middleware.CSPMiddleware")

# Content Security Policy

CSP_DEFAULT_SRC = ("'none'",)

CSP_IMG_SRC = "'self'"

CSP_STYLE_SRC = ("'self'", "*.jsdelivr.net", "fonts.googleapis.com", "'unsafe-inline'")

CSP_SCRIPT_SRC = (
    "'self'",
    "*.fontawesome.com",
    "*.jsdelivr.net",
    "*.jquery.com",
    "*.googletagmanager.com",
)

CSP_FONT_SRC = ("'self'", "*.jsdelivr.net", "fonts.gstatic.com", "*.fontawesome.com")

CSP_CONNECT_SRC = ("'self'", "*.fontawesome.com")

CSP_INCLUDE_NONCE_IN = ["script-src"]

# Cross site protection

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Force SSL => Done by NGINX
# SECURE_SSL_REDIRECT = True

# HSTS => Done by NGINX
# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

STATIC_ROOT = os.path.join(BASE_DIR, "public/")
