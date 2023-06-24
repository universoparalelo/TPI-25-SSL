import ply.lex as lex
import ply.yacc as yacc
from sys import *
import re

# Lista de tokens. Es un requisito que esten
tokens = [
   'xml', 'version', 'codificacion', 'DOCTYPE', 'o_Article', 'c_Article','o_ArticleInfo', 'c_ArticleInfo' , 'o_Section', 'c_Section', 'o_SimpleSec', 'c_SimpleSec', 'o_Info', 'c_Info', 'o_Abstract', 'c_Abstract', 'o_Address', 'c_Address', 'o_Author', 'c_Author', 'o_Copyright', 'c_Copyright', 'o_Title', 'c_Title', 'o_Para', 'c_Para', 'o_SimPara', 'c_SimPara', 'o_Emphasis', 'c_Emphasis', 'o_Link', 'c_Link', 'o_Email', 'c_Email', 'o_ItemizedList', 'c_ItemizedList', 'o_Important', 'c_Important', 'o_FirstName', 'c_FirstName', 'o_Surname', 'c_Surname', 'o_Street', 'c_Street', 'o_City', 'c_City', 'o_State', 'c_State', 'o_Phone', 'c_Phone', 'o_Date', 'c_Date', 'o_Year', 'c_Year', 'o_Holder', 'c_Holder', 'ImageData', 'VideoData', 'o_MediaObject', 'c_MediaObject', 'o_VideoObject', 'comment', 'c_VideoObject', 'o_ImageObject', 'c_ImageObject', 'o_ListItem', 'c_ListItem', 'o_InformalTable', 'c_InformalTable', 'o_Tgroup', 'c_Tgroup', 'o_Thead', 'c_Thead', 'o_Tfoot', 'c_Tfoot', 'o_Tbody', 'c_Tbody', 'o_Row', 'c_Row', 'o_Entrytbl', 'c_Entrytbl', 'o_Entry', 'c_Entry', 'url', 'url2', 'texto', 'lang', 'o_Comment', 'c_Comment'
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
t_o_Comment = r'[<]comment[>]' 
t_c_Comment = r'[<]/comment[>]'
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
    r'xlink:href="(https?|ftps?|ftp|http):\/\/[\wñáéíóúÁÉÍÓÚ?=&\-_.\/]+(\:[0-9]+)?(\/[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?(\#[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?"(>)'
    t.value = t.value.split('=')[1]
    return t

def t_url2(t):
    r'fileref="(https?|ftps?|ftp|http):\/\/[\wñáéíóúÁÉÍÓÚ?=&\-_.\/]+(\:[0-9]+)?(\/[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?(\#[\wñáéíóúÁÉÍÓÚ\-_.\/]+)?"(/>)'
    t.value = t.value.split('=')[1]
    return t

def t_comment(t):
    r'(<!-- )[\w.\?="<> ]+( -->)'
    return t

# Definimos una regla para el texto comun
def t_texto(t):
    r"[\w.,\?á-úÁ-ÚñÑü ¡!¿\*\/@©­­'\$:_]+"
    return t

# Definimos una regla para contar lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignora los espacios en blanco y tabuladores
t_ignore  = ' \t\n\r'

# Regla para controlar errores
def t_error(t):
    print(f"Error: Carácter no válido '{t.value[0]}' en la línea {t.lineno}, posición {find_column(t.lexer.lexdata, t)}")
    t.lexer.skip(1)

# funcion para hallar la linea donde se encuentra el error
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# variables auxiliares
h1 = 0
h2 = 0

# PARSER : producciones de cada etiqueta

def p_sigma(p):
    '''
    sigma : xml version codificacion DOCTYPE article 
    '''
    p[0] = '<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0"> \n<title>Document</title>\n</head>'+p[5]+'\n</html>'
    return p[0]

def p_article(p):
    '''
    article : o_Article lang title info A c_Article
            | o_Article lang title A c_Article
    '''
    if len(p) == 7:
        p[0] = '\n<body>'+p[3]+p[4]+p[5]+'\n</body>'
    else:
        p[0] = '\n<body>'+p[3]+p[5]+'\n</body>'
    
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
        | info A
        | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_section(p):
    '''
    section : o_Section title S c_Section
            | o_Section title info S c_Section
            | o_Section info S c_Section
    '''
    if len(p) == 5:
        p[0] = '\n<div>' + p[2] + p[3] + '\n</div>'
    else:
        p[0] = '\n<div>' + p[2] + p[3] + p[4] + '\n</div>'

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
        | simpleSec S
        | section S
        | empty 
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_simpleSec(p):
    '''
    simpleSec : o_SimpleSec S c_SimpleSec
                | o_SimpleSec info S c_SimpleSec
                | o_SimpleSec title S c_SimpleSec
                | o_SimpleSec info title S c_SimpleSec
    '''
    if len(p) == 4:
        p[0] = '\n<div>' + p[2] + '\n</div>'
    elif len(p) == 5:
        p[0] = '\n<div>' + p[2] + p[3] + '\n</div>'
    else:
        p[0] = '\n<div>' + p[2] + p[3]+ p[4] + '\n</div>'


def p_info(p):
    '''
    info : o_Info I c_Info 
    '''
    p[0] = '\n<div>' + p[2] + '\n</div>'

def p_articleInfo(p):
    '''
    articleInfo : o_ArticleInfo I c_ArticleInfo 
    '''
    p[0] = '\n<div>' + p[2] + '\n</div>'

def p_I(p):
    '''
    I : mediaObject I
        | abstract I 
        | address I 
        | author I  
        | date I
        | copyright I  
        | title I
        | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    

def p_abstract(p): 
    '''
    abstract : o_Abstract title R c_Abstract 
               | c_Abstract R o_Abstract
    '''
    if len(p) == 4:
        p[0] = '\n<p>' + p[2] + p[3] + '\n</p>'
    else:
        p[0] = '\n<p>' + p[2] + '\n</p>'

def p_R(p): 
    '''
    R : para R
        | simPara R
        | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]

