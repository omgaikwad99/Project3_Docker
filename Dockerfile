# Use Python Alpine as base image
FROM python:3.9-alpine

# Set working directory inside the container
WORKDIR /home/data

# Create the output directory
RUN mkdir -p /home/output/

# Copy Python script and text files into the container
COPY script.py IF.txt Limerick-1.txt /home/data/

# Run the Python script
CMD ["sh", "-c", "python -u script.py && sh"]
