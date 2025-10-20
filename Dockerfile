FROM apache/airflow:2.5.1

USER root
# Install system dependencies if needed
RUN apt-get update && apt-get install -y gcc g++ python3-dev && rm -rf /var/lib/apt/lists/*

# Switch to airflow user before installing Python libs
USER airflow

# Copy requirements file into image
COPY requirements.txt /requirements.txt

# Install your Python dependencies properly
RUN pip install --no-cache-dir -r /requirements.txt