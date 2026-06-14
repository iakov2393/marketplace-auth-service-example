import contextvars
import uuid

trace_id_var: contextvars.ContextVar[str] = contextvars.ContextVar(
    "trace_id", default="-"
)


def get_trace_id() -> str:
    return trace_id_var.get()


def set_trace_id(trace_id: str | None) -> contextvars.Token:
    return trace_id_var.set(trace_id or str(uuid.uuid4()))


def reset_trace_id(token: contextvars.Token) -> None:
    trace_id_var.reset(token)
