FROM python:3.9-alpine

WORKDIR /app/

# Create non-root user.
RUN addgroup -S nopriv && adduser -S -G nopriv nopriv

# Set permissions to allow non-root user to run the Python code.
RUN chown -R nopriv:nopriv /app && chmod -R 700 /app

# Switch to non-root user.
USER nopriv

# Copy the Python files into the container.
# Note: Working directory should be root of repo.
COPY blog /app/blog

# Copy the blog posts into the container.
COPY assets /app/assets

# Install dependencies.
RUN python3 -m pip install -r blog/requirements.txt

CMD ["python3", "blog/manage.py", "runserver", "0:8000"]
