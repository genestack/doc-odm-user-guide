# coding: utf-8

"""
    ODM Integration API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: default-released
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from integration_curator.api_client import ApiClient


class ExpressionIntegrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_expression_sample_link(self, source_id, target_id, **kwargs):  # noqa: E501
        """Create link between an expression object and sample  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_expression_sample_link(source_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: (required)
        :param str target_id: (required)
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_expression_sample_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_expression_sample_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
            return data

    def create_expression_sample_link_with_http_info(self, source_id, target_id, **kwargs):  # noqa: E501
        """Create link between an expression object and sample  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_expression_sample_link_with_http_info(source_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: (required)
        :param str target_id: (required)
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_id', 'target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_expression_sample_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `create_expression_sample_link`")  # noqa: E501
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params or
                params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `create_expression_sample_link`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501
        if 'target_id' in params:
            path_params['targetId'] = params['target_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Genestack-API-Token']  # noqa: E501

        return self.api_client.call_api(
            '/integration/link/expression/{sourceId}/to/sample/{targetId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_expression_sample_link(self, source_id, target_id, **kwargs):  # noqa: E501
        """Delete link between a expression object and sample  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_expression_sample_link(source_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: (required)
        :param str target_id: (required)
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_expression_sample_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_expression_sample_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
            return data

    def delete_expression_sample_link_with_http_info(self, source_id, target_id, **kwargs):  # noqa: E501
        """Delete link between a expression object and sample  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_expression_sample_link_with_http_info(source_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: (required)
        :param str target_id: (required)
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_id', 'target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_expression_sample_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `delete_expression_sample_link`")  # noqa: E501
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params or
                params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `delete_expression_sample_link`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']  # noqa: E501
        if 'target_id' in params:
            path_params['targetId'] = params['target_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Genestack-API-Token']  # noqa: E501

        return self.api_client.call_api(
            '/integration/link/expression/{sourceId}/to/sample/{targetId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_expression_by_sample(self, id, **kwargs):  # noqa: E501
        """Retrieve expression objects related to samples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_expression_by_sample(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier (accession) of the SPoT object. (required)
        :param int page_limit: Maximum number of results to return. This value must be between 0 and 100 (inclusive).
        :param int page_offset: Index of first result to return. This can be used to retrieve large numbers of results in batches.
        :return: ListResponse. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_expression_by_sample_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_expression_by_sample_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_expression_by_sample_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve expression objects related to samples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_expression_by_sample_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier (accession) of the SPoT object. (required)
        :param int page_limit: Maximum number of results to return. This value must be between 0 and 100 (inclusive).
        :param int page_offset: Index of first result to return. This can be used to retrieve large numbers of results in batches.
        :return: ListResponse. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'page_limit', 'page_offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_expression_by_sample" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_expression_by_sample`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page_limit' in params:
            query_params.append(('pageLimit', params['page_limit']))  # noqa: E501
        if 'page_offset' in params:
            query_params.append(('pageOffset', params['page_offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/tab-separated-values'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Genestack-API-Token']  # noqa: E501

        return self.api_client.call_api(
            '/integration/link/expression/by/sample/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)