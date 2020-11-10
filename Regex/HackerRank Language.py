# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

language = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"

for _ in range(int(input())):
	name = re.findall(r'\d* ([A-Z]*)', input())[0]
	print("VALID" if re.search(r'\b'+name+r'\b', language) else "INVALID")