import sys
from antlr4 import *
sys.path.append('antlr/gen/java')
from JavaLexer import JavaLexer
from JavaParser import JavaParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.statement()
    print(tree.getChild(0).getText())
 
if __name__ == '__main__':
    main(sys.argv)

"""
code = open('sample.java', 'r').read()
codeStream = InputStream(code)
lexer = JavaLexer(codeStream)

# First lexing way
tokensStream = CommonTokenStream(lexer)
parser = JavaParser(tokensStream)

# Second lexing way
'''tokens = lexer.getAllTokens()
tokensSource = ListTokenSource(tokens)
tokensStream = CommonTokenStream(tokensSource)
parser = JavaParser(tokensStream)'''

tree = parser.compilationUnit()
print("Tree " + tree.toStringTree(recog=parser))

"""