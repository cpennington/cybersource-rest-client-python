# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TokenizeResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key_id': 'str',
        'token': 'str',
        'masked_pan': 'str',
        'card_type': 'str',
        'timestamp': 'int',
        'signed_fields': 'str',
        'signature': 'str',
        'discoverable_services': 'dict(str, object)'
    }

    attribute_map = {
        'key_id': 'keyId',
        'token': 'token',
        'masked_pan': 'maskedPan',
        'card_type': 'cardType',
        'timestamp': 'timestamp',
        'signed_fields': 'signedFields',
        'signature': 'signature',
        'discoverable_services': 'discoverableServices'
    }

    def __init__(self, key_id=None, token=None, masked_pan=None, card_type=None, timestamp=None, signed_fields=None, signature=None, discoverable_services=None):
        """
        TokenizeResult - a model defined in Swagger
        """

        self._key_id = None
        self._token = None
        self._masked_pan = None
        self._card_type = None
        self._timestamp = None
        self._signed_fields = None
        self._signature = None
        self._discoverable_services = None

        if key_id is not None:
          self.key_id = key_id
        if token is not None:
          self.token = token
        if masked_pan is not None:
          self.masked_pan = masked_pan
        if card_type is not None:
          self.card_type = card_type
        if timestamp is not None:
          self.timestamp = timestamp
        if signed_fields is not None:
          self.signed_fields = signed_fields
        if signature is not None:
          self.signature = signature
        if discoverable_services is not None:
          self.discoverable_services = discoverable_services

    @property
    def key_id(self):
        """
        Gets the key_id of this TokenizeResult.
        The Key ID.

        :return: The key_id of this TokenizeResult.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this TokenizeResult.
        The Key ID.

        :param key_id: The key_id of this TokenizeResult.
        :type: str
        """

        self._key_id = key_id

    @property
    def token(self):
        """
        Gets the token of this TokenizeResult.
        The generated token. The token replaces card data and is used as the Subscription ID in the CyberSource Simple Order API or SCMP API.

        :return: The token of this TokenizeResult.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this TokenizeResult.
        The generated token. The token replaces card data and is used as the Subscription ID in the CyberSource Simple Order API or SCMP API.

        :param token: The token of this TokenizeResult.
        :type: str
        """

        self._token = token

    @property
    def masked_pan(self):
        """
        Gets the masked_pan of this TokenizeResult.
        The masked card number displaying the first 6 digits and the last 4 digits.

        :return: The masked_pan of this TokenizeResult.
        :rtype: str
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """
        Sets the masked_pan of this TokenizeResult.
        The masked card number displaying the first 6 digits and the last 4 digits.

        :param masked_pan: The masked_pan of this TokenizeResult.
        :type: str
        """

        self._masked_pan = masked_pan

    @property
    def card_type(self):
        """
        Gets the card_type of this TokenizeResult.
        The card type.

        :return: The card_type of this TokenizeResult.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this TokenizeResult.
        The card type.

        :param card_type: The card_type of this TokenizeResult.
        :type: str
        """

        self._card_type = card_type

    @property
    def timestamp(self):
        """
        Gets the timestamp of this TokenizeResult.
        The UTC date and time in milliseconds at which the signature was generated.

        :return: The timestamp of this TokenizeResult.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this TokenizeResult.
        The UTC date and time in milliseconds at which the signature was generated.

        :param timestamp: The timestamp of this TokenizeResult.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def signed_fields(self):
        """
        Gets the signed_fields of this TokenizeResult.
        Indicates which fields from the response make up the data that is used when verifying the response signature. See the [sample code] (https://github.com/CyberSource/cybersource-flex-samples/blob/master/java/spring-boot/src/main/java/com/cybersource/flex/application/CheckoutController.java) on how to verify the signature.

        :return: The signed_fields of this TokenizeResult.
        :rtype: str
        """
        return self._signed_fields

    @signed_fields.setter
    def signed_fields(self, signed_fields):
        """
        Sets the signed_fields of this TokenizeResult.
        Indicates which fields from the response make up the data that is used when verifying the response signature. See the [sample code] (https://github.com/CyberSource/cybersource-flex-samples/blob/master/java/spring-boot/src/main/java/com/cybersource/flex/application/CheckoutController.java) on how to verify the signature.

        :param signed_fields: The signed_fields of this TokenizeResult.
        :type: str
        """

        self._signed_fields = signed_fields

    @property
    def signature(self):
        """
        Gets the signature of this TokenizeResult.
        Flex-generated digital signature. To ensure the values have not been tampered with while passing through the client, verify this server-side using the public key generated from the /keys resource.

        :return: The signature of this TokenizeResult.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this TokenizeResult.
        Flex-generated digital signature. To ensure the values have not been tampered with while passing through the client, verify this server-side using the public key generated from the /keys resource.

        :param signature: The signature of this TokenizeResult.
        :type: str
        """

        self._signature = signature

    @property
    def discoverable_services(self):
        """
        Gets the discoverable_services of this TokenizeResult.

        :return: The discoverable_services of this TokenizeResult.
        :rtype: dict(str, object)
        """
        return self._discoverable_services

    @discoverable_services.setter
    def discoverable_services(self, discoverable_services):
        """
        Sets the discoverable_services of this TokenizeResult.

        :param discoverable_services: The discoverable_services of this TokenizeResult.
        :type: dict(str, object)
        """

        self._discoverable_services = discoverable_services

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TokenizeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
