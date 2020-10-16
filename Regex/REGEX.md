## Matching Specific String
```py
regex_pattern = r'hackerrank'
```
## Matching Anything But a Newline
```py
regex_pattern = r"^(.{3}\.){3}.{3}$"
```
## Matching Digits & Non-Digit Characters
```py
Regex_Pattern = r"[\d]{2}\D[\d]{2}\D[\d]{4}"
```
## Matching Whitespace & Non-Whitespace Character
```py
Regex_Pattern = r"(\S\S\s){2}\S\S"
```
## Matching Word & Non-Word Character
```py
Regex_Pattern = r"[\w]{3}\W[\w]{10}\W[\w]{3}"
```
## Matching Start & End
```py
Regex_Pattern = r"^\d\w{4}\.$"
```
## Matching Specific Characters
```py
Regex_Pattern = r'^[1-3][120][xs0][30Aa][xsu][.,]$'
```
## Excluding Specific Characters
```py
Regex_Pattern = r'^\D[^aeiou][^cbDF]\S[^AEUIO][^.,]$'
```
## Matching Character Ranges
```py
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
```
## Matching {x} Repetitions
```py
Regex_Pattern = r'^[A-Za-z24680]{40}[13579\s]{5}$'
```
## Matching {x, y} Repetitions
```py
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'
```
## Matching Zero Or More Repetitions
```py
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'
```
## Matching One Or More Repetitions
```py
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'
```
## Matching Ending Items
```py
Regex_Pattern = r'^[A-Za-z]*s$'
```
## Matching Word Boundaries
```py
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
```
## Capturing & Non-Capturing Groups
```py
Regex_Pattern = r'(ok){3,}'
```
## Alternative Matching
```py
Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'
```
## Matching Same Text Again & Again
```py
Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeuioAEUIO])(\S)\1\2\3\4\5\6\7\8\9\10$'
```
## Backreferences To Failed Groups
```py
Regex_Pattern = r"^\d\d(-?)(\d\d\1){2}\d\d$"
```
## Branch Reset Groups
```php
$Regex_Pattern = '/^\d{2}((\-\-\-)|(\-)|(\.)|(:))(\d{2}\1){2}\d{2}$/';
```
## Forward References
```php
$Regex_Pattern = '/^tac(tac(tic)?)*$/';
```
## Positive Lookahead
```py
Regex_Pattern = r'o(?=oo)'
```
## Negative Lookahead
```py
Regex_Pattern = r"(.)(?!\1)"
```
## Positive Lookbehind
```py
Regex_Pattern = r"(?<=[13579])\d"
```
### Negative Lookbehind
```py
Regex_Pattern = r"(?<![aeiouAEOIU])."
```