from flask.cli import load_dotenv
import grpc
from concurrent import futures
import os
import archivo_pb2
import archivo_pb2_grpc

load_dotenv()

MICSERVER1_PORT = os.getenv("MICSERVER1_PORT")

class ArchivoServicer(archivo_pb2_grpc.ArchivoServicer):
    def ListarArchivos(self, request, context):
        # Directorio que quieres listar
        directorio = "./files"
        
        try:
            archivos = os.listdir(directorio)
        except Exception as e:
            # Manejar errores en caso de que el directorio no se pueda acceder, etc.
            return archivo_pb2.ArchivoLista(archivos=[])

        return archivo_pb2.ArchivoLista(archivos=archivos)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    archivo_pb2_grpc.add_ArchivoServicer_to_server(ArchivoServicer(), server)
    server.add_insecure_port(f'[::]:{MICSERVER1_PORT}')
    server.start()
    print(f"Microservicio mserv1 escuchando en el {MICSERVER1_PORT}...")
    server.wait_for_termination()

if __name__ == '__main__':
    main()