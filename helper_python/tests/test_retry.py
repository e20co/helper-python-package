from unittest.mock import patch
from helper.retry import retry
import logging
from unittest import TestCase
from datetime import datetime
from datetime import timedelta


class TestRetry(TestCase):

    def test_retry__works_on_first_try(self):
        retry_count = 3

        # a new function object
        def add(a, b):
            return a + b

        with self.assertLogs(level='DEBUG') as logger_context:
            logger = logging.getLogger()

            result = retry(retry_count, add, 3, 5, logger=logger)  # System Under Test
            self.assertEqual(8, result)

            self.assertEqual(logger_context.output, ['DEBUG:root:1 number of retries needed.'])

    def test_retry__never_works(self):
        retry_count = 3
        expected_message = "division by zero"

        # a new function object
        def divide(a, b):
            return a / b

        with self.assertLogs(level='INFO') as logger_context:
            logger = logging.getLogger()

            with patch('time.sleep', return_value=None) as mock:
                with self.assertRaises(ZeroDivisionError) as context_manager:
                    retry(retry_count, divide, 3, 0, logger=logger)  # System Under Test

                self.assertEqual(retry_count, mock.call_count)

            self.assertEqual(logger_context.output, ['WARNING:root:division by zero',
                                                     'WARNING:root:division by zero',
                                                     'WARNING:root:division by zero',
                                                     'ERROR:root:All retries failed.'])

        exception = context_manager.exception
        self.assertEqual(expected_message, str(exception))

    def test_retry__starts_working_after_some_retries(self):
        retry_count = 3
        wait_for_seconds = 0.01  # milliseconds

        # a new function object
        def works_after_date_time(past_date_time):
            after = False
            present_date_time = datetime.now()
            delta = timedelta(milliseconds=12)
            past_date_time = past_date_time + delta

            if past_date_time < present_date_time:
                after = True
            else:
                raise Exception("past time plus delta newer than current datetime.")

            return after

        past_date_time = datetime.now()
        result = retry(retry_count, works_after_date_time, past_date_time, wait=wait_for_seconds)  # System Under Test
        self.assertTrue(result)

    def test_retry__function_without_arguments(self):
        retry_count = 3

        # a new function object
        def always_true():
            return True

        with self.assertLogs(level='DEBUG') as logger_context:
            logger_name = 'test.logger'
            logger_message = 'DEBUG:{}:1 number of retries needed.'.format(logger_name)
            with patch('time.sleep', return_value=None) as mock:

                logger = logging.getLogger(logger_name)

                result = retry(retry_count, always_true, logger=logger)  # System Under Test
                self.assertTrue(result)

                self.assertEqual(1, mock.call_count)

            self.assertEqual(logger_context.output, [logger_message])
