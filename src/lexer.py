import ply.lex as lex
import ply.yacc as yacc
from sys import *
import re

# Lista de tokens. Es un requisito que esten
tokens = [
   'xml', 'version', 'codificacion', 'DOCTYPE', 'o_Book', 'c_Book', 'o_Chapter', 'c_Chapter', 'o_Article', 'c_Article','o_ArticleInfo', 'c_ArticleInfo' , 'o_Section', 'c_Section', 'o_SimpleSec', 'c_SimpleSec', 'o_Info', 'c_Info', 'o_Abstract', 'c_Abstract', 'o_Address', 'c_Address', 'o_Author', 'c_Author', 'o_Copyright', 'c_Copyright', 'o_Title', 'c_Title', 'o_Para', 'c_Para', 'o_SimPara', 'c_SimPara', 'o_Emphasis', 'c_Emphasis', 'Link', 'o_Email', 'c_Email', 'o_ItemizedList', 'c_ItemizedList', 'o_Important', 'c_Important', 'o_FirstName', 'c_FirstName', 'o_Surname', 'c_Surname', 'o_Street', 'c_Street', 'o_City', 'c_City', 'o_State', 'c_State', 'o_Phone', 'c_Phone', 'o_Date', 'c_Date', 'o_Year', 'c_Year', 'o_Holder', 'c_Holder', 'ImageData', 'VideoData', 'o_MediaObject', 'c_MediaObject', 'o_VideoObject', 'comment', 'c_VideoObject', 'o_ImageObject', 'c_ImageObject', 'o_ListItem', 'c_ListItem', 'o_InformalTable', 'c_InformalTable', 'o_Tgroup', 'c_Tgroup', 'o_Thead', 'c_Thead', 'o_Tfoot', 'c_Tfoot', 'o_Tbody', 'c_Tbody', 'o_Row', 'c_Row', 'o_Entrytbl', 'c_Entrytbl', 'o_Entry', 'c_Entry', 'url', 'url2', 'texto', 'lang', 'atributos', 'A', 'B', 'S', 'SB', 'Y', 'Z', 'I', 'R', 'D', 'U', 'C', 'T', 'H', 'J', 'X', 'P', 'M', 'Vi', 'L', 'W', 'TG'
]

