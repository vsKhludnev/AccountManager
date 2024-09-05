from loguru import logger
import sys

logger = logger.bind(module='main')
logger.remove()

format_logs = '{time:HH:MM:SS} || {level} || {module}:{function}:{line} || {message}'
level_logs = 'TRACE'
logger.add(sys.stderr, format=format_logs, level=level_logs)