# Python logging basic setting

```python
# logger.py

import logging

def _logger_init():
    logger = logging.getLogger('module')
    # do not pass log to the handlers of ancestor loggers
    # https://docs.python.org/3/library/logging.html#logging.Logger.propagate
    logger.propagate = False
    logger.setLevel(logging.INFO)
    stream_hanlder = logging.StreamHandler()
    fmt = "%(name)s - %(created)d %(levelname)s %(filename)s:%(lineno)d %(message)s"
    stream_format = logging.Formatter(fmt)
    stream_hanlder.setFormatter(stream_format)
    logger.addHandler(stream_hanlder)
    return logger

logger = _logger_init()

```

## Use in `xxx.py`

```python
# xxx.py

from /module_path/logger import logger

logger.info(f"print a info log")

```

## Reference

https://www.reddit.com/r/learnpython/comments/7fbgj2/logging_is_it_typical_to_set_loggerpropagatefalse/
