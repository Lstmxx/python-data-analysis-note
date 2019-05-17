import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
# data = data.cumsum()
ax  = data.plot.scatter(x='A',y='B',color = 'Blue',label = 'Class_1')
ax_2 = data.plot.scatter(x='A',y='C',color = 'Green',label = 'Class_2',ax = ax)
data.plot.scatter(x='A',y='D',color = 'red',label = 'Class_3',ax = ax_2)


# data.plot()
plt.show()