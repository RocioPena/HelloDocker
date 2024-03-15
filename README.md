# HelloDocker

Install redis
sudo apt install redis

redis-server


Intall alpine
docker pull alpine

Para ver la imagen de alpine
docker images


Install ubuntu
docker pull ubuntu:18.04

Para ver la imagen de ubuntu
docker images


Como generar un contenedor
-it= interactivo
--name= nombre del contenedor

docker run -it --name mi_contenedor ubuntu:18.04

y tiene que aparecer lo siguiente:   root@f5442eaa536c:/#  



root@f5442eaa536c:/#  apt update

root@f5442eaa536c:/# apt install python

Visualizar los contenedores
docker ps -a