# Expresiones regulares para reglas simples
t_xml = r'(<\?xml)'
t_DOCTYPE = r'(<!DOCTYPE>)'
t_o_InformalTable = r'[<]informaltable[>]'
t_c_InformalTable = r'[<]/informaltable[>]'
t_o_ItemizedList = r'[<]itemizedlist[>]'
t_c_ItemizedList = r'[<]/itemizedlist[>]'
t_o_ArticleInfo = r'[<]articleinfo[>]'
t_c_ArticleInfo = r'[<]/articleinfo[>]'
t_o_MediaObject = r'[<]mediaobject[>]'
t_c_MediaObject = r'[<]/mediaobject[>]'
t_o_VideoObject = r'[<]videoobject[>]'
t_c_VideoObject = r'[<]/videoobject[>]'
t_o_ImageObject = r'[<]imageobject[>]'
t_c_ImageObject = r'[<]/imageobject[>]'
t_o_Copyright = r'[<]copyright[>]'
t_c_Copyright = r'[<]/copyright[>]'
t_o_Important = r'[<]important[>]'
t_c_Important = r'[<]/important[>]'
t_o_FirstName = r'[<]firstname[>]'
t_c_FirstName = r'[<]/firstname[>]'
t_o_SimpleSec = r'[<]simplesec[>]'
t_c_SimpleSec = r'[<]/simplesec[>]'
t_o_Entrytbl = r'[<]entrytbl[>]'
t_c_Entrytbl = r'[<]/entrytbl[>]'
t_o_Emphasis = r'[<]emphasis[>]'
t_c_Emphasis = r'[<]/emphasis[>]'
t_o_Abstract = r'[<]abstract[>]'
t_c_Abstract = r'[<]/abstract[>]'
t_o_ListItem = r'[<]listitem[>]'
t_c_ListItem = r'[<]/listitem[>]'
t_o_SimPara = r'[<]simpara[>]'
t_c_SimPara = r'[<]/simpara[>]'
t_o_Chapter = r'[<]chapter[>]'
t_c_Chapter = r'[<]/chapter[>]'
t_o_Address = r'[<]address[>]'
t_c_Address = r'[<]/address[>]'
t_o_Section = r'[<]section[>]'
t_c_Section = r'[<]/section[>]'
t_o_Surname = r'[<]surname[>]'
t_c_Surname = r'[<]/surname[>]'
t_o_Street = r'[<]street[>]'
t_c_Street = r'[<]/street[>]'
t_o_Author = r'[<]author[>]'
t_c_Author = r'[<]/author[>]'
t_o_Article = r'[<]article'
t_c_Article = r'[<]/article[>]'
t_o_Holder = r'[<]holder[>]'
t_c_Holder = r'[<]/holder[>]'
t_ImageData = r'[<]imagedata'
t_VideoData = r'[<]videodata'
t_o_Tgroup = r'[<]tgroup[>]'
t_c_Tgroup = r'[<]/tgroup[>]'
t_o_State = r'[<]state[>]'
t_c_State = r'[<]/state[>]'
t_o_Phone = r'[<]phone[>]'
t_c_Phone = r'[<]/phone[>]'
t_o_Title = r'[<]title[>]'
t_c_Title = r'[<]/title[>]'
t_o_Email = r'[<]email[>]'
t_c_Email = r'[<]/email[>]'
t_o_Thead = r'[<]thead[>]'
t_c_Thead = r'[<]/thead[>]'
t_o_Tfoot = r'[<]tfoot[>]'
t_c_Tfoot = r'[<]/tfoot[>]'
t_o_Tbody = r'[<]tbody[>]'
t_c_Tbody = r'[<]/tbody[>]'
t_o_Entry = r'[<]entry[>]'
t_c_Entry = r'[<]/entry[>]'
t_o_Book = r'[<]book[>]'
t_c_Book = r'[<]/book[>]'
t_o_Para = r'[<]para[>]'
t_c_Para = r'[<]/para[>]'
t_o_Info = r'[<]info[>]'
t_c_Info = r'[<]/info[>]'
t_o_City = r'[<]city[>]'
t_c_City = r'[<]/city[>]'
t_o_Date = r'[<]date[>]'
t_c_Date = r'[<]/date[>]'
t_o_Year = r'[<]year[>]'
t_c_Year = r'[<]/year[>]'
t_o_Row = r'[<]row[>]'
t_c_Row = r'[<]/row[>]'
t_Link = r'[<]link'

def t_version(t):
    r'(version[=]["][0-9.]+["])'
    return t

def t_codificacion(t):
    r'(standalone[=]["](si|no)["]\?)[>]'
    return t

def t_lang(t):
    r'lang[=]["](en|es)["][>]'
    return t

def t_url(t):
    r'(fileref|href)[=]["](https|http|ftps|ftp)\://([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\?+|\=+|;|&|\-+|_+|\.+)+(\:[0-9]+|)(/([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\-+|_+|\?+|\=+|;|&|\.+|/+)+|)(\#([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\-+|_+|\?+|\=+|;|&|\.+|/+)+|)["][/][>]'
    return t

def t_comment(t):
    r'(<!-- )[\w.\?="<> ]+( -->)'
    return t

# Definimos una regla para el texto comun
def t_texto(t):
    r"[\w.,\?á-úÁ-ÚñÑü ¡!¿\*\/@©­­'\$]+"
    return t

# Definimos una regla para contar lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignora los espacios en blanco y tabuladores
t_ignore  = ' \t\n\r'

# Regla para controlar errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# **********OPCIONES PARA INGRESAR TEXTO XML**********

# Leer el archivo con codificación UTF-8
# with open("../prueba/index.xml", "r", encoding="utf-8") as archivo:
#     contenido = archivo.read()

# Dato que ingresa el usuario
data = input("Ingrese un texto en formato xml: \n")

# Construye el lexer
lexer = lex.lex()
# optimize=1,lextab="footab"

# lexer.input(contenido)
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No mas para leer
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)
    print(tok)


