import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#print(df)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
#print(df2.dtypes)
#print(df.tail(3))
#print(df.to_numpy())
#print(df.describe())
#print(df.T)
s = pd.Series(np.random.randint(0, 7, size=10))
#print(s)
s.value_counts()
#print(df.A)
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2018', periods=1000))
ts = ts.cumsum()
#ts.plot()
df3 = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,columns=['A', 'B', 'C', 'D'])
df3 = df3.cumsum()
df3.plot(); plt.legend(loc='best')
