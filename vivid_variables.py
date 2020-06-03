import sys
from antlr4 import *
sys.path.append('antlr/gen/java')
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from JavaParserListener import JavaParserListener

class VariableListener(JavaParserListener):  
    """Custom listener for scraping variable names (does not include those declared in for control statements)."""

    
    def __init__(self):
        super(VariableListener, self).__init__() # Call base constructor
        self.in_for_control = False # Whether the listener is currently walking through a for control statement
        self.variable_list = [] # List of variable names not declared in for control statements


    def enterForControl(self, ctx):         
        self.in_for_control = True

    def exitForControl(self, ctx):         
        self.in_for_control = False

    def enterVariableDeclarator(self, ctx):
        if not self.in_for_control:
            self.variable_list.append(ctx.getChild(0).getText())

 
def generate_parse_tree(source):
    """Generates an ANTLR parse tree from a piece of source code."""

    input_stream = FileStream(source)
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    return tree

def scrape_variables(source):
    """Gathers all the names of the variables instantiated, except for those in for control statements."""

    tree = generate_parse_tree(source)
    listener = VariableListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.variable_list

