### Ryhmä 3 projektisuunnitelma, RAT projekti

#### Projektin tavoite ja tarkoitus
Projektin tarkoituksena on tuottaa ohjelmisto, jolla yritys voi hallita, ylläpitää ja päivittää tietokoneitaan. Tällä on tarkoitus helpottaa huomattavasti IT-osaston toimintaa, jotta jokaisella koneella ei tarvitse käydä fyysisesti paikan päällä asentamassa mm. jokaista päivitystä. 

#### Asiakas
Firma Oy, it-osasto 

#### Asiakasvaatimukset/käyttäjätarinat

Ohjelmistolta vaaditaan ainakin seuraavat ominaisuudet:

•	tiedoston siirto clientiltä serverille ja vice versa

•	pääsy terminaaliin ja output etäkoneelle

•	ohjelman suoritus

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

HYVÄKSYMISKRITEERIT (Acceptance criteria): 
ehdot, jotka kuvaavat miten käyttäjätarinassa kuvatun toiminnan toteutuminen voidaan valmiissa tuotteessa arvioida:

Tiedoston siirto, pääsy terminaalin ja ohjelman suoritus onnistuu etänä IT-osastolta

#### Ohjelmointikielet ja -teknologiat
Python, socket: backendin pohja
Graafinen käyttöliittymä: QT/Tkinter GUI 

#### Aikataulu
Viikko 1-2: projektin ideointi + suunnitelma, dokumentointi, projektin ajanhallinta/aikataulu, github repo, forkkaus, kloonaus, pull request, koodin pohja, virtuaaliympäristöt (win 10, Ubuntu), port forward
 
#### Mahdolliset roolit/työnjako, jos ryhmässä useita henkilöitä 
Kai: RAT:n perus toiminnallisuus, socket

Jorma: Virtuaaliympäristöt, joissa testaus suoritetaan, RAT:n perus toiminnallisuus

Keijo: Projektin aikataulu, RAT:n perus toiminnallisuus

