# =====================================================================
# STAGE 1: Testing & Quality Assurance
# =====================================================================
FROM python:3.12-slim AS tester
WORKDIR /app

# Copy python dependencies out of the local docker/ subdirectory
COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code out of the local src/ subdirectory
COPY src/standalone_calculator.py .

# Force run pytest. If a single test fails, the Docker build crashes immediately,
# preventing broken code from ever being published to ghcr.io
RUN pytest -v standalone_calculator.py

# =====================================================================
# STAGE 2: Pristine Production Runtime
# =====================================================================
FROM python:3.12-slim AS runtime
WORKDIR /app

# Extract the verified script out of our staging environment
COPY --from=tester /app/standalone_calculator.py .

# Run as a standalone execution payload
ENTRYPOINT ["python", "standalone_calculator.py"]
