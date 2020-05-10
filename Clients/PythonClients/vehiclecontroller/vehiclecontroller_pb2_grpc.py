# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from vehiclecontroller import vehiclecontroller_pb2 as vehiclecontroller_dot_vehiclecontroller__pb2


class VehicleControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DriveForward = channel.unary_unary(
        '/vehiclecontroller.VehicleController/DriveForward',
        request_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveRequest.SerializeToString,
        response_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveResponse.FromString,
        )
    self.DriveBackward = channel.unary_unary(
        '/vehiclecontroller.VehicleController/DriveBackward',
        request_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveRequest.SerializeToString,
        response_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveResponse.FromString,
        )
    self.SteerRight = channel.unary_unary(
        '/vehiclecontroller.VehicleController/SteerRight',
        request_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerRequest.SerializeToString,
        response_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerResponse.FromString,
        )
    self.SteerLeft = channel.unary_unary(
        '/vehiclecontroller.VehicleController/SteerLeft',
        request_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerRequest.SerializeToString,
        response_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerResponse.FromString,
        )


class VehicleControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DriveForward(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DriveBackward(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SteerRight(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SteerLeft(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VehicleControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DriveForward': grpc.unary_unary_rpc_method_handler(
          servicer.DriveForward,
          request_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveRequest.FromString,
          response_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveResponse.SerializeToString,
      ),
      'DriveBackward': grpc.unary_unary_rpc_method_handler(
          servicer.DriveBackward,
          request_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveRequest.FromString,
          response_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.DriveResponse.SerializeToString,
      ),
      'SteerRight': grpc.unary_unary_rpc_method_handler(
          servicer.SteerRight,
          request_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerRequest.FromString,
          response_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerResponse.SerializeToString,
      ),
      'SteerLeft': grpc.unary_unary_rpc_method_handler(
          servicer.SteerLeft,
          request_deserializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerRequest.FromString,
          response_serializer=vehiclecontroller_dot_vehiclecontroller__pb2.SteerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'vehiclecontroller.VehicleController', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
