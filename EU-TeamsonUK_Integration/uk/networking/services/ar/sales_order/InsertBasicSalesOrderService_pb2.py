# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/services/ar/sales_order/InsertBasicSalesOrderService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from uk.networking.requests.ar.sales_order import InsertBasicSalesOrderRequest_pb2 as uk_dot_networking_dot_requests_dot_ar_dot_sales__order_dot_InsertBasicSalesOrderRequest__pb2
from uk.networking.responses.ar.sales_order import InsertBasicSalesOrderResponse_pb2 as uk_dot_networking_dot_responses_dot_ar_dot_sales__order_dot_InsertBasicSalesOrderResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/services/ar/sales_order/InsertBasicSalesOrderService.proto',
  package='TeamsonUK.Usability.Networking.Services.AR.SalesOrder',
  syntax='proto3',
  serialized_options=b'\n9uk.co.teamson.usability.networking.services.ar.salesorderP\001\312\0025TeamsonUK\\Usability\\Networking\\Services\\AR\\SalesOrder',
  serialized_pb=b'\nHuk/networking/services/ar/sales_order/InsertBasicSalesOrderService.proto\x12\x35TeamsonUK.Usability.Networking.Services.AR.SalesOrder\x1aHuk/networking/requests/ar/sales_order/InsertBasicSalesOrderRequest.proto\x1aJuk/networking/responses/ar/sales_order/InsertBasicSalesOrderResponse.proto2\xe6\x01\n\x1cInsertBasicSalesOrderService\x12\xc5\x01\n\x15InsertBasicSalesOrder\x12S.TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.InsertBasicSalesOrderRequest\x1aU.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.InsertBasicSalesOrderResponse\"\x00\x42u\n9uk.co.teamson.usability.networking.services.ar.salesorderP\x01\xca\x02\x35TeamsonUK\\Usability\\Networking\\Services\\AR\\SalesOrderb\x06proto3'
  ,
  dependencies=[uk_dot_networking_dot_requests_dot_ar_dot_sales__order_dot_InsertBasicSalesOrderRequest__pb2.DESCRIPTOR,uk_dot_networking_dot_responses_dot_ar_dot_sales__order_dot_InsertBasicSalesOrderResponse__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_INSERTBASICSALESORDERSERVICE = _descriptor.ServiceDescriptor(
  name='InsertBasicSalesOrderService',
  full_name='TeamsonUK.Usability.Networking.Services.AR.SalesOrder.InsertBasicSalesOrderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=282,
  serialized_end=512,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertBasicSalesOrder',
    full_name='TeamsonUK.Usability.Networking.Services.AR.SalesOrder.InsertBasicSalesOrderService.InsertBasicSalesOrder',
    index=0,
    containing_service=None,
    input_type=uk_dot_networking_dot_requests_dot_ar_dot_sales__order_dot_InsertBasicSalesOrderRequest__pb2._INSERTBASICSALESORDERREQUEST,
    output_type=uk_dot_networking_dot_responses_dot_ar_dot_sales__order_dot_InsertBasicSalesOrderResponse__pb2._INSERTBASICSALESORDERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSERTBASICSALESORDERSERVICE)

DESCRIPTOR.services_by_name['InsertBasicSalesOrderService'] = _INSERTBASICSALESORDERSERVICE

# @@protoc_insertion_point(module_scope)
