tab := RTTabTable new input: 'https://docs.google.com/uc?authuser=0&id=0B-x64msqzS7FZmJlU2Z3YnplM0k' asUrl retrieveContents usingDelimiter: $,.
tab removeFirstRow.
tab replaceEmptyValuesWith: '0' inColumns: #(2 3 4).
tab convertColumnsAsFloat: #(2 3 4).
b := RTMapLocationBuilder new.
b shape circle
size: [ :v | (2 raisedTo: v) / 2 ];
color: (Color red alpha: 0.3).
tab values do: [ :row | b addPoint: row second @ row third value: row fourth ].
b
