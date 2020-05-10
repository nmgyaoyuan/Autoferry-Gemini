# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehiclecontroller/vehiclecontroller.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vehiclecontroller/vehiclecontroller.proto',
  package='vehiclecontroller',
  syntax='proto3',
  serialized_options=_b('\n\"io.grpc.examples.vehiclecontrollerB\021VehicleControllerP\001\242\002\003HLW'),
  serialized_pb=_b('\n)vehiclecontroller/vehiclecontroller.proto\x12\x11vehiclecontroller\"\x1d\n\x0c\x44riveRequest\x12\r\n\x05value\x18\x01 \x01(\x02\" \n\rDriveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1d\n\x0cSteerRequest\x12\r\n\x05value\x18\x01 \x01(\x02\" \n\rSteerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xe3\x02\n\x11VehicleController\x12S\n\x0c\x44riveForward\x12\x1f.vehiclecontroller.DriveRequest\x1a .vehiclecontroller.DriveResponse\"\x00\x12T\n\rDriveBackward\x12\x1f.vehiclecontroller.DriveRequest\x1a .vehiclecontroller.DriveResponse\"\x00\x12Q\n\nSteerRight\x12\x1f.vehiclecontroller.SteerRequest\x1a .vehiclecontroller.SteerResponse\"\x00\x12P\n\tSteerLeft\x12\x1f.vehiclecontroller.SteerRequest\x1a .vehiclecontroller.SteerResponse\"\x00\x42?\n\"io.grpc.examples.vehiclecontrollerB\x11VehicleControllerP\x01\xa2\x02\x03HLWb\x06proto3')
)




_DRIVEREQUEST = _descriptor.Descriptor(
  name='DriveRequest',
  full_name='vehiclecontroller.DriveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='vehiclecontroller.DriveRequest.value', index=0,
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
  serialized_start=64,
  serialized_end=93,
)


_DRIVERESPONSE = _descriptor.Descriptor(
  name='DriveResponse',
  full_name='vehiclecontroller.DriveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='vehiclecontroller.DriveResponse.success', index=0,
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
  serialized_start=95,
  serialized_end=127,
)


_STEERREQUEST = _descriptor.Descriptor(
  name='SteerRequest',
  full_name='vehiclecontroller.SteerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='vehiclecontroller.SteerRequest.value', index=0,
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
  serialized_start=129,
  serialized_end=158,
)


_STEERRESPONSE = _descriptor.Descriptor(
  name='SteerResponse',
  full_name='vehiclecontroller.SteerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='vehiclecontroller.SteerResponse.success', index=0,
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
  serialized_start=160,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['DriveRequest'] = _DRIVEREQUEST
DESCRIPTOR.message_types_by_name['DriveResponse'] = _DRIVERESPONSE
DESCRIPTOR.message_types_by_name['SteerRequest'] = _STEERREQUEST
DESCRIPTOR.message_types_by_name['SteerResponse'] = _STEERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DriveRequest = _reflection.GeneratedProtocolMessageType('DriveRequest', (_message.Message,), {
  'DESCRIPTOR' : _DRIVEREQUEST,
  '__module__' : 'vehiclecontroller.vehiclecontroller_pb2'
  # @@protoc_insertion_point(class_scope:vehiclecontroller.DriveRequest)
  })
_sym_db.RegisterMessage(DriveRequest)

DriveResponse = _reflection.GeneratedProtocolMessageType('DriveResponse', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERESPONSE,
  '__module__' : 'vehiclecontroller.vehiclecontroller_pb2'
  # @@protoc_insertion_point(class_scope:vehiclecontroller.DriveResponse)
  })
_sym_db.RegisterMessage(DriveResponse)

SteerRequest = _reflection.GeneratedProtocolMessageType('SteerRequest', (_message.Message,), {
  'DESCRIPTOR' : _STEERREQUEST,
  '__module__' : 'vehiclecontroller.vehiclecontroller_pb2'
  # @@protoc_insertion_point(class_scope:vehiclecontroller.SteerRequest)
  })
_sym_db.RegisterMessage(SteerRequest)

SteerResponse = _reflection.GeneratedProtocolMessageType('SteerResponse', (_message.Message,), {
  'DESCRIPTOR' : _STEERRESPONSE,
  '__module__' : 'vehiclecontroller.vehiclecontroller_pb2'
  # @@protoc_insertion_point(class_scope:vehiclecontroller.SteerResponse)
  })
_sym_db.RegisterMessage(SteerResponse)


DESCRIPTOR._options = None

_VEHICLECONTROLLER = _descriptor.ServiceDescriptor(
  name='VehicleController',
  full_name='vehiclecontroller.VehicleController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=195,
  serialized_end=550,
  methods=[
  _descriptor.MethodDescriptor(
    name='DriveForward',
    full_name='vehiclecontroller.VehicleController.DriveForward',
    index=0,
    containing_service=None,
    input_type=_DRIVEREQUEST,
    output_type=_DRIVERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DriveBackward',
    full_name='vehiclecontroller.VehicleController.DriveBackward',
    index=1,
    containing_service=None,
    input_type=_DRIVEREQUEST,
    output_type=_DRIVERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SteerRight',
    full_name='vehiclecontroller.VehicleController.SteerRight',
    index=2,
    containing_service=None,
    input_type=_STEERREQUEST,
    output_type=_STEERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SteerLeft',
    full_name='vehiclecontroller.VehicleController.SteerLeft',
    index=3,
    containing_service=None,
    input_type=_STEERREQUEST,
    output_type=_STEERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VEHICLECONTROLLER)

DESCRIPTOR.services_by_name['VehicleController'] = _VEHICLECONTROLLER

# @@protoc_insertion_point(module_scope)
