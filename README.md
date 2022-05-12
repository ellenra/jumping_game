# Jumping Game

Peli on simppeli tasohyppelypeli johon kirjaudutaan omalla käyttäjätunnuksella.

## Dokumentaatio

[Vaatimusmaarittely](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/ellenra/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[1. Release](https://github.com/ellenra/ot-harjoitustyo/releases/tag/viikko5)

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


