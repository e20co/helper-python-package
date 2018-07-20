from helper.aws.aws_region import AWSRegion
from helper.type_checking import check_value
from helper.type_checking import check_string


class AWSSecret:
    """ AWSSecret represents an AWS Secret.

    An AWS Secret consists of an AWS Access Key ID, an AWS Secret Access Key and
    the AWS Region name. The class creates immutable objects.
    """

    def __init__(
        self,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        aws_region: AWSRegion
    ) -> None:
        """
        The constructor for the AWS Secret class.

        Args:
            value (str): The value to check.
            value_name (str): The value name, this is used to improve the
                              readability of the exceptions messages.

        Returns:
            bool: True if the value passes the checks.

        Raises:
            ValueError: If the given `value` is `None` or an empty string.
            TypeError: If given `value` is not an instance of string.
        """

        check_string(aws_access_key_id, "AWS Access Key ID")
        check_string(aws_secret_access_key, "AWS Secret Access Key")
        check_value(aws_region, "AWS Region", AWSRegion)

        self.__access_key_id = aws_access_key_id
        self.__secret_access_key = aws_secret_access_key
        self.__region = aws_region

    def __eq__(self, other: object) -> bool:
        same = False

        if isinstance(other, AWSSecret):
            same = ((self.__access_key_id == other.__access_key_id)
                    and (self.__secret_access_key == other.__secret_access_key)
                    and (self.__region == other.__region))

        return same

    def __repr__(self) -> str:
        representation = "{}('{}', '{}', eval(\"{}\"))".format(
            self.__class__.__name__,
            self.__access_key_id,
            self.__secret_access_key,
            repr(self.__region))

        return representation

    @property
    def access_key_id(self) -> str:
        return self.__access_key_id

    @property
    def secret_access_key(self) -> str:
        return self.__secret_access_key

    @property
    def region(self) -> AWSRegion:
        return self.__region
