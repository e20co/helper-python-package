from unittest import TestCase
from helper.aws.aws_secret import AWSSecret
from helper.aws.aws_region import AWSRegion


class TestAWSSecret(TestCase):

    def test_constructor__valid(self):
        aws_access_key_id = "OIUHJBKNKLKSID"
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = AWSRegion.US_EAST_1

        aws_secret = AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        self.assertEqual(aws_access_key_id, aws_secret.access_key_id)
        self.assertEqual(aws_secret_access_key, aws_secret.secret_access_key)
        self.assertEqual(aws_region, aws_secret.region)

    def test_aws_access_key_id__none(self):
        expected_exception_message = "AWS Access Key ID cannot be `None`."

        aws_access_key_id = None
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = AWSRegion.US_EAST_1

        with self.assertRaises(ValueError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_access_key_id__wrong_type(self):
        expected_exception_message = "AWS Access Key ID has to be an instance of <class 'str'> or a subclass of it and not <class 'int'>."

        aws_access_key_id = 45
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = AWSRegion.US_EAST_1

        with self.assertRaises(TypeError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_access_key_id__empty_string(self):
        expected_exception_message = "AWS Access Key ID cannot be empty."

        aws_access_key_id = ""
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = AWSRegion.US_EAST_1

        with self.assertRaises(ValueError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_secret_access_key__none(self):
        expected_exception_message = "AWS Secret Access Key cannot be `None`."

        aws_access_key_id = "AWEFDSERD"
        aws_secret_access_key = None
        aws_region = AWSRegion.US_EAST_1

        with self.assertRaises(ValueError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_secret_access_key__wrong_type(self):
        expected_exception_message = "AWS Secret Access Key has to be an instance of <class 'str'> or a subclass of it and not <class 'int'>."

        aws_access_key_id = "AWEFDSERD"
        aws_secret_access_key = 45
        aws_region = AWSRegion.US_EAST_1

        with self.assertRaises(TypeError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_secret_access_key__empty_string(self):
        expected_exception_message = "AWS Secret Access Key cannot be empty."

        aws_access_key_id = "AWEFDSERD"
        aws_secret_access_key = ""
        aws_region = AWSRegion.US_EAST_1

        with self.assertRaises(ValueError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_region__none(self):
        expected_exception_message = "AWS Region cannot be `None`."

        aws_access_key_id = "AWEFDSERD"
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = None

        with self.assertRaises(ValueError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_aws_region__wrong_type(self):
        expected_exception_message = "AWS Region has to be an instance of <enum 'AWSRegion'> or a subclass of it and not <class 'str'>."

        aws_access_key_id = "AWEFDSERD"
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = "45"

        with self.assertRaises(TypeError) as context_manager:
            AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)  # System Under Test

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_compare__different_equal_instances(self):
        aws_access_key_id = "OIUHJBKNKLKSID"
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = AWSRegion.US_EAST_1

        aws_secret_1 = AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)
        aws_secret_2 = AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)

        self.assertTrue(aws_secret_1 == aws_secret_2)  # System Under Test
        self.assertEqual(aws_secret_1, aws_secret_2)  # System Under Test
        self.assertFalse(aws_secret_1 is aws_secret_2)  # System Under Test
        self.assertNotEqual(id(aws_secret_1), id(aws_secret_2))  # System Under Test

    def test_compare__same_instance(self):
        aws_access_key_id = "OIUHJBKNKLKSID"
        aws_secret_access_key = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region = AWSRegion.US_EAST_1

        aws_secret = AWSSecret(aws_access_key_id, aws_secret_access_key, aws_region)

        self.assertTrue(aws_secret == aws_secret)  # System Under Test
        self.assertEqual(aws_secret, aws_secret)  # System Under Test
        self.assertTrue(aws_secret is aws_secret)  # System Under Test
        self.assertEqual(id(aws_secret), id(aws_secret))  # System Under Test

    def test_compare__different_unequal_instances(self):
        aws_access_key_id_1 = "OIUHJBKNKLKSID"
        aws_secret_access_key_1 = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region_1 = AWSRegion.US_EAST_1

        aws_access_key_id_2 = "POUIGJHBNLK"
        aws_secret_access_key_2 = "uiH09*&Yuihjkj*97hjnm"
        aws_region_2 = AWSRegion.US_WEST_1

        aws_secret_1 = AWSSecret(aws_access_key_id_1, aws_secret_access_key_1, aws_region_1)
        aws_secret_2 = AWSSecret(aws_access_key_id_2, aws_secret_access_key_2, aws_region_2)

        self.assertTrue(aws_secret_1 != aws_secret_2)  # System Under Test
        self.assertNotEqual(aws_secret_1, aws_secret_2)  # System Under Test
        self.assertTrue(aws_secret_1 is not aws_secret_2)  # System Under Test
        self.assertNotEqual(id(aws_secret_1), id(aws_secret_2))  # System Under Test

    def test_repr(self):
        aws_access_key_id_1 = "OIUHJBKNKLKSID"
        aws_secret_access_key_1 = "K*(Ihuu9(*UJnp*&^%$))"
        aws_region_1 = AWSRegion.US_EAST_1

        aws_secret_1 = AWSSecret(aws_access_key_id_1, aws_secret_access_key_1, aws_region_1)

        string_representation = repr(aws_secret_1)  # System Under Test
        aws_secret_2 = eval(string_representation)

        self.assertEqual(aws_secret_1, aws_secret_2)
        self.assertEqual(aws_secret_1.access_key_id, aws_secret_2.access_key_id)
        self.assertEqual(aws_secret_1.secret_access_key, aws_secret_2.secret_access_key)
        self.assertEqual(aws_secret_1.region, aws_secret_2.region)
