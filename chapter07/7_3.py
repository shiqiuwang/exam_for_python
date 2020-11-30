import numpy as np
import pandas as pd

mat = np.random.random((10, 10))
with open(file='..//chapter07/test3', mode='w', encoding='utf=8') as f:
    for i in range(10):
        for j in range(10):
            if j != 9:
                f.write(str(mat[i, j]))
                f.write(' ')
            else:
                f.write(str(mat[i, j]))
        f.write('\n')

new_mat = pd.DataFrame(mat)
new_mat.to_csv('test33.csv', index=False, encoding='utf-8')
