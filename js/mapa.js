document.addEventListener('DOMContentLoaded', () => {
    // 1. Inicializa os marcadores
    carregarMarcadores();

    // 2. Configura o Panzoom no mapa-conteudo
    const elem = document.querySelector('.mapa-conteudo');
    const panzoom = Panzoom(elem, {
        maxScale: 4,     // Zoom máximo (4x)
        minScale: 0.5,   // Zoom mínimo
        contain: 'outside', // Garante que o mapa não "fuja" da tela
        cursor: 'default'
    });

    // 3. Ativa o zoom com a roda do rato (Scroll)
    const parent = elem.parentElement;
    parent.addEventListener('wheel', (event) => {
        // Usa a lógica interna da biblioteca para zoom suave
        panzoom.zoomWithWheel(event);
    });

    // 4. Se precisares de resetar o zoom ou chamar o panzoom noutro lugar:
    window.panzoom = panzoom; 
});

async function carregarMarcadores() {
    try {
        const resposta = await fetch('locais.json');
        const locais = await resposta.json();
        
        const areaMarcadores = document.getElementById('marcadores-area');
        
        locais.forEach(local => {
            const pin = document.createElement('div');
            pin.className = 'marcador';
            pin.style.top = local.top;
            pin.style.left = local.left;
            pin.title = local.nome;
            
            // Evento de clique modificado para não bugar com o arrasto
            pin.addEventListener('mousedown', (e) => e.stopPropagation()); 
            pin.addEventListener('click', () => abrirPainel(local));
            
            areaMarcadores.appendChild(pin);
        });
    } catch (erro) {
        console.error("Os corvos não conseguiram entregar os mapas:", erro);
    }
}

function abrirPainel(local) {
    const painel = document.getElementById('painelInfo');
    document.getElementById('painelNome').innerText = local.nome;
    document.getElementById('painelCasa').innerText = local.casa;
    document.getElementById('painelDesc').innerText = local.descricao;
    
    const imgElement = document.getElementById('painelImg');
    imgElement.src = local.imagem;
    imgElement.style.display = 'block';

    painel.classList.add('ativo');
}

function fecharPainel() {
    document.getElementById('painelInfo').classList.remove('ativo');
}