import re
# RegularExpression, 在代码中常简写为regex、regexp或RE

rec = ['hello', 'hi', 'happy']
for x in rec:
    regex = re.match(r'h.+', x)
    print(regex)