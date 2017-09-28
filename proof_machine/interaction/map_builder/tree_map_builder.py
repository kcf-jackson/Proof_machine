from proof_machine.interaction.infer_state import infer_state
from proof_machine.interaction.map_builder.treeManipulation import treeToNodes, genericTreeMapping
from proof_machine.interaction.parser.tree_parser import parse
from proof_machine.object.namespace import lookup_ptype
from proof_machine.object.tree import Node
from proof_machine.others import which


def buildTreeMapping(expr1, expr2, namespace):
    tree1 = parse(expr1, namespace)
    tree2 = parse(expr2, namespace)
    mapSpec = getNodesMapping(tree1, tree2)
    extraNodes = convertSymbolToNodes(mapSpec['extraSym'], namespace)
    sourceSignature = getTreeSignature(tree1)
    sourceTreeCode = treeToLeavesCode(tree1)
    targetMapCode = treeToBaseThreeCode(tree2)

    def treeFunction(tree, quiet=True):
        # this function checks the signature, apply the tree map if the check passes.
        tree = infer_state(tree)
        treeSignature = getTreeSignature(tree, sourceTreeCode)
        signaturePass = treeSignatureTest(treeSignature, sourceSignature, quiet)
        if signaturePass:
            nodesList = treeToNodes(tree, sourceTreeCode) + extraNodes
            res = genericTreeMapping(nodesList, targetMapCode, mapSpec['mapDict'])
            return res
        else:
            return tree

    return treeFunction


# ===================================================================================
# Convert list of symbols to list of nodes
def convertSymbolToNodes(symbolList, namespace):
    return [Node(x, lookup_ptype(x, namespace)) for x in symbolList]


# ===================================================================================
# Mapping between two trees
# Find the extra symbols in the 2nd tree and the mapping between the two trees
def getNodesMapping(tree1, tree2):
    a1Sym = getSymbolList(tree1)
    a2Sym = getSymbolList(tree2)
    extraSym = symDiff(a1Sym, a2Sym)
    mapDict = findMapping(a1Sym + extraSym, a2Sym)
    return {'extraSym': extraSym, 'mapDict': mapDict}


# Convert a tree into list of symbols
def getSymbolList(tree):
    nodesList = treeToNodes(tree)
    symList = [x.value for x in nodesList]
    return symList


# Find the extra symbol in symbol list 2
def symDiff(symList1, symList2):
    return sorted(list(set(symList2) - set(symList1)))


# Given symbol list 1 and 2, find the possible mapping
def findMapping(symList1, symList2):
    mapDict = {}
    for ind, sym in enumerate(symList2):
        matched_pos = [k + 1 for k in which(symList1, sym)]
        mapDict[ind + 1] = matched_pos[0]  # pick the first element if there is multiple match
    return mapDict
