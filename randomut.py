# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:05:33 2022

@author: NCARAMEL
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday March 08 13:07:40 2022

@author: Caramello
"""
import os as os
import numpy as np 
import pandas as pd
os.chdir('./')    
listseq=pd.DataFrame(columns=['seqnum','seq'], index=range(100))
listseq.seqnum=range(100)

seq=["A","F","L","A","N","C","E","R","E","Q","I","H","L","A","G","S","I","Q","P","H","G","I","L","L","A","V","K","E","P","D","N","V","V","I","Q","A","S","I","N","A","A","E","F","L","N","T","N","S","V","V","G","R","P","L","R","D","L","G","G","D","L","P","L","Q","I","L","P","H","L","N","G","P","L","H","L","A","P","M","T","L","R","C","T","V","G","S","P","P","R","R","V","D","C","T","I","H","R","P","S","N","G","G","L","I","V","E","L","E","P","A","A","L","D","G","A","F","H","R","I","T","S","S","S","S","L","M","G","L","C","D","E","T","A","T","I","I","R","E","I","T","G","Y","D","R","V","M","V","V","R","F","D","E","E","G","N","G","E","I","L","S","E","R","R","R","A","D","L","E","A","F","L","G","N","R","Y","P","A","S","T","I","P","Q","I","A","R","R","L","Y","E","H","N","R","V","R","L","L","V","D","V","N","Y","T","P","V","P","L","Q","P","R","I","S","P","L","N","G","R","D","L","D","M","S","L","S","C","L","R","S","M","S","P","I","H","Q","K","Y","M","Q","D","M","G","V","G","A","T","L","V","C","S","L","M","V","S","G","R","L","W","G","L","I","A","C","H","H","Y","E","P","R","F","V","P","F","H","I","R","A","A","G","E","A","L","A","E","T","C","A","I","R","I","A","T","L","E","S","A","A","A"]
listAA=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','U','T','W','Y','V']

position=range(180,205)
for a in listseq.index:
    pos=position[np.random.randint(len(position))]
    newseq=seq.copy()
    newseq[pos]=listAA[np.random.randint(20)]
    print(''.join(newseq))
    listseq.seq[a]=''.join(newseq.copy())


listseq.to_csv(path_or_buf='list_nIFP_mutants.txt', sep="\t", index=False)

