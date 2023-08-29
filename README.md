# API Gateway y Microservicios - ST0263
- Estudiante: Juan Esteban Cardona Ospina.
 
- Profesor: EDWIN NELSON MONTOYA MUNERA.

 ## 1. Breve Descripcion del Proyecto:
  - Este trabajo consistia en implementar un API Gateway para cominicar dos microservicios, los cuales son(msev1, mserv2) usando herramientas como gRPC y RABBITMQ.
    El Api nada mas comunica las solicitudes que se le piden para que devuelva los resultados plasmados en los microservicios, y asi mismo debia funcionar en una
    instancia que se subio a AWS con IP elasticas, reglas de seguridad y puertos para peticiones, puertos usados: (5000, 5001, 5002)

## 1.1 Aspectos Cumplidos o Desarrollados:
   - Implementación de un API Gateway que maneja la comunicacion y solicitudes de un usuario.
   - Interacción con los microservicios mserv1 y mserv2 mediante gRPC.
   -  Lanzamiento de instancia de AWS, comunicandose entre si.
   -  Reglas de seguridad de la instacia, en AWS configuradas. 

## 1.2. Aspectos NO Cumplidos o Desarrollados:
   - Uso de la herramienta RabbitMQ para encolar y procesar solicitudes asíncronas hechas por un usuario para cuando gRPC no funcione. ya que no se pudo implementar el sistema de colas.

## 2. Información General de Diseño y Tecnologías Utilizadas:
   - En este proyecto, se utiliza una estructura basada en microservicios, donde el API Gateway cumple la función de ser el punto de inicio, y los microservicios desempeñan tareas individuales específicas. Se emplea la tecnología gRPC para que el API Gateway se comunique con los microservicios, facilitando un intercambio eficiente de información. Además, para manejar las solicitudes cuando la comunicación a través de gRPC no esté disponible, se utiliza RabbitMQ. Este último actúa como una herramienta de gestión para asegurar que las solicitudes sean manejadas de manera adecuada y sin pérdidas.

## 3. Descripción del Ambiente de Desarrollo y Técnico:
   - Lenguaje de Programación para la implementacion: Python
   - Librerías y Paquetes usados: grpc, flask, dotenv

## Compilación y Ejecución:
   - Abrir 3 terminales, en las cuales vamos a ejecutar las instancias de los microservicios y el API:
   - Instancia 1: cd Reto2-Top_telematica y corre python3 api_gateway.py
   - Instancia 2: cd Reto2-Top_telematica y corre python3 mserv1.py
   - Instancia 3: cd Reto2-Top_telematica y corre python3 mserv2.py

## Detalles del Desarrollo y Técnicos:
  - He desarrollado clases que se encargan de manejar la comunicación con los microservicios a través de gRPC.
  - El API Gateway se encarga de dirigir las peticiones hacia los microservicios utilizando solicitudes HTTP como intermediario.
  - Cada uno de los microservicios tiene su propia función especializada que ha sido diseñada para listar y buscar archivos en una carpeta específica.

## Resultados:
  mserv1:
  
  ![image](https://github.com/Juanes2002/Reto2-Top_telematica/assets/105470955/280f7ebe-5d84-4312-88f8-bdd2e3767d52)

## 4. Descripción del Ambiente de Ejecución en Producción:
   blinker==1.6.2
   certifi==2023.7.22
   charset-normalizer==3.2.0
   click==8.1.7
   colorama==0.4.6
   Flask==2.3.3
   grpcio==1.57.0
   grpcio-tools==1.57.0
   idna==3.4
   itsdangerous==2.1.2
   Jinja2==3.1.2
   MarkupSafe==2.1.3
   protobuf==4.24.2
   requests==2.31.0
   urllib3==2.0.4
   Werkzeug==2.3.7

## IPs:
 - https://52.4.214.61:5000/listar_archivos
 - https://52.4.214.61:5000/buscar_archivos

##Referencias:
  - https://www.paradigmadigital.com/dev/grpc-que-es-como-funciona/
  - https://www.intel.la/content/www/xl/es/cloud-computing/microservices.html
  - https://www.pragma.com.co/academia/lecciones/conozcamos-sobre-rabbitmq-sus-componentes-y-beneficios
  - https://www.youtube.com/watch?v=p23J6NTDhEk&pp=ugMICgJlcxABGAHKBSByYWJiaXRtcSBjb211bmljYWNpb24gbW9tIHB5dGhvbg%3D%3D
  - https://www.youtube.com/watch?v=iQ4kENLfaNI&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO&ab_channel=jumpstartCS




  
