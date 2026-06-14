from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from src.infrastructure.tracing import get_trace_id, reset_trace_id, set_trace_id

TRACE_HEADER = "X-Trace-Id"


class TracingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        token = set_trace_id(request.headers.get(TRACE_HEADER))
        try:
            response = await call_next(request)
            response.headers[TRACE_HEADER] = get_trace_id()
            return response
        finally:
            reset_trace_id(token)
