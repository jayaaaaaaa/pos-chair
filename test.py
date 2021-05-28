import main2
import pandas as pd

ch0_value = round(main2.poschair()[0],2)
ch1_value = round(main2.poschair()[2],2)
ch2_value = round(main2.poschair()[4],2)
ch3_value = round(main2.poschair()[6],2)
ch4_value = round(main2.poschair()[8],2)

X_new = pd.DataFrame([[ch0_value, ch1_value, ch2_value, ch3_value, ch4_value]])
print(X_new)