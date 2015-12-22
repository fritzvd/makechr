# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: valiant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='valiant.proto',
  package='valiant',
  serialized_pb=_b('\n\rvaliant.proto\x12\x07valiant\"v\n\nObjectFile\x12\x0e\n\x06magic1\x18\x05 \x01(\x05\x12\x0e\n\x06magic2\x18\x08 \x01(\x06\x12%\n\x06header\x18\r \x01(\x0b\x32\x15.valiant.ObjectHeader\x12!\n\x04\x64\x61ta\x18\x0e \x01(\x0b\x32\x13.valiant.ObjectData\"\x1e\n\x0cObjectHeader\x12\x0e\n\x06module\x18\x01 \x01(\t\"\x88\x01\n\nObjectData\x12\'\n\x08\x62inaries\x18\x01 \x03(\x0b\x32\x15.valiant.DirectBinary\x12&\n\x08settings\x18\x02 \x01(\x0b\x32\x14.valiant.GfxSettings\x12)\n\ncomponents\x18\x03 \x03(\x0b\x32\x15.valiant.GfxComponent\"K\n\x0bGfxSettings\x12\x10\n\x08\x62g_color\x18\x01 \x01(\x05\x12*\n\x0c\x63hr_metadata\x18\x05 \x03(\x0b\x32\x14.valiant.ChrMetadata\"S\n\x0cGfxComponent\x12\x1f\n\x04role\x18\x01 \x01(\x0e\x32\x11.valiant.DataRole\x12\x14\n\x0c\x62inary_index\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"j\n\x0b\x43hrMetadata\x12\r\n\x05order\x18\x01 \x01(\x05\x12\x12\n\nsorted_idx\x18\x02 \x03(\x05\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x17\n\x0fis_locked_tiles\x18\x04 \x01(\x05\x12\x11\n\ttraversal\x18\x05 \x01(\t\"Q\n\x0c\x44irectBinary\x12\x0b\n\x03\x62in\x18\x01 \x01(\x0c\x12\x0f\n\x07padding\x18\x02 \x01(\x05\x12\x0f\n\x07pre_pad\x18\x03 \x01(\x05\x12\x12\n\nnull_value\x18\x04 \x01(\x05*X\n\x08\x44\x61taRole\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03\x43HR\x10\x01\x12\r\n\tNAMETABLE\x10\x02\x12\r\n\tATTRIBUTE\x10\x03\x12\x0b\n\x07PALETTE\x10\x04\x12\x0e\n\nSPRITELIST\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DATAROLE = _descriptor.EnumDescriptor(
  name='DataRole',
  full_name='valiant.DataRole',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAMETABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTRIBUTE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PALETTE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPRITELIST', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=670,
  serialized_end=758,
)
_sym_db.RegisterEnumDescriptor(_DATAROLE)

DataRole = enum_type_wrapper.EnumTypeWrapper(_DATAROLE)
NONE = 0
CHR = 1
NAMETABLE = 2
ATTRIBUTE = 3
PALETTE = 4
SPRITELIST = 5



_OBJECTFILE = _descriptor.Descriptor(
  name='ObjectFile',
  full_name='valiant.ObjectFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='magic1', full_name='valiant.ObjectFile.magic1', index=0,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic2', full_name='valiant.ObjectFile.magic2', index=1,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='valiant.ObjectFile.header', index=2,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='valiant.ObjectFile.data', index=3,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=144,
)


_OBJECTHEADER = _descriptor.Descriptor(
  name='ObjectHeader',
  full_name='valiant.ObjectHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='valiant.ObjectHeader.module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=176,
)


_OBJECTDATA = _descriptor.Descriptor(
  name='ObjectData',
  full_name='valiant.ObjectData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaries', full_name='valiant.ObjectData.binaries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settings', full_name='valiant.ObjectData.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='components', full_name='valiant.ObjectData.components', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=315,
)


_GFXSETTINGS = _descriptor.Descriptor(
  name='GfxSettings',
  full_name='valiant.GfxSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bg_color', full_name='valiant.GfxSettings.bg_color', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chr_metadata', full_name='valiant.GfxSettings.chr_metadata', index=1,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=392,
)


