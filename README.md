# Jumping Game

Peli on simppeli tasohyppelypeli johon kirjaudutaan omalla käyttäjätunnuksella.

## Dokumentaatio

[Käyttöohje](https://github.com/ellenra/jumping_game/blob/master/dokumentaatio/kayttoohje.md)

[Arkkitehtuurikuvaus](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/ellenra/jumping_game/blob/master/dokumentaatio/testaus.md)

[Vaatimusmaarittely](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)


## Asennus ja pelin aloitus
1. Asenna riippuvuudet komennolla:
> poetry install
2. Käynnistä peli komennolla:
> poetry run invoke start

## Komentorivitoiminnot

Ohjelman voi suorittaa komennolla:
> poetry run invoke start

### Testaus

Testit suoritetaan komennolla:
> poetry run invoke test

Testikattavuusraportti:
> poetry run invoke coverage-report

### Pylint

Pylintin tarkastukset tiedostossa .pylintrc komennolla:
> poetry run invoke lint


