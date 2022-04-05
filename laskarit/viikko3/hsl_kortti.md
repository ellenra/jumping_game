```mermaid
sequenceDiagram
  main-)Laitehallinto: HKLLaitehallinto
  main-)Rautatietori: Lataajalaite()
  main-)Laitehallinto: lisaa_lataaja(rautatietori)
  main-)Ratikka6: Lukijalaite()
  main-)Laitehallinto: lisaa_lukija(ratikka6)
  main-)Bussi244: Lukijalaite()
  main-)Laitehallinto: lisaa_lukija(bussi244)
  main-)Lippuluukku: Kioski()
  Kalle-)Lippuluukku: osta_matkakortti(Kalle)
  main-)Rautatietori: lataa_arvoa(kallen_kortti, 3)
  
```
