document.addEventListener('DOMContentLoaded', () => {
    carregarPersonagens();
});

// Guardamos todos os personagens aqui para a barra de pesquisa funcionar sem precisar baixar o JSON de novo
let todosPersonagens = []; 

async function carregarPersonagens() {
    try {
        const resposta = await fetch('personagens_got.json');
        todosPersonagens = await resposta.json();
        
        // Renderiza tudo na primeira vez
        renderizarPersonagens(todosPersonagens);
        
        // Ativa o ouvinte da barra de pesquisa
        configurarPesquisa();

    } catch (erro) {
        console.error("Os corvos foram abatidos e não trouxeram os personagens:", erro);
    }
}

function renderizarPersonagens(personagens) {
    const grid = document.getElementById('personagens-grid');
    grid.innerHTML = ''; // Limpa o grid antes de desenhar (importante para a pesquisa)
    
    // Se a pesquisa não achar ninguém (ex: digitou "Batman")
    if (personagens.length === 0) {
        grid.innerHTML = `<p style="text-align: center; width: 100%; color: #888; font-style: italic; grid-column: 1 / -1;">Nenhum rosto encontrado em Westeros para essa busca...</p>`;
        return;
    }

    personagens.forEach(personagem => {
        const card = document.createElement('div');
        card.className = 'personagem-card';
        
        // Tratamento rápido para deixar os nomes das casas mais limpos (A API vem com 'House ' e alguns erros)
        let casaFormatada = personagem.casa.replace('House ', '').replace('Lanister', 'Lannister');
        if (!casaFormatada || casaFormatada === "Unknown" || casaFormatada === "None") {
            casaFormatada = "Desconhecida";
        }

        // Monta o card estilo retrato/polaroid
        card.innerHTML = `
            <div class="personagem-img-wrapper">
                <img src="${personagem.imagem}" alt="${personagem.nome}" onerror="this.src='img/logo.png'">
            </div>
            <div class="personagem-info">
                <h3 class="personagem-nome">${personagem.nome}</h3>
                <p class="personagem-titulo">${personagem.titulo}</p>
                <span class="personagem-casa">⚔️ ${casaFormatada}</span>
            </div>
        `;
        
        grid.appendChild(card);
    });
}

function configurarPesquisa() {
    const inputPesquisa = document.getElementById('pesquisa-input');
    
    inputPesquisa.addEventListener('input', (evento) => {
        const termoDigitado = evento.target.value.toLowerCase();
        
        // Filtra a lista principal verificando se o nome OU a casa contém o que foi digitado
        const personagensFiltrados = todosPersonagens.filter(p => 
            p.nome.toLowerCase().includes(termoDigitado) || 
            p.casa.toLowerCase().includes(termoDigitado)
        );
        
        renderizarPersonagens(personagensFiltrados);
    });
}