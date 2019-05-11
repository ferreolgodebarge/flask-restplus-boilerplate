import os
import sys
import multiprocessing

# Network and connections
bind = "0.0.0.0:5000"
backlog = 2048
worker_connections = 4098
max_requests = 4098
timeout = 30
graceful_timeout = 30

# Processes
proc_name = 'gunicorn'
pidfile = "{}/app/pids/{}.pid".format(os.getcwd(), proc_name)
workers = multiprocessing.cpu_count() * 2 + 1
daemon = True
check_config = False
preload_app = False
reload = False

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


# Handle Zero Downtime Deployment with one master
def zdd(server):
    app_root = os.environ.get("GUNICORN_APP_ROOT")
    server.log.info("[pre_exec] Starting hook, app_root = {}".format(app_root))
    if app_root:
        origin_cwd = server.START_CTX['cwd']
        os.chdir(app_root)
        server.log.info(
            "[pre_exec] Switching cwd: {} -> {}".format(origin_cwd, app_root))
        origin_path = os.path.dirname(sys.executable)
        new_path = os.path.join(app_root, 'env', 'bin')
        server.START_CTX[0] = server.START_CTX[0].replace(
            origin_path, new_path)
        server.START_CTX['args'] = [arg.replace(
            origin_path, new_path) for arg in server.START_CTX['args']]
    server.log.info("[pre_exec] Done running hook, START_CTX = {}".format(
        server.START_CTX))


pre_exec = zdd
