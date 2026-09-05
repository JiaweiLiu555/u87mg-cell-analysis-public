FROM python:3.11-slim

WORKDIR /app
COPY requirements.deploy.txt .
RUN pip install --no-cache-dir -r requirements.deploy.txt

COPY deploy_app.py .
COPY src ./src
COPY demo_outputs/generated ./demo_outputs/generated

ENV PYTHONDONTWRITEBYTECODE=1
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
EXPOSE 8501

CMD ["sh", "-c", "streamlit run deploy_app.py --server.port \${PORT:-8501}"]

