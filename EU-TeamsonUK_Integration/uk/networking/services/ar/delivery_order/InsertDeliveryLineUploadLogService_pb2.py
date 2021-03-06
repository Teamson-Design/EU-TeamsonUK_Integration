# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uk/networking/services/ar/delivery_order/InsertDeliveryLineUploadLogService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from uk.networking.requests.ar.delivery_order import InsertDeliveryLineUploadLogRequest_pb2 as uk_dot_networking_dot_requests_dot_ar_dot_delivery__order_dot_InsertDeliveryLineUploadLogRequest__pb2
from uk.networking.responses.ar.delivery_order import InsertDeliveryLineUploadLogResponse_pb2 as uk_dot_networking_dot_responses_dot_ar_dot_delivery__order_dot_InsertDeliveryLineUploadLogResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uk/networking/services/ar/delivery_order/InsertDeliveryLineUploadLogService.proto',
  package='TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder',
  syntax='proto3',
  serialized_options=b'\n<uk.co.teamson.usability.networking.services.ar.deliveryorderP\001\312\0028TeamsonUK\\Usability\\Networking\\Services\\AR\\DeliveryOrder',
  serialized_pb=b'\nQuk/networking/services/ar/delivery_order/InsertDeliveryLineUploadLogService.proto\x12\x38TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder\x1aQuk/networking/requests/ar/delivery_order/InsertDeliveryLineUploadLogRequest.proto\x1aSuk/networking/responses/ar/delivery_order/InsertDeliveryLineUploadLogResponse.proto2\x84\x02\n\"InsertDeliveryLineUploadLogService\x12\xdd\x01\n\x1bInsertDeliveryLineUploadLog\x12\\.TeamsonUK.Usability.Networking.Requests.AR.DeliveryOrder.InsertDeliveryLineUploadLogRequest\x1a^.TeamsonUK.Usability.Networking.Responses.AR.DeliveryOrder.InsertDeliveryLineUploadLogResponse\"\x00\x42{\n<uk.co.teamson.usability.networking.services.ar.deliveryorderP\x01\xca\x02\x38TeamsonUK\\Usability\\Networking\\Services\\AR\\DeliveryOrderb\x06proto3'
  ,
  dependencies=[uk_dot_networking_dot_requests_dot_ar_dot_delivery__order_dot_InsertDeliveryLineUploadLogRequest__pb2.DESCRIPTOR,uk_dot_networking_dot_responses_dot_ar_dot_delivery__order_dot_InsertDeliveryLineUploadLogResponse__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_INSERTDELIVERYLINEUPLOADLOGSERVICE = _descriptor.ServiceDescriptor(
  name='InsertDeliveryLineUploadLogService',
  full_name='TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder.InsertDeliveryLineUploadLogService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=312,
  serialized_end=572,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertDeliveryLineUploadLog',
    full_name='TeamsonUK.Usability.Networking.Services.AR.DeliveryOrder.InsertDeliveryLineUploadLogService.InsertDeliveryLineUploadLog',
    index=0,
    containing_service=None,
    input_type=uk_dot_networking_dot_requests_dot_ar_dot_delivery__order_dot_InsertDeliveryLineUploadLogRequest__pb2._INSERTDELIVERYLINEUPLOADLOGREQUEST,
    output_type=uk_dot_networking_dot_responses_dot_ar_dot_delivery__order_dot_InsertDeliveryLineUploadLogResponse__pb2._INSERTDELIVERYLINEUPLOADLOGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSERTDELIVERYLINEUPLOADLOGSERVICE)

DESCRIPTOR.services_by_name['InsertDeliveryLineUploadLogService'] = _INSERTDELIVERYLINEUPLOADLOGSERVICE

# @@protoc_insertion_point(module_scope)
