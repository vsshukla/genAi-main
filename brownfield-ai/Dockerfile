# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set environment variables (add any necessary ones here)
ENV OPENAI_API_KEY=your_openai_api_key_here

# Expose port (if you're using an API)
EXPOSE 8000

# Run the application (you may need to update this command)
CMD ["python", "workflows/resolve_task.py"]
