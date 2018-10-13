# Receptář pro GitWorking workshop

Projekt slouží k vytvoření receptáře nejenom pro účastníky kurzů a workshopů PyLadies a jejich organizátory.

## Instalace
Pro instalaci receptáře není nic specifického potřeba krom několika bodů:
* Mít nainstalovaný Python (např. z [těchto stránek](https:\\www.python.org)), ideálně ve verzi 2.7 či 3.6
* Stáhnout si poslední verzi repozitáře z Githubu v zabaleném souboru [ZIP](https://github.com/hroncok/receptar/archive/master.zip) nebo si jej můžete naklonovat (git clone) z adresy https://github.com/hroncok/receptar
  * V případě stažení souboru ZIP je potřeba jej rozbalit do vámi zvolené vybrané složky
  * Pro klonovaný repozitář pomocí _clone_ rozbalování není nutné

## Spuštění
Pro spuštění _Receptáře_ potřebujete:
* V příkazové řádce změnit aktuální složku na takovou, do níž jste rozbalili stažený ZIP či v níž naklonovaný repozitář z Githubu pomocí _clone_
* V příkazové řádce či terminálu spustit příkaz
  * V případě, že máte nainstalovaný Python ve verzi 2.7 s vyšší 
```python
python receptar.py
```
  * či máte-li nainstalovaný Python ve verzi 3.6 a vyšší 
```python
python3 receptar.py
```

Aktuální verzi Pythonu, který máte nainstalovaný, můžete určit spuštěním 
```python
python --version
``` 
či 
```python
python3 --version
```

## Návod

## Testy
Jak spustit testy:

```shell
$ python3 -m pytest tests
````
Testování by bylo fajn, nicméně nemáme na něj dostatečnou lidskou kapacitu. Můžeš se zapojit do rozvoje projektu a testy
nám pomoci připravit.

## Zapojení se do tvorby
Pokud byste měli zájem se podílet na spolutvorbě tohoto _Receptáře_, napište prosím soukromou zprávu autorovi projektu [@hroncok](https://github.com/hroncok) či proveďte u sebe lokální změny a zašlete _Pull request_ na původní projekt. Autoři budou velmi rádi za jakékoliv kontruktivní návrhy, které vylepší stávající úroveň _Receptáře_ k lepšímu :sparkles:.


## Autoři projektu
Původním autorem a majitelem projektu je [@hroncok](https://github.com/hroncok), pod jehož dohledem je receptář udržován. Dalšími autorkami a autory jsou účastníci
workshopů a různých eventů od PyLadies.

## Licence
Protože samozřejmě víme jak moc je důležité duševní vlastnictví a jeho ochrana, tak i tento projekt je chráněn licencí.
Používáme licenci _MIT_ (více na [odkaz](https://choosealicense.com/licenses/mit/))
