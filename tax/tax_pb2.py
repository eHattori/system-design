# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tax.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttax.proto\x12\x03tax\"\x18\n\x07Product\x12\r\n\x05price\x18\x01 \x01(\x02\"+\n\rCalculatedTax\x12\r\n\x05price\x18\x01 \x01(\x02\x12\x0b\n\x03tax\x18\x02 \x01(\x02\x32=\n\x03Tax\x12\x36\n\x12GetCalculatedPrice\x12\x0c.tax.Product\x1a\x12.tax.CalculatedTaxb\x06proto3')



_PRODUCT = DESCRIPTOR.message_types_by_name['Product']
_CALCULATEDTAX = DESCRIPTOR.message_types_by_name['CalculatedTax']
Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'tax_pb2'
  # @@protoc_insertion_point(class_scope:tax.Product)
  })
_sym_db.RegisterMessage(Product)

CalculatedTax = _reflection.GeneratedProtocolMessageType('CalculatedTax', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATEDTAX,
  '__module__' : 'tax_pb2'
  # @@protoc_insertion_point(class_scope:tax.CalculatedTax)
  })
_sym_db.RegisterMessage(CalculatedTax)

_TAX = DESCRIPTOR.services_by_name['Tax']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCT._serialized_start=18
  _PRODUCT._serialized_end=42
  _CALCULATEDTAX._serialized_start=44
  _CALCULATEDTAX._serialized_end=87
  _TAX._serialized_start=89
  _TAX._serialized_end=150
# @@protoc_insertion_point(module_scope)