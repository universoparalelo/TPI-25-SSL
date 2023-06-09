import ply.lex as lex
import ply.yacc as yacc
from sys import *
import re

# Lista de tokens. Es un requisito que esten
tokens = [
   'xml', 'version', 'codificacion', 'DOCTYPE', 'o_Book', 'c_Book', 'o_Chapter', 'c_Chapter', 'o_Article', 'c_Article','o_ArticleInfo', 'c_ArticleInfo' , 'o_Section', 'c_Section', 'o_SimpleSec', 'c_SimpleSec', 'o_Info', 'c_Info', 'o_Abstract', 'c_Abstract', 'o_Address', 'c_Address', 'o_Author', 'c_Author', 'o_Copyright', 'c_Copyright', 'o_Title', 'c_Title', 'o_Para', 'c_Para', 'o_SimPara', 'c_SimPara', 'o_Emphasis', 'c_Emphasis', 'o_Link', 'c_Link', 'o_Email', 'c_Email', 'o_ItemizedList', 'c_ItemizedList', 'o_Important', 'c_Important', 'o_FirstName', 'c_FirstName', 'o_Surname', 'c_Surname', 'o_Street', 'c_Street', 'o_City', 'c_City', 'o_State', 'c_State', 'o_Phone', 'c_Phone', 'o_Date', 'c_Date', 'o_Year', 'c_Year', 'o_Holder', 'c_Holder', 'ImageData', 'VideoData', 'o_MediaObject', 'c_MediaObject', 'o_VideoObject', 'comment', 'c_VideoObject', 'o_ImageObject', 'c_ImageObject', 'o_ListItem', 'c_ListItem', 'o_InformalTable', 'c_InformalTable', 'o_Tgroup', 'c_Tgroup', 'o_Thead', 'c_Thead', 'o_Tfoot', 'c_Tfoot', 'o_Tbody', 'c_Tbody', 'o_Row', 'c_Row', 'o_Entrytbl', 'c_Entrytbl', 'o_Entry', 'c_Entry', 'url', 'url2', 'texto', 'lang', 'o_Appendix', 'c_Appendix', 'o_Comment', 'c_Comment','o_Set', 'c_Set', 'o_Subtitle', 'c_Subtitle'
]

# tokens que no usamos   
# 'A', 'B', 'S', 'SB', 'Y', 'Z', 'I', 'R', 'D', 'U', 'C', 'T', 'H', 'J', 'X', 'P', 'M', 'Vi', 'L', 'W', 'TG'

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
t_o_Subtitle = r'[<]subtitle[>]' 
t_c_Subtitle = r'[<]/subtitle[>]'
t_o_Comment = r'[<]comment[>]' 
t_c_Comment = r'[<]/comment[>]'
t_o_Appendix = r'[<]appendix[>]' 
t_c_Appendix = r'[<]/appendix[>]'
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
t_o_Set = r'[<]set[>]'
t_c_Set = r'[<]/set[>]'
t_o_Row = r'[<]row[>]'
t_c_Row = r'[<]/row[>]'
t_o_Link = r'[<]link'
t_c_Link = r'[<]/link[>]'

def t_version(t):
    r'(version[=]["][0-9.]+["])'
    return t

def t_codificacion(t):
    r'((standalone|encoding)[=]["](si|no|UTF-8)["]\?)[>]'
    return t

def t_lang(t):
    r'lang[=]["](en|es)["][>]'
    return t

def t_url(t):
    r'xlink:href="(https?|ftps?|ftp):\/\/[\wñáéíóúÁÉÍÓÚ?=&\-_.\/]+(\:[0-9]+)?(\/[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?(\#[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?"(>)'
    return t

def t_url2(t):
    r'xlink:href="(https?|ftps?|ftp):\/\/[\wñáéíóúÁÉÍÓÚ?=&\-_.\/]+(\:[0-9]+)?(\/[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?(\#[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?"/>'
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
    print(f"Illegal character {t.value[0]}, en la posicion {t.lineno}")
    t.lexer.skip(1)

# PARSER : producciones de cada etiqueta

# estoy adivinando que mierda significa el p[0]
def p_sigma(p):
    '''
    sigma : xml version codificacion DOCTYPE article 
            | xml version codificacion DOCTYPE book
    '''

def p_article(p):
    '''
    article : o_Article lang title info A c_Article
            | o_Article lang title A c_Article
    '''


def p_A(p):
    '''
    A : itemizedList A
        | important A
        | para A
        | simPara A
        | articleInfo A 
        | address A
        | mediaObject A
        | informalTable A 
        | COMMENT A
        | abstract A
        | simpleSec A
        | section A
        | empty
    '''


def p_book(p):
    '''
    book : o_Book title B c_Book
            | o_Book title info B c_Book
    '''

