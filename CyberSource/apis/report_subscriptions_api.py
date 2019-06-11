# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ReportSubscriptionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config) 


    def create_subscription(self, request_body, **kwargs):
        """
        Create Report Subscription for a report name by organization
        Create a report subscription for your organization. The report name must be unique. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_subscription(request_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RequestBody1 request_body: Report subscription request payload (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_subscription_with_http_info(request_body, **kwargs)
        else:
            (data) = self.create_subscription_with_http_info(request_body, **kwargs)
            return data

    def create_subscription_with_http_info(self, request_body, **kwargs):
        """
        Create Report Subscription for a report name by organization
        Create a report subscription for your organization. The report name must be unique. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_subscription_with_http_info(request_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RequestBody1 request_body: Report subscription request payload (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_body', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_body' is set
        if ('request_body' not in params) or (params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `create_subscription`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            raise ValueError("Invalid value for parameter `organization_id` when calling `create_subscription`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            raise ValueError("Invalid value for parameter `organization_id` when calling `create_subscription`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            raise ValueError("Invalid value for parameter `organization_id` when calling `create_subscription`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in params:
            body_params = params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/report-subscriptions', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_subscription(self, report_name, **kwargs):
        """
        Delete subscription of a report name by organization
        Delete a report subscription for your organization. You must know the unique name of the report you want to delete. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_subscription(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_subscription_with_http_info(report_name, **kwargs)
        else:
            (data) = self.delete_subscription_with_http_info(report_name, **kwargs)
            return data

    def delete_subscription_with_http_info(self, report_name, **kwargs):
        """
        Delete subscription of a report name by organization
        Delete a report subscription for your organization. You must know the unique name of the report you want to delete. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_subscription_with_http_info(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_name' is set
        if ('report_name' not in params) or (params['report_name'] is None):
            raise ValueError("Missing the required parameter `report_name` when calling `delete_subscription`")

        if 'report_name' in params and len(params['report_name']) > 80:
            raise ValueError("Invalid value for parameter `report_name` when calling `delete_subscription`, length must be less than or equal to `80`")
        if 'report_name' in params and len(params['report_name']) < 1:
            raise ValueError("Invalid value for parameter `report_name` when calling `delete_subscription`, length must be greater than or equal to `1`")
        if 'report_name' in params and not re.search('[a-zA-Z0-9-_+]+', params['report_name']):
            raise ValueError("Invalid value for parameter `report_name` when calling `delete_subscription`, must conform to the pattern `/[a-zA-Z0-9-_+]+/`")

        collection_formats = {}

        path_params = {}
        if 'report_name' in params:
            path_params['reportName'] = params['report_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/report-subscriptions/' + report_name, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_all_subscriptions(self, **kwargs):
        """
        Get all subscriptions
        View a summary of all report subscriptions. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_subscriptions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ReportingV3ReportSubscriptionsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_subscriptions_with_http_info(**kwargs)
        else:
            (data) = self.get_all_subscriptions_with_http_info(**kwargs)
            return data

    def get_all_subscriptions_with_http_info(self, **kwargs):
        """
        Get all subscriptions
        View a summary of all report subscriptions. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_subscriptions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ReportingV3ReportSubscriptionsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/report-subscriptions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportSubscriptionsGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription(self, report_name, **kwargs):
        """
        Get subscription for report name
        View the details of a report subscription, such as the report format or report frequency, using the report’s unique name. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Retrieve (required)
        :return: ReportingV3ReportSubscriptionsGet200ResponseSubscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_with_http_info(report_name, **kwargs)
        else:
            (data) = self.get_subscription_with_http_info(report_name, **kwargs)
            return data

    def get_subscription_with_http_info(self, report_name, **kwargs):
        """
        Get subscription for report name
        View the details of a report subscription, such as the report format or report frequency, using the report’s unique name. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_with_http_info(report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_name: Name of the Report to Retrieve (required)
        :return: ReportingV3ReportSubscriptionsGet200ResponseSubscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_name' is set
        if ('report_name' not in params) or (params['report_name'] is None):
            raise ValueError("Missing the required parameter `report_name` when calling `get_subscription`")

        if 'report_name' in params and len(params['report_name']) > 80:
            raise ValueError("Invalid value for parameter `report_name` when calling `get_subscription`, length must be less than or equal to `80`")
        if 'report_name' in params and len(params['report_name']) < 1:
            raise ValueError("Invalid value for parameter `report_name` when calling `get_subscription`, length must be greater than or equal to `1`")
        if 'report_name' in params and not re.search('[a-zA-Z0-9-_+]+', params['report_name']):
            raise ValueError("Invalid value for parameter `report_name` when calling `get_subscription`, must conform to the pattern `/[a-zA-Z0-9-_+]+/`")

        collection_formats = {}

        path_params = {}
        if 'report_name' in params:
            path_params['reportName'] = params['report_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/report-subscriptions/' + report_name, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportSubscriptionsGet200ResponseSubscriptions',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
