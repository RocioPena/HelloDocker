# HelloDocker

## 1. Install redis

Paso 1: Instalacion de redis
```
sudo apt install redis
```

## 2. Correr el servidor de redis

Paso 2: Servidor
```
redis-server
```

## 3. Interfaz de redis

Paso 3: Correr el cli de redis
Nota: abrir otro terminar para ejecutarlo
```
redis-cli
```

Tiene que aparecer lo siguiente:
```127.0.0.1:6379>```


Intall alpine
```
docker pull alpine
```

Para ver la imagen de alpine
```
docker images
```


Install ubuntu
```
docker pull ubuntu:18.04
```

Para ver la imagen de ubuntu
```
docker images
```


Como generar un contenedor
```
-it= interactivo
--name= nombre del contenedor
```

```
docker run -it --name mi_contenedor ubuntu:18.04
```

y tiene que aparecer lo siguiente:   ```root@f5442eaa536c:/#  ```



```root@f5442eaa536c:/#  apt update```

```root@f5442eaa536c:/# apt install python```

Visualizar los contenedores
```
docker ps -a
```