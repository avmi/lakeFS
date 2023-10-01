"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lakefs_client.api_client import ApiClient, Endpoint as _Endpoint
from lakefs_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lakefs_client.model.commit_list import CommitList
from lakefs_client.model.diff_list import DiffList
from lakefs_client.model.error import Error
from lakefs_client.model.find_merge_base_result import FindMergeBaseResult
from lakefs_client.model.merge import Merge
from lakefs_client.model.merge_result import MergeResult


class RefsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.diff_refs_endpoint = _Endpoint(
            settings={
                'response_type': (DiffList,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth',
                    'saml_auth'
                ],
                'endpoint_path': '/repositories/{repository}/refs/{leftRef}/diff/{rightRef}',
                'operation_id': 'diff_refs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'left_ref',
                    'right_ref',
                    'after',
                    'amount',
                    'prefix',
                    'delimiter',
                    'type',
                ],
                'required': [
                    'repository',
                    'left_ref',
                    'right_ref',
                ],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                    'amount',
                ]
            },
            root_map={
                'validations': {
                    ('amount',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': -1,
                    },
                },
                'allowed_values': {
                    ('type',): {

                        "TWO_DOT": "two_dot",
                        "THREE_DOT": "three_dot"
                    },
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'left_ref':
                        (str,),
                    'right_ref':
                        (str,),
                    'after':
                        (str,),
                    'amount':
                        (int,),
                    'prefix':
                        (str,),
                    'delimiter':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'left_ref': 'leftRef',
                    'right_ref': 'rightRef',
                    'after': 'after',
                    'amount': 'amount',
                    'prefix': 'prefix',
                    'delimiter': 'delimiter',
                    'type': 'type',
                },
                'location_map': {
                    'repository': 'path',
                    'left_ref': 'path',
                    'right_ref': 'path',
                    'after': 'query',
                    'amount': 'query',
                    'prefix': 'query',
                    'delimiter': 'query',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_merge_base_endpoint = _Endpoint(
            settings={
                'response_type': (FindMergeBaseResult,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth',
                    'saml_auth'
                ],
                'endpoint_path': '/repositories/{repository}/refs/{sourceRef}/merge/{destinationBranch}',
                'operation_id': 'find_merge_base',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'source_ref',
                    'destination_branch',
                ],
                'required': [
                    'repository',
                    'source_ref',
                    'destination_branch',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'source_ref':
                        (str,),
                    'destination_branch':
                        (str,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'source_ref': 'sourceRef',
                    'destination_branch': 'destinationBranch',
                },
                'location_map': {
                    'repository': 'path',
                    'source_ref': 'path',
                    'destination_branch': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.log_commits_endpoint = _Endpoint(
            settings={
                'response_type': (CommitList,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth',
                    'saml_auth'
                ],
                'endpoint_path': '/repositories/{repository}/refs/{ref}/commits',
                'operation_id': 'log_commits',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'ref',
                    'after',
                    'amount',
                    'objects',
                    'prefixes',
                    'limit',
                    'first_parent',
                ],
                'required': [
                    'repository',
                    'ref',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'amount',
                ]
            },
            root_map={
                'validations': {
                    ('amount',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': -1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'ref':
                        (str,),
                    'after':
                        (str,),
                    'amount':
                        (int,),
                    'objects':
                        ([str],),
                    'prefixes':
                        ([str],),
                    'limit':
                        (bool,),
                    'first_parent':
                        (bool,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'ref': 'ref',
                    'after': 'after',
                    'amount': 'amount',
                    'objects': 'objects',
                    'prefixes': 'prefixes',
                    'limit': 'limit',
                    'first_parent': 'first_parent',
                },
                'location_map': {
                    'repository': 'path',
                    'ref': 'path',
                    'after': 'query',
                    'amount': 'query',
                    'objects': 'query',
                    'prefixes': 'query',
                    'limit': 'query',
                    'first_parent': 'query',
                },
                'collection_format_map': {
                    'objects': 'multi',
                    'prefixes': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.merge_into_branch_endpoint = _Endpoint(
            settings={
                'response_type': (MergeResult,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth',
                    'saml_auth'
                ],
                'endpoint_path': '/repositories/{repository}/refs/{sourceRef}/merge/{destinationBranch}',
                'operation_id': 'merge_into_branch',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'source_ref',
                    'destination_branch',
                    'merge',
                ],
                'required': [
                    'repository',
                    'source_ref',
                    'destination_branch',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'source_ref':
                        (str,),
                    'destination_branch':
                        (str,),
                    'merge':
                        (Merge,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'source_ref': 'sourceRef',
                    'destination_branch': 'destinationBranch',
                },
                'location_map': {
                    'repository': 'path',
                    'source_ref': 'path',
                    'destination_branch': 'path',
                    'merge': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def diff_refs(
        self,
        repository,
        left_ref,
        right_ref,
        **kwargs
    ):
        """diff references  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.diff_refs(repository, left_ref, right_ref, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            left_ref (str): a reference (could be either a branch or a commit ID)
            right_ref (str): a reference (could be either a branch or a commit ID) to compare against

        Keyword Args:
            after (str): return items after this value. [optional]
            amount (int): how many items to return. [optional] if omitted the server will use the default value of 100
            prefix (str): return items prefixed with this value. [optional]
            delimiter (str): delimiter used to group common prefixes by. [optional]
            type (str): [optional] if omitted the server will use the default value of "three_dot"
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DiffList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['left_ref'] = \
            left_ref
        kwargs['right_ref'] = \
            right_ref
        return self.diff_refs_endpoint.call_with_http_info(**kwargs)

    def find_merge_base(
        self,
        repository,
        source_ref,
        destination_branch,
        **kwargs
    ):
        """find the merge base for 2 references  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_merge_base(repository, source_ref, destination_branch, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            source_ref (str): source ref
            destination_branch (str): destination branch name

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            FindMergeBaseResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['source_ref'] = \
            source_ref
        kwargs['destination_branch'] = \
            destination_branch
        return self.find_merge_base_endpoint.call_with_http_info(**kwargs)

    def log_commits(
        self,
        repository,
        ref,
        **kwargs
    ):
        """get commit log from ref. If both objects and prefixes are empty, return all commits.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.log_commits(repository, ref, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            ref (str):

        Keyword Args:
            after (str): return items after this value. [optional]
            amount (int): how many items to return. [optional] if omitted the server will use the default value of 100
            objects ([str]): list of paths, each element is a path of a specific object. [optional]
            prefixes ([str]): list of paths, each element is a path of a prefix. [optional]
            limit (bool): limit the number of items in return to 'amount'. Without further indication on actual number of items.. [optional]
            first_parent (bool): if set to true, follow only the first parent upon reaching a merge commit. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CommitList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['ref'] = \
            ref
        return self.log_commits_endpoint.call_with_http_info(**kwargs)

    def merge_into_branch(
        self,
        repository,
        source_ref,
        destination_branch,
        **kwargs
    ):
        """merge references  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.merge_into_branch(repository, source_ref, destination_branch, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            source_ref (str): source ref
            destination_branch (str): destination branch name

        Keyword Args:
            merge (Merge): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MergeResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['source_ref'] = \
            source_ref
        kwargs['destination_branch'] = \
            destination_branch
        return self.merge_into_branch_endpoint.call_with_http_info(**kwargs)

