# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/requests/ar/sales_order/InsertBasicSalesOrderRequest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from uk.data.ar.sales_order import BasicSalesOrder_pb2 as uk_dot_data_dot_ar_dot_sales__order_dot_BasicSalesOrder__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/requests/ar/sales_order/InsertBasicSalesOrderRequest.proto',
  package='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder',
  syntax='proto3',
  serialized_options=b'\n9uk.co.teamson.usability.networking.requests.ar.salesorderP\001\312\0025TeamsonUK\\Usability\\Networking\\Requests\\AR\\SalesOrder',
  serialized_pb=b'\nHuk/networking/requests/ar/sales_order/InsertBasicSalesOrderRequest.proto\x12\x35TeamsonUK.Usability.Networking.Requests.AR.SalesOrder\x1a,uk/data/ar/sales_order/BasicSalesOrder.proto\"p\n\x1cInsertBasicSalesOrderRequest\x12P\n\x0forder_to_insert\x18\x01 \x01(\x0b\x32\x37.TeamsonUK.Usability.Data.AR.SalesOrder.BasicSalesOrderBu\n9uk.co.teamson.usability.networking.requests.ar.salesorderP\x01\xca\x02\x35TeamsonUK\\Usability\\Networking\\Requests\\AR\\SalesOrderb\x06proto3'
  ,
  dependencies=[uk_dot_data_dot_ar_dot_sales__order_dot_BasicSalesOrder__pb2.DESCRIPTOR,])




_INSERTBASICSALESORDERREQUEST = _descriptor.Descriptor(
  name='InsertBasicSalesOrderRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.InsertBasicSalesOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_to_insert', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.InsertBasicSalesOrderRequest.order_to_insert', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=289,
)

_INSERTBASICSALESORDERREQUEST.fields_by_name['order_to_insert'].message_type = uk_dot_data_dot_ar_dot_sales__order_dot_BasicSalesOrder__pb2._BASICSALESORDER
DESCRIPTOR.message_types_by_name['InsertBasicSalesOrderRequest'] = _INSERTBASICSALESORDERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InsertBasicSalesOrderRequest = _reflection.GeneratedProtocolMessageType('InsertBasicSalesOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSERTBASICSALESORDERREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.InsertBasicSalesOrderRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.InsertBasicSalesOrderRequest)
  })
_sym_db.RegisterMessage(InsertBasicSalesOrderRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
