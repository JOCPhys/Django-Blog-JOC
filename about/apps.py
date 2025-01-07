from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the 'about' Django application.

    This class defines the configuration for the 'about' app, including
    the default auto field type and the application name.

    Attributes:
        default_auto_field (str): Specifies the type of auto-created primary key field.
        name (str): The name of the Django application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
