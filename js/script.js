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
    const temaSalvo = localStorage.getItem('temaEscolhidoWesteros');
    if (temaSalvo) {
        mudarTema(temaSalvo);
    }

    if (typeof characterContainer !== 'undefined' && characterContainer) {
        carregarPersonagens();
    }

    if (typeof conjurarNeve === 'function') {
        conjurarNeve();
    }

    // Inicia o observador de rolagem (Fade-in)
    iniciarObservadorAnimacoes();

    // Inicia os sussurros do Varys
    inicializarSussurros();
    
    // Inicia o Botão de Voltar ao Topo
    iniciarBotaoTopo();
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
   5. SISTEMA DE CARROSSEL 
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
    wrapper.style.transform = `translateX(-${slideIndex * 100}%)`;
    
    slides.forEach((slide, index) => {
        slide.classList.toggle("active", index === slideIndex);
    });

    pontos.forEach((ponto, index) => {
        ponto.classList.toggle("active", index === slideIndex);
    });
}

/* =========================================================
   6. EFEITO DE NEVE (ANIMAÇÃO DE FLOCOS CAINDO)
   ========================================================= */
function conjurarNeve() {
    const snowContainer = document.getElementById('snow-container');
    if (!snowContainer) return; 

    const quantidadeFlocos = 70; 

    for (let i = 0; i < quantidadeFlocos; i++) {
        const floco = document.createElement('div');
        floco.classList.add('snowflake');
        
        floco.style.left = `${Math.random() * 100}%`;
        
        const tamanho = Math.random() * 3 + 2;
        floco.style.width = `${tamanho}px`;
        floco.style.height = `${tamanho}px`;
        
        const duracao = Math.random() * 9 + 6;
        floco.style.animationDuration = `${duracao}s`;
        
        floco.style.animationDelay = `${Math.random() * 5}s`;
        
        floco.style.opacity = Math.random();

        snowContainer.appendChild(floco);
    }
}

/* =========================================================
   7. ANIMAÇÕES DE ROLAGEM (FADE-IN OBSERVER)
   ========================================================= */
function iniciarObservadorAnimacoes() {
    const observador = new IntersectionObserver((entradas) => {
        entradas.forEach((entrada) => {
            if (entrada.isIntersecting) {
                entrada.target.classList.add('is-visible');
                observador.unobserve(entrada.target);
            }
        });
    }, {
        rootMargin: '0px 0px -50px 0px', 
        threshold: 0.15 
    });

    const elementosOcultos = document.querySelectorAll('.fade-in-section');
    elementosOcultos.forEach((el) => observador.observe(el));
}

/* =========================================================
   8. OS SUSSURROS DE VARYS (CURIOSIDADES ALEATÓRIAS)
   ========================================================= */
