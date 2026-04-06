document.addEventListener('DOMContentLoaded', () => {
    carregarGuerras();
});

async function carregarGuerras() {
    try {
        const resposta = await fetch('guerras.json');
        const guerras = await resposta.json();
        
        const container = document.getElementById('guerras-container');
        
        guerras.forEach((guerra, index) => {
            const card = document.createElement('article');
            card.className = 'guerra-card';
            
            // Lógica para alternar o lado da imagem (zigue-zague visual)
            const ordemInversa = index % 2 !== 0 ? 'guerra-inversa' : '';
            if (ordemInversa) card.classList.add(ordemInversa);

            card.innerHTML = `
                <div class="guerra-img-box">
                    <img src="${guerra.imagem}" alt="${guerra.nome}" onerror="this.src='img/hero-fundo.jpg'">
                </div>
                <div class="guerra-info">
                    <span class="guerra-ano">⏳ ${guerra.ano}</span>
                    <h3 class="guerra-nome">${guerra.nome}</h3>
                    
                    <div class="guerra-detalhes">
                        <p><strong>⚔️ Facções:</strong> ${guerra.combatentes}</p>
                        <p><strong>🛡️ Desfecho:</strong> ${guerra.desfecho}</p>
                        <p class="guerra-baixas"><span>💀 Baixas Estimadas:</span> ${guerra.baixas}</p>
                    </div>
                    
                    <div class="divisor-guerra"></div>
                    
                    <p class="guerra-descricao">${guerra.descricao}</p>
                </div>
            `;
            
            container.appendChild(card);
        });

    } catch (erro) {
        console.error("Os corvos se perderam no campo de batalha:", erro);
    }
}