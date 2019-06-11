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


class Ptsv2payoutsClientReferenceInformation(object):
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
        'code': 'str'
    }

    attribute_map = {
        'code': 'code'
    }

    def __init__(self, code=None):
        """
        Ptsv2payoutsClientReferenceInformation - a model defined in Swagger
        """

        self._code = None

        if code is not None:
          self.code = code

    @property
    def code(self):
        """
        Gets the code of this Ptsv2payoutsClientReferenceInformation.
        Client-generated order reference or tracking number. CyberSource recommends that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  For information about tracking orders, see \"Tracking and Reconciling Your Orders\" in [Getting Started with CyberSource Advanced for the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Getting_Started_SCMP/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports. 

        :return: The code of this Ptsv2payoutsClientReferenceInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ptsv2payoutsClientReferenceInformation.
        Client-generated order reference or tracking number. CyberSource recommends that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  For information about tracking orders, see \"Tracking and Reconciling Your Orders\" in [Getting Started with CyberSource Advanced for the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Getting_Started_SCMP/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports. 

        :param code: The code of this Ptsv2payoutsClientReferenceInformation.
        :type: str
        """
        if code is not None and len(code) > 50:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `50`")

        self._code = code

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
        if not isinstance(other, Ptsv2payoutsClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
