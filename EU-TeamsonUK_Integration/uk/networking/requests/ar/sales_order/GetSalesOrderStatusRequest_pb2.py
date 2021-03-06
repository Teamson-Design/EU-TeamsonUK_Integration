# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/requests/ar/sales_order/GetSalesOrderStatusRequest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/requests/ar/sales_order/GetSalesOrderStatusRequest.proto',
  package='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder',
  syntax='proto3',
  serialized_options=b'\n9uk.co.teamson.usability.networking.requests.ar.salesorderP\001\312\0025TeamsonUK\\Usability\\Networking\\Requests\\AR\\SalesOrder',
  serialized_pb=b'\nFuk/networking/requests/ar/sales_order/GetSalesOrderStatusRequest.proto\x12\x35TeamsonUK.Usability.Networking.Requests.AR.SalesOrder\"?\n\'GetSalesOrderStatusByOrderNumberRequest\x12\x14\n\x0corder_number\x18\x01 \x01(\t\"C\n)GetSalesOrderStatusByDocumentEntryRequest\x12\x16\n\x0e\x64ocument_entry\x18\x02 \x01(\t\"c\n(GetSalesOrderStatusByCustomerInfoRequest\x12\x18\n\x10\x62usiness_partner\x18\x01 \x01(\t\x12\x1d\n\x15\x63ustomer_order_number\x18\x02 \x01(\t\"D\n+BulkGetSalesOrderStatusByOrderNumberRequest\x12\x15\n\rorder_numbers\x18\x01 \x03(\t\"I\n-BulkGetSalesOrderStatusByDocumentEntryRequest\x12\x18\n\x10\x64ocument_entries\x18\x01 \x03(\t\"\x87\x02\n,BulkGetSalesOrderStatusByCustomerInfoRequest\x12\x8a\x01\n\rcustomer_sets\x18\x01 \x03(\x0b\x32s.TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest.CustomerInfoSet\x1aJ\n\x0f\x43ustomerInfoSet\x12\x1d\n\x15\x63ustomer_order_number\x18\x01 \x01(\t\x12\x18\n\x10\x62usiness_partner\x18\x02 \x01(\tBu\n9uk.co.teamson.usability.networking.requests.ar.salesorderP\x01\xca\x02\x35TeamsonUK\\Usability\\Networking\\Requests\\AR\\SalesOrderb\x06proto3'
)




_GETSALESORDERSTATUSBYORDERNUMBERREQUEST = _descriptor.Descriptor(
  name='GetSalesOrderStatusByOrderNumberRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByOrderNumberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_number', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByOrderNumberRequest.order_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=129,
  serialized_end=192,
)


_GETSALESORDERSTATUSBYDOCUMENTENTRYREQUEST = _descriptor.Descriptor(
  name='GetSalesOrderStatusByDocumentEntryRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByDocumentEntryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document_entry', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByDocumentEntryRequest.document_entry', index=0,
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
  serialized_start=194,
  serialized_end=261,
)


_GETSALESORDERSTATUSBYCUSTOMERINFOREQUEST = _descriptor.Descriptor(
  name='GetSalesOrderStatusByCustomerInfoRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByCustomerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='business_partner', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByCustomerInfoRequest.business_partner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_order_number', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByCustomerInfoRequest.customer_order_number', index=1,
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
  serialized_start=263,
  serialized_end=362,
)


_BULKGETSALESORDERSTATUSBYORDERNUMBERREQUEST = _descriptor.Descriptor(
  name='BulkGetSalesOrderStatusByOrderNumberRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_numbers', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberRequest.order_numbers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=364,
  serialized_end=432,
)


_BULKGETSALESORDERSTATUSBYDOCUMENTENTRYREQUEST = _descriptor.Descriptor(
  name='BulkGetSalesOrderStatusByDocumentEntryRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document_entries', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryRequest.document_entries', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=434,
  serialized_end=507,
)


_BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST_CUSTOMERINFOSET = _descriptor.Descriptor(
  name='CustomerInfoSet',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest.CustomerInfoSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_order_number', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest.CustomerInfoSet.customer_order_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='business_partner', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest.CustomerInfoSet.business_partner', index=1,
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
  serialized_start=699,
  serialized_end=773,
)

_BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST = _descriptor.Descriptor(
  name='BulkGetSalesOrderStatusByCustomerInfoRequest',
  full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_sets', full_name='TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest.customer_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST_CUSTOMERINFOSET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=773,
)

_BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST_CUSTOMERINFOSET.containing_type = _BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST
_BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST.fields_by_name['customer_sets'].message_type = _BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST_CUSTOMERINFOSET
DESCRIPTOR.message_types_by_name['GetSalesOrderStatusByOrderNumberRequest'] = _GETSALESORDERSTATUSBYORDERNUMBERREQUEST
DESCRIPTOR.message_types_by_name['GetSalesOrderStatusByDocumentEntryRequest'] = _GETSALESORDERSTATUSBYDOCUMENTENTRYREQUEST
DESCRIPTOR.message_types_by_name['GetSalesOrderStatusByCustomerInfoRequest'] = _GETSALESORDERSTATUSBYCUSTOMERINFOREQUEST
DESCRIPTOR.message_types_by_name['BulkGetSalesOrderStatusByOrderNumberRequest'] = _BULKGETSALESORDERSTATUSBYORDERNUMBERREQUEST
DESCRIPTOR.message_types_by_name['BulkGetSalesOrderStatusByDocumentEntryRequest'] = _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYREQUEST
DESCRIPTOR.message_types_by_name['BulkGetSalesOrderStatusByCustomerInfoRequest'] = _BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSalesOrderStatusByOrderNumberRequest = _reflection.GeneratedProtocolMessageType('GetSalesOrderStatusByOrderNumberRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSALESORDERSTATUSBYORDERNUMBERREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByOrderNumberRequest)
  })
_sym_db.RegisterMessage(GetSalesOrderStatusByOrderNumberRequest)

GetSalesOrderStatusByDocumentEntryRequest = _reflection.GeneratedProtocolMessageType('GetSalesOrderStatusByDocumentEntryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSALESORDERSTATUSBYDOCUMENTENTRYREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByDocumentEntryRequest)
  })
_sym_db.RegisterMessage(GetSalesOrderStatusByDocumentEntryRequest)

GetSalesOrderStatusByCustomerInfoRequest = _reflection.GeneratedProtocolMessageType('GetSalesOrderStatusByCustomerInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSALESORDERSTATUSBYCUSTOMERINFOREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.GetSalesOrderStatusByCustomerInfoRequest)
  })
_sym_db.RegisterMessage(GetSalesOrderStatusByCustomerInfoRequest)

BulkGetSalesOrderStatusByOrderNumberRequest = _reflection.GeneratedProtocolMessageType('BulkGetSalesOrderStatusByOrderNumberRequest', (_message.Message,), {
  'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYORDERNUMBERREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByOrderNumberRequest)
  })
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByOrderNumberRequest)

BulkGetSalesOrderStatusByDocumentEntryRequest = _reflection.GeneratedProtocolMessageType('BulkGetSalesOrderStatusByDocumentEntryRequest', (_message.Message,), {
  'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYDOCUMENTENTRYREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByDocumentEntryRequest)
  })
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByDocumentEntryRequest)

BulkGetSalesOrderStatusByCustomerInfoRequest = _reflection.GeneratedProtocolMessageType('BulkGetSalesOrderStatusByCustomerInfoRequest', (_message.Message,), {

  'CustomerInfoSet' : _reflection.GeneratedProtocolMessageType('CustomerInfoSet', (_message.Message,), {
    'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST_CUSTOMERINFOSET,
    '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
    # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest.CustomerInfoSet)
    })
  ,
  'DESCRIPTOR' : _BULKGETSALESORDERSTATUSBYCUSTOMERINFOREQUEST,
  '__module__' : 'uk.networking.requests.ar.sales_order.GetSalesOrderStatusRequest_pb2'
  # @@protoc_insertion_point(class_scope:TeamsonUK.Usability.Networking.Requests.AR.SalesOrder.BulkGetSalesOrderStatusByCustomerInfoRequest)
  })
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByCustomerInfoRequest)
_sym_db.RegisterMessage(BulkGetSalesOrderStatusByCustomerInfoRequest.CustomerInfoSet)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
