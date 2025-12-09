import yara
import sys



rule_source="""
rule ContainsDS_H {
    strings:
        $s = "D$ H"
    condition:
        $s
}
"""


rules = yara.compile(source=rule_source)
matches = rules.match(sys.argv[1])
print(matches)