```mermaid
 classDiagram
      Pelilauta "*" --> "1" Peli
      Pelaaja --> Peli
      Pelaaja -- Pelinappula
      Pelinappula -- Ruutu
      Ruutu -- Pelilauta
      Ruutu : int Aloitusruutu
      Ruutu : int Vankila
      Ruutu : int Sattuma ja yhteismaa
      Ruutu : int Asemat ja laitokset
      Ruutu : int Normaalit kadut
      
     
```
