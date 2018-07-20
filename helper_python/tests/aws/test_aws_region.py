from unittest import TestCase
from helper.aws.aws_region import AWSRegion


class TestAWSSecret(TestCase):

    def test_us_east_1(self):
        region_name_value = "us-east-1"
        region_name_name = "US_EAST_1"

        self.assertEqual(AWSRegion.US_EAST_1, AWSRegion.US_EAST_1)
        self.assertEqual(region_name_name, AWSRegion.US_EAST_1.name)
        self.assertEqual(region_name_value, AWSRegion.US_EAST_1.value)
        self.assertEqual(region_name_value, str(AWSRegion.US_EAST_1))
        self.assertEqual(AWSRegion.US_EAST_1, AWSRegion(region_name_value))

    def test_us_east_2(self):
        region_name_value = "us-east-2"
        region_name_name = "US_EAST_2"

        self.assertEqual(AWSRegion.US_EAST_2, AWSRegion.US_EAST_2)
        self.assertEqual(region_name_name, AWSRegion.US_EAST_2.name)
        self.assertEqual(region_name_value, AWSRegion.US_EAST_2.value)
        self.assertEqual(region_name_value, str(AWSRegion.US_EAST_2))
        self.assertEqual(AWSRegion.US_EAST_2, AWSRegion(region_name_value))

    def test_us_west_1(self):
        region_name_value = "us-west-1"
        region_name_name = "US_WEST_1"

        self.assertEqual(AWSRegion.US_WEST_1, AWSRegion.US_WEST_1)
        self.assertEqual(region_name_name, AWSRegion.US_WEST_1.name)
        self.assertEqual(region_name_value, AWSRegion.US_WEST_1.value)
        self.assertEqual(region_name_value, str(AWSRegion.US_WEST_1))
        self.assertEqual(AWSRegion.US_WEST_1, AWSRegion(region_name_value))

    def test_us_west_2(self):
        region_name_value = "us-west-2"
        region_name_name = "US_WEST_2"

        self.assertEqual(AWSRegion.US_WEST_2, AWSRegion.US_WEST_2)
        self.assertEqual(region_name_name, AWSRegion.US_WEST_2.name)
        self.assertEqual(region_name_value, AWSRegion.US_WEST_2.value)
        self.assertEqual(region_name_value, str(AWSRegion.US_WEST_2))
        self.assertEqual(AWSRegion.US_WEST_2, AWSRegion(region_name_value))

    def test_gov_cloud(self):
        region_name_value = "us-gov-west-1"
        region_name_name = "GovCloud"

        self.assertEqual(AWSRegion.GovCloud, AWSRegion.GovCloud)
        self.assertEqual(region_name_name, AWSRegion.GovCloud.name)
        self.assertEqual(region_name_value, AWSRegion.GovCloud.value)
        self.assertEqual(region_name_value, str(AWSRegion.GovCloud))
        self.assertEqual(AWSRegion.GovCloud, AWSRegion(region_name_value))

    def test_ca_central_1(self):
        region_name_value = "ca-central-1"
        region_name_name = "CA_CENTRAL_1"

        self.assertEqual(AWSRegion.CA_CENTRAL_1, AWSRegion.CA_CENTRAL_1)
        self.assertEqual(region_name_name, AWSRegion.CA_CENTRAL_1.name)
        self.assertEqual(region_name_value, AWSRegion.CA_CENTRAL_1.value)
        self.assertEqual(region_name_value, str(AWSRegion.CA_CENTRAL_1))
        self.assertEqual(AWSRegion.CA_CENTRAL_1, AWSRegion(region_name_value))

    def test_eu_central_1(self):
        region_name_value = "eu-central-1"
        region_name_name = "EU_CENTRAL_1"

        self.assertEqual(AWSRegion.EU_CENTRAL_1, AWSRegion.EU_CENTRAL_1)
        self.assertEqual(region_name_name, AWSRegion.EU_CENTRAL_1.name)
        self.assertEqual(region_name_value, AWSRegion.EU_CENTRAL_1.value)
        self.assertEqual(region_name_value, str(AWSRegion.EU_CENTRAL_1))
        self.assertEqual(AWSRegion.EU_CENTRAL_1, AWSRegion(region_name_value))

    def test_eu_west_1(self):
        region_name_value = "eu-west-1"
        region_name_name = "EU_WEST_1"

        self.assertEqual(AWSRegion.EU_WEST_1, AWSRegion.EU_WEST_1)
        self.assertEqual(region_name_name, AWSRegion.EU_WEST_1.name)
        self.assertEqual(region_name_value, AWSRegion.EU_WEST_1.value)
        self.assertEqual(region_name_value, str(AWSRegion.EU_WEST_1))
        self.assertEqual(AWSRegion.EU_WEST_1, AWSRegion(region_name_value))

    def test_eu_west_2(self):
        region_name_value = "eu-west-2"
        region_name_name = "EU_WEST_2"

        self.assertEqual(AWSRegion.EU_WEST_2, AWSRegion.EU_WEST_2)
        self.assertEqual(region_name_name, AWSRegion.EU_WEST_2.name)
        self.assertEqual(region_name_value, AWSRegion.EU_WEST_2.value)
        self.assertEqual(region_name_value, str(AWSRegion.EU_WEST_2))
        self.assertEqual(AWSRegion.EU_WEST_2, AWSRegion(region_name_value))

    def test_eu_west_3(self):
        region_name_value = "eu-west-3"
        region_name_name = "EU_WEST_3"

        self.assertEqual(AWSRegion.EU_WEST_3, AWSRegion.EU_WEST_3)
        self.assertEqual(region_name_name, AWSRegion.EU_WEST_3.name)
        self.assertEqual(region_name_value, AWSRegion.EU_WEST_3.value)
        self.assertEqual(region_name_value, str(AWSRegion.EU_WEST_3))
        self.assertEqual(AWSRegion.EU_WEST_3, AWSRegion(region_name_value))

    def test_sa_east_1(self):
        region_name_value = "sa-east-1"
        region_name_name = "SA_EAST_1"

        self.assertEqual(AWSRegion.SA_EAST_1, AWSRegion.SA_EAST_1)
        self.assertEqual(region_name_name, AWSRegion.SA_EAST_1.name)
        self.assertEqual(region_name_value, AWSRegion.SA_EAST_1.value)
        self.assertEqual(region_name_value, str(AWSRegion.SA_EAST_1))
        self.assertEqual(AWSRegion.SA_EAST_1, AWSRegion(region_name_value))

    def test_repr(self):
        aws_region_1 = AWSRegion.US_EAST_1

        string_representation = repr(aws_region_1)  # System Under Test
        aws_region_2 = eval(string_representation)

        self.assertEqual(aws_region_1, aws_region_2)
