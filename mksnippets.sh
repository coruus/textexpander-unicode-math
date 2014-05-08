#!/usr/bin/env sh
gsed="$(which gsed || echo -n 'sed')"&&
wget 'http://mirrors.ctan.org/macros/latex/contrib/unicode-math/unicode-math-table.tex'&&
cut -d '{' -f 2,3  unicode-math-table.tex | tr -d '"\' | tr -s '}{' ' '  | ${gsed} -re 's/([^ ]*) ([^ ]*).*/\2 \1/' > unicode-math.txt&&
python textexpander.py > commasymbols.textexpander
