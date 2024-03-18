# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RpcHeader.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fRpcHeader.proto\x12\rhadoop.common\"\xa2\x02\n\x15RpcRequestHeaderProto\x12,\n\x07rpcKind\x18\x01 \x01(\x0e\x32\x1b.hadoop.common.RpcKindProto\x12\x42\n\x05rpcOp\x18\x02 \x01(\x0e\x32\x33.hadoop.common.RpcRequestHeaderProto.OperationProto\x12\x0e\n\x06\x63\x61llId\x18\x03 \x02(\x11\x12\x10\n\x08\x63lientId\x18\x04 \x02(\x0c\x12\x16\n\nretryCount\x18\x05 \x01(\x11:\x02-1\"]\n\x0eOperationProto\x12\x14\n\x10RPC_FINAL_PACKET\x10\x00\x12\x1b\n\x17RPC_CONTINUATION_PACKET\x10\x01\x12\x18\n\x14RPC_CLOSE_CONNECTION\x10\x02\"\xca\x05\n\x16RpcResponseHeaderProto\x12\x0e\n\x06\x63\x61llId\x18\x01 \x02(\r\x12\x44\n\x06status\x18\x02 \x02(\x0e\x32\x34.hadoop.common.RpcResponseHeaderProto.RpcStatusProto\x12\x1b\n\x13serverIpcVersionNum\x18\x03 \x01(\r\x12\x1a\n\x12\x65xceptionClassName\x18\x04 \x01(\t\x12\x10\n\x08\x65rrorMsg\x18\x05 \x01(\t\x12L\n\x0b\x65rrorDetail\x18\x06 \x01(\x0e\x32\x37.hadoop.common.RpcResponseHeaderProto.RpcErrorCodeProto\x12\x10\n\x08\x63lientId\x18\x07 \x01(\x0c\x12\x16\n\nretryCount\x18\x08 \x01(\x11:\x02-1\"3\n\x0eRpcStatusProto\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\t\n\x05\x46\x41TAL\x10\x02\"\xe1\x02\n\x11RpcErrorCodeProto\x12\x15\n\x11\x45RROR_APPLICATION\x10\x01\x12\x18\n\x14\x45RROR_NO_SUCH_METHOD\x10\x02\x12\x1a\n\x16\x45RROR_NO_SUCH_PROTOCOL\x10\x03\x12\x14\n\x10\x45RROR_RPC_SERVER\x10\x04\x12\x1e\n\x1a\x45RROR_SERIALIZING_RESPONSE\x10\x05\x12\x1e\n\x1a\x45RROR_RPC_VERSION_MISMATCH\x10\x06\x12\x11\n\rFATAL_UNKNOWN\x10\n\x12#\n\x1f\x46\x41TAL_UNSUPPORTED_SERIALIZATION\x10\x0b\x12\x1c\n\x18\x46\x41TAL_INVALID_RPC_HEADER\x10\x0c\x12\x1f\n\x1b\x46\x41TAL_DESERIALIZING_REQUEST\x10\r\x12\x1a\n\x16\x46\x41TAL_VERSION_MISMATCH\x10\x0e\x12\x16\n\x12\x46\x41TAL_UNAUTHORIZED\x10\x0f\"\xdd\x02\n\x0cRpcSaslProto\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x34\n\x05state\x18\x02 \x02(\x0e\x32%.hadoop.common.RpcSaslProto.SaslState\x12\r\n\x05token\x18\x03 \x01(\x0c\x12\x33\n\x05\x61uths\x18\x04 \x03(\x0b\x32$.hadoop.common.RpcSaslProto.SaslAuth\x1a\x64\n\x08SaslAuth\x12\x0e\n\x06method\x18\x01 \x02(\t\x12\x11\n\tmechanism\x18\x02 \x02(\t\x12\x10\n\x08protocol\x18\x03 \x01(\t\x12\x10\n\x08serverId\x18\x04 \x01(\t\x12\x11\n\tchallenge\x18\x05 \x01(\x0c\"\\\n\tSaslState\x12\x0b\n\x07SUCCESS\x10\x00\x12\r\n\tNEGOTIATE\x10\x01\x12\x0c\n\x08INITIATE\x10\x02\x12\r\n\tCHALLENGE\x10\x03\x12\x0c\n\x08RESPONSE\x10\x04\x12\x08\n\x04WRAP\x10\x05*J\n\x0cRpcKindProto\x12\x0f\n\x0bRPC_BUILTIN\x10\x00\x12\x10\n\x0cRPC_WRITABLE\x10\x01\x12\x17\n\x13RPC_PROTOCOL_BUFFER\x10\x02\x42\x34\n\x1eorg.apache.hadoop.ipc.protobufB\x0fRpcHeaderProtos\xa0\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RpcHeader_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036org.apache.hadoop.ipc.protobufB\017RpcHeaderProtos\240\001\001'
  _globals['_RPCKINDPROTO']._serialized_start=1396
  _globals['_RPCKINDPROTO']._serialized_end=1470
  _globals['_RPCREQUESTHEADERPROTO']._serialized_start=35
  _globals['_RPCREQUESTHEADERPROTO']._serialized_end=325
  _globals['_RPCREQUESTHEADERPROTO_OPERATIONPROTO']._serialized_start=232
  _globals['_RPCREQUESTHEADERPROTO_OPERATIONPROTO']._serialized_end=325
  _globals['_RPCRESPONSEHEADERPROTO']._serialized_start=328
  _globals['_RPCRESPONSEHEADERPROTO']._serialized_end=1042
  _globals['_RPCRESPONSEHEADERPROTO_RPCSTATUSPROTO']._serialized_start=635
  _globals['_RPCRESPONSEHEADERPROTO_RPCSTATUSPROTO']._serialized_end=686
  _globals['_RPCRESPONSEHEADERPROTO_RPCERRORCODEPROTO']._serialized_start=689
  _globals['_RPCRESPONSEHEADERPROTO_RPCERRORCODEPROTO']._serialized_end=1042
  _globals['_RPCSASLPROTO']._serialized_start=1045
  _globals['_RPCSASLPROTO']._serialized_end=1394
  _globals['_RPCSASLPROTO_SASLAUTH']._serialized_start=1200
  _globals['_RPCSASLPROTO_SASLAUTH']._serialized_end=1300
  _globals['_RPCSASLPROTO_SASLSTATE']._serialized_start=1302
  _globals['_RPCSASLPROTO_SASLSTATE']._serialized_end=1394
# @@protoc_insertion_point(module_scope)
