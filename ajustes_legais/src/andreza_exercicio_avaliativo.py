# -*- coding: utf-8 -*-
"""Andreza_Exercicio_Avaliativo (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U_lCEbtPPu-H_ZBkT7TDfo8guZ_xBQmj

# Problema 1

Dado o modelo matemático da equação normal da reta, a saber:

$x \cos(\theta) + y sen(\theta) - \rho = 0 \tag{A4} $

Considere que 2 pontos de coordenadas cartesianas foram observados $ n=10 $ vezes, e para cada observação foram atribuídas variâncias de diferentes qualidades.





### Resolução:
Baseado na sequência de indagações apresentadas acima, tem-se que:
- As medidas observadas são as coordenadas \( x \) e \( y \).
- Os parâmetros a serem determinados são os coeficientes \( \theta \) e \( \rho \).
- O modelo matemático (\( F \)) é implícito e não linear.

| index |       x       |       y       |  rho_observed  |  variance  |
|-------|---------------|---------------|----------------|------------|
| 0     | -2.5092       | -9.5883       | -9.5671        | 1.1075     |
| 1     |  9.0143       |  9.3982       | 13.3339        | 0.6705     |
| 2     |  4.6399       |  6.6489       | 7.0744         | 0.5651     |
| 3     |  1.9732       | -5.7532       | -4.0852        | 1.4489     |
| 4     | -6.8796       | -6.3635       | -7.8986        | 1.4656     |
| 5     | -6.8801       | -6.3319       | -9.5681        | 1.3084     |
| 6     | -8.8383       | -3.9152       | -8.9506        | 0.8046     |
| 7     |  7.3235       |  0.4951       | 4.1038         | 0.5977     |
| 8     |  2.0223       | -1.3611       | -0.0768        | 1.1842     |
| 9     |  4.1615       | -4.1754       | 0.1011         | 0.9402     |

## Perguntas:

1. Quem são as observações ou medidas e quais os parâmetros a serem determinados?
"""

import pandas as pd

dados = {
    "index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "x": [-2.5092, 9.0143, 4.6399, 1.9732, -6.8796, -6.8801, -8.8383, 7.3235, 2.0223, 4.1615],
    "y": [-9.5883, 9.3982, 6.6489, -5.7532, -6.3635, -6.3319, -3.9152, 0.4951, -1.3611, -4.1754],
    "rho_observed": [-9.5671, 13.3339, 7.0744, -4.0852, -7.8986, -9.5681, -8.9506, 4.1038, -0.0768, 0.1011],
    "variance": [1.1075, 0.6705, 0.5651, 1.4489, 1.4656, 1.3084, 0.8046, 0.5977, 1.1842, 0.9402]
}

df = pd.DataFrame(dados)

display(df)

"""Os **parâmetros a serem determinados** no modelo são:

- $\theta$ (ângulo que a reta faz com o eixo horizontal)
- $\rho$ (distância perpendicular da reta à origem)

Esses são os coeficientes desconhecidos da equação normal da reta, dada por:

$$
x \cos(\theta) + y \sin(\theta) - \rho = 0
$$

As variáveis $x$ e $y$ são observações (dados conhecidos), enquanto $\theta$ e $\rho$ são os parâmetros que precisam ser estimados.

2. O modelo matemático $ F $ é explícito ou implícito?

R: O modelo matemático $F$ apresentado é **implícito**.

Isso ocorre porque os parâmetros $\theta$ e $\rho$ estão definidos implicitamente na equação:

$$x \cos(\theta) + y \sin(\theta) - \rho = 0$$

Não é possível isolar explicitamente as observações (x e y) em função dos parâmetros. Portanto, trata-se de um modelo implícito não linear.
"""

# Modelo implícito da reta
def modelo_implicito(x, y, theta, rho):
    return x * np.cos(theta) + y * np.sin(theta) - rho

"""3. $ F $ é linear ou não linear?

R: O modelo matemático $F$ apresentado é **não linear**.

Isto ocorre porque o parâmetro $\theta$ está dentro das funções trigonométricas $\sin(\theta)$ e $\cos(\theta)$, que não são lineares.

Explicitamente, o modelo é dado por:
$$F(x, y, \theta, \rho) = x \cos(\theta) + y \sin(\theta) - \rho = 0$$

A presença das funções trigonométricas de um parâmetro torna o modelo não linear com relação a $\theta$.
$$F(\theta, \rho) = x \cos(\theta) + y \sin(\theta) - \rho = 0
$$
"""

def F(theta, rho, x, y):
    return x * np.cos(theta) + y * np.sin(theta) - rho

"""4. Existe deficiência de posto na matriz das equações normais $ N $?

# AVALIAR A QUALIDADE

## Calcular os parâmetros
$𝜃
$ e
$
ρ$ usando o método dos mínimos quadrados ponderados.
"""

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

# Criando corretamente o DataFrame
dados = pd.DataFrame({
    "x": [-2.5092, 9.0143, 4.6399, 1.9732, -6.8796, -6.8801, -8.8383, 7.3235, 2.0223, 4.1615],
    "y": [-9.5883, 9.3982, 6.6489, -5.7532, -6.3635, -6.3319, -3.9152, 0.4951, -1.3611, -4.1754],
    "rho_observed": [-9.5671, 13.3339, 7.0744, -4.0852, -7.8986, -9.5681, -8.9506, 4.1038, -0.0768, 0.1011],
    "variance": [1.1075, 0.6705, 0.5651, 1.4489, 1.4656, 1.3084, 0.8046, 0.5977, 1.1842, 0.9402]
})

# Função de resíduos ponderados
def residuals(params, x, y, rho_obs, weights):
    theta, rho = params
    predicted = x * np.cos(theta) + y * np.sin(theta)
    return weights * (predicted - rho_obs)

