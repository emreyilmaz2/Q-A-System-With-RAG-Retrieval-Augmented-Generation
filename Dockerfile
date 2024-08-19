# Python 3.8 imajını kullan
FROM python:3.10
# Çalışma dizinini oluştur
WORKDIR /app

# Gerekli bağımlılıkları yükleyin
RUN apt-get update && apt-get install -y \
    build-essential \
    swig \
    wget \
    curl \
    git \
    libopenblas-dev \
    liblapack-dev \
    && apt-get clean

# Gereklilikleri yükle
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set the environment variable to tell Django to use the correct settings
ENV DJANGO_SETTINGS_MODULE=qa_system.settings

# Model dosyalarını kopyala
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
