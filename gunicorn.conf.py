

### FOR PROD
# bind = 'unix:/tmp/socket_django.sock'

### FOR DEV
bind = '127.0.0.1:8000'

backlog = 2048

workers = 2
worker_class = 'gthread'
threads = 2

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

