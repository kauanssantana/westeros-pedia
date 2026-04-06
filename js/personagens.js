document.addEventListener('DOMContentLoaded', () => {
    carregarPersonagens();
});

// Variáveis globais para guardar o estado atual da pesquisa
let todosPersonagens = []; 
let casaFiltroAtual = 'todas';
let textoPesquisaAtual = '';

async function carregarPersonagens() {
    try {
        const resposta = await fetch('personagens_got.json');
        todosPersonagens = await resposta.json();
        
        // Renderiza tudo na primeira vez
        renderizarPersonagens(todosPersonagens);
        
        // Ativa os ouvintes (Pesquisa e Botões)
        configurarPesquisa();
        configurarFiltrosCasas();

    } catch (erro) {
        console.error("Os corvos foram abatidos e não trouxeram os personagens:", erro);
    }
}

function renderizarPersonagens(personagens) {
    const grid = document.getElementById('personagens-grid');
    grid.innerHTML = ''; // Limpa o grid antes de desenhar
    
    if (personagens.length === 0) {
        grid.innerHTML = `<p style="text-align: center; width: 100%; color: #888; font-style: italic; grid-column: 1 / -1;">Nenhum rosto encontrado em Westeros para essa busca...</p>`;
        return;
    }

    personagens.forEach(personagem => {
        const card = document.createElement('div');
        card.className = 'personagem-card';
        
        // Tratamento do nome da casa
        let casaFormatada = personagem.casa.replace('House ', '').replace('Lanister', 'Lannister');
        if (!casaFormatada || casaFormatada === "Unknown" || casaFormatada === "None" || casaFormatada === "") {
            casaFormatada = "Desconhecida";
        }

        // Monta o card
        card.innerHTML = `
            <div class="personagem-img-wrapper">
                <img src="${personagem.imagem}" alt="${personagem.nome}" onerror="this.src='img/hero-fundo.jpg'">
            </div>
            <div class="personagem-info">
                <h3 class="personagem-nome">${personagem.nome}</h3>
                <div>
                    <span class="personagem-casa">${personagem.casa}</span>
                </div>
                <p class="personagem-titulo">${personagem.titulo}</p>
                <p class="personagem-status">Status: ${personagem.status}</p>
                <p class="personagem-descricao">${personagem.descricao}</p>
            </div>
        `;;
        
        grid.appendChild(card);
    });
}

function aplicarFiltros() {
    const personagensFiltrados = todosPersonagens.filter(p => {

        const termo = textoPesquisaAtual.toLowerCase();
        const bateTexto = p.nome.toLowerCase().includes(termo) || 
                          p.titulo.toLowerCase().includes(termo) ||
                          p.casa.toLowerCase().includes(termo);
        
        let bateCasa = true;
        if (casaFiltroAtual !== 'todas') {
            bateCasa = p.casa.toLowerCase().includes(casaFiltroAtual.toLowerCase());
        }

        return bateTexto && bateCasa;
    });
    
    renderizarPersonagens(personagensFiltrados);
}

function configurarPesquisa() {
    const inputPesquisa = document.getElementById('pesquisa-input');
    
    inputPesquisa.addEventListener('input', (evento) => {
        textoPesquisaAtual = evento.target.value;
        aplicarFiltros(); // Chama a inteligência de filtros
    });
}

function configurarFiltrosCasas() {
    const botoes = document.querySelectorAll('.filtros-personagens .btn-filtro');
    
    botoes.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove destaque dos outros botões e coloca no clicado
            botoes.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');
            
            // Pega qual casa foi selecionada e aplica os filtros
            casaFiltroAtual = btn.getAttribute('data-casa');
            aplicarFiltros();
        });
    });
}