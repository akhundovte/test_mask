from os.path import join
from os import environ


from shared.settings.config import LOGS_DIR

# The socket to bind.
bind = f'0.0.0.0:{environ.get("PORT")}'

# The number of worker processes for handling requests.
workers = 4

# The type of workers to use.
worker_class = 'gevent'

# Load application code before the worker processes are forked.
preload_app = False

# The granularity of log output
loglevel = 'info'

# The Access log file to write to.
accesslog = join(LOGS_DIR, 'gunicorn_access.log')

# The Error log file to write to.
errorlog = join(LOGS_DIR, 'gunicorn.log')

# Redirect stdout/stderr to Error log.
capture_output = True
