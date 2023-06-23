# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR .

# Install dependencies
# COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
# COPY . /code/

# Expose the port that Django runs on (default is 8000)
EXPOSE 9000

# Start the Django development server
CMD ["python", "gpt3app/manage.py", "runserver", "0.0.0.0:9000"]
