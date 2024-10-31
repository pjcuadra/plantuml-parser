"""Test execution for plantuml parser"""

# Copyright 2024 René Fischer - renefischer@fischer-homenet.de
#
# Copyright 2018 Pedro Cuadra - pjcuadra@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from lark import Lark

dir_path = os.path.dirname(os.path.realpath(__file__))
test_data_path = os.path.join(dir_path, 'data')


def get_parser():
    """Factory method for starting parser"""
    grammar_file_path = os.path.join(dir_path, "..", "grammar", "grammar.ebnf")

    f = open(grammar_file_path, encoding="utf-8")

    parser = Lark(f.read())

    return parser


def test_class():
    """Fuction for testing all plantuml class diagrams located in class_diagram folder"""
    parser = get_parser()

    diagrams_path = os.path.join(test_data_path, 'class_diagram')

    for _, _, files in os.walk(diagrams_path):
        files.remove("README")
        for filename in files:
            f = open(os.path.join(diagrams_path, filename), encoding="utf-8")
            parser.parse(f.read())


def test_state():
    """Fuction for testing all plantuml class diagrams located in class_diagram folder"""
    parser = get_parser()

    diagrams_path = os.path.join(test_data_path, 'state_diagram')

    for _, _, files in os.walk(diagrams_path):
        for filename in files:
            f = open(os.path.join(diagrams_path, filename), encoding="utf-8")
            parser.parse(f.read())
                     
