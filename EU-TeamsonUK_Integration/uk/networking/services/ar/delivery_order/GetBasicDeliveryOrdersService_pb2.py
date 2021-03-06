# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/services/ar/delivery_order/GetBasicDeliveryOrdersService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from uk.data.ar.delivery_order import BasicDeliveryOrder_pb2 as uk_dot_data_dot_ar_dot_delivery__order_dot_BasicDeliveryOrder__pb2
from uk.networking.requests.ar.delivery_order import GetBasicDeliveryOrdersRequest_pb2 as uk_dot_networking_dot_requests_dot_ar_dot_delivery__order_dot_GetBasicDeliveryOrdersRequest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/services/ar/delivery_order/GetBasicDeliveryOrdersService.proto',
  package='TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder',
  syntax='proto3',
  serialized_options=b'\n<uk.co.teamson.usability.networking.services.ar.deliveryorderP\001\312\0028TeamsonUK\\Usability\\Networking\\Services\\AR\\DeliveryOrder',
  serialized_pb=b'\nLuk/networking/services/ar/delivery_order/GetBasicDeliveryOrdersService.proto\x12\x38TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder\x1a\x32uk/data/ar/delivery_order/BasicDeliveryOrder.proto\x1aLuk/networking/requests/ar/delivery_order/GetBasicDeliveryOrdersRequest.proto2\xd4\x01\n\x1dGetBasicDeliveryOrdersService\x12\xb2\x01\n\x16GetBasicDeliveryOrders\x12W.TeamsonUK.Usability.Networking.Requests.AR.DeliveryOrder.GetBasicDeliveryOrdersRequest\x1a=.TeamsonUK.Usability.Data.AR.DeliveryOrder.BasicDeliveryOrder0\x01\x42{\n<uk.co.teamson.usability.networking.services.ar.deliveryorderP\x01\xca\x02\x38TeamsonUK\\Usability\\Networking\\Services\\AR\\DeliveryOrderb\x06proto3'
  ,
  dependencies=[uk_dot_data_dot_ar_dot_delivery__order_dot_BasicDeliveryOrder__pb2.DESCRIPTOR,uk_dot_networking_dot_requests_dot_ar_dot_delivery__order_dot_GetBasicDeliveryOrdersRequest__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_GETBASICDELIVERYORDERSSERVICE = _descriptor.ServiceDescriptor(
  name='GetBasicDeliveryOrdersService',
  full_name='TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder.GetBasicDeliveryOrdersService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=269,
  serialized_end=481,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBasicDeliveryOrders',
    full_name='TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder.GetBasicDeliveryOrdersService.GetBasicDeliveryOrders',
    index=0,
    containing_service=None,
    input_type=uk_dot_networking_dot_requests_dot_ar_dot_delivery__order_dot_GetBasicDeliveryOrdersRequest__pb2._GETBASICDELIVERYORDERSREQUEST,
    output_type=uk_dot_data_dot_ar_dot_delivery__order_dot_BasicDeliveryOrder__pb2._BASICDELIVERYORDER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETBASICDELIVERYORDERSSERVICE)

DESCRIPTOR.services_by_name['GetBasicDeliveryOrdersService'] = _GETBASICDELIVERYORDERSSERVICE

# @@protoc_insertion_point(module_scope)
