# Open Election Data API

![Offene Wahlen](https://github.com/OKFNat/offenewahlen-at/blob/master/images/logos/ow-at.png)

Open Election Data API ist ein Open Source Projekt von [Offene Wahlen Österreich](https://offenwahlen.at), koordiniert vom Verein [Open Knowledge Österreich](https://okfn.at).

[![Build Status](https://travis-ci.org/OKFNat/offenewahlen_api.svg?branch=master)](https://travis-ci.org/OKFNat/offenewahlen_api)

[![Coverage Status](https://coveralls.io/repos/github/OKFNat/offenewahlen_api/badge.svg?branch=master)](https://coveralls.io/github/OKFNat/offenewahlen_api?branch=master)

**Technisches**

Es handelt sich um eine [Django](https://www.djangoproject.com/)-App (Python Web-Framework) mit einer [PostgreSQL](https://www.postgresql.org/)-Datenbank. Es wird nur Open Source Software verwendet, und auch der selbst entwickelte Code steht unter der [MIT](https://opensource.org/licenses/MIT)-Lizenz frei zur verfügung.

**Das Repository**

In diesem GitHub-Repository wird gemeinsam der Code entwickelt, sowie das Projektmanagement mitsamt Dokumentation verwaltet.

**Ressourcen**

Über die folgenden Ressourcen findest du alle relevanten Informationen zu dem Projekt:
* [Wiki](https://github.com/OKFNat/offenewahlen-api/wiki): Wiki von diesem Repository. Dient zur Verwaltung des Wissens und zur Dokumentation. Erster Anlaufpunkt, wenn man mehr über das Projekt erfahren möchte.
* [Milestones](https://github.com/OKFNat/offenewahlen-api/milestones?direction=asc&sort=due_date&state=open): Hier werden die Projekt-Milestones verwaltet. Gute Übersicht zum Projektstand.
* [Board](https://github.com/OKFNat/offenewahlen-api/milestones#boards?repos=96933110): Hier werden die Projekt-Aktivitäten mit Hilfe von Milesontes und Issues verwaltet. Hier sieht man, wer was bis wann macht und wie man sich einbringen kann.
* [OKFNat/offenewahlen-at](https://github.com/OKFNat/offenewahlen-at): Repository zum Projekt Offene Wahlen Österreich. Das dazugehörige [Wiki](https://github.com/OKFNat/offenewahlen-at/wiki) ist eine umfassende Sammlung von Wissen rund um Wahlen und Open Data - von Wahlforschung über Wahlrecht bis hin zu Visualisierungen und Tools.
* [offenewahlen.at](http://offenewahlen.at/): Website des Projektes Offene Wahlen Österreich. Dort findest du Infos zu weiteren Aktivitäten.

## INSTALL

Hier wird das Installieren der Django-App auf den Localhost zum Entwickeln erklärt. Die Django-App läuft auf MacOS, Win und Linux.

**1. Benötigte Software installieren**

Um die App lokal auf deinem Rechner laufen zu lassen, benötigst du:
* Python 3 ([hier](https://www.python.org/downloads/))
* pip ([hier](https://pip.pypa.io/en/stable/), falls nötig)
* virtualenv ([hier](https://virtualenv.pypa.io/en/stable/) oder [hier](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
* PostgreSQL ([hier](https://www.postgresql.org/))

**2. GitHub Repository runterladen**

Nach erfolgreicher Installation der benötigten Software: Öffne deine Shell und gehe in den Ordner, in dem du die App haben möchtest. Dort musst du das GitHub-Repository hinein klonen.

```bash
git clone https://github.com/OKFNat/offenewahlen_api.git
ls
```

**3. Setup Virtual Environment**

Du solltest das runtergeladene Repository in deinem Ordner sehen. Geh in den Root-Ordner und erstelle darin das Virtual Environment.

```bash
cd offenewahlen_api/
virtualenv venv
source venv/bin/activate
```

Nach dem Erstellen und Aktivieren des Virtual Environment sollte man checken, welche Python Version im Virtual Environment verwendet wird.

```bash
python --version
```

Dies sollte eine Python 3.x Version ausgeben. Wenn nicht, gibt es zwei Möglichkeiten, dies zu fixen:
1. Den Link der beim Ausführen von `which python` innerhalb des Virtual Environments ausgegeben wird auf den Pfad von Python 3 setzen (z. B. auf Ubuntu/Linux: `ln -s venv/bin/python /usr/bin/python3`).
2. Den Pfad für Python 3 beim Erstellen des Virtual Environment mittels `-p`-Flag übergeben (z. B. auf Ubuntu/Linux: `virtalenv venv -p=/usr/bin/python3`).
3. Beim folgenden Ausführen von Befehlen `python3` statt `python` verwenden.

Nun kannst du in das Virtual Environment die benötigten Python Packages aus der `requirements.txt` Datei installieren. Der Vorteil: Die Packages werden dadurch nur im Virtual Environment installiert und nicht auf deinem Betriebssystem.

```bash
pip install -U -r requirements.txt
```

Settings laden.
```
export DJANGO_SETTINGS_MODULE=offenewahlen_api.settings_development
```

**4. Datenbank initialisieren**

Die App ist an sich jetzt schon funktionsfähig, es muss aber noch die Datenbank initalisiert werden.

```bash
python src/manage.py migrate
```

Nun sollten die Tabellen in der PostgreSQL-Datenbank angelegt sein. Mit [pgAdmin](https://www.pgadmin.org/), einem PostgreSQL-GUI, kannst du dies z. B. ansehen.

**5. Django-Befehle ausführen**

Wenn du `python src/manage.py` aufrufst, siehst du eine Liste an Befehlen, die die die Django-App zur Verfügung stellt. Um den Server lokal zu starten, benötigst du den Befehl `runserver`.

```bash
python src/manage.py runserver
```

**6. Django-App im Browser anzeigen**

Wenn soweit alles gepasst hat, solltest du nun die App im Browser unter [http://localhost:8000](http://localhost:8000) sehen können.

## DEVELOPMENT

Alle Infos rund um das Entwickeln sind über [DEVELOPMENT.md](DEVELOPMENT.md) zu finden.

**Ersten Schritte**

1. Dieses Repository durchgehen.
2. Doku in [API Wiki](https://github.com/OKFNat/offenewahlen-api/wiki) durchgehen.
3. Aufgabenbereiche in [Projects](https://github.com/OKFNat/offenewahlen-api/projects) ansehen.
4. Task-Management via [Board](https://github.com/OKFNat/offenewahlen-api/milestones#boards?repos=96933110) ansehen.

## DOKUMENTATION

Die Dokumentation findet in diesem Repository in den Files [README.md](README.md) und [DATA.md](DATA.md) sowie dem dazugehörigen [GitHub Wiki](https://github.com/OKFNat/offenewahlen-api/wiki) statt. Das Wiki ist eine frei zugängliche Wissens-Sammlung rund um die App und für alle offen zum Verwenden und Verändern.

## MITMACHEN

Dies ist ein Open Source Projekt, daher lebt das Projekt von vielen helfenden Händen.

Wenn du das Projekt gerne ehrenamtlich unterstützen möchtest, melde dich einfach [direkt bei uns](http://offenewahlen.at/kontakt). Jeder noch so kleiner Beitrag ist wichtig und hilfreich.

Aktuell sind wir vor allem **auf der Suche nach einer Person, die uns bei Kommunikation/PR unterstützt**.

Anbei eine paar Ideen, wie man sich bei dem Team einbringen kann:
* **Kommunikation:** hilf mit beim Bloggen, bei Social Media oder beim erarbeiten einer Kampagne.
* **Fehler melden**: Wenn du einen Fehler gefunden hast, erstelle bitte ein [Issue](https://github.com/OKFNat/offenewahlen-api/issues/new) dazu. Immer am besten mit Screenshot und möglichst exakter Fehlerbeschreibung.
* **Fehler beheben**: Sieh dir die [Issues](https://github.com/OKFNat/offenewahlen-api/issues) an und schließe eines. Nähere Infos unter **[Development](#development)**.
* **Web-Design / Grafik**: mach bei der Daten-Visualisierung am Frontend mit. Auch GrafikerInnen für Logos etc. sind gesucht.
* **Web-Entwicklung, UX/UI**: alles was mit klassicher Website-Entwicklung zu tun hat - vor allem Frontend UX/UI. Von HTML5 über CSS3 bis hin zu JavaScript (jQuery, Bootstrap, D3).
* **Django EntwicklerIn**: die App ist mit dem Web-Framework Django umgesetzt. Daher ist hier Know-How sehr gesucht.
* **Wahl-Know-How**: Fachwissen rund um Wahlen ist natürlich essentiell. Wenn dich Wahlen interessieren, gibt es eine Vielzahl von Möglichkeiten dich einzubringen und zu lernen. Egal ob bei der Visualisierung, bei der Kommunikation oder der Dokumentation.
* **Übersetzen**: die App ist mehrsprachig. Aktuell ist geplant, in die österr. Minderheitensprachen zu übersetzen, aber es sind keine Grenzen gesetzt.
* **Dokumentation**: Die Dokumentation zur App wird für verschiedene User-Gruppen passend aufbereitet bzw. kann sie auch in Englisch übersetzt werden.
* **[Newsletter](http://offenewahlen.at/newsletter)**: abonniere den Newsletter und bleib am Laufenden.
* **Funding**: Wir suchen passende Funding-Möglichkeiten, um das Projekt kontinuierlich weiter wachsen zu lassen und zu verbessern. Wenn du eine Idee hast, wie man zu Förderungen kommt oder mit uns gemeinsam einreichen möchtest, meld dich bitte.
* **[Spenden](https://offenewahlen.at/spenden)**: Du kannst uns auch finanziell unterstützen, indem du eine kleine Spende da lässt. Das Geld wird Projekt-bezogen verwendet und dient zum Verbessern der verschiedenen Aktivitäten von Offene Wahlen Österreich - von der API über den Datenstandard bis hin zum Abhalten von Coding-Workshops.

**Ersten Schritte**

Es empfiehlt sich, zu Beginn die Dokumentation und unser Projekt-Management kurz anzusehen, um einen Überblick zum Projekt zu bekommen. Dies muss nicht komplett bzw. in einer gewissen Reihenfolge erfolgen.
* Dieses Repository durchlesen.
* Doku in [API Wiki](https://github.com/OKFNat/offenewahlen-api/wiki) durchgehen.
* Entwicklungs-Stand in [Milestones](https://github.com/OKFNat/offenewahlen-api/milestones?direction=asc&sort=due_date&state=open) ansehen.
* Aufgabenbereiche in [Projects](https://github.com/OKFNat/offenewahlen-api/projects) ansehen.
* Task-Management via [Board](https://github.com/OKFNat/offenewahlen-api/milestones#boards?repos=96933110) ansehen.
* [Offene Wahlen Österreich Wiki](https://github.com/OKFNat/offenewahlen-at/wiki) durchgehen.
* [offenewahlen.at](https://offenewahlen.at) besuchen und Newsletter abonnieren.

Wenn du Fragen hast, kannst du dich jederzeit via Email (info@offenewahlen.at) oder unter [Kontakt](http://offenewahlen.at/kontakt) melden.

## DATEN

Für die App werden verschiedene Daten als Grundlage verwendet. Einige werden von anderen übernommen, andere von uns selber zusammen getragen. Beachte: Wir erheben keinen Anspruch auf Vollständigkeit oder Korrektheit, die Qualität der vorhandenen Daten sollte aber recht gut sein. Unser Ziel ist es, erst mal alle notwendigen Daten für die *API* zusammen zu tragen. Danach sollen diese Schritt für Schritt erweitert werden. Wir freuen uns sehr über jede Unterstützung dabei. Wenn du einen Fehler findest, oder selber spannende Daten besitzt - **meld dich bitte!**


Die Basis-Daten dienen zum Setup der App und als Datengrundlage, um die Ergebnisse passend visualisieren zu können. Die Test-Daten werden zum Testen der einzelnen Prozess-Schritte verwendet. Dies ermöglicht ein verifizieren der App auf seine verschiedenen Funktionen - vom Datenimport bis hin zu Visualisierung.


Die so gesammelten und kuratierten Daten werden kontinuierlich in **Wikidata** importiert, um dies als primäres Repository für Unique-Identifiers rund um Wahlen aufzubauen. Dazu gibt es mit [OKFNat/offenewahlen-wikidata](https://github.com/OKFNat/offenewahlen-wikidata) ein eigenes Repository mit weiteren Infos.


Nähere Infos zu den einzelnen Daten findest du unter **[DATA.md](DATA.md)**.

## COPYRIGHT

Sämtlicher von uns entwickelter Quellcode ist Open Source und steht unter der [MIT](https://opensource.org/licenses/MIT)-Lizenz frei zur verfügung.

Von uns genutzte Software ist alles Open Source.

Alle Materialien wie Texte, Bilder und Folien die im Rahmen dieses Projektes erstellt werden, stehen unter [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), soweit nicht explizit anders erwähnt.

## GLOSSAR

**Coverage.py**

Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not. Coverage measurement is typically used to gauge the effectiveness of tests. It can show which parts of your code are being exercised by tests, and which are not.

**Coveralls.io**

Coveralls is a web service to help you track your code coverage over time, and ensure that all your new code is fully covered.

**Travis CI**

Travis CI is a hosted, distributed continuous integration service used to build and test software projects hosted at GitHub.

**Sphinx**

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It can create reports in pdf and html.
