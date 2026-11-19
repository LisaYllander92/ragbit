FROM python:3.13-slim

# puts in app folder in the root and changes my directory to /app (linux starts with /)
WORKDIR /app/

# /app/frontend, but I'm still in /app
COPY frontend frontend

# insteed of installing a package -> keep structure as it is for the imports
ENV PYTHONPATH=/app/frontend

# installed uv
RUN pip install --no-cache-dir uv

# change directory to where our files are that we want in the image (app.py)
WORKDIR /app/frontend/src/frontend 

# install packages
RUN uv sync --no-dev

# runs the api
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


