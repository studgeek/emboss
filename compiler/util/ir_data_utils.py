# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from compiler.util import ir_data

class IrDataSerializer:
  """Provides methods for serializing IR data objects"""

  def __init__(self, ir: ir_data.Message):
    assert ir is not None
    self.ir = ir

  def to_json(self, *args, **kwargs):
    """Converts the IR data class to a JSON string"""
    return self.ir.to_json(*args, **kwargs)

  @staticmethod
  def from_json(data_cls: type[ir_data.Message], data):
    """Constructs an IR data class from the given JSON string"""
    return data_cls.from_json(data)