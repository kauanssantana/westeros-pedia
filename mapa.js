document.addEventListener('DOMContentLoaded', () => {
    carregarMarcadores();
});

// Busca os dados gerados pelo Python
async function carregarMarcadores() {
    try {
        const resposta = await fetch('locais.json');
        const locais = await resposta.json();
        
        const areaMarcadores = document.getElementById('marcadores-area');
        
        locais.forEach(local => {
            // Cria o elemento div para o pin
            const pin = document.createElement('div');
            pin.className = 'marcador';
            pin.style.top = local.top;
            pin.style.left = local.left;
            pin.title = local.nome;
            
            // Adiciona o evento de clique
            pin.addEventListener('click', () => abrirPainel(local));
            
            areaMarcadores.appendChild(pin);
        });
    } catch (erro) {
        console.error("Os corvos não conseguiram entregar os mapas:", erro);
    }
}

function abrirPainel(local) {
    const painel = document.getElementById('painelInfo');
    
    // Atualiza os dados no HTML do painel
    document.getElementById('painelNome').innerText = local.nome;
    document.getElementById('painelCasa').innerText = local.casa;
    document.getElementById('painelDesc').innerText = local.descricao;
    
    const imgElement = document.getElementById('painelImg');
    imgElement.src = local.imagem;
    imgElement.style.display = 'block';

    // Desliza o painel para a tela
    painel.classList.add('ativo');
}

function fecharPainel() {
    document.getElementById('painelInfo').classList.remove('ativo');
}