tokens = ('BIT','NOT','AND','OR','XOR','NAND','NOR')

literals = ['(',')']


t_NOT = r'NOT'
t_AND = r'AND'
t_OR = r'OR'
t_XOR = r'XOR'
t_NAND = r'NAND'
t_NOR = r'NOR'


t_BIT = r'[01]'

t_ignore = " \n"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()

def p_statement(t):
	'statement : argument'
	print(t[1])

def p_argument_bit(t):
	"argument : BIT"
	t[0] = int(t[1])

def p_argument_paren(t):
	"argument : '(' argument ')'"
	t[0] = t[2]

def p_argument_not(t):
	"argument : NOT argument"
	t[0] = 1-int(t[2])

def p_argument_operate(t):
	'''argument : argument AND argument
					| argument OR argument
					| argument XOR argument
					| argument NAND argument
					| argument NOR argument'''
	if(t[2] == t_AND): t[0] = t[1]*t[3]
	elif(t[2] == t_OR): t[0] = t[1] | t[3]
	elif(t[2] == t_XOR): t[0] = (t[1] | t[3])*(1-(t[1]*t[3]))
	elif(t[2] == t_NAND): t[0] = 1 - (t[1]*t[3])
	elif(t[2] == t_NOR): t[0] = 1 - (t[1] | t[3])



def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)


# To run the parser do the following in a terminal window: cat plyParserInputs/parser.out | python Bit_Parser.py
