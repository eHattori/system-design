from concurrent import futures
import tax_pb2_grpc as pb2_grpc
import tax_pb2 as pb2

import grpc
import random


class TaxService(pb2_grpc.TaxServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetCalculatedPrice(self, request, context):
        price = round(request.price, 2)
        tax = round(random.uniform(1.1, 1.4), 2)

        result = {'price': price * tax, 'tax': tax}

        return pb2.CalculatedTax(**result)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
  pb2_grpc.add_TaxServicer_to_server(TaxService(), server)
  server.add_insecure_port('[::]:50051')
  print('gRPC TaxService run in  [::]:50051')
  server.start()
  server.wait_for_termination()


if __name__ == "__main__":
    serve()
