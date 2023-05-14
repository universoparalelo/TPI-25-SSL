# import ply.lex as lex
# import ply.yacc as yacc
# from sys import *

# tokens = ['OPEN_TAG', 'CLOSE_TAG']

# def t_OPEN_TAG(t):
#     r'[<][a-zA-Z0-9 ]+[>]'
#     t.lexer.num_otags += 1
#     return t

# def t_CLOSE_TAG(t):
#     r'[<][/][a-zA-Z0-9 ]+[>]'
#     t.lexer.num_ctags += 1
#     return t

# t_ignore = ' '

# def t_error(t):
#     print(f"Illegal character {t.value[0]}")
#     t.lexer.skip(1)

# lexer = lex.lex()
# lexer.num_otags = 0
# lexer.num_ctags = 0

# lexer.input("<book> texto ejemploooo ")

# while True:
#     tok = lexer.token()
#     if not tok:
#         if (lexer.num_ctags == lexer.num_otags):
#             print("Todas las etiquetas de apertura tienen su cierre")
#         else:
#             print("Falta alguna etiqueta de cierre o apertura")
#         break      # No more input
#     print(tok)
    
import re
# m = re.search('<article (lang="(es|en)")?>', '<article lang="es">')
print(re.match('<article(lang="(es|en)")?>','<article lang="es">'))
