"""

a) Joseph Carl Robnett Licklider var først ut med "internett", da het det ARPANET. Og 
 hoved designet var til bruk av forsvaret.

b) Paritet som feildeteksjonsmetode bruker én bit for å sjekke om antallet til 1, og
0 er partall / odetall for en byte.

c) Cirucuit switch: Ikke så effektiv mtp båndbredde. En forbindelse blir etablert før overføring
starter, og den blir avsluttet når overføringen er ferdig. Sender og mottaker blir koblet til en
dedikert linje, så lenge de holder på. Først da kommunikasjonen er ferdig blir linjen avkoblet.

Packet switch: Noder deler båndbredde med hverandre. Data blir sendt i små pakker, med
respektivt ID, så pakker kan ankomme i tilfeldig rekkefølge, og enda være i godt behold.

d) De 5 protokoll lagene er :
Applikasjon: Opp. er å sørge for at data fra applukajonsprossessene blir sendt til riktig prossess.
Transport: Opp. er å overføre datablokk mellom 2 endepunkt. Gjemmer også funksjone til data.
Nettverk: Opp. er å ordne data slik at det blir rutet gjennom et nettverk. Den finner 
  vei for dataer til deres spesifikke nettverk.
Link: Opp. er å overføre en datablokk mellom 2 punkter. Blir også sjekket for feil, slik at 
  overvføringe skjer feilfritt.
Fysisk: Opp. er å overføre en bit mellom 2 punker. Her blir også egenskapen til en bit gjort.

e) En ruter har oppgave i å videresende nettverkk pakker (f.eks. IP pakker) til deres 
riktige mottaker. 










"""


