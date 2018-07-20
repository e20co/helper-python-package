from enum import Enum, unique


@unique
class AWSRegion(Enum):
    """ This Enum contains the values for the AWS Regions.
    """

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        representation = "{}('{}')".format(
            self.__class__.__name__,
            self.value)

        return representation

    # US N. Virginia
    US_EAST_1 = "us-east-1"

    # US Ohio
    US_EAST_2 = "us-east-2"

    # US N. California
    US_WEST_1 = "us-west-1"

    # US Oregon
    US_WEST_2 = "us-west-2"

    # AWS GovCloud (US)
    GovCloud = "us-gov-west-1"

    # Canada (Central) Montreal
    CA_CENTRAL_1 = "ca-central-1"

    # EU (Frankfurt)
    EU_CENTRAL_1 = "eu-central-1"

    # EU (Ireland)
    EU_WEST_1 = "eu-west-1"

    # EU (London)
    EU_WEST_2 = "eu-west-2"

    # EU (Paris)
    EU_WEST_3 = "eu-west-3"

    # South America (São Paulo)
    SA_EAST_1 = "sa-east-1"
