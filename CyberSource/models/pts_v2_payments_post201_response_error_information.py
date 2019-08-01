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


class PtsV2PaymentsPost201ResponseErrorInformation(object):
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
        'reason': 'str',
        'message': 'str',
        'details': 'list[PtsV2PaymentsPost201ResponseErrorInformationDetails]'
    }

    attribute_map = {
        'reason': 'reason',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, reason=None, message=None, details=None):
        """
        PtsV2PaymentsPost201ResponseErrorInformation - a model defined in Swagger
        """

        self._reason = None
        self._message = None
        self._details = None

        if reason is not None:
          self.reason = reason
        if message is not None:
          self.message = message
        if details is not None:
          self.details = details

    @property
    def reason(self):
        """
        Gets the reason of this PtsV2PaymentsPost201ResponseErrorInformation.
        The reason of the status.  Possible values:  - AVS_FAILED  - CONTACT_PROCESSOR  - EXPIRED_CARD  - PROCESSOR_DECLINED  - INSUFFICIENT_FUND  - STOLEN_LOST_CARD  - ISSUER_UNAVAILABLE  - UNAUTHORIZED_CARD  - CVN_NOT_MATCH  - EXCEEDS_CREDIT_LIMIT  - INVALID_CVN  - DECLINED_CHECK  - BLACKLISTED_CUSTOMER  - SUSPENDED_ACCOUNT  - PAYMENT_REFUSED  - CV_FAILED  - INVALID_ACCOUNT  - GENERAL_DECLINE  - INVALID_MERCHANT_CONFIGURATION  - DECISION_PROFILE_REJECT  - SCORE_EXCEEDS_THRESHOLD  - PENDING_AUTHENTICATION 

        :return: The reason of this PtsV2PaymentsPost201ResponseErrorInformation.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this PtsV2PaymentsPost201ResponseErrorInformation.
        The reason of the status.  Possible values:  - AVS_FAILED  - CONTACT_PROCESSOR  - EXPIRED_CARD  - PROCESSOR_DECLINED  - INSUFFICIENT_FUND  - STOLEN_LOST_CARD  - ISSUER_UNAVAILABLE  - UNAUTHORIZED_CARD  - CVN_NOT_MATCH  - EXCEEDS_CREDIT_LIMIT  - INVALID_CVN  - DECLINED_CHECK  - BLACKLISTED_CUSTOMER  - SUSPENDED_ACCOUNT  - PAYMENT_REFUSED  - CV_FAILED  - INVALID_ACCOUNT  - GENERAL_DECLINE  - INVALID_MERCHANT_CONFIGURATION  - DECISION_PROFILE_REJECT  - SCORE_EXCEEDS_THRESHOLD  - PENDING_AUTHENTICATION 

        :param reason: The reason of this PtsV2PaymentsPost201ResponseErrorInformation.
        :type: str
        """

        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this PtsV2PaymentsPost201ResponseErrorInformation.
        The detail message related to the status and reason listed above.

        :return: The message of this PtsV2PaymentsPost201ResponseErrorInformation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this PtsV2PaymentsPost201ResponseErrorInformation.
        The detail message related to the status and reason listed above.

        :param message: The message of this PtsV2PaymentsPost201ResponseErrorInformation.
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """
        Gets the details of this PtsV2PaymentsPost201ResponseErrorInformation.

        :return: The details of this PtsV2PaymentsPost201ResponseErrorInformation.
        :rtype: list[PtsV2PaymentsPost201ResponseErrorInformationDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this PtsV2PaymentsPost201ResponseErrorInformation.

        :param details: The details of this PtsV2PaymentsPost201ResponseErrorInformation.
        :type: list[PtsV2PaymentsPost201ResponseErrorInformationDetails]
        """

        self._details = details

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseErrorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
