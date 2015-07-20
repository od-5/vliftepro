# coding=utf-8
from functools import wraps
import os
from traceback import print_exc
import json
import uuid
from django.http import HttpResponse
import sys

__author__ = 'alexy'

def render_to_json(f):
    """
        Декоратор, отдающий HttpResponse, содержащий JSON.
        Если декорируемая функция возвращает HttpResponse, он отдается без изменений.
        В случае исключения оно также отдается в виде json.
    """
    @wraps(f)
    def _decorator(request, *args, **kwargs):
        try:
            data = f(request, *args, **kwargs)
            if isinstance(data, HttpResponse):
                response = data
            else:
                json_content = json.dumps(data, ensure_ascii=False)
                if isinstance(json_content, unicode):
                    json_content = json_content.encode('utf-8')
                response = HttpResponse(json_content, 'application/json; charset=UTF-8')
        except Exception, e:
            print_exc()
            #json_content = JsonExceptionLogger().safe_json()
            json_content = json.dumps({"error": unicode(e)}, ensure_ascii=False)
            if isinstance(json_content, unicode):
                json_content = json_content.encode('utf-8')
            print >>sys.stderr, json_content
            response = HttpResponse(json_content.encode('utf-8'), 'application/json; charset=UTF-8')
        return response

    return _decorator


def get_slider_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join('slider', self.city.slug, filename)