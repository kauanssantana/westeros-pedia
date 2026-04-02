document.addEventListener('DOMContentLoaded', () => {
    carregarHistoria();
});

async function carregarHistoria() {
    try {
        const resposta = await fetch('historia.json');
        const eventos = await resposta.json();
        
        const container = document.getElementById('timeline-container');
        
        eventos.forEach((evento, index) => {
            const node = document.createElement('div');
            // Alterna a classe 'left' e 'right' dependendo de ser par ou ímpar
            node.className = `timeline-item ${index % 2 === 0 ? 'left' : 'right'}`;

            node.innerHTML = `
                <div class="timeline-content">
                    <span class="timeline-ano">${evento.ano}</span>
                    <div class="timeline-img-box">
                        <img src="${evento.imagem}" alt="${evento.titulo}" onerror="this.src='img/hero-fundo.jpg'">
                    </div>
                    <h3 class="timeline-titulo">${evento.titulo}</h3>
                    <span class="timeline-foco">🔥 ${evento.foco}</span>
                    <p class="timeline-desc">${evento.descricao}</p>
                </div>
            `;
            
            container.appendChild(node);
        });

    } catch (erro) {
        console.error("Os meistres não encontraram os pergaminhos da história:", erro);
    }
}