# PlatUML Parser

This is a Proof-of-Concept a PlantUML parser. This still WIP, and support is
being added incrementally. PlantUML is being parsed using LARK and described in
EBNF.

## Usage

```
python plantuml-parser.py -i <plantuml-file>
```

## TODOs

* Finish Supporting all Class Diagram features in
  http://plantuml.com/class-diagram
* Add support for other diagrams;

  * Sequence Diagram
  * Usecase Diagram
  * Activity Diagram
  * Component Diagram
  * State Diagram
  * Object Diagram
  * Deployment Diagram
  * Timing Diagram

* Add setup.py
* Output AST as JSON or other usable format instead of STDOUT
