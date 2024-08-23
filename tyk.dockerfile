FROM tykio/tyk-gateway:latest
COPY tyk.conf /opt/tyk-gateway/tyk.conf
COPY flask-api.json /opt/tyk-gateway/apps/flask-api.json
EXPOSE 8080
CMD ["tyk", "start", "--conf=/opt/tyk-gateway/tyk.conf"]
