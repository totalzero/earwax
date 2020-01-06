projekt earwax - koncepcja gry fps, czyli jak przedstawiæ swiat gry np. typu fps zupe³nie bez grafiki, z samym dzwiêkiem.

Projekt zupelnie szkoleniowy - staram sie doskonalic swoj warsztat programistyczny.
projekt napisany w calosci w pythonie, wykorzystuje biblioteke pyglet
http://pyglet.org/
do komunikacji z screenreaderami wykorzystalem biblioteke Tolk
https://github.com/dkager/tolk
do utworzenia pliku exe wykorzystalem auto py to exe
https://pypi.org/project/auto-py-to-exe/
Uwaga!!!
koniecznie trzeba miec zainstalowanego screenreadera - np. nvda
https://www.nvda.pl
-Puki co najlepiej dziala wlasnie z tym programem, testowane rowniez z JAWS14 - ale ma jakis konflikt, pewnie go rozwiaze ... kiedys.

tworzac ta gre mam na celu przede wszystkim:
Zastanowic sie jak przedstawic swiat, tak aby byl on zrozumialy i w pelni odbierany przez gracza, zupelnie bez uzycia grafiki.
-Gra jest domyslnie przeznaczona raczej dla niewidomych, jako, ze ja sam programuje jako niewidomy, i pisalem od poczatku z wykorzystaniem bibliotek do komunikacji z screenreaderem - co to jest screenreader odsylam do strony nvda.pl
skutek tego jest taki, ze bez tego programu o ktorym wspominam powyzej bedzie mnosto bledow.... raczej

ogolnie to prosze wszystkich o wyrozumialosc - jest to moj pierwszy projekt, jest on mocno nie doskonaly i pelen bledow, za rowno koncepcyjnych jak i kodowych.

Drogi profesjonalny programisto, zanim zajrzysz w kod tego nieszczesnego projektu - zazyj porzadna dawke czegos na uspokojenie.
Bardzo bym nie chcial miec cie na sumieniu przez moj kod.

klawiszologia
z- aktualna pozycja wyrazona w wsp x y
lctrl - strzal
llshift - wybor miedzy wyjsciami a przedmiotami na ziemi
f - przelacza sie po przedmiotach lub wyjsciach - zalerznie od ustawienia lshift
enter potwierdza wybor, podnosi bron/amunicje, przechodzi do innej lokacji
q - wybor celu 
m - nazwa lokacji w jakiej sie znajduje
h - hp gracza
n - lista wszystkich npcow w grze wraz z ich aktualnymi wsp
c - lista objektow na ziemi, czyli broni i amunicji i tak dalej
e - lista wyjsc wraz z wsp
a - aktualny poziom amunicji i magazynkow
tab - zmiana broni
i - lista przedmiotow w ekwipunku
x - cele misji
