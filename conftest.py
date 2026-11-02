# At the repository root, so pytest puts the root on sys.path.
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "search.settings")
django.setup()