# Vetores numpy
x = dados["x"].to_numpy()
y = dados["y"].to_numpy()
rho_obs = dados["rho_observed"].to_numpy()
weights = 1 / np.sqrt(dados["variance"].to_numpy())

# Chute inicial dos parâmetros
initial_guess = [0.5, 0.0]

# Ajuste com mínimos quadrados ponderados
result = least_squares(residuals, x0=initial_guess, args=(x, y, rho_obs, weights))

# Parâmetros estimados
theta_est, rho_est = result.x

# Exibindo resultado
print(f"θ estimado: {np.degrees(theta_est):.4f} graus")
print(f"ρ estimado: {rho_est:.4f}")

"""### Resíduos"""

# Cálculo dos resíduos não ponderados
residuos_nao_ponderados = x * np.cos(theta_est) + y * np.sin(theta_est) - rho_est

# Cálculo dos resíduos ponderados
residuos_ponderados = weights * residuos_nao_ponderados

# Criando um DataFrame para exibir lado a lado
residuos_df = pd.DataFrame({
    "x": x,
    "y": y,
    "rho_observado": rho_obs,
    "rho_estimado": x * np.cos(theta_est) + y * np.sin(theta_est),
    "resíduo": residuos_nao_ponderados,
    "resíduo_ponderado": residuos_ponderados
})

# Exibindo os resíduos
display(residuos_df.round(4))

"""## Parametros Estimados

### Parâmetros Estimados

- **$\theta_{est}$ (rad)**:
"""

print(f"θest (rad): {theta_est:.4f}")

"""- **$\theta_{est}$ (graus)**:

"""

print(f"θest (graus): {np.degrees(theta_est):.2f}°")

"""- **$\rho_{est}$**:

"""

print(f"ρest: {rho_est:.4f}")

"""- **MSE (Erro Quadrático Médio)**:"""

# Erro Quadrático Médio (MSE)
mse = np.mean(residuos_nao_ponderados ** 2)
print(f"MSE (Erro Quadrático Médio): {mse:.4f}")

"""## Resíduos Padronizados:"""

# Cálculo dos resíduos padronizados
residuos_padronizados = residuos_nao_ponderados / np.sqrt(dados["variance"].to_numpy())

# Adicionando ao DataFrame
residuos_df["resíduo_padronizado"] = residuos_padronizados

# Exibindo os resíduos padronizados
display(residuos_df[["x", "y", "resíduo", "resíduo_padronizado"]].round(4))

"""### Resíduos Padronizados

Os resíduos padronizados são obtidos dividindo-se cada resíduo pelo desvio padrão (raiz da variância) associado à observação:

$$\text{Resíduo Padronizado}_i = \frac{F_i}{\sqrt{\text{Var}_i}}$$

Eles permitem identificar **valores discrepantes**: geralmente, valores maiores que 2 ou menores que -2 em módulo indicam possíveis outliers.

## Interpretação:

### Resíduos Padronizados: Algum dos resíduos padronizados ultrapassou os limites de ±2?
"""

# Verifica se algum resíduo padronizado ultrapassou ±2
outliers = residuos_df[np.abs(residuos_padronizados) > 2]

# Exibe os casos se existirem
if not outliers.empty:
    print("⚠️ Observações com resíduos padronizados fora dos limites ±2:")
    display(outliers[["x", "y", "resíduo_padronizado"]].round(4))
else:
    display("✅ Nenhum resíduo padronizado ultrapassou os limites de ±2.")

"""### Existe utliers presentes nos dados fornecidos?

R: Existe outliers presentes nos dados fornecidos?

**Sim**, a análise dos **resíduos padronizados** revelou a presença de **vários outliers**.

Foram consideradas como potenciais observações discrepantes aquelas com resíduos padronizados com módulo superior a 2 $(|r_i| > 2$). No conjunto de dados analisado, **8 das 10 observações** ultrapassaram esse limite, indicando que esses pontos estão significativamente distantes da reta ajustada pelo modelo.

Esses outliers podem ter diferentes origens, como:

- Erros de medição (instrumentos imprecisos ou mal calibrados),
- Variabilidade natural dos dados,
- Falhas na modelagem ou necessidade de segmentação (por exemplo, mais de uma reta pode representar melhor os dados).

**Conclusão:** Há **fortes evidências de outliers**, e uma investigação adicional é recomendada para compreender seu impacto e, se necessário, aplicar técnicas de ajuste robusto ou reavaliar a consistência dos dados.

## Conclusão:

**Resíduos Padronizados**

A análise dos resíduos padronizados demonstrou que a maioria das observações apresenta valores com módulo superior a 2. Isso indica que os dados não estão perfeitamente alinhados com o modelo ajustado, e há desvios significativos em diversas observações.

Esse comportamento sugere que o modelo pode estar sofrendo influência de valores extremos ou que a variabilidade dos dados não é totalmente explicada pela reta estimada.

Recomenda-se investigar a natureza dessas discrepâncias e considerar o uso de técnicas de ajuste robusto.

**Outliers**:

A presença de **outliers** foi confirmada com base nos resíduos padronizados. Foram identificadas **8 observações com $|r_i| > 2$**, o que representa uma parcela significativa do conjunto de dados.

Esses outliers podem comprometer a qualidade do ajuste, influenciar a inclinação da reta e distorcer as estimativas dos parâmetros. É importante considerar:

- A verificação das observações para possíveis erros;
- A aplicação de técnicas que sejam menos sensíveis a outliers, como regressão robusta;
- Ou segmentar os dados, caso eles representem populações diferentes.

A presença de outliers justifica uma abordagem mais cuidadosa na interpretação dos resultados.
"""