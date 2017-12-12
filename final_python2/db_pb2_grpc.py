# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import db_pb2 as db__pb2


class DBStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.put = channel.unary_unary(
        '/DB/put',
        request_serializer=db__pb2.PutRequest.SerializeToString,
        response_deserializer=db__pb2.PutResponse.FromString,
        )
    self.get = channel.unary_unary(
        '/DB/get',
        request_serializer=db__pb2.GetRequest.SerializeToString,
        response_deserializer=db__pb2.GetResponse.FromString,
        )
    self.info = channel.unary_unary(
        '/DB/info',
        request_serializer=db__pb2.Empty.SerializeToString,
        response_deserializer=db__pb2.InfoResponse.FromString,
        )


class DBServicer(object):

  def put(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def info(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'put': grpc.unary_unary_rpc_method_handler(
          servicer.put,
          request_deserializer=db__pb2.PutRequest.FromString,
          response_serializer=db__pb2.PutResponse.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=db__pb2.GetRequest.FromString,
          response_serializer=db__pb2.GetResponse.SerializeToString,
      ),
      'info': grpc.unary_unary_rpc_method_handler(
          servicer.info,
          request_deserializer=db__pb2.Empty.FromString,
          response_serializer=db__pb2.InfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))