def p_B(p):
    '''
    B : itemizedList B
        | important B 
        | para B
        | simPara B
        | articleInfo B 
        | section B
        | address B
        | mediaObject B
        | informalTable B
        | COMMENT B
        | abstract B
        | simpleSec B 
        | article B
        | set B
        | appendix B 
        | empty
    '''

def p_section(p):
    '''
    section : o_Section title S c_Section
            | c_Section title info S c_Section
    '''

def p_S(p):
    '''
    S : itemizedList S
        | important S 
        | para S
        | simPara S
        | address S
        | mediaObject S
        | informalTable S
        | COMMENT S
        | abstract S
        | itemizedList 
        | important 
        | para 
        | simPara 
        | address 
        | mediaObject 
        | informalTable
        | COMMENT 
        | abstract 
    '''


def p_simpleSec(p):
    '''
    simpleSec : o_SimpleSec S c_SimpleSec
                | o_SimpleSec info S c_SimpleSec
                | o_SimpleSec title S c_SimpleSec
                | o_SimpleSec info title S c_SimpleSec
    '''

def p_subtitle(p):
    '''
    subtitle : o_Subtitle texto c_Subtitle
    '''

def p_set(p):
    '''
    set : o_Set title subtitle SB c_Set
    '''

def p_SB(p):
    '''
    SB : set SB
        | book SB
        | empty
    '''

def p_info(p):
    '''
    info : o_Info I c_Info 
    '''

def p_articleInfo(p):
    '''
    articleInfo : o_ArticleInfo I c_ArticleInfo 
    '''

def p_I(p):
    '''
    I : mediaObject I
        | abstract I 
        | address I 
        | author I  
        | date I
        | copyright I  
        | title I
        | mediaObject 
        | abstract  
        | address  
        | author  
        | date  
        | copyright  
        | title
    '''

def p_abstract(p): 
    '''
    abstract : o_Abstract title R c_Abstract 
               | c_Abstract R o_Abstract
    '''

def p_R(p): 
    '''
    R : para R
        | simPara R
        | para
        | simPara
    '''

def p_address(p):
    '''
    address : o_Address D c_Address
    '''

def p_D(p):
    '''
    D : texto D
        | street D
        | city D
        | state D
        | phone D
        | email D
        | empty 
    '''

def p_author(p): 
    '''
    author : o_Author firstName U surname c_Author
    '''

def p_U(p): 
    '''
    U : firstName U
        | U surname
        | empty
    '''

def p_copyright(p): 
    '''
    copyright : o_Copyright year C c_Copyright
    '''
    
def p_C(p):
    '''
    C : year C
        | C holder     
        | empty
    '''

def p_title(p):
    '''
    title : o_Title T c_Title
    '''

def p_T(p):
    '''
    T : T T 
        | texto 
        | emphasis
        | link 
        | email
    '''

def p_chapter(p):
    '''
    chapter : o_Chapter title H c_Chapter
            | o_Chapter title para H c_Chapter
    '''
    
def p_H(p): 
    '''
    H : section H
        | simpleSec H
        | title H
        | para H
        | important H 
        | informalTable H
        | mediaObject H
        | empty
    '''

def p_appendix(p): 
    ''' 
    appendix : o_Appendix title chapter c_Appendix 
    ''' 
 
def p_simPara(p): 
    ''' 
    simPara : o_SimPara X c_SimPara 
    ''' 
 
def p_emphasis(p): 
    ''' 
    emphasis : o_Emphasis X c_Emphasis 
    ''' 
      
def p_COMMENT(p): 
    ''' 
    COMMENT : o_Comment X c_Comment 
    ''' 
 
def p_X(p): 
    ''' 
    X : X X 
        | texto 
        | emphasis 
        | link 
        | email 
        | author 
        | COMMENT 
    ''' 
     
def p_link(p): 
    ''' 
    link : o_Link url X c_Link 
    ''' 
 
def p_para(p): 
    ''' 
    para : o_Para P c_Para 
    ''' 
 
def p_P(p): 
    ''' 
    P : P P 
        | texto 
        | emphasis 
        | link 
        | email 
        | author 
        | COMMENT 
        | itemizedList 
        | important 
        | address 
        | mediaObject 
        | informalTable 
    ''' 
 
def p_important(p): 
    ''' 
    important : o_Important M c_Important 
            | o_Important title M c_Important
    ''' 
 
def p_M(p): 
    ''' 
    M : M M 
        | itemizedList 
        | para 
        | simPara 
        | address 
        | mediaObject 
        | informalTable 
        | COMMENT 
        | abstract 
    ''' 
 
def p_firstName(p): 
    ''' 
    firstName : o_FirstName Y c_FirstName 
    ''' 
     
def p_surname(p): 
    ''' 
    surname : o_Surname Y c_Surname 
    '''

def p_street(p):
    '''
    street : o_Street Y c_Street
    '''

def p_city(p):
    '''
    city : o_City Y c_City
    '''

