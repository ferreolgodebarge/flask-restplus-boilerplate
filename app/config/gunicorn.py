import os
import multiprocessing

# Network and connections
bind = "0.0.0.0:5000"
backlog = 2048
worker_connections = 4098
max_requests = 4098
timeout = 30
graceful_timeout = 30

# Processes
proc_name = 'flask-resplus-boilerplate'
pidfile = os.environ.get(
    "PID",
    "{}/app/pids/{}.pid".format(os.getcwd(), proc_name),
)
workers = multiprocessing.cpu_count() * 2 + 1
daemon = False
check_config = False
preload_app = True
reload = True

# Logs
loglevel = "debug"
accesslog = os.environ.get(
    "ACCESS_LOG_FILES",
    "{}/app/logs/{}-access.log".format(os.getcwd(), proc_name),
)
errorlog = os.environ.get(
    "ERROR_LOG_FILES",
    "{}/app/logs/{}-error.log".format(os.getcwd(), proc_name),
)
