```mermaid
 classDiagram
      Pelilauta "*" --> "1" Peli
      Pelaaja --> Peli
      Pelaaja -- Pelinappula
      Pelinappula -- Ruutu
      Ruutu -- Pelilauta
```