const curiosidadesVarys = [
    "A Fortaleza Vermelha levou décadas para ser construída. Quando o Rei Maegor, o Cruel, finalizou a obra, ele mandou matar todos os construtores para que ninguém além dele conhecesse as passagens secretas.",
    "O Trono de Ferro original dos livros é descrito como uma monstruosidade assimétrica de espadas retorcidas, com quase 12 metros de altura, onde os reis frequentemente se cortavam e sangravam.",
    "A Muralha não é feita apenas de gelo, terra e pedra. Ela possui feitiços antigos e poderosos tecidos nela para impedir que criaturas mágicas cruzem para o sul.",
    "Valíria não era governada por um rei, mas por quarenta famílias nobres de senhores de dragões que disputavam o poder. Curiosamente, os Targaryen não eram os mais poderosos entre eles.",
    "Aerys II, o Rei Louco, não era insano na juventude. Sua paranóia e crueldade se agravaram após o 'Desafio de Valdocaso', onde foi mantido refém por meses por um de seus próprios lordes.",
    "Sor Barristan Selmy entrou furtivamente em Valdocaso disfarçado de mendigo para resgatar o Rei Aerys II, um feito considerado uma das maiores missões de infiltração da história.",
    "Antes da chegada de Aegon, o Conquistador, Porto Real não passava de três colinas cobertas de florestas onde pescadores locais trabalhavam.",
    "Castamere, a sede da Casa Reyne, era em grande parte subterrânea. Tywin Lannister os derrotou desviando um rio e inundando as minas, afogando todos lá dentro, fato que inspirou a canção 'As Chuvas de Castamere'.",
    "Aegon IV, o Indigno, legitimou todos os seus bastardos em seu leito de morte, desencadeando as cinco sangrentas Rebeliões Blackfyre que assombraram os Targaryen por gerações.",
    "A espada de aço valiriano de Aegon, o Conquistador, se chamava 'Blackfyre'. A de sua irmã Visenya era 'Irmã Sombria'. O paradeiro de ambas é atualmente um grande mistério nos livros.",
    "Harrenhal foi o maior castelo já construído em Westeros. O Rei Harren achou que suas paredes colossais o protegeriam dos Targaryen, esquecendo de um detalhe fatal: dragões podem voar.",
    "O famoso Lema da Casa Lannister, 'Um Lannister sempre paga suas dívidas', não é o lema oficial. As verdadeiras palavras da Casa são 'Ouça-me Rugir'.",
    "Os meistres da Cidadela forjam colares com metais diferentes para cada área de estudo. Ouro para matemática, prata para medicina, e o raro aço valiriano para o estudo de magia e ocultismo.",
    "Os Filhos da Floresta criaram os Caminhantes Brancos espetando vidro de dragão no coração de homens vivos, uma arma desesperada para se defenderem da invasão dos Primeiros Homens.",
    "A Dança dos Dragões, a trágica guerra civil Targaryen, foi o evento que mais causou a morte e o quase completo desaparecimento dos dragões no mundo conhecido.",
    "Aenys I, o segundo rei Targaryen, era tão fraco, indeciso e frágil que muitos em Westeros duvidavam que ele fosse realmente filho do imponente Aegon, o Conquistador.",
    "O Deus de Muitas Faces, adorado pelos Homens Sem Rosto em Braavos, é na verdade a personificação da morte extraída de todas as outras religiões do mundo conhecido.",
    "A espada 'Gelo', usada por Ned Stark, era tão colossal que em combates normais seria inútil. Tywin Lannister a derreteu para forjar a 'Lamento de Viúva' e a 'Cumpridora de Promessas'.",
    "O continente de Essos é tão vasto e misterioso que suas fronteiras orientais, como Yi Ti, Asshai e as Terras Sombrias, são praticamente desconhecidas e temidas pelos meistres de Westeros.",
    "No livro, o castelo de Pedra do Dragão foi todo esculpido e moldado com fogo mágico de dragão, dando às suas torres e muralhas as formas perfeitas de gárgulas e dragões reais."
];

function inicializarSussurros() {
    const btnVarys = document.getElementById('btnVarys');
    const textoSussurro = document.getElementById('texto-sussurro');

    if (btnVarys && textoSussurro) {
        btnVarys.addEventListener('click', () => {
            const indexAleatorio = Math.floor(Math.random() * curiosidadesVarys.length);
            
            textoSussurro.style.opacity = 0;
            
            setTimeout(() => {
                textoSussurro.innerHTML = `<strong>Você sabia?</strong> ${curiosidadesVarys[indexAleatorio]}`;
                textoSussurro.style.opacity = 1;
            }, 300);
        });
    }
}

/* =========================================================
   9. BOTÃO VOLTAR AO TOPO (MAGIA GLOBAL)
   ========================================================= */
function iniciarBotaoTopo() {

    const btnTopo = document.createElement('button');
    btnTopo.innerHTML = '&#8679;'; 
    btnTopo.className = 'btn-voltar-topo';
    btnTopo.title = "Voltar ao topo da página";
    document.body.appendChild(btnTopo);

   
    window.addEventListener('scroll', () => {
        
        if (window.scrollY > 300) {
            btnTopo.classList.add('mostrar');
        } else {
            btnTopo.classList.remove('mostrar');
        }
    });

    
    btnTopo.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' 
        });
    });
}