_GFXCOMPONENT = _descriptor.Descriptor(
  name='GfxComponent',
  full_name='valiant.GfxComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='valiant.GfxComponent.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_index', full_name='valiant.GfxComponent.binary_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='valiant.GfxComponent.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=477,
)


_CHRMETADATA = _descriptor.Descriptor(
  name='ChrMetadata',
  full_name='valiant.ChrMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order', full_name='valiant.ChrMetadata.order', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorted_idx', full_name='valiant.ChrMetadata.sorted_idx', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='valiant.ChrMetadata.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_locked_tiles', full_name='valiant.ChrMetadata.is_locked_tiles', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traversal', full_name='valiant.ChrMetadata.traversal', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=585,
)


_DIRECTBINARY = _descriptor.Descriptor(
  name='DirectBinary',
  full_name='valiant.DirectBinary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bin', full_name='valiant.DirectBinary.bin', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='padding', full_name='valiant.DirectBinary.padding', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_pad', full_name='valiant.DirectBinary.pre_pad', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='null_value', full_name='valiant.DirectBinary.null_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=668,
)

_OBJECTFILE.fields_by_name['header'].message_type = _OBJECTHEADER
_OBJECTFILE.fields_by_name['data'].message_type = _OBJECTDATA
_OBJECTDATA.fields_by_name['binaries'].message_type = _DIRECTBINARY
_OBJECTDATA.fields_by_name['settings'].message_type = _GFXSETTINGS
_OBJECTDATA.fields_by_name['components'].message_type = _GFXCOMPONENT
_GFXSETTINGS.fields_by_name['chr_metadata'].message_type = _CHRMETADATA
_GFXCOMPONENT.fields_by_name['role'].enum_type = _DATAROLE
DESCRIPTOR.message_types_by_name['ObjectFile'] = _OBJECTFILE
DESCRIPTOR.message_types_by_name['ObjectHeader'] = _OBJECTHEADER
DESCRIPTOR.message_types_by_name['ObjectData'] = _OBJECTDATA
DESCRIPTOR.message_types_by_name['GfxSettings'] = _GFXSETTINGS
DESCRIPTOR.message_types_by_name['GfxComponent'] = _GFXCOMPONENT
DESCRIPTOR.message_types_by_name['ChrMetadata'] = _CHRMETADATA
DESCRIPTOR.message_types_by_name['DirectBinary'] = _DIRECTBINARY
DESCRIPTOR.enum_types_by_name['DataRole'] = _DATAROLE

ObjectFile = _reflection.GeneratedProtocolMessageType('ObjectFile', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTFILE,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.ObjectFile)
  ))
_sym_db.RegisterMessage(ObjectFile)

ObjectHeader = _reflection.GeneratedProtocolMessageType('ObjectHeader', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTHEADER,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.ObjectHeader)
  ))
_sym_db.RegisterMessage(ObjectHeader)

ObjectData = _reflection.GeneratedProtocolMessageType('ObjectData', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTDATA,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.ObjectData)
  ))
_sym_db.RegisterMessage(ObjectData)

GfxSettings = _reflection.GeneratedProtocolMessageType('GfxSettings', (_message.Message,), dict(
  DESCRIPTOR = _GFXSETTINGS,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.GfxSettings)
  ))
_sym_db.RegisterMessage(GfxSettings)

GfxComponent = _reflection.GeneratedProtocolMessageType('GfxComponent', (_message.Message,), dict(
  DESCRIPTOR = _GFXCOMPONENT,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.GfxComponent)
  ))
_sym_db.RegisterMessage(GfxComponent)

ChrMetadata = _reflection.GeneratedProtocolMessageType('ChrMetadata', (_message.Message,), dict(
  DESCRIPTOR = _CHRMETADATA,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.ChrMetadata)
  ))
_sym_db.RegisterMessage(ChrMetadata)

DirectBinary = _reflection.GeneratedProtocolMessageType('DirectBinary', (_message.Message,), dict(
  DESCRIPTOR = _DIRECTBINARY,
  __module__ = 'valiant_pb2'
  # @@protoc_insertion_point(class_scope:valiant.DirectBinary)
  ))
_sym_db.RegisterMessage(DirectBinary)


# @@protoc_insertion_point(module_scope)
