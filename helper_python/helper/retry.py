from typing import Any
from typing import Callable
from typing import Tuple
from typing import Union
from logging import LoggerAdapter
from logging import Logger
import time
import logging


def retry(
    retry_count: int,
    function: Callable,
    *args: Tuple[Any],
    logger: Union[Logger, LoggerAdapter] = None,
    wait: float = 0.1
) -> Union[Any, None]:
    """ This function retries a given function for N times. If an exception
    occurs after N times, the function stops and throws the exception.
    This function is indendet to be used as an generic retry mechanism.

    Args:
        retry_count (int): The number of times to retry
        function (Callable): The function which should be retried
        *args (Tuple[Any]): The arguments with which the given function should
                           be called with.
        logger (Logger): Logging object.
        wait (float): Waiting time in between tries.

    Returns:
        Any: Any argument or None. Basically whatever the given function
             would return normally.

    Raises:
        Exception: If the retry is not successful throw the last caught exception.
    """
    retries = 0
    result = None
    stop = False
    exception = None

    while retries < retry_count and not stop:
        retries = retries + 1

        try:
            result = function(*args)
            stop = True  # stop is not True if an exception is thrown

            if logger is not None:
                logger.debug("{} number of retries needed.".format(retries))

        except Exception as ex:
            exception = ex
            if logger is not None:
                logger.warning(str(exception))

        time.sleep(wait)

    if not stop and exception is not None:
        if logger is not None:
            message = "All retries failed."
            logger.error(message)

        raise exception

    return result
