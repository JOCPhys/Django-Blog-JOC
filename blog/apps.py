from django.apps import AppConfig

"""Configuration for the 'blog' application.

    This class defines the app configuration for the 'blog' Django app.
    It specifies the default auto field for model primary keys and
    sets the application name.

    Attributes:
        default_auto_field (str): The default auto field type for models.
        name (str): The name of the application.
    """

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
