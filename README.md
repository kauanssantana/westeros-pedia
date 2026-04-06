# ⚔️ WesterosPedia

> O guia definitivo e a enciclopédia completa para qualquer Meistre da Cidadela, das terras geladas do Norte aos desertos de Dorne!

![Capa do Projeto](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)



---

## 📖 Sobre o Projeto

A WesterosPedia é uma aplicação web imersiva desenvolvida inteiramente com Vanilla JavaScript (sem frameworks) que consome bancos de dados customizados em formato JSON. O projeto foi meticulosamente desenhado para catalogar o vasto universo de Game of Thrones / As Crônicas de Gelo e Fogo.

Com uma interface sombria, elegante e de alta performance, a enciclopédia oferece uma navegação rica através da história, grandes casas, personagens memoráveis e criaturas lendárias. Tudo isso envelopado em um design 100% responsivo, adaptando-se perfeitamente de grandes monitores de desktop até as telas dos celulares.

---

## ✨ Principais Funcionalidades

* 🏰 Grandes Casas: Navegue pelas famílias nobres de Westeros, filtre por região (O Norte, Dorne, O Vale, etc.), conheça os seus lemas, sedes e história, com efeitos visuais interativos nos brasões.

* 👥 Registro de Personagens: Pesquise instantaneamente entre dezenas de personagens por nome, título ou Casa. Descubra suas biografias e acompanhe o seu cruel status de vida (Vivo/Morto).

* 🗺️ Mapa Interativo: Explore a geografia do Mundo Conhecido. Navegue pelo mapa com recursos de Pan & Zoom e clique nos marcadores interativos (Pins) para revelar informações detalhadas sobre as fortalezas e cidades.

* ⚔️ Guerras e Batalhas: Um memorial dos conflitos mais sangrentos. Acompanhe os anos, facções combatentes, desfechos e estatísticas de baixas estimadas de eventos que vão da Conquista de Aegon ao Saque de Porto Real.

* 📜 Linha do Tempo (História): Uma Timeline dinâmica com os eventos mais chocantes que moldaram o destino dos Sete Reinos ao longo dos séculos.

* 🐉 Bestiário & 🛐 Religiões: Descubra os segredos das feras exóticas (com tags de nível de perigo/tamanho) e entenda os dogmas, clérigos e deidades de cada culto espalhado pelo mundo.

* 🎨 Temas Dinâmicos (Bônus): Altere a atmosfera do site instantaneamente escolhendo a lealdade à sua casa favorita (Stark, Targaryen, Lannister, etc.), o que adapta as cores neon, detalhes e gradientes de toda a interface.

---

## 💻 Tecnologias Utilizadas

O projeto foi desenvolvido dominando as tecnologias base da web, focando em lógica pura, componentização via manipulação do DOM e performance:

* **HTML5:** Semântica e acessibilidade.
* **CSS3:** Variáveis globais (:root) para temas dinâmicos, Flexbox e CSS Grid para layouts complexos, animações (keyframes, transições de hover) e Media Queries para responsividade total no mobile.
* **JavaScript (ES6+):** Fetch API (Promises/Async-Await) para leitura local dos JSONs, manipulação direta e massiva do DOM (Template Literals) e criação de sistemas de busca e filtros integrados em tempo real.
* **Python:** Utilizado nos bastidores (Web Scraping / APIs) para coletar, estruturar, limpar e forjar os bancos de dados vitais da aplicação (arquivos .json).
* **Panzoom.js:** Biblioteca super leve utilizada unicamente para a navegação fluida (zoom e arrasto) na página do Mapa.

---

## 🚀 Como Executar o Projeto

Como o projeto faz o uso da Fetch API do JavaScript para carregar os arquivos .json, por questões de segurança dos navegadores modernos (CORS), o arquivo index.html não pode ser aberto simplesmente com um duplo-clique. É necessário rodar um servidor local.

1. Faça o clone deste repositório:
   ```bash
   git clone https://github.com/kauanssantana/westerospedia.git

2. Abra a pasta do projeto no VS Code (ou no seu editor favorito).

3. Utilize a extensão Live Server (ou rode um servidor simples em Python via terminal: python -m http.server 8000).

4. Abra o endereço correspondente no seu navegador e declare a sua lealdade ao Trono de Ferro!
