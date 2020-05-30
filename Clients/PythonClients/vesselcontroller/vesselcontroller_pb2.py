# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vesselcontroller/vesselcontroller.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vesselcontroller/vesselcontroller.proto',
  package='vesselcontroller',
  syntax='proto3',
  serialized_options=_b('\n!io.grpc.examples.vesselcontrollerB\020VesselControllerP\001\242\002\003HLW'),
  serialized_pb=_b('\n\'vesselcontroller/vesselcontroller.proto\x12\x10vesselcontroller\"\"\n\x0e\x43ontrolRequest\x12\x10\n\x08throttle\x18\x01 \x01(\x02\"\"\n\x0f\x43ontrolResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xe8\x04\n\x10VesselController\x12P\n\x07\x46orward\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x12Q\n\x08\x42\x61\x63kward\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x12Q\n\x08Portside\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x12R\n\tStarboard\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x12M\n\x04Idle\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x12X\n\x0fRotateClockwise\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x12_\n\x16RotateCounterClockwise\x12 .vesselcontroller.ControlRequest\x1a!.vesselcontroller.ControlResponse\"\x00\x42=\n!io.grpc.examples.vesselcontrollerB\x10VesselControllerP\x01\xa2\x02\x03HLWb\x06proto3')
)




_CONTROLREQUEST = _descriptor.Descriptor(
  name='ControlRequest',
  full_name='vesselcontroller.ControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttle', full_name='vesselcontroller.ControlRequest.throttle', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=61,
  serialized_end=95,
)


_CONTROLRESPONSE = _descriptor.Descriptor(
  name='ControlResponse',
  full_name='vesselcontroller.ControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='vesselcontroller.ControlResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=97,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['ControlRequest'] = _CONTROLREQUEST
DESCRIPTOR.message_types_by_name['ControlResponse'] = _CONTROLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlRequest = _reflection.GeneratedProtocolMessageType('ControlRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLREQUEST,
  '__module__' : 'vesselcontroller.vesselcontroller_pb2'
  # @@protoc_insertion_point(class_scope:vesselcontroller.ControlRequest)
  })
_sym_db.RegisterMessage(ControlRequest)

ControlResponse = _reflection.GeneratedProtocolMessageType('ControlResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLRESPONSE,
  '__module__' : 'vesselcontroller.vesselcontroller_pb2'
  # @@protoc_insertion_point(class_scope:vesselcontroller.ControlResponse)
  })
_sym_db.RegisterMessage(ControlResponse)


DESCRIPTOR._options = None

_VESSELCONTROLLER = _descriptor.ServiceDescriptor(
  name='VesselController',
  full_name='vesselcontroller.VesselController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=134,
  serialized_end=750,
  methods=[
  _descriptor.MethodDescriptor(
    name='Forward',
    full_name='vesselcontroller.VesselController.Forward',
    index=0,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Backward',
    full_name='vesselcontroller.VesselController.Backward',
    index=1,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Portside',
    full_name='vesselcontroller.VesselController.Portside',
    index=2,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Starboard',
    full_name='vesselcontroller.VesselController.Starboard',
    index=3,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Idle',
    full_name='vesselcontroller.VesselController.Idle',
    index=4,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RotateClockwise',
    full_name='vesselcontroller.VesselController.RotateClockwise',
    index=5,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RotateCounterClockwise',
    full_name='vesselcontroller.VesselController.RotateCounterClockwise',
    index=6,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VESSELCONTROLLER)

DESCRIPTOR.services_by_name['VesselController'] = _VESSELCONTROLLER

# @@protoc_insertion_point(module_scope)
