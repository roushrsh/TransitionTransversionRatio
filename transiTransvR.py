#http://rosalind.info/problems/tran/

string1 = "GAGAACGGTAAACTGGTAGAAAGAGCGCGCCGCTTACCTTGGGCTAGACACACGGAAAAAGCAAGCCAATATGTGGTAGATGAAAGAACTTTATGATAAGTCCGAGCCGCCTGCTTGATGAGATCGCGTCGACACTGTTCTTTCGATGGTCAGTGTGTTCTTCAAAGTCTGAAGAGTGCGGGTACGTAGCGTACTAAATATCCTGGAAATAGCACTATTGCCCTGGGACGGTGGGATACTCCATTAACAACAGGATAGCAGTTCTACGGAGAAGGTAGTGAGCATTGTATGCTTGGATAGATCATTGCAATCATTGCTTGCATCGACACGATATAAAAATCCACGCGCATCAGAAAGACCTTCACCAGGCGTCTGCGAGGCAACAGAGGGGCTGGTTGTCAACGTCCTGGACAATTGCCTTGGGTCTGAGGGTCCGGTATAATCCCGGCTGGGTCTTCTTAGCGCAGGGTCAAATCGGCCAGGGGATCATGAGACAGCTGGATCTTCACCTCTACAAAGTCAGTAACACTGAAGATAGAGAGCACCCCGGATACCAACACGGGGTGCATTTGTAAGCTATGGGCTACATTCAGGGCCTATACGGAAATAGAATGAGCGCTACTAATCACTAGCTTGTGAGCACCCGCGATCTGTGTATAACAAAAGAGAGGGGATTGGACTATTAGAGATTTAGTCCAAAGAATGTGCGTGTTGGGATCCGCTCATTGAAAGTATATTAAAACTGCTCTCAATGGCGGTCTTTTGGAGTTTTTGGGGCCCGTGTTCCGGTTGACGAAAACTATACCGGCGGTTCAAGTTAAGCGCCGATCCTGTTCCTTCTGACGTGGAC"
string2 = "GAGAACGGTAACCTGGTAGGGAGAATACGTCGCTTACGTTTGGTTAGACACACGCGGAGGACAGGTCGTTATTCGGTAGACGCAAGGACTTTATGATAAATTCGAATCGCCATCTTGGTGAGATAGCGTCGGTAACGGTCTCTCGATGATCAACGTGTCCCTCAAAATCTGAGGAATCCGGTTACGTGGCGTGCCACATACCCGAGAAATAGCGCTACTGCACTGGAGCGGCGGGATAGTCGCGTAGCGGCACTATTGCAGTTCCACAAAAAAAACGGTGGGGGTCGCATGCTTGGGTAGATCATCGCAATCTTTGCTTGCACCCACACGGTACAGGAACCCCTGCGCAACAAAGACACCTTCGCCAAGTCTCTGCAGAGTGACACAGCGACTTCTCCTCAACGTCCTGGACGGTTGTCTTGGGTCCGAGCGTCTGGTATAGCCCCGACAAAGTCCTCTTAACACAAGGCCAAAACAGCCTTGAGGCCAGAGGGCAACTAGATCTTCACCGCTACATAGTCAGTAGTTTCGGAGATAGAGAGACCCTCGTGTTCCAACGCGTGGTGTGCGTGTAGACTATGGGTTGCACTCAGTGATTATACGGGAATTGAAGGGGCACAACTAATCGCTAATTCTTGGGCACCCGCGATCCGTGGGTAGCTGAAGGGCGGAGATTCGACTATTAGGGATTTAGTCCAGAGAGTATGCGTGTTGTGACCTGCTCATTGAAAAGTCAGTGAATCCGCCCTCAATGACGGCCTTTAGATGTTATCAGGGCCTGTATCCCGATCTACGTAAGCTATGTCGTCGCTTCACATTGAGCGCCAATCCTGTTCTTTCTAGTGTGGAC"
transi = 0
transv = 0

for a, b in zip(string1, string2):
    if (a == b):
        continue
    elif((a=="A") or (a=="G")):
        if ((b=="A") or (b=="G")):
            transi=transi +1
        elif((b=="C") or (b=="T")):
            transv=transv + 1
    elif((a== "C") or (a=="T")):
        if ((b=="C") or (b=="T")):
            transi=transi + 1
        elif((b=="A") or (b=="G")):
            transv=transv+1

print float(transi)/float(transv)
