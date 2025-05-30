# Usa imagem base leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script principal para dentro do container
COPY app.py .

# Expõe a porta da aplicação Flask
EXPOSE 5000

# Comando para iniciar o app
CMD ["python", "app.py"]
