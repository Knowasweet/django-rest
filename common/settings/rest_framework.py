REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKEND': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'EXCEPTION_HANDLER': 'utils.exceptionhandler.custom_exception_handler',
}

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {"Token": {"type": "apiKey", "name": "Authorization", "in": "header"}},
    "LOGIN_URL": "admin:login",
    "LOGOUT_URL": "admin:logout",
}