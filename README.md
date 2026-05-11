# Análise de Anúncios de Venda de Carros

Aplicação web interativa construída com Streamlit para explorar e visualizar dados de anúncios de venda de veículos.

## Funcionalidades

- **Histograma do Odômetro**: distribuição da quilometragem dos veículos anunciados
- **Dispersão Odômetro vs Preço**: relação entre quilometragem e preço de venda

## Estrutura do Projeto

```
vehicles_project/
├── app.py               # Aplicação Streamlit principal
├── vehicles.csv         # Dataset de anúncios de veículos
├── requirements.txt     # Dependências Python
├── notebooks/
│   └── EDA.ipynb        # Análise exploratória de dados
└── .streamlit/
    └── config.toml      # Configuração do servidor Streamlit
```

## Como executar

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv vehicles_env
source vehicles_env/bin/activate   # Linux/macOS
vehicles_env\Scripts\activate      # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a aplicação

```bash
streamlit run app.py
```

Acesse em: [http://localhost:10000](http://localhost:10000)

## Dataset

O arquivo `vehicles.csv` contém anúncios de venda de carros com as seguintes colunas:

| Coluna | Descrição |
|---|---|
| price | Preço do veículo (USD) |
| year | Ano de fabricação |
| manufacturer | Fabricante |
| model | Modelo |
| condition | Condição (excellent, good, fair) |
| odometer | Quilometragem |
| fuel | Tipo de combustível |
| transmission | Tipo de câmbio |

## Tecnologias

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
