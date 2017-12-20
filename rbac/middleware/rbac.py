#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from django.conf import settings
from django.shortcuts import HttpResponse, redirect
from django.utils.safestring import mark_safe


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        """
        检查用户是否具有权限访问当前URL
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """

        """跳过无需权限访问的URL"""
        for pattern in settings.RBAC_NO_AUTH_URL:
            if re.match(pattern, request.path_info):
                return None

        """获取当前用户session中的权限信息"""
        permission_url_dict = request.session.get(settings.RBAC_PERMISSION_URL_SESSION_KEY)
        if not permission_url_dict:
            return HttpResponse(settings.RBAC_PERMISSION_MSG)

        """当前URL和session中的权限进行匹配"""
        flag = False
        for group_id, codes_urls in permission_url_dict.items():
            urls = codes_urls['urls']
            codes = codes_urls['codes']
            for url in urls:
                pattern = settings.RBAC_MATCH_PARTTERN.format(url)
                if re.match(pattern, request.path_info):
                    flag = True
                    request.permission_code_list = codes
                    break
            if flag:
                break

        if not flag:
            return HttpResponse(settings.RBAC_PERMISSION_MSG)
