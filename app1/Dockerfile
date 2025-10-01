#Usar uma imagem oficial de py
FROM python:3.9-slim

#Definir o diretorio de trabalho para o container
WORKDIR /app

#Copia o arquivo de requisitos pra o container
COPY requirements.txt .

#Instala as dependencias da aplicação
RUN pip install --no-cache-dir -r requirements.txt

#Copia aplicação pro container
COPY . .

#Expondo a porta que o servidor vai usar(como to usando flask vai ser a 5000)
EXPOSE 5000

#Definindo comando para iniciar a aplicação
CMD ["python", "app.py"]