def p_address(p):
    '''
    address : o_Address D c_Address
    '''
    p[0] = '\n<p>' + p[2] + '\n</p>'

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
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_author(p): 
    '''
    author : o_Author firstName U surname c_Author
    '''
    p[0] = '\n<p>' + p[2]  + p[4] + '\n</p>'

def p_U(p): 
    '''
    U : firstName U
        | U surname
        | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]

def p_copyright(p): 
    '''
    copyright : o_Copyright year C c_Copyright
    '''
    p[0] = '\n<p>' + p[2] + '</p>'
    
def p_C(p):
    '''
    C : year C
        | C holder     
        | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]

def p_title(p):
    '''
    title : o_Title T c_Title
    '''
    global h1
    h1 += 1
    if h1 == 1:
        p[0] = '\n<h1>' + p[2] + '</h1>'
    else:
        p[0] = '\n<h2>' + p[2] + '</h2>'

def p_T(p):
    '''
    T : texto T
    | emphasis T
    | link T
    | email T
    | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    elif p[1] == '':
        p[0] = p[1]

 
def p_simPara(p): 
    ''' 
    simPara : o_SimPara X c_SimPara 
    ''' 
    p[0] = '\n<p>' + p[2] + '</p>'
 
def p_emphasis(p): 
    ''' 
    emphasis : o_Emphasis X c_Emphasis 
    ''' 
    p[0] = '\n<p>' + p[2] + '</p>'
      
def p_COMMENT(p): 
    ''' 
    COMMENT : o_Comment X c_Comment 
    ''' 
    p[0] = '\n<p>' + p[2] + '</p>'
 
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
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
     
def p_link(p): 
    ''' 
    link : o_Link url X c_Link 
    ''' 
    p[0] = '<a href=' + p[2] + p[3] + '</a>'
 

def p_para(p): 
    ''' 
    para : o_Para P c_Para 
    ''' 
    p[0] = '\n<p>' + p[2] + '</p>'
 
def p_P(p): 
    ''' 
    P : texto P
        | emphasis P 
        | link P
        | email P
        | author P
        | COMMENT P
        | itemizedList P 
        | important P
        | address P
        | mediaObject P 
        | informalTable P
        | empty 
    ''' 
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
 
def p_important(p): 
    ''' 
    important : o_Important M c_Important 
            | o_Important title M c_Important
    ''' 
    if len(p) == 5:
        p[0] = '\n<p>' + p[1] + p[2] + '</p>'
    else:
        p[0] = '\n<p>' + p[1] + '</p>'
 
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
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    
 
def p_firstName(p): 
    ''' 
    firstName : o_FirstName Y c_FirstName 
    ''' 
    p[0] = '<p>' + p[2] + '</p>'
     
def p_surname(p): 
    ''' 
    surname : o_Surname Y c_Surname 
    '''
    p[0] = '<p>' + p[2] + '</p>'

def p_street(p):
    '''
    street : o_Street Y c_Street
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_city(p):
    '''
    city : o_City Y c_City
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_state(p):
    '''
    state : o_State Y c_State
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_phone(p):
    '''
    phone : o_Phone Y c_Phone
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_email(p):
    '''
    email : o_Email Y c_Email
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_date(p):
    '''
    date : o_Date Y c_Date
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_year(p):
    '''
    year : o_Year Y c_Year
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

def p_holder(p):
    '''
    holder : o_Holder Y c_Holder
    '''
    p[0] = '\n<p>' + p[2] + '</p>'

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
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_mediaObject(p):
    '''
    mediaObject : o_MediaObject info Vi c_MediaObject
                | o_MediaObject Vi c_MediaObject 
    '''
    if len(p) == 5:
        p[0] = '\n<div>' + p[2] + p[3] + '</div>'
    else:
        p[0] = '\n<div>' + p[2] + '</div>'

