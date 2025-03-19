text = """
ORIGIN
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""

preproinsulin= ''.join(filter(str.islower, text))
print(preproinsulin)
first4= preproinsulin[0:4]
print(first4)
print(len(preproinsulin))
assert(len(preproinsulin) == 110)  #if not equal to 110, there will be error
# Save the cleaned text to preproinsulin-seq-clean.txt
with open('preproinsulin-seq-clean.txt', 'w') as f:
    f.write(preproinsulin)
# with>  open & close the file("file name")
# f.write> prints the value to the file
print()

# has 24 char len
Isinsulin_seq_clean= preproinsulin[:24]
print(Isinsulin_seq_clean)
print(len(Isinsulin_seq_clean))
assert(len(Isinsulin_seq_clean) == 24)
with open('Isinsulin_seq_clean.txt', 'w') as f:
    f.write(Isinsulin_seq_clean)
print()
# has 30 chac
binsulin_seq_clean= preproinsulin[:30]
print(binsulin_seq_clean)
print(len(binsulin_seq_clean))
assert(len(binsulin_seq_clean) == 30)
with open('binsulin_seq_clean.txt', 'w') as f:
    f.write(binsulin_seq_clean)
print()
# has 35 chac
cinsulin_seq_clean= preproinsulin[:35]
print(cinsulin_seq_clean)
print(len(cinsulin_seq_clean))
assert(len(cinsulin_seq_clean) == 35)
with open('cinsulin_seq_clean.txt', 'w') as f:
    f.write(cinsulin_seq_clean)
print()
# has 21 chac
ainsulin_seq_clean= preproinsulin[:21]
print(ainsulin_seq_clean)
print(len(ainsulin_seq_clean))
assert(len(ainsulin_seq_clean) == 21)
with open('ainsulin_seq_clean.txt', 'w') as f:
    f.write(ainsulin_seq_clean)




