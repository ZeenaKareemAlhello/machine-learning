FROM python:3.13.3-slim

RUN pip install uv

WORKDIR /app

#to use the uvicorn command without say uv run uvicorn
ENV PATH="/app/.venv/bin:$PATH"

COPY ["pyproject.toml", "uv.lock", ".python-version","./"]
RUN uv sync --locked

COPY ["src/service/churn.py","model_C=1.0.bin","./"]

EXPOSE 9696

ENTRYPOINT [ "uvicorn", "churn:app", "--host", "0.0.0.0", "--port", "9696" ]