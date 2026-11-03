
'''Protein Sequence: TSWVTSACDGHPQSCADSCADGHPQSACDTSWVTSACDGHPQSCADSCADGHPQS ACDTSWVTSACDGHPQSCADSCADGHPQSACD '''
seq=input("enter a sequence:").upper()
amino="ABBCDSSKJAGTDKLSFDASDNBS"
count=0
for aa in amino:
    count=seq.count(aa)
    if count>0:
        print(f"{aa}:{count}")
wt=len(seq)*110
print(f"Weight of the sequence is:{wt}")    
