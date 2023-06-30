# -*- coding: utf-8 -*-
"""MultiprocessingQueue.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vB0l6nx2L1CRqUu34H-WF9S4AKLeF13X
"""

# How to use multiprocessing.Queue as a FIFO queue:

from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())