import logging
import os
import sys
import uuid
from logging.handlers import TimedRotatingFileHandler
from contextvars import ContextVar

# Store session ID for current executionthread
request_id_ctx_var : ContextVar[str] = ContextVar("request_id", default="n/a")

class ContextualFilter(logging.Filter):
    def filter(self, record):
        # Add session id to every log record
        record.request_id = request_id_ctx_var.get()
        return True

def setup_logging():

    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, 'app.log')

    # Handler: Rotate logs every day, keep 7 days of logs
    handler = TimedRotatingFileHandler(
        log_file, 
        when='midnight', 
        interval=1, 
        backupCount=7,
        encoding = "utf-8"
        )

    # Format: Include timestamp, logger name, log level, session id, and message
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(request_id)s | %(message)s")

    #file handler append mode
    handler.setFormatter(formatter)
    handler.addFilter(ContextualFilter())

    # Configuring root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)

    # Also log to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(ContextualFilter())
    root_logger.addHandler(console_handler)