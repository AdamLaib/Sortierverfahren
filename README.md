Hier ist eine einfachere Version des `README.md` auf Deutsch:

---

# Sortieralgorithmen in Python

In diesem Repository befinden sich Implementierungen von verschiedenen grundlegenden Sortieralgorithmen in Python. Das Verstehen dieser Algorithmen ist wichtig, um effiziente Software zu entwickeln. Im Folgenden findest du eine kurze Beschreibung der einzelnen Sortieralgorithmen.

## Inhaltsverzeichnis
- [Bubble Sort](#bubble-sort)
- [Heap Sort](#heap-sort)
- [Insertion Sort](#insertion-sort)
- [Quick Sort](#quick-sort)
- [Verwendung](#verwendung)

## Bubble Sort

**Datei:** `bubblesort.py`

Bubble Sort ist ein einfacher, vergleichsbasierter Sortieralgorithmus. Er durchläuft die Liste wiederholt, vergleicht benachbarte Elemente und tauscht sie, wenn sie in der falschen Reihenfolge sind. Dieser Vorgang wird wiederholt, bis die Liste sortiert ist.

- **Zeitkomplexität:** O(n²) im schlimmsten und durchschnittlichen Fall, O(n) im besten Fall.
- **Speicherkomplexität:** O(1) (in-place Sortierung).

### So funktioniert es:
1. Beginne am Anfang der Liste.
2. Vergleiche die ersten zwei Elemente; wenn das erste größer ist als das zweite, tausche sie.
3. Gehe zum nächsten Paar und wiederhole den Vorgang.
4. Wiederhole diesen Vorgang, bis das Ende der Liste erreicht ist, und beginne dann von vorne.
5. Wiederhole dies, bis die Liste sortiert ist.

## Heap Sort

**Datei:** `heapsort.py`

Heap Sort ist ein vergleichsbasierter Sortieralgorithmus, der eine Binärheap-Datenstruktur verwendet. Er teilt die Eingabe in einen sortierten und einen unsortierten Bereich und verkleinert den unsortierten Bereich schrittweise, indem er das größte Element extrahiert und in den sortierten Bereich verschiebt.

- **Zeitkomplexität:** O(n log n) in allen Fällen.
- **Speicherkomplexität:** O(1) (in-place Sortierung).

### So funktioniert es:
1. Erstelle einen Max-Heap aus den Eingabedaten.
2. Das größte Element befindet sich jetzt an der Wurzel des Heaps. Tausche es mit dem letzten Element des Heaps und verkleinere die Heap-Größe um eins.
3. "Heapify" die Wurzel des Baumes.
4. Wiederhole den Vorgang, bis alle Elemente sortiert sind.

## Insertion Sort

**Datei:** `insertionsort.py`

Insertion Sort ist ein einfacher Sortieralgorithmus, der das endgültige sortierte Array ein Element nach dem anderen aufbaut. Es ist weniger effizient bei großen Listen, aber vorteilhaft bei kleinen Datensätzen oder fast sortierten Arrays.

- **Zeitkomplexität:** O(n²) im schlimmsten Fall, O(n) im besten Fall.
- **Speicherkomplexität:** O(1) (in-place Sortierung).

### So funktioniert es:
1. Beginne mit dem zweiten Element in der Liste.
2. Vergleiche es mit den vorherigen Elementen und füge es an der richtigen Stelle ein.
3. Wiederhole diesen Vorgang für jedes folgende Element.

## Quick Sort

**Datei:** `quicksort.py`

Quick Sort ist ein schneller und effizienter Sortieralgorithmus, der das "Teile und Herrsche"-Prinzip verwendet. Er wählt ein "Pivot"-Element aus und teilt das Array in zwei Teile, sortiert dann jedes Teilstück rekursiv.

- **Zeitkomplexität:** O(n log n) im Durchschnitt, O(n²) im schlimmsten Fall.
- **Speicherkomplexität:** O(log n) im Durchschnitt (abhängig von der Rekursionstiefe).

### So funktioniert es:
1. Wähle ein Pivot-Element aus der Liste.
2. Teile die Liste so auf, dass alle Elemente kleiner als das Pivot links und alle größeren rechts stehen.
3. Sortiere die beiden Teilstücke rekursiv.
4. Füge die sortierten Teilstücke zusammen.

## Verwendung

Jeder Algorithmus ist in einer eigenen Python-Datei implementiert. Du kannst die Algorithmen direkt ausführen oder in andere Projekte einbinden.


---

Dieses `README.md` beschreibt die grundlegenden Funktionsweisen und Eigenschaften der implementierten Sortieralgorithmen auf einfache Weise.