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


class Riskv1decisionsTravelInformationLegs(object):
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
        'origination': 'str',
        'destination': 'str',
        'departure_date_time': 'str'
    }

    attribute_map = {
        'origination': 'origination',
        'destination': 'destination',
        'departure_date_time': 'departureDateTime'
    }

    def __init__(self, origination=None, destination=None, departure_date_time=None):
        """
        Riskv1decisionsTravelInformationLegs - a model defined in Swagger
        """

        self._origination = None
        self._destination = None
        self._departure_date_time = None

        if origination is not None:
          self.origination = origination
        if destination is not None:
          self.destination = destination
        if departure_date_time is not None:
          self.departure_date_time = departure_date_time

    @property
    def origination(self):
        """
        Gets the origination of this Riskv1decisionsTravelInformationLegs.
        Use to specify the airport code for the origin of the leg of the trip, which is designated by the pound (#) symbol in the field name. This code is usually three digits long, for example: SFO = San Francisco. Do not use the colon (:) or the dash (-). For airport codes, see the IATA Airline and Airport Code Search. The leg number can be a positive integer from 0 to N. For example: `travelInformation.legs.0.origination=SFO` `travelInformation.legs.1.origination=SFO`  **Note** In your request, send either the complete route or the individual legs (`legs.0.origination` and `legs.n.destination`). If you send all the fields, the complete route takes precedence over the individual legs.  For details, see the `decision_manager_travel_leg#_orig` field description in [Decision Manager Using the SCMP API Developer Guide.](https://www.cybersource.com/developers/documentation/fraud_management/) 

        :return: The origination of this Riskv1decisionsTravelInformationLegs.
        :rtype: str
        """
        return self._origination

    @origination.setter
    def origination(self, origination):
        """
        Sets the origination of this Riskv1decisionsTravelInformationLegs.
        Use to specify the airport code for the origin of the leg of the trip, which is designated by the pound (#) symbol in the field name. This code is usually three digits long, for example: SFO = San Francisco. Do not use the colon (:) or the dash (-). For airport codes, see the IATA Airline and Airport Code Search. The leg number can be a positive integer from 0 to N. For example: `travelInformation.legs.0.origination=SFO` `travelInformation.legs.1.origination=SFO`  **Note** In your request, send either the complete route or the individual legs (`legs.0.origination` and `legs.n.destination`). If you send all the fields, the complete route takes precedence over the individual legs.  For details, see the `decision_manager_travel_leg#_orig` field description in [Decision Manager Using the SCMP API Developer Guide.](https://www.cybersource.com/developers/documentation/fraud_management/) 

        :param origination: The origination of this Riskv1decisionsTravelInformationLegs.
        :type: str
        """
        if origination is not None and len(origination) > 3:
            raise ValueError("Invalid value for `origination`, length must be less than or equal to `3`")

        self._origination = origination

    @property
    def destination(self):
        """
        Gets the destination of this Riskv1decisionsTravelInformationLegs.
        Use to specify the airport code for the destination of the leg of the trip, which is designated by the pound (#) symbol in the field name. This code is usually three digits long, for example: SFO = San Francisco. Do not use the colon (:) or the dash (-). For airport codes, see [IATA Airline and Airport Code Search](https://www.iata.org/publications/Pages/code-search.aspx). The leg number can be a positive integer from 0 to N. For example:  `travelInformation.legs.0.destination=SFO` `travelInformation.legs.1.destination=SFO`  **Note** In your request, send either the complete route or the individual legs (`legs.0.origination` and `legs.n.destination`). If you send all the fields, the complete route takes precedence over the individual legs.  For details, see the `decision_manager_travel_leg#_dest` field description in [Decision Manager Using the SCMP API Developer Guide.](https://www.cybersource.com/developers/documentation/fraud_management/) 

        :return: The destination of this Riskv1decisionsTravelInformationLegs.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this Riskv1decisionsTravelInformationLegs.
        Use to specify the airport code for the destination of the leg of the trip, which is designated by the pound (#) symbol in the field name. This code is usually three digits long, for example: SFO = San Francisco. Do not use the colon (:) or the dash (-). For airport codes, see [IATA Airline and Airport Code Search](https://www.iata.org/publications/Pages/code-search.aspx). The leg number can be a positive integer from 0 to N. For example:  `travelInformation.legs.0.destination=SFO` `travelInformation.legs.1.destination=SFO`  **Note** In your request, send either the complete route or the individual legs (`legs.0.origination` and `legs.n.destination`). If you send all the fields, the complete route takes precedence over the individual legs.  For details, see the `decision_manager_travel_leg#_dest` field description in [Decision Manager Using the SCMP API Developer Guide.](https://www.cybersource.com/developers/documentation/fraud_management/) 

        :param destination: The destination of this Riskv1decisionsTravelInformationLegs.
        :type: str
        """
        if destination is not None and len(destination) > 3:
            raise ValueError("Invalid value for `destination`, length must be less than or equal to `3`")

        self._destination = destination

    @property
    def departure_date_time(self):
        """
        Gets the departure_date_time of this Riskv1decisionsTravelInformationLegs.
        Departure date and time for the each leg of the trip. Use one of the following formats: - `yyyy-MM-dd HH:mm z` - `yyyy-MM-dd hh:mm a z` - `yyyy-MM-dd hh:mma z`  Where:\\ `HH` = hour in 24-hour format\\ `hh` = hour in 12-hour format\\ `a` = am or pm (case insensitive)\\ `z` = time zone of the departing flight. For example, if the airline is based in city A, but the flight departs from city B, `z` is the time zone of city B at the time of departure.\\ **Important** For travel information, use GMT instead of UTC, or use the local time zone.  #### Examples  2011-03-20 11:30 PM PDT\\ 2011-03-20 11:30pm GMT\\ 2011-03-20 11:30pm GMT-05:00\\ Eastern Standard Time: GMT-05:00 or EST\\  **Note** When specifying an offset from GMT, the format must be exactly as specified in the example. Insert no spaces between the time zone and the offset. 

        :return: The departure_date_time of this Riskv1decisionsTravelInformationLegs.
        :rtype: str
        """
        return self._departure_date_time

    @departure_date_time.setter
    def departure_date_time(self, departure_date_time):
        """
        Sets the departure_date_time of this Riskv1decisionsTravelInformationLegs.
        Departure date and time for the each leg of the trip. Use one of the following formats: - `yyyy-MM-dd HH:mm z` - `yyyy-MM-dd hh:mm a z` - `yyyy-MM-dd hh:mma z`  Where:\\ `HH` = hour in 24-hour format\\ `hh` = hour in 12-hour format\\ `a` = am or pm (case insensitive)\\ `z` = time zone of the departing flight. For example, if the airline is based in city A, but the flight departs from city B, `z` is the time zone of city B at the time of departure.\\ **Important** For travel information, use GMT instead of UTC, or use the local time zone.  #### Examples  2011-03-20 11:30 PM PDT\\ 2011-03-20 11:30pm GMT\\ 2011-03-20 11:30pm GMT-05:00\\ Eastern Standard Time: GMT-05:00 or EST\\  **Note** When specifying an offset from GMT, the format must be exactly as specified in the example. Insert no spaces between the time zone and the offset. 

        :param departure_date_time: The departure_date_time of this Riskv1decisionsTravelInformationLegs.
        :type: str
        """
        if departure_date_time is not None and len(departure_date_time) > 25:
            raise ValueError("Invalid value for `departure_date_time`, length must be less than or equal to `25`")

        self._departure_date_time = departure_date_time

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
        if not isinstance(other, Riskv1decisionsTravelInformationLegs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
