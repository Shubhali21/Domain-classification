# Use official Python runtime as a parent image
FROM python:3.10.5-slim

# Set working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container 
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r Requirements.txt
# Download NLTK stopwords inside the container
RUN python -m nltk.downloader stopwords

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
