from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


from django.apps import AppConfig

class relationship_appConfig(AppConfig):
    name = 'relationship_app'
    def ready(self):
        import relationship_app.signals