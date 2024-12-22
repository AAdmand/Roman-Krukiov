from fake_math import divide as f_div
from true_math import divide as t_div
print('result1 = ', f_div(12, 4))
print('result2 = ', f_div(12, 0))
print('result3 = ', t_div(13, 5))
print('result4 = ', t_div(13, 0))