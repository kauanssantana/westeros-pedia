document.addEventListener('DOMContentLoaded', () => {
    carregarReligioes();
});

async function carregarReligioes() {
    try {
        const resposta = await fetch('religioes.json');
        const religioes = await resposta.json();
        
        const grid = document.getElementById('religioes-grid');
        grid.innerHTML = '';
        
        religioes.forEach(religiao => {
            const card = document.createElement('div');
            card.className = 'religiao-card';

            card.innerHTML = `
                <div class="religiao-img-box">
                    <img src="${religiao.imagem}" alt="${religiao.nome}" onerror="this.src='img/hero-fundo.jpg'">
                </div>
                <div class="religiao-info">
                    <h3 class="religiao-nome">${religiao.nome}</h3>
                    <p class="religiao-lema">${religiao.lema}</p>
                    
                    <div class="religiao-detalhes">
                        <p><strong>🛐 Deidade:</strong> ${religiao.deidade}</p>
                        <p><strong>📖 Clérigos:</strong> ${religiao.clerigos}</p>
                        <p><strong>🌍 Centro de Culto:</strong> ${religiao.centro}</p>
                    </div>
                    
                    <div class="religiao-divisor"></div>
                    
                    <p class="religiao-desc">${religiao.descricao}</p>
                </div>
            `;
            
            grid.appendChild(card);
        });

    } catch (erro) {
        console.error("Os Alto Septões proibiram a leitura destes pergaminhos:", erro);
    }
}