# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/responses/ar/sales_order/GetSalesOrderStatusResponse.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/responses/ar/sales_order/GetSalesOrderStatusResponse.proto',
  package='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder',
  syntax='proto3',
  serialized_options=b'\n:uk.co.teamson.usability.networking.responses.ar.salesorderP\001\312\0026TeamsonUK\\Usability\\Networking\\Responses\\AR\\SalesOrder',
  serialized_pb=b'\nHuk/networking/responses/ar/sales_order/GetSalesOrderStatusResponse.proto\x12\x36TeamsonUK.Usability.Networking.Responses.AR.SalesOrder\"x\n\x1bGetSalesOrderStatusResponse\x12Y\n\x0corder_status\x18\x01 \x01(\x0e\x32\x43.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.OrderStatus\"\xa2\x04\n-BulkGetSalesOrderStatusByCustomerInfoResponse\x12\x9f\x01\n\x19\x63ustomer_order_status_set\x18\x01 \x03(\x0b\x32|.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerOrderStatusSet\x1aJ\n\x0f\x43ustomerInfoSet\x12\x1d\n\x15\x63ustomer_order_number\x18\x01 \x01(\t\x12\x18\n\x10\x62usiness_partner\x18\x02 \x01(\t\x1a\x82\x02\n\x16\x43ustomerOrderStatusSet\x12\x8c\x01\n\rcustomer_info\x18\x01 \x01(\x0b\x32u.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerInfoSet\x12Y\n\x0corder_status\x18\x02 \x01(\x0e\x32\x43.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.OrderStatus\"\xbf\x02\n,BulkGetSalesOrderStatusByOrderNumberResponse\x12\x92\x01\n\x10order_status_map\x18\x01 \x03(\x0b\x32x.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse.OrderStatusMapEntry\x1az\n\x13OrderStatusMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12R\n\x05value\x18\x02 \x01(\x0e\x32\x43.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.OrderStatus:\x02\x38\x01\"\xc3\x02\n.BulkGetSalesOrderStatusByDocumentEntryResponse\x12\x94\x01\n\x10order_status_map\x18\x01 \x03(\x0b\x32z.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse.OrderStatusMapEntry\x1az\n\x13OrderStatusMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12R\n\x05value\x18\x02 \x01(\x0e\x32\x43.TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.OrderStatus:\x02\x38\x01*A\n\x0bOrderStatus\x12\x0e\n\nNOT_EXISTS\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\n\n\x06\x43LOSED\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x42w\n:uk.co.teamson.usability.networking.responses.ar.salesorderP\x01\xca\x02\x36TeamsonUK\\Usability\\Networking\\Responses\\AR\\SalesOrderb\x06proto3'
)

_ORDERSTATUS = _descriptor.EnumDescriptor(
  name='OrderStatus',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.OrderStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_EXISTS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1451,
  serialized_end=1516,
)
_sym_db.RegisterEnumDescriptor(_ORDERSTATUS)

OrderStatus = enum_type_wrapper.EnumTypeWrapper(_ORDERSTATUS)
NOT_EXISTS = 0
OPEN = 1
CLOSED = 2
CANCELED = 3



_GETSALESORDERSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetSalesOrderStatusResponse',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.GetSalesOrderStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_status', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.GetSalesOrderStatusResponse.order_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=132,
  serialized_end=252,
)


_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERINFOSET = _descriptor.Descriptor(
  name='CustomerInfoSet',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerInfoSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_order_number', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerInfoSet.customer_order_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='business_partner', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerInfoSet.business_partner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=466,
  serialized_end=540,
)

_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET = _descriptor.Descriptor(
  name='CustomerOrderStatusSet',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerOrderStatusSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_info', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerOrderStatusSet.customer_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_status', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerOrderStatusSet.order_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=543,
  serialized_end=801,
)

_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE = _descriptor.Descriptor(
  name='BulkGetSalesOrderStatusByCustomerInfoResponse',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_order_status_set', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.customer_order_status_set', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERINFOSET, _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=801,
)


_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY = _descriptor.Descriptor(
  name='OrderStatusMapEntry',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse.OrderStatusMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse.OrderStatusMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse.OrderStatusMapEntry.value', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1001,
  serialized_end=1123,
)

_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE = _descriptor.Descriptor(
  name='BulkGetSalesOrderStatusByOrderNumberResponse',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_status_map', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse.order_status_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=1123,
)


