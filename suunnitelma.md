### Ryhmä 3 projektisuunnitelma, RAT (Remote Access Tool) projekti

#### Projektin tavoite ja tarkoitus
Projektin tarkoituksena on tuottaa ohjelmisto, jolla yritys voi hallita, ylläpitää/valvoa tietokoneitaan. Tällä on tarkoitus helpottaa huomattavasti IT-osaston toimintaa, jotta jokaisella koneella ei tarvitse käydä fyysisesti paikan päällä asentamassa mm. jokaista päivitystä. 

#### Asiakas
Firma Oy, it-osasto 

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
Firma Oy:n it-vastaava

MITÄ (käyttäjän tavoite): 
IT-vastaava haluaa pääsyn Firman koneille etänä

MIKSI (perustelut miksi tarvitaan): 
Ohjelmistojen päivitys olisi sujuvaa eikä jokaisella koneella tarvitse käydä erikseen ajamassa päivityksiä

HYVÄKSYMISKRITEERIT: 
ehdot, jotka kuvaavat miten käyttäjätarinassa kuvatun toiminnan toteutuminen voidaan valmiissa tuotteessa arvioida:

Tiedoston siirto, pääsy terminaalin ja ohjelman suoritus onnistuu etänä IT-osastolta

#### Ohjelmointikielet ja -teknologiat
Python, socket: backend
Graafinen käyttöliittymä: QT/Tkinter GUI 

#### Aikataulu
Viikko 1-2: projektin ideointi + suunnitelma, dokumentointi, projektin ajanhallinta/aikataulu, github repo, forkkaus, kloonaus, pull request, koodin pohja, virtuaaliympäristöt (win 10, Ubuntu), port forward

Viikko 3-4: projektin koodin pohja ja ominaisuuksien toteuttaminen, GUI tkinterillä, testaus virtuaalikoneiden/fyysisten koneiden välillä
 
#### Mahdolliset roolit/työnjako, jos ryhmässä useita henkilöitä 
Kai: RAT:n perus toiminnallisuus, socket

Jorma: Virtuaaliympäristöt, joissa testaus suoritetaan, RAT:n perus toiminnallisuus

Keijo: Projektin aikataulu, RAT:n perus toiminnallisuus

