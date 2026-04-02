document.addEventListener('DOMContentLoaded', () => {
    carregarCasas();
});

async function carregarCasas() {
    try {
        const resposta = await fetch('casas.json');
        const casas = await resposta.json();
        
        const grid = document.getElementById('casas-grid');
        
        casas.forEach(casa => {
            // Cria o elemento do card
            const card = document.createElement('article');
            card.className = `casa-card ${casa.id}`;
            
            // ATENÇÃO AQUI: Guardamos a região dentro do HTML do card para o filtro funcionar!
            card.setAttribute('data-regiao', casa.regiao); 
            
            // Preenche o conteúdo HTML do card
            card.innerHTML = `
                <div class="casa-card-img-box">
                    <img src="${casa.brasao}" alt="Brasão da ${casa.nome}" onerror="this.src='img/logo.png'">
                </div>
                <div class="casa-card-info">
                    <h3 class="casa-card-nome">${casa.nome}</h3>
                    <p class="casa-card-lema">"${casa.lema}"</p>
                    <div class="casa-card-detalhes">
                        <span><strong>Sede:</strong> ${casa.sede}</span>
                        <span><strong>Região:</strong> ${casa.regiao}</span>
                    </div>
                    <p class="casa-card-historia">${casa.historia}</p>
                    <div class="casa-card-personagens" style="margin-top: 15px; border-top: 1px dashed rgba(212, 175, 55, 0.3); padding-top: 15px;">
                        <span style="color: var(--gold); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Personagens Memoráveis:</span>
                        <p style="color: #ccc; font-size: 0.95rem; margin-top: 5px; font-style: italic;">${casa.personagens_memoraveis}</p>
                    </div>
                </div>
            `;
            
            grid.appendChild(card);
        });

        // Chama a função dos botões depois que os cards já existem na tela
        configurarFiltros();

    } catch (erro) {
        console.error("Os corvos se perderam com as informações das Casas:", erro);
    }
}

function configurarFiltros() {
    const botoes = document.querySelectorAll('.btn-filtro');
    const cards = document.querySelectorAll('.casa-card');

    botoes.forEach(btn => {
        btn.addEventListener('click', () => {
            // 1. Remove a cor dourada de todos os botões e coloca só no que foi clicado
            botoes.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');

            // 2. Descobre qual região o usuário quer ver
            const regiaoSelecionada = btn.getAttribute('data-regiao');

            // 3. Faz a mágica acontecer card por card
            cards.forEach(card => {
                const regiaoDoCard = card.getAttribute('data-regiao');

                if (regiaoSelecionada === 'todas' || regiaoDoCard === regiaoSelecionada) {
                    // Se for a região certa (ou 'todas'), mostra o card
                    card.style.display = 'flex'; 
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50); // Um atrasozinho mínimo para a animação ficar suave
                } else {
                    // Se for de outra região, esconde!
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.8)'; // Dá um leve efeito de encolher ao sumir
                    setTimeout(() => {
                        card.style.display = 'none'; // Some completamente do Grid para os outros ocuparem o espaço
                    }, 300); // Espera 300ms (tempo da transição) para tirar da tela
                }
            });
        });
    });
}