FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

COPY app /app
COPY pyproject.toml /
COPY run_app.py /
COPY models /models

WORKDIR /

ENV PATH="/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ENV TZ=Asia/Shanghai
ENV LANG=zh_CN.utf8
ENV LANGUAGE=zh_CN.utf8
ENV PYTHONPATH=.

ENTRYPOINT ["python", "run_app.py"]
