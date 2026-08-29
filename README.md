# 100 Dni z Pythonem

Moje rozwiązania i notatki z kursu [**100 Days of Code: The Complete Python Pro Bootcamp**](https://www.udemy.com/course/100-days-of-code/) Angeli Yu na Udemy. Każdy folder `dzien X` odpowiada jednemu dniowi kursu i zawiera samodzielny skrypt lub mini-projekt. Rozwiązania nie są przepisane 1:1 z kursu — część z nich rozbudowałem o dodatkową walidację danych, obsługę wyjątków czy dodatkową logikę.

**Postęp:** 19 / 100 dni ✅ (ostatnia aktualizacja: dzień 19 — Wyścig żółwi)

## Spis treści

| Dzień | Projekt | Główne zagadnienia |
|---|---|---|
| 01 | [Generator nazw zespołu](<dzien 1>) | zmienne, f-stringi, `input()`/`print()` |
| 02 | [Kalkulator napiwku](<dzien 2>) | operacje arytmetyczne, formatowanie liczb |
| 03 | [Treasure Island + Pizza Deliveries](<dzien 3>) | `if`/`elif`/`else`, wczesne wyjście (`sys.exit()`), kolorowa grafika ASCII (kody ANSI) |
| 04 | [Papier, kamień, nożyce + 2 mini-gry](<dzien 4>) | moduł `random` (`randint`, `choice`), ASCII art, warunki |
| 05 | [Generator haseł](<dzien 5>) | pętle `for`, listy, `random.shuffle` |
| 06 | [Reeborg's World — labirynt](<dzien 6>) | funkcje, sterowanie robotem, redukcja powtórzeń kodu |
| 07 | [Hangman](<dzien 7>) | listy, pętla `while`, śledzenie stanu gry (odgadnięte/błędne litery) |
| 08 | [Szyfr Cezara](<dzien 8>) | funkcje, indeksowanie alfabetu, przesunięcie modulo, wieloużytkowa pętla programu |
| 09 | [Silent Auction](<dzien 9>) | słowniki, iteracja po kluczach, wyszukiwanie najwyższej oferty |
| 10 | [Kalkulator](<dzien 10>) | funkcje jako wartości, walidacja danych wejściowych, obsługa `ZeroDivisionError`, kontynuacja obliczeń na wyniku poprzedniego działania |
| 11 | [Blackjack](<dzien 11>) (projekt zaliczeniowy) | dynamiczna wartość Asa (1 lub 11), logika krupiera dobierającego karty do 17, ukrywanie drugiej karty krupiera, rozgrywka w pętli |
| 12 | [Zgadnij liczbę](<dzien 12>) | wybór poziomu trudności, walidacja wejścia, docstringi, podział logiki na funkcje |
| 13 | [Debugging](<dzien 13>) | czytanie cudzego kodu, znajdowanie i naprawa błędu na podstawie tracebacku |
| 14 | [Higher Lower — porównanie kont](<dzien 14>) | porównywanie danych liczbowych, zapobieganie powtórzeniom tych samych profili, wielorundowa rozgrywka |
| 15 | [Automat do kawy](<dzien 15>) | stan automatu w słownikach (`MENU`, `RESOURCES`), walidacja wrzucanych monet, wydawanie reszty |
| 16 | [Automat do kawy (OOP)](<dzien 16/oop-coffee-machine-start>) | programowanie obiektowe, klasy `CoffeeMaker`, `Menu`, `MoneyMachine`, podział na moduły |
| 17 | [Quiz Game](<dzien 17/quiz-game-start>) | OOP, współpracujące klasy `Question` i `QuizBrain`, lokalna baza pytań prawda/fałsz |
| 18 | [Grafika żółwia: figury, spirograf, random walk, Hirst Painting](<dzien 18>) | moduł `turtle`, `colorgram` — ekstrakcja palety kolorów z obrazu i odtworzenie jej jako siatki kropek |
| 19 | [Wyścig żółwi (zakłady)](<dzien 19>) | moduł `turtle`, `screen.textinput()`, symulacja wyścigu, logika wygranej/przegranej zakładu |

*(tabela będzie uzupełniana wraz z postępem kursu)*

## Technologie

- Python 3.10+
- biblioteka standardowa: `random`, `string`, `sys`
- `turtle` — grafika żółwia
- [`colorgram.py`](https://pypi.org/project/colorgram.py/) — ekstrakcja dominujących kolorów z obrazu (dzień 18)

## Jak uruchomić

Każdy projekt jest samodzielnym skryptem. Aby uruchomić wybrany dzień:

```bash
git clone https://github.com/SurQwaski/100-dni-z-pythonem.git
cd 100-dni-z-pythonem
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install colorgram.py        # potrzebne tylko dla dnia 18
python3 "dzien 5/password_generator.py"
```

## O kursie

Kurs uczy Pythona od podstaw (zmienne, pętle, funkcje) przez programowanie obiektowe, aż po GUI, web scraping, pracę z API, automatyzację i podstawy web developmentu (Flask). Ten folder to mój dziennik postępów i miejsce, w którym utrwalam materiał, pisząc kod samodzielnie po każdej lekcji — bez przepisywania gotowych rozwiązań z kursu.