_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY = _descriptor.Descriptor(
  name='OrderStatusMapEntry',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse.OrderStatusMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse.OrderStatusMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse.OrderStatusMapEntry.value', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1001,
  serialized_end=1123,
)

_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE = _descriptor.Descriptor(
  name='BulkGetSalesOrderStatusByDocumentEntryResponse',
  full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_status_map', full_name='TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse.order_status_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1126,
  serialized_end=1449,
)

_GETSALESORDERSTATUSRESPONSE.fields_by_name['order_status'].enum_type = _ORDERSTATUS
_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERINFOSET.containing_type = _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE
_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET.fields_by_name['customer_info'].message_type = _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERINFOSET
_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET.fields_by_name['order_status'].enum_type = _ORDERSTATUS
_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET.containing_type = _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE
_BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE.fields_by_name['customer_order_status_set'].message_type = _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET
_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY.fields_by_name['value'].enum_type = _ORDERSTATUS
_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY.containing_type = _BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE
_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE.fields_by_name['order_status_map'].message_type = _BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY
_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY.fields_by_name['value'].enum_type = _ORDERSTATUS
_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY.containing_type = _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE
_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE.fields_by_name['order_status_map'].message_type = _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY
DESCRIPTOR.message_types_by_name['GetSalesOrderStatusResponse'] = _GETSALESORDERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['BulkGetSalesOrderStatusByCustomerInfoResponse'] = _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE
DESCRIPTOR.message_types_by_name['BulkGetSalesOrderStatusByOrderNumberResponse'] = _BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE
DESCRIPTOR.message_types_by_name['BulkGetSalesOrderStatusByDocumentEntryResponse'] = _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE
DESCRIPTOR.enum_types_by_name['OrderStatus'] = _ORDERSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSalesOrderStatusResponse = _reflection.GeneratedProtocolMessageType('GetSalesOrderStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSALESORDERSTATUSRESPONSE,
  '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.GetSalesOrderStatusResponse)
  })
_sym_db.RegisterMessage(GetSalesOrderStatusResponse)

BulkGetSalesOrderStatusByCustomerInfoResponse = _reflection.GeneratedProtocolMessageType('BulkGetSalesOrderStatusByCustomerInfoResponse', (_message.Message,), {

  'CustomerInfoSet' : _reflection.GeneratedProtocolMessageType('CustomerInfoSet', (_message.Message,), {
    'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERINFOSET,
    '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
    # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerInfoSet)
    })
  ,

  'CustomerOrderStatusSet' : _reflection.GeneratedProtocolMessageType('CustomerOrderStatusSet', (_message.Message,), {
    'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE_CUSTOMERORDERSTATUSSET,
    '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
    # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerOrderStatusSet)
    })
  ,
  'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYCUSTOMERINFORESPONSE,
  '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoResponse)
  })
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByCustomerInfoResponse)
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerInfoSet)
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByCustomerInfoResponse.CustomerOrderStatusSet)

BulkGetSalesOrderStatusByOrderNumberResponse = _reflection.GeneratedProtocolMessageType('BulkGetSalesOrderStatusByOrderNumberResponse', (_message.Message,), {

  'OrderStatusMapEntry' : _reflection.GeneratedProtocolMessageType('OrderStatusMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY,
    '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
    # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse.OrderStatusMapEntry)
    })
  ,
  'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE,
  '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberResponse)
  })
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByOrderNumberResponse)
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByOrderNumberResponse.OrderStatusMapEntry)

BulkGetSalesOrderStatusByDocumentEntryResponse = _reflection.GeneratedProtocolMessageType('BulkGetSalesOrderStatusByDocumentEntryResponse', (_message.Message,), {

  'OrderStatusMapEntry' : _reflection.GeneratedProtocolMessageType('OrderStatusMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY,
    '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
    # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse.OrderStatusMapEntry)
    })
  ,
  'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE,
  '__module__' : 'uk.networking.responses.ar.sales_order.GetSalesOrderStatusResponse_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Responses.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryResponse)
  })
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByDocumentEntryResponse)
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByDocumentEntryResponse.OrderStatusMapEntry)


DESCRIPTOR._options = None
_BULKGETSALESORDERSTATUSBYORDERNUMBERRESPONSE_ORDERSTATUSMAPENTRY._options = None
_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYRESPONSE_ORDERSTATUSMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
