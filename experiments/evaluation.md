# Evaluationtable

Absolute correct columns out of 10 random PDFs:
| Column                | 0shot  | 1shot | 3shot  | 5shot  | Ground Truth Nulls | Notes                                                     |
|-----------------------|--------|-------|--------|--------|--------------------|-----------------------------------------------------------|
| Flaeche               | 7      | 10    | 8      | 7      | 0                  |                                                           |
| Typ                   | 7      | 7     | 7      | 9      | 0                  | different missclassified examples                         |
| Baujahr               | 10     | 10    | 9      | 10     | 4                  |                                                           |      
| Heizsystem            | 3      | 10    | 10     | 10     | 9                  | really rare, can be removed                               |
| Anzahl Räume          | 4      | 6     | 6      | 9      | 5                  | different missclassified examples                         |
| Raum_Typen            | 3      | 6     | 8      | 8      | 0                  |                                                           |
| Balkon                | 8      | 9     | 10     | 10     | 0                  |                                                           |
| Garten                | 9      | 9     | 9      | 10     | 0                  | garten everywhere false except in 0shot and 5shot         |
| Verkehrswert          | 9      | 10    | 10     | 10     | 0                  |                                                           |
| Gesamtverkehrswert    | 10     | 10    | 10     | 10     | 0                  |                                                           |
| Anzahl_Objekte        | 10     | 10    | 10     | 10     | 0                  |                                                           |
