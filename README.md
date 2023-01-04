# Normalizacao-de-Dados
Z-Score e MinMaxScaler

Normalização de Dados, também conhecido na estatística como Z-Score, é quando temos uma distribuição de dados quaisquer em determinada escala e gostariamos de converter-los para uma distribuição com o comportamento de uma distrbuição Normal (também conhecida como Gaussiana).

Para fazer a normalização dos dados devemos converte-los de acordo com a seguinte fórmula:

$$ Z = \frac{x - \mu}{\sigma} $$

Onde $x$ é um dado da nossa distribuição, $\mu$ é a média desta distribuição e $\sigma$ é o desvio padrão da distribuição.

O codigo Z-Score recebe uma lista de dados e possui funções para calcular:  A média (mean_data), desvio padrão (DesvioP) e  para normalização segundo a formula do Z (normalize) e retorna a lista de dados normalizados.

O _MinMaxScaler_ é uma técnica de reescalonamento de um conjunto de dados parecida com a normalização ou no caso Z-score. A diferença é que ao invés de utilizar média e desvio padrão, utiliza-se os valores extremos (máximo e mínino), segundo a equação a seguir:

$$ S = \frac{x - min}{max - min} $$

Onde X é um determinado elemento da lista, $min$ é o menor valor da lista e $max$ e o maior valor da lista.

O codigo _MinMaxScaler_ recebe uma lista de dados quaisquer e converte para a escala segundo o MinMaxScaler.
