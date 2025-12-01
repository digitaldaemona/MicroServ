# STAGE 1: Build Stage
FROM node:20-slim as build-stage
WORKDIR /usr/src/app

# Copy package files
COPY frontend/package.json .
COPY frontend/package-lock.json .

# Install dependencies
RUN npm install

# Copy application source
COPY frontend/src ./src
COPY frontend/public ./public

# Build the React application
RUN npm run build

# STAGE 2: Runtime Stage (using Nginx)
# NOTE: The resulting 'build' folder is mounted directly to the Nginx container in docker-compose.yml
FROM alpine:latest
WORKDIR /usr/src/app

# Placeholder command (since the build output is served by the Nginx container)
CMD ["echo", "Frontend build complete. Artifacts are served by Nginx."]