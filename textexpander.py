from __future__ import division, print_function

from plistlib import writePlistToString as plist
from uuid import uuid4

now = '2014-05-01T21:06:33Z'
abbrevs = dict(line.split(' ') for line in
'''\
rceil 2309
rfloor 230B
rangle 27e9
rAngle 27eb
sqrt 221a
cbrt 221b
langle 27e8
lceil 2308
lfloor 230a
lAngle 27ea
bra 27e8
ket 27e9
vert 007c
Vert 2016
Vvert 2980
bigA 22c0
bigV 22c1
bigcap 22c2
bigcup 22c3
bigbbsum 2140
bigprod 220f
coprod 2210
bigsum 2211
bigodot 2a00
bigo+ 2a01
bigoX 2a02
bigcup. 2a03
bigcup+ 2a04
bigsqcap 2a05
bigsqcup 2a06
bigmod2sum 2a0a
bigX 2a09
pm 00b1
times 00d7
dagger 2020
ddagger 2021
smblkcircle 2022
fracslash 2044
minus 2212
mp 2213
divslash 2215
smallsetminus 2216
ast 2217
asterisk 2217
smwhtcircle 2218
smblkcircle 2219
wedge 2227
vee 2228
cap 2229
cup 222a
dotminus 2238
cuplarrow 228c
cup. 228d
cup+ 228e
sqcap 2293
sqcup 2294
o+ 2295
o- 2996
ox 2297
o/ 2298
o. 2299
cdot 22c5
Cap 2305
not 00ac'''.split('\n')
+ open('unicode-math.txt').read().split('\n')[:-1])

abbrevs = {abbrev: int(replace, base=16)
           for abbrev, replace in abbrevs.iteritems()}
# Narrow build
abbrevs = {abbrev: unichr(replace) for abbrev, replace
           in abbrevs.iteritems()
           if replace < 0x10000}

def snippet(abbrev, replace):
    return dict(abbreviation=',{} '.format(abbrev),
                abbreviationMode=0,
                creationDate=now,
                flags=0,
                label='',
                lastUsed=now,
                modificationDate=now,
                snippetType=0,
                uuidString=str(uuid4()),
                plainText=unicode(replace + u' '))



snippets = dict(groupInfo=dict(groupName="Latex comma",
                               expandAfterMode=2),
                snippetsTE2=list(snippet(abbreviation, replacement)
                                 for abbreviation, replacement
                                 in abbrevs.iteritems()))

print(plist(snippets))