def p_state(p):
    '''
    state : o_State Y c_State
    '''

def p_phone(p):
    '''
    phone : o_Phone Y c_Phone
    '''

def p_email(p):
    '''
    email : o_Email Y c_Email
    '''

def p_date(p):
    '''
    date : o_Date Y c_Date
    '''

def p_year(p):
    '''
    year : o_Year Y c_Year
    '''

def p_holder(p):
    '''
    holder : o_Holder Y c_Holder
    '''

def p_Y(p):
    '''
    Y : texto Y
        | link Y
        | emphasis Y 
        | COMMENT Y
        | texto
        | link 
        | emphasis 
        | COMMENT
    '''


def p_mediaObject(p):
    '''
    mediaObject : o_MediaObject info Vi c_MediaObject
                | o_MediaObject info c_MediaObject 
    '''

def p_Vi(p):
    '''
    Vi : videoObject Vi
        | imageObject Vi
        | videoObject
        | imageObject
    '''

def p_videoObject(p):
    '''
    videoObject : o_VideoObject info videoData c_VideoObject
                | o_VideoObject videoData c_VideoObject
    '''

def p_videoData(p):
    '''
    videoData : VideoData url2
    '''

def p_imageObject(p):
    '''
    imageObject : o_ImageObject info imageData c_ImageObject
                | o_ImageObject imageData c_ImageObject
    '''

def p_imageData(p):
    '''
    imageData : ImageData url2
    '''

def p_itemizedList(p):
    '''
    itemizedList : o_ItemizedList listItem Z c_ItemizedList
    '''

def p_Z(p):
    '''
    Z : listItem Z
        | empty
    '''

def p_listItem(p):
    '''
    listItem : o_ListItem L c_ListItem
    '''

def p_L(p):
    '''
    L : itemizedList L
        | important L
        | para L
        | simPara L 
        | address L
        | mediaObject L 
        | informalTable L 
        | COMMENT L
        | abstract L
        | itemizedList 
        | important 
        | para 
        | simPara 
        | address 
        | mediaObject 
        | informalTable 
        | comment 
        | abstract
    '''


def p_informalTable(p):
    '''
    informalTable : o_InformalTable TG c_InformalTable
    '''

def p_TG(p):
    '''
    TG : mediaObject TG
        | tgroup TG
        | mediaObject
        | tgroup
    '''

def p_tgroup(p):
    '''
    tgroup : o_Tgroup tbody thead tfoot c_Tgroup
            | o_Tgroup thead tbody thead tfoot c_Tgroup
            | o_Tgroup tfoot tbody thead tfoot c_Tgroup
            | o_Tgroup thead tfoot tbody thead tfoot c_Tgroup
    '''

def p_tbody(p):
    '''
    tbody : o_Tbody ROW ROW c_Tbody
    '''

def p_tfoot(p):
    '''
    tfoot : o_Tfoot ROW ROW c_Tfoot
    '''

def p_thead(p):
    '''
    thead : o_Thead ROW ROW c_Thead
    '''

def p_ROW(p):
    '''
    ROW :  ROW2 ROW
        | empty 
    '''

def p_ROW2(p):
    '''
    ROW2 : o_Row W c_Row
    '''

def p_W(p):
    '''
    W : entry W
        | entrytbl W
        | entry
        | entrytbl
    '''

def p_entrytbl(p):
    '''
    entrytbl : o_Entrytbl tbody c_Entrytbl
            | o_Entrytbl thead tbody c_Entrytbl
    '''

def p_entry(p):
    '''
    entry : o_Entry J c_Entry
    '''

def p_J(p):
    '''
    J : texto J
        | itemizedList J
        | important J
        | para J
        | simPara J
        | mediaObject J
        | COMMENT J
        | abstract J
        | empty
    '''

# Defino el string vacio
def p_empty(p):
    ''' 
    empty : 
    '''
    p[0] = None

# Manejo de errores sintacticos
def p_error(p):
    print(f"Error de sintaxis en la entrada: {p.value}")



# **********OPCIONES PARA INGRESAR TEXTO XML**********

# Leer el archivo con codificación UTF-8
# with open("../prueba/index.xml", "r", encoding="utf-8") as archivo:
#     contenido = archivo.read()

# Dato que ingresa el usuario
# data = input("Ingrese un texto en formato xml: \n")

# Construye el lexer
lexer = lex.lex()
# optimize=1,lextab="footab"

# lexer.input(contenido)
# lexer.input(data)
# ya no le pasamos la data al lexer, se la pasamos al parser

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No mas para leer
#     # print(tok.type, tok.value, tok.lineno, tok.lexpos)
#     print(tok)

parser = yacc.yacc()


def parse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        parser.parse(content)

# Llama a la función parse_file() con el nombre del archivo como argumento
parse_file('../prueba/index.xml')

