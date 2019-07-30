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


class StudyIntegrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_sample_study_link(self, source_id, target_id, **kwargs):  # noqa: E501
        """Create link between a sample and study  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sample_study_link(source_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: (required)
        :param str target_id: (required)
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_sample_study_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_sample_study_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
            return data

    def create_sample_study_link_with_http_info(self, source_id, target_id, **kwargs):  # noqa: E501
        """Create link between a sample and study  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sample_study_link_with_http_info(source_id, target_id, async_req=True)
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
                    " to method create_sample_study_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `create_sample_study_link`")  # noqa: E501
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params or
                params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `create_sample_study_link`")  # noqa: E501

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
            '/integration/link/sample/{sourceId}/to/study/{targetId}', 'POST',
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

    def delete_sample_study_link(self, source_id, target_id, **kwargs):  # noqa: E501
        """Delete link between a sample and study  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sample_study_link(source_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: (required)
        :param str target_id: (required)
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sample_study_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sample_study_link_with_http_info(source_id, target_id, **kwargs)  # noqa: E501
            return data

    def delete_sample_study_link_with_http_info(self, source_id, target_id, **kwargs):  # noqa: E501
        """Delete link between a sample and study  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sample_study_link_with_http_info(source_id, target_id, async_req=True)
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
                    " to method delete_sample_study_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params or
                params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `delete_sample_study_link`")  # noqa: E501
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params or
                params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `delete_sample_study_link`")  # noqa: E501

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
            '/integration/link/sample/{sourceId}/to/study/{targetId}', 'DELETE',
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

    def get_studies_by_samples(self, **kwargs):  # noqa: E501
        """Retrieve studies related to samples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_studies_by_samples(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: Query string supporting key-value metadata pairs, negation, numeric range filtering and boolean combinations.  

                           **Note**

                               In the below, we use ``(less-than)`` to represent the single character less-than sign.  

                           **Examples**

                               A **query** is a boolean combination of **terms** or sub-**expressions** e.g.  1. ``csv:Gender=female AND genestack.bio:organism=\"Human\"``  2. ``bio:age(less-than)50 || genestack.bio:organism!=Mouse``  We now describe the precise query language exhibited by these examples.  

                           **Literal values**

                               **Strings** are (1) delimited with double quote characters (``\"``). Literal quote characters and backslashes (2) may be escaped with the backslash character (``\\``). Basic **strings** with characters matching ``[a-zA-Z0-9:-_$]`` (3) need not be quoted.  The following are examples:  1. ``\"hello world\"``  2. ``\"Here is a quote: \\\", and here a backslash: \\\\\"``  3. ``hello$World``  **Numbers** are (1) base-10 integer values, or (2) base-10 numbers with a fractional part, e.g.  1. ``-5``  2. ``7.23``  

                           **Terms**

                               A **term** is either (1) a metadata **key-value term**, (2) a negated metadata **key-value term** or (3) a **numerical range term**, described below.  A **key-value term** has the form ``metadataKey=value``, where the left and right operands are both **strings**.  This will match literal metadata values exactly.  A **negated key-value term** has the form ``metadataKey!=value``, where the operands are as above.  A **numerical range term** has the form ``metadataKey(op)value``, where the operator ``(op)`` is either a less-than or greater-than character, the left operand is a **string** and the right operand a **number**.  The following are examples:  1. ``genestack.bio:organism=\"Homo sapiens\"``  2. ``age:years(less-than)50``  

                           **Binary connectives**

                               The **binary connectives** are ``&&`` and ``||``, with synonyms:  1. ``and``  2. ``AND``  3. ``or``  4. ``OR``  **Connectives** must be separated from other tokens with whitespace.  Complex **expressions** may be formed with parenthesis characters, otherwise standard precedence rules apply.  The following are examples:  1. ``a=b``  2. ``a=b AND c=d``  3. ``(a=b || c=d) AND e(less-than)50``

        :param str query: Search for objects via a full-text query over all metadata.
        :param bool search_specific_terms: Modifies the full-text query to search across more specific dictionary terms. For example, search query \"Body fluid\" will also search for files with term \"Blood\" in their metadata, given there exists a dictionary that describes such relation.
        :param int page_limit: Maximum number of results to return. This value must be between 0 and 100 (inclusive).
        :param int page_offset: Index of first result to return. This can be used to retrieve large numbers of results in batches.
        :return: ListResponse. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_studies_by_samples_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_studies_by_samples_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_studies_by_samples_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve studies related to samples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_studies_by_samples_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: Query string supporting key-value metadata pairs, negation, numeric range filtering and boolean combinations.  

                           **Note**

                               In the below, we use ``(less-than)`` to represent the single character less-than sign.  

                           **Examples**

                               A **query** is a boolean combination of **terms** or sub-**expressions** e.g.  1. ``csv:Gender=female AND genestack.bio:organism=\"Human\"``  2. ``bio:age(less-than)50 || genestack.bio:organism!=Mouse``  We now describe the precise query language exhibited by these examples.  

                           **Literal values**

                               **Strings** are (1) delimited with double quote characters (``\"``). Literal quote characters and backslashes (2) may be escaped with the backslash character (``\\``). Basic **strings** with characters matching ``[a-zA-Z0-9:-_$]`` (3) need not be quoted.  The following are examples:  1. ``\"hello world\"``  2. ``\"Here is a quote: \\\", and here a backslash: \\\\\"``  3. ``hello$World``  **Numbers** are (1) base-10 integer values, or (2) base-10 numbers with a fractional part, e.g.  1. ``-5``  2. ``7.23``  

                           **Terms**

                               A **term** is either (1) a metadata **key-value term**, (2) a negated metadata **key-value term** or (3) a **numerical range term**, described below.  A **key-value term** has the form ``metadataKey=value``, where the left and right operands are both **strings**.  This will match literal metadata values exactly.  A **negated key-value term** has the form ``metadataKey!=value``, where the operands are as above.  A **numerical range term** has the form ``metadataKey(op)value``, where the operator ``(op)`` is either a less-than or greater-than character, the left operand is a **string** and the right operand a **number**.  The following are examples:  1. ``genestack.bio:organism=\"Homo sapiens\"``  2. ``age:years(less-than)50``  

                           **Binary connectives**

                               The **binary connectives** are ``&&`` and ``||``, with synonyms:  1. ``and``  2. ``AND``  3. ``or``  4. ``OR``  **Connectives** must be separated from other tokens with whitespace.  Complex **expressions** may be formed with parenthesis characters, otherwise standard precedence rules apply.  The following are examples:  1. ``a=b``  2. ``a=b AND c=d``  3. ``(a=b || c=d) AND e(less-than)50``

        :param str query: Search for objects via a full-text query over all metadata.
        :param bool search_specific_terms: Modifies the full-text query to search across more specific dictionary terms. For example, search query \"Body fluid\" will also search for files with term \"Blood\" in their metadata, given there exists a dictionary that describes such relation.
        :param int page_limit: Maximum number of results to return. This value must be between 0 and 100 (inclusive).
        :param int page_offset: Index of first result to return. This can be used to retrieve large numbers of results in batches.
        :return: ListResponse. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['filter', 'query', 'search_specific_terms', 'page_limit', 'page_offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_studies_by_samples" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'search_specific_terms' in params:
            query_params.append(('searchSpecificTerms', params['search_specific_terms']))  # noqa: E501
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
            '/integration/link/studies/by/samples', 'GET',
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

    def get_study_by_sample(self, id, **kwargs):  # noqa: E501
        """Retrieve studies related to samples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_study_by_sample(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier (accession) of the SPoT object. (required)
        :return: Study. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_study_by_sample_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_study_by_sample_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_study_by_sample_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve studies related to samples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_study_by_sample_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier (accession) of the SPoT object. (required)
        :return: Study. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_study_by_sample" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_study_by_sample`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Genestack-API-Token']  # noqa: E501

        return self.api_client.call_api(
            '/integration/link/study/by/sample/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Study',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)