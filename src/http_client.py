
#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPL v3 Copyright: 2019, Eli Schwartz <eschwartz@archlinux.org>

from http.client import (responses, HTTPConnection, HTTPSConnection,
        BAD_REQUEST, FOUND, FORBIDDEN, HTTP_VERSION_NOT_SUPPORTED,
        INTERNAL_SERVER_ERROR, METHOD_NOT_ALLOWED, MOVED_PERMANENTLY,
        NOT_FOUND, NOT_IMPLEMENTED, NOT_MODIFIED, OK, PARTIAL_CONTENT,
        PRECONDITION_FAILED, REQUEST_ENTITY_TOO_LARGE, REQUEST_URI_TOO_LONG,
        REQUESTED_RANGE_NOT_SATISFIABLE, REQUEST_TIMEOUT, SEE_OTHER,
        SERVICE_UNAVAILABLE, UNAUTHORIZED, _CS_IDLE, _CS_REQ_SENT)

if False:
    responses, HTTPConnection, HTTPSConnection, BAD_REQUEST, FOUND, FORBIDDEN, HTTP_VERSION_NOT_SUPPORTED, INTERNAL_SERVER_ERROR, METHOD_NOT_ALLOWED
    MOVED_PERMANENTLY, NOT_FOUND, NOT_IMPLEMENTED, NOT_MODIFIED, OK, PARTIAL_CONTENT, PRECONDITION_FAILED, REQUEST_ENTITY_TOO_LARGE, REQUEST_URI_TOO_LONG
    REQUESTED_RANGE_NOT_SATISFIABLE, REQUEST_TIMEOUT, SEE_OTHER, SERVICE_UNAVAILABLE, UNAUTHORIZED, _CS_IDLE, _CS_REQ_SENT