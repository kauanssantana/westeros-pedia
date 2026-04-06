document.addEventListener('DOMContentLoaded', () => {
    carregarBestiario();
});

let todasCriaturas = [];
let filtroAtualBestiario = 'todas';

async function carregarBestiario() {
    try {
        const resposta = await fetch('bestiario.json');
        todasCriaturas = await resposta.json();
        
        renderizarBestiario(todasCriaturas);
        configurarFiltrosBestiario();

    } catch (erro) {
        console.error("Os corvos foram devorados por um dragão:", erro);
    }
}

function renderizarBestiario(criaturas) {
    const grid = document.getElementById('bestiario-grid');
    grid.innerHTML = '';
    
    if (criaturas.length === 0) {
        grid.innerHTML = `<p style="text-align: center; width: 100%; color: #888; font-style: italic;">Nenhuma besta encontrada nos registos.</p>`;
        return;
    }

    criaturas.forEach(beast => {
        const card = document.createElement('div');
        card.className = 'besta-card';

        let iconeCat = '🐾';
        if(beast.categoria === 'Dragão') iconeCat = '🐉';
        if(beast.categoria === 'Lobo Gigante') iconeCat = '🐺';
        if(beast.categoria === 'Magia Negra') iconeCat = '💀';
        if(beast.categoria === 'Raças Antigas') iconeCat = '🌲';

        card.innerHTML = `
            <div class="besta-img-box">
                <img src="${beast.imagem}" alt="${beast.nome}" onerror="this.src='img/hero-fundo.jpg'">
                <span class="besta-tamanho">${beast.tamanho}</span>
            </div>
            <div class="besta-info">
                <h3 class="besta-nome">${beast.nome}</h3>
                <span class="besta-categoria">${iconeCat} ${beast.categoria}</span>
                <div class="besta-divisor"></div>
                <p class="besta-desc">${beast.descricao}</p>
            </div>
        `;
        
        grid.appendChild(card);
    });
}

function aplicarFiltroBestiario() {
    if (filtroAtualBestiario === 'todas') {
        renderizarBestiario(todasCriaturas);
    } else {
        const filtradas = todasCriaturas.filter(c => c.categoria === filtroAtualBestiario);
        renderizarBestiario(filtradas);
    }
}

function configurarFiltrosBestiario() {
    const botoes = document.querySelectorAll('.filtros-bestiario .btn-filtro');
    
    botoes.forEach(btn => {
        btn.addEventListener('click', () => {
            botoes.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');
            
            filtroAtualBestiario = btn.getAttribute('data-categoria');
            aplicarFiltroBestiario();
        });
    });
}