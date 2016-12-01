# coding: utf-8

"""
    VeriCiteLmsApiV1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ReportURLLinkReponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, assignment_id=None, context_id=None, external_content_id=None, url=None, user_id=None):
        """
        ReportURLLinkReponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'assignment_id': 'str',
            'context_id': 'str',
            'external_content_id': 'str',
            'url': 'str',
            'user_id': 'str'
        }

        self.attribute_map = {
            'assignment_id': 'assignmentID',
            'context_id': 'contextID',
            'external_content_id': 'externalContentID',
            'url': 'url',
            'user_id': 'userID'
        }

        self._assignment_id = assignment_id
        self._context_id = context_id
        self._external_content_id = external_content_id
        self._url = url
        self._user_id = user_id


    @property
    def assignment_id(self):
        """
        Gets the assignment_id of this ReportURLLinkReponse.
        Assignment ID.

        :return: The assignment_id of this ReportURLLinkReponse.
        :rtype: str
        """
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        """
        Sets the assignment_id of this ReportURLLinkReponse.
        Assignment ID.

        :param assignment_id: The assignment_id of this ReportURLLinkReponse.
        :type: str
        """

        self._assignment_id = assignment_id

    @property
    def context_id(self):
        """
        Gets the context_id of this ReportURLLinkReponse.
        Context ID.

        :return: The context_id of this ReportURLLinkReponse.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this ReportURLLinkReponse.
        Context ID.

        :param context_id: The context_id of this ReportURLLinkReponse.
        :type: str
        """

        self._context_id = context_id

    @property
    def external_content_id(self):
        """
        Gets the external_content_id of this ReportURLLinkReponse.
        external Content ID

        :return: The external_content_id of this ReportURLLinkReponse.
        :rtype: str
        """
        return self._external_content_id

    @external_content_id.setter
    def external_content_id(self, external_content_id):
        """
        Sets the external_content_id of this ReportURLLinkReponse.
        external Content ID

        :param external_content_id: The external_content_id of this ReportURLLinkReponse.
        :type: str
        """

        self._external_content_id = external_content_id

    @property
    def url(self):
        """
        Gets the url of this ReportURLLinkReponse.
        The url to retrieve the report

        :return: The url of this ReportURLLinkReponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ReportURLLinkReponse.
        The url to retrieve the report

        :param url: The url of this ReportURLLinkReponse.
        :type: str
        """

        self._url = url

    @property
    def user_id(self):
        """
        Gets the user_id of this ReportURLLinkReponse.
        User ID.

        :return: The user_id of this ReportURLLinkReponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ReportURLLinkReponse.
        User ID.

        :param user_id: The user_id of this ReportURLLinkReponse.
        :type: str
        """

        self._user_id = user_id

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
