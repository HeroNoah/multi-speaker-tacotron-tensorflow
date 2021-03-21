import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import numpy as np
data = np.random.randint(-100, 100, 50).cumsum()

font_path = 'C:/Windows/Fonts/D2Coding.ttf'
font_path2 = 'C:/Users/heron/AppData/Local/Microsoft/Windows/Fonts/NanumGothicCoding.ttf'
fontprop = fm.FontProperties(fname=font_path2, size=18)

plt.ylabel('가격', fontproperties=fontprop)
plt.title('가격변동 추이', fontproperties=fontprop)
plt.plot(range(50), data, 'r')
plt.show()