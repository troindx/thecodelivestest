# Use the official Python image.
FROM python:latest

# Set environment variables to prevent Python from writing .pyc files to disc
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install dependencies
COPY ./back/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY ./back/app /app/app
COPY ./.env.dist /app/.env

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
