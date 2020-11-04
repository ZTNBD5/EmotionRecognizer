# Raport danych

Dane składają się z dwóch części:
1. Metadane (`online_ratings.csv`, `video_list.csv`, `participant_ratings.csv`, `participant_questionnaire.csv`)
2. Dane uczące oraz testowe (katalog `data_preprocessed_python`)

#### Opis plików:
1. online_ratings.csv - jest to osobny eksperyment.  Ten plik nie będzie używany w naszym projekcie

Ten plik zawiera wszystkie indywidualne oceny wideo zebrane podczas samooceny online. Oceny zostały zebrane za pomocą narzędzia do samooceny online. Uczestnicy oceniali arousal, valence i dominance za pomocą manekinów SAM w 9-stopniowej skali. Ponadto uczestnicy oceniali również odczuwane emocje za pomocą koła emocji.
Tabela w pliku zawiera jeden wiersz na ocenę indywidualną i następujące kolumny:

- Online_id	Identyfikator wideo odpowiadający tej samej kolumnie w pliku video_list
- Valence	Ocena (liczba całkowita od 1 do 9).
- Arousal	Ocena (liczba całkowita od 1 do 9).
- Dominance	Ocena (liczba całkowita od 1 do 9).
- Wheel_slice	Kawałek wybrany na kole emocji. W przypadku niektórych uczestników ocena koła emocji nie została odpowiednio zarejestrowana. W takich przypadkach wartość Wheel_slice wynosi 0. W przeciwnym razie, mapowanie emocji na kole do liczb całkowitych podane tutaj to:
1 Pride
2 Elation
3 Joy
4 Satisfaction
5 Relief
6 Hope
7 Interest
8 Surprise
9 Sadness
10 Fear
11 Shame
12 Guilt
13 Envy
14 Disgust
15 Contempt
16 Anger
- Wheel_strength Siła wybrana na kole emocji (liczba całkowita od 0 = słaba do 4 = silna).

2. video_list.csv - zawiera opis filmów
3. participant_ratings.csv - zawiera to samo co katalog z danymi tylko w postaci csv i nie ma danych z sensorów EEG
4. participant_questionnaire.csv - nie używane w naszym projekcie
5. Katalog data_preprocessed_matlab

W katalogu znajdują się 32 pliki, po jednym na uczestnika. Pliki te zawierają próbkowaną w dół (do 128 Hz), wstępnie przetworzoną i posegmentowaną wersję danych w formacie python / numpy.

Każdy plik uczestnika zawiera dwie tablice:

- *data*  	    40 x 40 x 8064	wideo/próba x kanał x dane
- *labels*    	40 x 4	wideo/próba x etykieta (valence, arousal, dominance, liking)

**kanał** - jest to po prostu dany sygnał EEG (EEG ma 40 kanałów czyli daje 40 różnych sygnałów, które będą wejściem do sieci neuronowej). Pojedynczy sygnał/kanał ma 8064 wartości. 
**etykieta** - wartość 1-9 zmiennoprzecinkowa

Opis poszczególnych kanałów:
1	Fp1	
2	AF3
3	F3
4	F7
5	FC5
6	FC1
7	C3
8	T7
9	CP5
10	CP1
11	P3
12	P7
13	PO3
14	O1
15	Oz
16	Pz
17	Fp2
18	AF4
19	Fz
20	F4
21	F8
22	FC6
23	FC2
24	Cz
25	C4
26	T8
27	CP6
28	CP2
29	P4
30	P8
31	PO4
32	O2
33	hEOG (horizontal EOG, hEOG1 - hEOG2)	
34	vEOG (vertical EOG, vEOG1 - vEOG2)
35	zEMG (Zygomaticus Major EMG, zEMG1 - zEMG2)
36	tEMG (Trapezius EMG, tEMG1 - tEMG2)
37	GSR (values from Twente converted to Geneva format (Ohm))
38	Respiration belt
39	Plethysmograph
40	Temperature

Kanały od 1 do 32:
- Dane zostały obniżone do 128 Hz.
- Artefakty EOG usunięto jak w [1].
- Zastosowano pasmowoprzepustowy filtr częstotliwości 4,0-45,0 Hz.
- Dane uśredniono do wspólnego odniesienia.
- Kolejność kanałów EEG została zmieniona tak, aby wszystkie były zgodne z kolejnością genewską, jak powyżej.
- Dane podzielono na 60-sekundowe badania i usunięto 3-sekundowe dane wyjściowe przed badaniem.
- Kolejność prób została zmieniona z kolejności prezentacji na kolejność wideo (Experiment_id).

Kanały od 33 do 40:
- Dane zostały obniżone do 128 Hz.
- Dane podzielono na 60-sekundowe badania i usunięto 3-sekundowe dane wyjściowe przed badaniem.
- Kolejność prób została zmieniona z kolejności prezentacji na kolejność wideo (Experiment_id).