def p_Vi(p):
    '''
    Vi : videoObject Vi
        | imageObject Vi
        | videoObject
        | imageObject
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_videoObject(p):
    '''
    videoObject : o_VideoObject info videoData c_VideoObject
                | o_VideoObject videoData c_VideoObject
    '''
    if len(p) == 5:
        p[0] = '\n<figure>' + p[2] + p[3] + '</figure>'
    else:
        p[0] = '\n<figure>' + p[2] + '</figure>'

def p_videoData(p):
    '''
    videoData : VideoData url2
    '''
    p[0] = '<video src="' + p[2]

def p_imageObject(p):
    '''
    imageObject : o_ImageObject info imageData c_ImageObject
                | o_ImageObject imageData c_ImageObject
    '''
    if len(p) == 5:
        p[0] = '\n<figure>' + p[2] + p[3] + '\n</figure>'
    else:
        p[0] = '\n<figure>' + p[2] + '\n</figure>'

def p_imageData(p):
    '''
    imageData : ImageData url2
    '''
    p[0] = '<img src=' + p[2]

def p_itemizedList(p):
    '''
    itemizedList : o_ItemizedList listItem Z c_ItemizedList
    '''
    p[0] = '\n<ul>' + p[2] + p[3] + '\n</ul>'

def p_Z(p):
    '''
    Z : listItem Z
        | empty
    '''
    if len(p)==3:
        p[0] = p[1] + p[2]
    else: 
        p[0] = p[1]

def p_listItem(p):
    '''
    listItem : o_ListItem L c_ListItem
    '''
    p[0] = '\n<li>' + p[2] + '</li>'

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
        | empty
    '''
    if len(p) == 3:
        p[0] = p[1] 


def p_informalTable(p):
    '''
    informalTable : o_InformalTable MO c_InformalTable
                | o_InformalTable TG c_InformalTable
    '''
    if len(p) == 4:
        p[0] = '\n<table>' + p[2] + p[3] + '\n</table>'
    else:
        p[0] = '\n<table>' + p[2] + '\n</table>'

def p_TG(p):
    '''
    TG : tgroup TG
        | tgroup
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_MO(p):
    '''
    MO : mediaObject MO
        | mediaObject
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_tgroup(p):
    '''
    tgroup : o_Tgroup tbody c_Tgroup
            | o_Tgroup tbody tfoot c_Tgroup
            | o_Tgroup thead tbody c_Tgroup
            | o_Tgroup thead tbody tfoot c_Tgroup
    '''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p)== 5:
        p[0] = p[2] + p[3]
    else:
        p[0] = p[2] + p[3] + p[4]

def p_tbody(p):
    '''
    tbody : o_Tbody ROW c_Tbody
    '''
    p[0] = '\n<tbody>' + p[2] + '\n</tbody>'

def p_tfoot(p):
    '''
    tfoot : o_Tfoot ROW  c_Tfoot
    '''
    p[0] = '\n<tbody>' + p[2] + '\n</tbody>'

def p_thead(p):
    '''
    thead : o_Thead ROW c_Thead
    '''
    p[0] = '\n<tbody>' + p[2] + '\n</tbody>'

def p_ROW(p):
    '''
    ROW : o_Row W c_Row
    '''
    p[0] = '\n<tr>' + p[2] + '</tr>'

def p_W(p):
    '''
    W : entry W
        | entrytbl W
        | entry
        | entrytbl
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_entrytbl(p):
    '''
    entrytbl : o_Entrytbl tbody c_Entrytbl
            | o_Entrytbl thead tbody c_Entrytbl
    '''
    if len(p) == 3:
        p[0] = '\n<td>' + p[2] +'\n</td>'
    else:
        p[0] = '\n<td>' + p[2] + p[3] + '\n</td>'

def p_entry(p):
    '''
    entry : o_Entry J c_Entry
    '''
    p[0] = '\n<td>' + p[2] + '</td>'

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
        | texto 
        | itemizedList 
        | important 
        | para 
        | simPara 
        | mediaObject 
        | COMMENT 
        | abstract 
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

# Defino el string vacio
def p_empty(p):
    ''' 
    empty : 
    '''
    p[0] = ''

# Manejo de errores sintacticos
def p_error(p):
    print(f"Error de sintaxis en la entrada: {p.value}")


# **********OPCIONES PARA INGRESAR TEXTO XML**********

# Construye el lexer
lexer = lex.lex()
# optimize=1,lextab="footab"

parser = yacc.yacc()

def parse_file(filename):
    
    with open(filename, 'r') as file:
        content = file.read()
        data = (parser.parse(content))

        # Nombre del archivo de salida
        file_name = "archivo.html"

        # Escribir el contenido en el archivo
        with open(file_name, "w") as file:
            file.write(data)

# Llama a la función parse_file() con el nombre del archivo como argumento
parse_file('../prueba/prueba3.xml')


