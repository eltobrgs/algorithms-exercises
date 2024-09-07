import matplotlib.pyplot as plt
import numpy as np

# criando dados de exemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# plotando o gráfico
plt.plot(x, y)
plt.show()
