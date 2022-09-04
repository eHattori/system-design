import tax_pb2_grpc as pb2_grpc 
import tax_pb2 as pb2 

import os

import grpc

class TaxClient():

  def __init__(self) -> None:
      self.host = os.getenv('RPC_HOST', 'localhost')
      self.server_port = 50051

      self.channel = grpc.insecure_channel(
          f'{self.host}:{self.server_port}'
      )

      self.stub = pb2_grpc.TaxStub(self.channel)

  def get_calculated_price(self, price):
    product_price = pb2.Product(price=price)
    print(f'Calculating a price: {price}')
    return self.stub.GetCalculatedPrice(product_price)

if __name__ == '__main__':
  client = TaxClient()
  result = client.get_calculated_price(10)
  print(f'{result}')

