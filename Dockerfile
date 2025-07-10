# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR .

# Copy the dependencies file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "st.py", "--server.port=8501", "--server.address=0.0.0.0"]
