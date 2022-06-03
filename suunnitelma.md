### Ryhmä 3 projektisuunnitelma, RAT (Remote Access Tool) projekti

#### Projektin tavoite ja tarkoitus
Projektin tarkoituksena on tuottaa ohjelmisto, jolla yritys voi hallita, ylläpitää/valvoa tietokoneitaan. Tällä on tarkoitus helpottaa huomattavasti IT-osaston toimintaa, jotta jokaisella koneella ei tarvitse käydä fyysisesti paikan päällä asentamassa mm. jokaista päivitystä. 

#### Asiakas
Yritys Oy, it-osasto 

#### Asiakasvaatimukset/käyttäjätarinat

Ohjelmistolta vaaditaan ainakin seuraavat ominaisuudet:

•	tiedoston siirto clientiltä serverille ja vice versa

•	pääsy terminaaliin ja output etäkoneelle

•	ohjelman/skriptin suoritus

•	mahdollisuus sammuttaa client tietokone

•	kuvakaappaus

Nice-to-have -ominaisuudet:

•	chat ominaisuus

•	port sniffer?

•	toimivuus Windows ja Linux ympäristöissä 


#### Käyttötapaukset

KUKA (käyttäjärooli): 
Yritys Oy:n it-vastaava

MITÄ (käyttäjän tavoite): 
IT-vastaava haluaa pääsyn Yrityksen koneille etänä

MIKSI (perustelut miksi tarvitaan): 
Yrityksen resurssien käytön, ohjelmiston ja yleisen tietoturvan valvonta ja hallinta. Ohjelmistojen päivitys olisi sujuvaa eikä jokaisella koneella tarvitse käydä erikseen ajamassa päivityksiä. 

HYVÄKSYMISKRITEERIT: 

Tiedoston siirto, pääsy terminaalin ja ohjelman/skriptin suoritus onnistuu etänä IT-osastolta

#### Ohjelmointikielet ja -teknologiat
Python, socket: backend

Graafinen käyttöliittymä: Tkinter GUI 

#### Aikataulu
Viikko 1-2: ideointi ja suunnittelu, dokumentointi, projektin ajanhallinta/aikataulu, github repo, fork, clone, pull request, koodin pohja, virtuaaliympäristöt (win 10, Ubuntu)

Viikko 3-4: projektin koodin pohja ja ominaisuuksien toteuttaminen, GUI QT:lla/tkinterillä, testaus virtuaalikoneiden/fyysisten koneiden välillä samassa aliverkossa

Viikko 5-6: Tkinteriin tutustuminen, Gui:n tekeminen, http versio vs socket versio, download ja upload

Viikko 7-8: Threading, chat-ikkuna, geo-sijainti, web-palvelin, josta IP ja portti haetaan 

#### Toteutus
Viikko 1-2: Projekti aloitettiin etähallintaohjelmiston ideoinnilla ja laatimalla suunnitelma ja aikataulu Monday.com:iin. Päädyimme SCRUM-tyyppiseen projektinhallintamenetelmään, jossa viikon sprinteillä oli oma tavoitteensa. Myös Githubin projetcs -osio otettiin käyttöön projektin tehtävien hallinnassa. Loimme repo(sitory)n Githubiin ja asensimme virtuaaliympäristöt (Windows 10 ja Ubuntu), jossa testaus suoritettaisiin.  

Viikko 3-4: Projektin koodin pohja luotiin, jossa perustoiminnallisuus oli osittain toimiva, jossa serveri ja client toimivat ensin lokaalisti. Tämän jälkeen kehitimme ohjelmaa niin että saimme otettua yhteyden virtuaalikoneiden välille sekä saman aliverkon koneiden välillä. Päädyimme GUI:n kehityksen osalta käyttämään Tkinteriä, johon tutustuimme ja teimme kokeiluja ja harjoituksia.

Viikko 5-6: Projektin commandline versioon saatiin lisättyä download-, upload- ja kuvankaappauksen toiminnallisuudet, joita esiteltiin välidemossa. Tässä vaiheessa projektia laadittiin hahmotelma lopullisesta GUI:n toteutuksesta. Testasimme myös http -yhteyttä hyödyntävää versiota, mutta päädyimme kuitenkin socket pohjaiseen versioon.

Viikko 7-8: Luotiin webpalvelin, josta server puolen admin käyttäjä voi tarkistaa ja tarvittaessa muuttaa käytettävän IP:n ja portin, ja josta client ohjelma noutaa ajankohtaisen käytössäolevan IP:n ja portin. Geo -funktiolla saadaan suuntaa-antava sijainti IP:n perusteella ja systeminfo kertoo client koneen järjestelmän tiedot. Skriptin suoritus myös onnistuu client koneella. Gui, thread ja chat..

#### Mahdolliset roolit/työnjako, jos ryhmässä useita henkilöitä 
Kai: RAT:n perus toiminnallisuus, socket

Jorma: Virtuaaliympäristöt, joissa testaus suoritetaan, RAT:n perus toiminnallisuus

Keijo: Projektin aikataulu, RAT:n perus toiminnallisuus

