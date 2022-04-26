# Arkkitehtuurikuvaus

## Rakenne



## Käyttöliittymä
Käyttöliittymässä on kolme erilaista näkymää: 
- Kirjautuminen
- Rekisteröityminen
- Pelin pelaaminen

## Päätoiminnallisuudet
Päätoiminnallisuuksien sovelluslogiikkaa sekvenssikaavioilla:
### Kirjautuminen sisään
```mermaid
sequenceDiagram
user-)login: click "Start game"
login-)verification: login("test", "abc123")
verification-)login_information: "test", "abc123"
login_information--)verification: user
verification--)login: user
login-)main: "Game starts..."

```
