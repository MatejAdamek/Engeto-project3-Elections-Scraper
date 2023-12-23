Engeto projekt 3
Třetí projekt na Python Akademii od Engeta.

Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete zde.

Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt . Pro instalaci doporučuji použít nové virtální prostředí a s nainstalovaným manažerem spustit následovně:

$ pip3 --version                     # overim verzi manazeru

$ pip3 install - r requirements.txt  # nainstalujeme knihovny

Spuštění projektu
Spuštění souboru projekt3.py v rámci přík. řádku požaduje dva povinné argumenty.

python projekt3.py <odkaz-uzemniho-celku> <vysledny-soubor>

Následně se vám stáhnou výsledky jako soubor s příponou .csv.

Ukázka projektu
Výsledky hlasování pro okres Prostějov:

argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
argument: vysledky_prostejov.csv
Spuštění programu: python projekt3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_prostejov.csv'

Částečný výstup:

code, location, registered, envelopes, valid,...
506761, Alojzov, 205, 145, 144, 29, 0, 0, 0, 0, 5, 17, 4, 1, 1, 0, 0, 0, 5, 32, 0, 0, 0, 0, 0, 1, 1, 15,0
589268, Bedihošť, 834, 527, 524, 51, 0, 0, 28, 1, 13, 123, 2, 2, 14, 1, 0, 0, 6, 140, 0, 0, 26, 0, 0, 0, 0, 82, 1