import os
from lark import Lark


def get_parser():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    grammar_file_path = os.path.join(dir_path, "..", "grammar", "main.ebnf")

    f = open(grammar_file_path)

    parser = Lark(f.read())

    return parser


def test_relations():
    uml_1 = """
    @startuml
    Class01 <|-- Class02
    Class03 *-- Class04
    Class05 o-- Class06
    Class07 .. Class08
    Class09 -- Class10
    @enduml
    """

    uml_2 = """
    @startuml
    Class11 <|.. Class12
    Class13 --> Class14
    Class15 ..> Class16
    Class17 ..|> Class18
    Class19 <--* Class20
    @enduml
    """

    uml_3 = """
    @startuml
    Class21 #-- Class22
    Class23 x-- Class24
    Class25 }-- Class26
    Class27 +-- Class28
    Class29 ^-- Class30
    @enduml
    """

    parser = get_parser()

    parser.parse(uml_1)
    parser.parse(uml_2)
    parser.parse(uml_3)


def test_relations_labels():
    uml_1 = """
    @startuml
    Class01 "1" *-- "many" Class02 : contains
    Class03 o-- Class04 : aggregation
    Class05 --> "1" Class06
    @enduml
    """

    uml_2 = """
    @startuml
    class Car

    Driver - Car : drives >
    Car *- Wheel : have 4 >
    Car -- Person : < owns
    @enduml
    """

    parser = get_parser()

    parser.parse(uml_1)
    parser.parse(uml_2)
