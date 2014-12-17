__author__ = 'TarunjitSingh'

import numpy as np
import json
import matplotlib.pyplot as plt

## Testing json
# with open("twitterSample.json") as fd:
#     fc = fd.read()
#     # print(fc)
#     jc = json.loads(fc)
#     print(jc[0]["id_str"])

# plt.plot([1,2,3,4],[1,4,9,16],"ro")
# plt.axis([0,6,0,20])
# plt.ylabel("some numbers")
# plt.xlabel("x-axis")
# plt.show()

##with numpy

# t = np.arange(0, 5, 0.2)
# plt.plot(t,t**3,'r--', antialiased= True)
# plt.show()


##Test Annotation

#
# ax = plt.subplot(111)
#
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s, lw=2)
#
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )
#
# plt.ylim(-2,2)
# plt.show()