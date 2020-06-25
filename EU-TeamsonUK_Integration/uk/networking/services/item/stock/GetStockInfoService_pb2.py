# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/services/item/stock/GetStockInfoService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from uk.data.item.stock import ItemStock_pb2 as uk_dot_data_dot_item_dot_stock_dot_ItemStock__pb2
from uk.networking.requests.item.stock import GetStockInfoRequest_pb2 as uk_dot_networking_dot_requests_dot_item_dot_stock_dot_GetStockInfoRequest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/services/item/stock/GetStockInfoService.proto',
  package='TeamsonUK.Usability.Networking.Services.Item.Stock',
  syntax='proto3',
  serialized_options=b'\n6uk.co.teamson.usability.networking.services.item.stock\312\0022TeamsonUK\\Usability\\Networking\\Services\\Item\\Stock',
  serialized_pb=b'\n;uk/networking/services/item/stock/GetStockInfoService.proto\x12\x32TeamsonUK.Usability.Networking.Services.Item.Stock\x1a\"uk/data/item/stock/ItemStock.proto\x1a;uk/networking/requests/item/stock/GetStockInfoRequest.proto2\xa1\x01\n\x13GetStockInfoService\x12\x89\x01\n\x0cGetStockInfo\x12G.TeamsonUK.Usability.Networking.Requests.Item.Stock.GetStockInfoRequest\x1a..TeamsonUK.Usability.Data.Item.Stock.ItemStock0\x01\x42m\n6uk.co.teamson.usability.networking.services.item.stock\xca\x02\x32TeamsonUK\\Usability\\Networking\\Services\\Item\\Stockb\x06proto3'
  ,
  dependencies=[uk_dot_data_dot_item_dot_stock_dot_ItemStock__pb2.DESCRIPTOR,uk_dot_networking_dot_requests_dot_item_dot_stock_dot_GetStockInfoRequest__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_GETSTOCKINFOSERVICE = _descriptor.ServiceDescriptor(
  name='GetStockInfoService',
  full_name='TeamsonUK.Usability.Networking.Services.Item.Stock.GetStockInfoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=213,
  serialized_end=374,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStockInfo',
    full_name='TeamsonUK.Usability.Networking.Services.Item.Stock.GetStockInfoService.GetStockInfo',
    index=0,
    containing_service=None,
    input_type=uk_dot_networking_dot_requests_dot_item_dot_stock_dot_GetStockInfoRequest__pb2._GETSTOCKINFOREQUEST,
    output_type=uk_dot_data_dot_item_dot_stock_dot_ItemStock__pb2._ITEMSTOCK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETSTOCKINFOSERVICE)

DESCRIPTOR.services_by_name['GetStockInfoService'] = _GETSTOCKINFOSERVICE

# @@protoc_insertion_point(module_scope)