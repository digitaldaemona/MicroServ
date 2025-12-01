# STAGE 1: Build Stage
FROM python:3.11-slim as builder
WORKDIR /usr/src/app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Runtime Stage
FROM python:3.11-slim
WORKDIR /usr/src/app

# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application source code
COPY backend/msrv_backend /usr/src/app/msrv_backend
COPY msrv.py .

# Standard port for the Flask app (internal to the container)
EXPOSE 5000

# Command to run the application (using Gunicorn in production, but simpler for dev/CI)
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "msrv_backend.app:create_app()"]
CMD ["python", "-m", "msrv_backend"]