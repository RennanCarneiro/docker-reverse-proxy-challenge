# Usa a imagem oficial do Nginx
FROM nginx:alpine

# Copia o arquivo de configuração local para o diretório de configuração do Nginx no container
COPY nginx.conf /etc/nginx/nginx.conf

COPY index.html /usr/share/nginx/html

# A imagem do Nginx já expõe a porta 80 por padrão, mas não custa nada reforçar.
EXPOSE 80

# O comando para iniciar o Nginx já é o padrão da imagem base
CMD ["nginx", "-g", "daemon off;"]