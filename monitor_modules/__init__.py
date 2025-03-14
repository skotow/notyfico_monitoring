# monitor_modules/__init__.py

# Optionally, you can import commonly used functions or classes here
from .monitor import monitor_system
from .service_checker import monitor_services
from .notifier import send_notification

# You can also define a version or any package-level constants
__version__ = '0.1.0'