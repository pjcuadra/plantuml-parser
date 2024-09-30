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

    grammar_file_path = os.path.join(dir_path, "..", "grammar", "grammar.ebnf")

    f = open(grammar_file_path)

    parser = Lark(f.read())

    return parser


def test_class():

    parser = get_parser()

    diagrams_path = os.path.join(test_data_path, 'class_diagram')

    for root, dirs, files in os.walk(diagrams_path):
        files.remove("README")
        for filename in files:
            print(f"Execute " + filename)
            f = open(os.path.join(diagrams_path, filename))
            parser.parse(f.read())
            
