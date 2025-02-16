# Gerador de Planos de Aula 📚

Este sistema gera automaticamente planos de aula com base na BNCC e exporta em PDF.

## Como Funciona?
1. O professor preenche os dados na interface web.
2. A IA sugere os conteúdos e atividades baseados na BNCC.
3. O plano de aula é gerado e baixado como PDF.

## Como Rodar?
- O projeto é hospedado no Render e pode ser acessado online.
- Para rodar localmente, basta executar:
  ```bash
  uvicorn app.main:app --reload
