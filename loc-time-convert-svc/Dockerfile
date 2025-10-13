FROM python:3.12-slim-bookworm
COPY --from=swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY app /app
COPY pyproject.toml /

# linux环境中命令行运行gunicorn需要将执行脚本放在/app同级目录
RUN mv /app/run_app.py /

WORKDIR /

ENV PATH="/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV ES_URL=http://elasticsearch:9200

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ENV TZ=Asia/Shanghai
ENV LANG=zh_CN.utf8
ENV LANGUAGE=zh_CN.utf8
ENV PYTHONPATH=.

ENTRYPOINT ["python", "run_app.py"]