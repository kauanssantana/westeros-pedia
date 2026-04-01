/* =========================================================
   1. VARIÁVEIS GLOBAIS E ELEMENTOS DO DOM
   ========================================================= */
const characterContainer = document.getElementById('characterContainer');
const searchBtn = document.getElementById('searchBtn');
const searchInput = document.getElementById('searchInput');

let todosOsPersonagens = []; 
let slideIndex = 0; // Para o Carrossel

/* =========================================================
   2. INICIALIZAÇÃO (DOMContentLoaded)
   ========================================================= */
document.addEventListener('DOMContentLoaded', () => {
    // A) Carrega o Tema Salvo
    const temaSalvo = localStorage.getItem('temaEscolhidoWesteros');
    if (temaSalvo) {
        mudarTema(temaSalvo);
    }

    // B) Se estiver na página de Personagens, carrega o JSON
    if (characterContainer) {
        carregarPersonagens();
    }

    // C) Se o carrossel existir na página, inicia o ajuste de largura
    const slidesWrapper = document.getElementById("carrosselSlides");
    if (slidesWrapper) {
        const slides = document.querySelectorAll(".carrossel-slide");
        // Ajusta a largura para que os slides fiquem lado a lado corretamente
        slidesWrapper.style.width = `${slides.length * 100}%`;
    }
});

/* =========================================================
   3. SISTEMA DE BUSCA DE PERSONAGENS (JSON/WIKI)
   ========================================================= */
async function carregarPersonagens() {
    try {
        const response = await fetch('personagens_got.json');
        todosOsPersonagens = await response.json();
        renderizarPersonagens(todosOsPersonagens);
    } catch (error) {
        console.error("Erro ao carregar os dados: ", error);
        characterContainer.innerHTML = '<p style="color: red;">Os corvos foram interceptados. Não foi possível ler os pergaminhos.</p>';
    }
}

function renderizarPersonagens(personagens) {
    if (!characterContainer) return;
    characterContainer.innerHTML = ''; 

    if (personagens.length === 0) {
        characterContainer.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">Nenhum lorde, cavaleiro ou patrulheiro encontrado.</p>';
        return;
    }

    personagens.forEach(char => {
        const card = document.createElement('div');
        card.classList.add('character-card');
        card.innerHTML = `
            <img src="${char.imagem}" alt="Retrato de ${char.nome}" class="character-img" loading="lazy">
            <h3 class="character-name">${char.nome}</h3>
            <p class="character-house">${char.casa}</p>
            <p class="character-title">${char.titulo}</p>
        `;
        characterContainer.appendChild(card);
    });
}

// Eventos de Busca
if (searchBtn && searchInput) {
    searchBtn.addEventListener('click', () => {
        const termoBusca = searchInput.value.toLowerCase();
        const personagensFiltrados = todosOsPersonagens.filter(char => 
            char.nome.toLowerCase().includes(termoBusca) || 
            char.casa.toLowerCase().includes(termoBusca)
        );
        renderizarPersonagens(personagensFiltrados);
    });

    searchInput.addEventListener('keyup', (evento) => {
        if (evento.key === 'Enter') searchBtn.click();
    });
}

/* =========================================================
   4. SISTEMA DE TEMAS (CASAS DE WESTEROS)
   ========================================================= */
function abrirMenuTemas(event) {
    event.stopPropagation(); 
    document.getElementById("caixaTemas").classList.toggle("mostrar");
    document.getElementById("btnTemas").classList.toggle("pressionado");
}

window.onclick = function(event) {
    if (!event.target.matches('.theme-btn')) {
        let caixaMenu = document.getElementById("caixaTemas");
        let botaoTemas = document.getElementById("btnTemas");
        
        if (caixaMenu && caixaMenu.classList.contains('mostrar')) {
            caixaMenu.classList.remove('mostrar');
            if (botaoTemas) botaoTemas.classList.remove('pressionado');
        }
    }
}

function mudarTema(nomeDoTema) {
    const corpo = document.body;
    corpo.classList.remove(
        'tema-stark', 'tema-targaryen', 'tema-lannister', 'tema-greyjoy', 
        'tema-tully', 'tema-arryn', 'tema-baratheon', 'tema-tyrell', 'tema-martell'
    );

    if (nomeDoTema !== 'padrao') {
        corpo.classList.add('tema-' + nomeDoTema);
    }

    localStorage.setItem('temaEscolhidoWesteros', nomeDoTema);
    
    let caixaMenu = document.getElementById("caixaTemas");
    let botaoTemas = document.getElementById("btnTemas");
    
    if (caixaMenu) caixaMenu.classList.remove("mostrar");
    if (botaoTemas) botaoTemas.classList.remove("pressionado");
}

/* =========================================================
   5. SISTEMA DE CARROSSEL ÉPICO (HOME)
   ========================================================= */
function mudarSlide(n) {
    const slidesWrapper = document.getElementById("carrosselSlides");
    const slides = document.querySelectorAll(".carrossel-slide");
    const pontos = document.querySelectorAll(".carrossel-ponto");

    if (!slidesWrapper) return;

    slideIndex += n;
    
    if (slideIndex >= slides.length) { slideIndex = 0; }
    if (slideIndex < 0) { slideIndex = slides.length - 1; }
    
    showSlide(slidesWrapper, slides, pontos);
}

function irParaSlide(index) {
    const slidesWrapper = document.getElementById("carrosselSlides");
    const slides = document.querySelectorAll(".carrossel-slide");
    const pontos = document.querySelectorAll(".carrossel-ponto");

    if (!slidesWrapper) return;
    slideIndex = index;
    showSlide(slidesWrapper, slides, pontos);
}

function showSlide(wrapper, slides, pontos) {
    // Move o carrossel em 100% para cada slide
    wrapper.style.transform = `translateX(-${slideIndex * 100}%)`;
    
    // Atualiza estados visuais
    slides.forEach((slide, index) => {
        slide.classList.toggle("active", index === slideIndex);
    });

    pontos.forEach((ponto, index) => {
        ponto.classList.toggle("active", index === slideIndex);
    });
}