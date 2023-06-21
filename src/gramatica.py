'''
Regla 1:Σ → DOCTYPE article Book 
Regla 2:Σ → DOCTYPE article Article

Regla 3: Article : <article> Title  A article
Regla 4: Article → <article> Title Info A </article>
Regla 5: A → AA | ItemizedList  | Important  | Para  | SimPara  | ArticleInfo | Address  | MediaObject  | InformalTable  | Comment  | Abstract | SimpleSect | Section | λ

Regla 6:Book→ <book> Title B </book>
Regla 7:Book→ <book> Title Info B </book>
Regla 8:B → BB | ItemizedList  | Important  | Para  | SimPara  | ArticleInfo  | Section  | 		Address  | MediaObject  | InformalTable | Comment | Abstract | SimpleSec | Article 
Etiquetas para secciones

Regla 9: Section → <section> Title S </section> 
Regla 10: Section → <section> Title Info S </section> 
Regla 11: S → SS | ItemizedList | Important | Para | SimPara | Address | MediaObject | InformalTable | Comment | Abstract 

Regla 12: SimpleSec → <simplesect> S </simplesect>
Regla 13: SimpleSec → <simplesect> Info S </simplesect>
Regla 14: SimpleSec → <simplesect> Title S </simplesect>
Regla 15: SimpleSec → <simplesect> Info Title S </simplesect>

Regla 16: Set → <set>  Title Subtitle SB  </set> 
Regla 17: SB → SB SB | set | book
Etiquetas básicas de párrafo

Regla 19: Info → <info> I <info>
Regla 20: I → II | MediaObject  | Abstract  | Address  | Author  | Date  | Copyright  | Title 

Regla 21: Abstract → <abstract> Title R </abstract>
Regla 22: Abstract → <abstract> R </abstract> 
Regla 23: R →  RR | Para | SimPara 

Regla 24: Address → <address> D </address> 
Regla 25: D → DD |  #texto | Street | City | State | Phone | Email |   λ

Regla 26: Author → <author> FirtsName U Surname  </author> 
Regla 27: U → FirstName U | U Surname 

Regla 28: Copyright → <copyright> Year C </copyright> 
Regla 29: C →  Year C | C Holder |  λ


Regla 30: Title → <title> T </title>
Regla 31: T  → TT | #texto | Emphasis | Link | Email

Regla 32: Chapter → <chapter> Title H </chapter>
Regla 33: Chapter → <chapter> Title Para H </chapter>
Regla 34: H →  HH | Section | SimpleSec | Title | Para | Important | Informaltable | Table | Mediaobject | λ

Regla 35: Appendix → <appendix> Title, Chapter </appendix>

Regla 36: SimPara → <simpara>  X </simpara> 
Regla 37: Emphasis → <emphasis>  X </emphasis>
Regla 38: Comment → <comment>  X </comment>
Regla 39: X →  XX | #texto | Emphasis | Link | Email | Author | Comment 

Regla 40: Link →  <link xlink:href=” #url ”> X </link>

Regla 41: Para → <para> P </para> 
Regla 42: P →  PP | #texto | Emphasis |Link |Email | Author | Comment | ItemizedList | Important | Address | MediaObject | InformalTable 

Regla 43: Important → <important> M </important>
Regla 44: Important → <important> Title M </important>
Regla 45: M →  MM | ItemizedList | Important | Para | SimPara | Adress | MediaObject | InformalTable | Comment | Abstract 

Regla 46: FirstName → <firstname> Y </firstname>
Regla 47: Surname →  <surname> Y </surname>
Regla 48: Street →  <street> Y </street>
Regla 49: City →  <city> Y </city>
Regla 50: State →  <state> Y </state>
Regla 51: Phone →  <phone> Y </phone>
Regla 52: Email →  <email> Y </email>
Regla 53: Date →  <date> Y </date>
Regla 54: Year →  <year> Y </year>
Regla 55: Holder →  <holder> Y </holder>
Regla 56: Y → YY | #texto | Link | Emphasis | Comment 
Etiquetas de multimedia y videos

Regla 57: MediaObject → <mediaObject> Info Vi </mediaObject> 
Regla 58: MediaObject → <mediaObject> Vi </mediaObject>
Regla 59: Vi →  ViVi | VideoObject | ImageObject

Regla 60: VideoObject → <videoObject> Info VideoData </videoObject>
Regla 61: VideoObject → <videoObject> VideoData  </videoObject>
Regla 62: VideoData → <videoData  fileref=”#url” />
Regla 63: ImageObject → <imageObject> Info ImageData </imageObject> 
Regla 64: ImageObject → <imageObject> ImageData </imageObject>
Regla 65: ImageData → <imageData fileref=”#url” />
Etiquetas de listas

Regla 66: ItemizedList → <itemizedlist> ListItem Z <itemizedlist> 
Regla 67: Z → ZZ | ListItem | λ 

Regla 68: ListItem → <listitem> L <listitem>
Regla 69: L → LL | ItemizedList | Important | Para | SimPara | Address | MediaObject | InformalTable | Comment | Abstract 
Etiquetas para tablas

Regla 70: InformalTable → <informalTable> TG </informalTable>
Regla 71: TG → TG TG | MediaObject | TGroup

Regla 72: tgroup → <tgroup> tbody thead tfoot </tgroup> 
Regla 73: tgroup → <tgroup> thead tbody thead tfoot </tgroup>
Regla 74: tgroup → <tgroup> tfoot tbody thead tfoot </tgroup>
Regla 75: tgroup → <tgroup> thead tfoot tbody thead tfoot </tgroup>

Regla 76: tbody → <tbody> Row Row </tbody>
Regla 77: Row → RowRow | row | λ

Regla 78: row → <row> W </row>
Regla 79: W →  WW | entry| entrytbl

Regla 80: entrytbl → <entrtbl> tbody </entrtbl>
Regla 81: entrytbl → <entrtbl> thead tbody </entrtbl>

Regla 82: entry →  <entry> J </entry>
Regla 83: J → JJ | #texto| ItemizedList|Important|Para| SimPara|MediaObject| |Comment| Abstract
'''