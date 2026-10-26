# Multi-stage, minimal, offline-friendly image for the harness.
# Core has no third-party runtime deps, so the runtime image stays tiny.

FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

# ---- test stage: run lint + types + tests at build time ----
FROM base AS test
COPY pyproject.toml ./
COPY harness ./harness
COPY tests ./tests
COPY README.md ./README.md
RUN pip install --no-cache-dir -e ".[dev]" \
    && ruff check . \
    && mypy \
    && pytest -q

# ---- runtime stage: slim image with only the package ----
FROM base AS runtime
# Run as a non-root user (least privilege, matches the project's security model).
RUN useradd --create-home --uid 10001 harness
COPY pyproject.toml ./
COPY harness ./harness
COPY README.md ./README.md
RUN pip install --no-cache-dir .
USER harness
ENTRYPOINT ["harness"]
CMD ["status"]
