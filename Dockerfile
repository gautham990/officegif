FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install necessary dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . .

# Expose the port that Flask is running on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application
CMD ["flask", "run"]

