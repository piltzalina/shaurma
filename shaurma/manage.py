# main.py
import os
from shaurma.wsgi import application
from django.core.wsgi import get_wsgi_application

# gunicorn не нужен, если платформа запускает python main.py — тогда так:
if __name__ == "__main__":
    import django
    from django.conf import settings

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shaurma.settings")
    django.setup()

    port = int(os.environ.get("PORT", 8000))
    from gunicorn.app.base import BaseApplication

    class StandaloneApp(BaseApplication):
        def load_config(self):
            self.options = {
                "bind": f"0.0.0.0:{port}",
                "workers": 2,
            }
        def load(self):
            return application

    StandaloneApp().run()
