## Documentation

### Files that cover the core functionalities
- Helper functions: initialisation.py, util.py
- Objects: classTree.py, classVariable.py
- Parsing function: treeParser.py
- Mapping funcitons: expressionAnalysis.py, genericTreePattern.py, treeEncoding.py

### Modules 'Parser'
**Task: Parse String expression into Tree expression**
Require: class BinaryTree, Namespace (in classVariable.py, classTree.py)

**Key functions: buildParseTree**
takes: str, Namespace
outputs: BinaryTree

**Workflow**
Arbitrary str -> Postfix -> Infix (full) -> buildParseTree -> Tree
Tree -> buildParseTree -> Infix (full) -> Postfix -> Infix (Simplified)

### Modules 'MapBuilder'

__treeSignature__ definition
A tree signature consists of two parts, the parent signature and the children signature. Parent signature must match in all value, ptype and states, while children signature only needs to match states. Given a signature and a benchmark signature, the given signature is considered to pass the benchmark test if the states in the former one is a superset of the benchmark states.

### Class Nodes
properties: value, ptype, state

### Todo
- example generator

### Done
- decide if buildTreeMapping should use converted expression or raw expression -> use converted
- state variable - children signature
- test new buildTreeMapping 1 and 2 - use old examples to test - Seems alright
- complete buildTreeMapping handling type check

### Libraries
#### bayesian model derivation
#### likelihood and MLE (requires differentiation)
#### matrix calculus and algebra
