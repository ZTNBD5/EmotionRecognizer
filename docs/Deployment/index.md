# Wdrożenie

### Implementacja
Serwis został zaimplementowany w języku Python przy użyciu frameworka Django.

### Opis działanie
Użytkownik jest proszony o podanie pliku CSV, który zawiera dane z EEG oraz z urządzeń peryferyjnych.
Następnie po kliknięciu przycisku "Analise emotions" plik jest przesyłany do serwisu i analizowany pod kątem
trzech uczuć: Valence, Arousal i Liking. Każde z uczuć jest wykrywane przy pomocy osobnego, wcześniej wytrenowanego
modelu. Wartość uczucia jest zwracana w skali od 0 do 1 i przedstawiona na grafie.

### Dane wejściowe
Plik wejściowy CSV musi zawierać 8064 wiersze i 40 kolumny. Każdy wiersz to kolejna próbka w czasie, a każda kolumna
to inny rodzaj próbki. Pierwsze 32 rodzaje próbek pochodzą z EEG, a kolejne 8 z urządzeń peryferyjnych.