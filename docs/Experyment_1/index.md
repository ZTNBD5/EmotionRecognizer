# Przebieg eksperymentu nr 1

#### Zreprodukowanie wyników opisanych w oryginalnym artykule DEAP-9 

**Założenia**
Używając klasyfikatora Bayesa próbujemy odtworzyć wyniki opublikowane w pracy https://www.eecs.qmul.ac.uk/mmv/datasets/deap/doc/tac_special_issue_2011.pdf przedstawione poniżej:



Do pracy wykorzystujemy język Python oraz środowisko Jupyter. Biblioteki użyte podczas eksperymentu to zestaw sklearn oraz numpy. 

**Opis eksperymentu**

Dane użyte do eksperymentu pochodzą z data_python_preprocessed. Nasz eksperyment jest analogiczny do przedstawionego w artykule, jednak z powodu małej ilości informacji na temat procesu wyodrębniania cech, postanowiliśmy pominąć ten krok i trenować klasyfikator bezpośrednio na przetworzonych danych z czujników. 

**Wyniki** 



**Konkluzje**

Jak widać wyniki różnią się nieco od tych, które otrzymano w oryginalnym dokumencie. Nie mniej jednak są one często zbliżone. Oznacza to, że z pewną dokładnością udało nam się odtworzyć wyniki. Różnice wynikają m.in. z innego podziału danych uczących na klasy.
