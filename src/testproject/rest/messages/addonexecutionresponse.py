# Copyright 2020 TestProject (https://testproject.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from src.testproject.enums import ExecutionResultType


class AddonExecutionResponse:
    """Object representing the response returned when execution a custom action

        Attributes:
            _executionresulttype (ExecutionResultType): The result of the action execution (Passed / Failed / ...)
            _message (str): A message returned by the agent in response to the action execution
            _fields (list): A potentially updated list of fields
    """

    def __init__(self):
        self._executionresulttype = None
        self._message = None
        self._fields = None

    @property
    def executionresulttype(self) -> ExecutionResultType:
        """Getter for the execution result type"""
        return self._executionresulttype

    @executionresulttype.setter
    def executionresulttype(self, value: ExecutionResultType):
        """Setter for the execution result type"""
        self._executionresulttype = value

    @property
    def message(self) -> str:
        """Getter for the action execution response message"""
        return self._message

    @message.setter
    def message(self, value: str):
        """Setter for the action execution response message"""
        self._message = value

    @property
    def fields(self) -> list:
        """Getter for the list of action execution response fields"""
        return self._fields

    @fields.setter
    def fields(self, value: list):
        """Setter for the list of action execution response fields"""
        self._fields = value
