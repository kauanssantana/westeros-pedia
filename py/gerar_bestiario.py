import json

bestiario_westeros = [
    # ================= OS DRAGÕES DA CONQUISTA E DE GOT =================
    {
        "id": "balerion",
        "nome": "Balerion, o Terror Negro",
        "categoria": "Dragão",
        "tamanho": "Colossal",
        "imagem": "img/best_balerion.jpg",
        "descricao": "O maior e mais antigo dragão dos Targaryen. As suas chamas eram negras como a noite e dizia-se que a sua sombra cobria cidades inteiras. Foi a montaria de Aegon, o Conquistador, e derreteu as colossais torres de Harrenhal."
    },
    {
        "id": "vhagar",
        "nome": "Vhagar",
        "categoria": "Dragão",
        "tamanho": "Colossal",
        "imagem": "img/best_vhagar.jpg",
        "descricao": "A montaria original da Rainha Visenya. Na época da Dança dos Dragões, era a maior criatura viva do mundo. Uma veterana ranzinza e coberta de cicatrizes de cem batalhas, montada finalmente pelo Príncipe Aemond Caolho."
    },
    {
        "id": "meraxes",
        "nome": "Meraxes",
        "categoria": "Dragão",
        "tamanho": "Colossal",
        "imagem": "img/best_meraxes.jpg",
        "descricao": "A gloriosa montaria de escamas prateadas e olhos dourados da Rainha Rhaenys Targaryen durante a Conquista. Era maior que Vhagar, mas menor que Balerion. Foi tragicamente abatida por um dardo de escorpião no olho durante a guerra em Dorne."
    },
    {
        "id": "drogon",
        "nome": "Drogon",
        "categoria": "Dragão",
        "tamanho": "Gigante",
        "imagem": "img/best_drogon.jpg",
        "descricao": "A reencarnação do próprio Balerion, segundo os Dothraki. O maior e mais feroz dos três dragões nascidos de Daenerys Targaryen. De escamas negras e chamas vermelhas, foi a montaria da rainha e reduziu Porto Real a cinzas."
    },
    {
        "id": "rhaegal",
        "nome": "Rhaegal",
        "categoria": "Dragão",
        "tamanho": "Gigante",
        "imagem": "img/best_rhaegal.jpeg",
        "descricao": "Batizado em honra ao Príncipe Rhaegar Targaryen. Possuía escamas de um verde profundo com detalhes em bronze. Lutou bravamente na Batalha de Winterfell sob o comando de Jon Snow, antes de encontrar um fim trágico perante a frota Greyjoy."
    },
    {
        "id": "viserion",
        "nome": "Viserion",
        "categoria": "Dragão",
        "tamanho": "Gigante",
        "imagem": "img/best_viserion.jpg",
        "descricao": "O dragão de escamas creme e douradas, batizado em memória do irmão de Daenerys. Foi morto pelo Rei da Noite e ressuscitado como uma besta morta-viva, cuspindo fogo azul que foi capaz de destruir a Muralha milenar."
    },

    {
        "id": "caraxes",
        "nome": "Caraxes, o Verme Sangrento",
        "categoria": "Dragão",
        "tamanho": "Grande",
        "imagem": "img/best_caraxes.jpg",
        "descricao": "Vermelho, esguio, veloz e brutalmente experiente em batalha. Caraxes possuía um pescoço invulgarmente longo e um guincho aterrador. Foi a montaria letal e inseparável do Príncipe Daemon Targaryen."
    },
    {
        "id": "syrax",
        "nome": "Syrax",
        "categoria": "Dragão",
        "tamanho": "Grande",
        "imagem": "img/best_syrax.jpg",
        "descricao": "A majestosa dragão de escamas amarelas, montaria exclusiva da Rainha Rhaenyra Targaryen. Imponente e ferozmente protetora, Syrax foi o principal símbolo do poder da facção dos Pretos."
    },
    {
        "id": "meleys",
        "nome": "Meleys, a Rainha Vermelha",
        "categoria": "Dragão",
        "tamanho": "Grande",
        "imagem": "img/best_meleys.jpg",
        "descricao": "Uma fera de escamas carmesim e membranas rosadas, conhecida por ser uma das dragões mais rápidas que já cruzou os céus. Montada pela Princesa Rhaenys, travou uma batalha épica contra Vhagar e Sunfyre."
    },
    {
        "id": "sunfyre",
        "nome": "Sunfyre, o Dourado",
        "categoria": "Dragão",
        "tamanho": "Médio",
        "imagem": "img/best_sunfyre.jpg",
        "descricao": "Considerado pelos meistres como o dragão mais belo já visto, com escamas de ouro reluzente e chamas de fogo rosado. Foi a leal montaria do Rei Aegon II Targaryen."
    },
    {
        "id": "vermithor",
        "nome": "Vermithor, a Fúria de Bronze",
        "categoria": "Dragão",
        "tamanho": "Colossal",
        "imagem": "img/best_vermithor.jpg",
        "descricao": "Outrora a montaria do amado Rei Jaehaerys. Com quase cem anos durante a Dança, Vermithor era o segundo maior dragão vivo, perdendo apenas para Vhagar. Uma besta temível que repousava em Pedra do Dragão."
    },
    {
        "id": "silverwing",
        "nome": "Silverwing (Asa de Prata)",
        "categoria": "Dragão",
        "tamanho": "Gigante",
        "imagem": "img/best_silverwing.jpg",
        "descricao": "A companheira de Vermithor e antiga montaria da Boa Rainha Alysanne. Era um dragão mais dócil com escamas prateadas que brilhavam ao sol, mas igualmente letal quando provocada."
    },
    {
        "id": "seasmoke",
        "nome": "Seasmoke (Fumaresia)",
        "categoria": "Dragão",
        "tamanho": "Médio",
        "imagem": "img/best_seasmoke.jpg",
        "descricao": "Um jovem e ágil dragão cinzento-pálido, perfeito para táticas de evasão. Foi orgulhosamente montado por Sor Laenor Velaryon na Guerra dos Degraus."
    },
    {
        "id": "arrax",
        "nome": "Arrax",
        "categoria": "Dragão",
        "tamanho": "Pequeno",
        "imagem": "img/best_arrax.jpg",
        "descricao": "Jovem, veloz e com escamas branco-peroladas, Arrax era a montaria do Príncipe Lucerys Velaryon. Não foi páreo para a fúria descomunal de Vhagar em Ponta Tempestade."
    },
    {
        "id": "vermax",
        "nome": "Vermax",
        "categoria": "Dragão",
        "tamanho": "Médio",
        "imagem": "img/best_vermax.jpg",
        "descricao": "O dragão verde-oliva do Príncipe Jacaerys Velaryon. Cresceu forte e leal, viajando com Jacaerys até Winterfell para assegurar o apoio da Casa Stark."
    },
    {
        "id": "dreamfyre",
        "nome": "Dreamfyre (Fogo de Sonho)",
        "categoria": "Dragão",
        "tamanho": "Gigante",
        "imagem": "img/best_dreamfyre.jpg",
        "descricao": "Uma dragão esbelta de escamas azul-claras e marcas prateadas, montaria da Rainha Helaena Targaryen. Teoriza-se que os ovos de Daenerys foram postos originalmente por Dreamfyre."
    },
    {
        "id": "moondancer",
        "nome": "Moondancer (Bailalua)",
        "categoria": "Dragão",
        "tamanho": "Pequeno",
        "imagem": "img/best_moondancer.jpg",
        "descricao": "A jovem dragão verde-pálido da Senhora Baela Targaryen. Embora pequena na época da Dança, compensava em extrema velocidade e agilidade."
    },
    {
        "id": "canibal",
        "nome": "O Canibal",
        "categoria": "Dragão",
        "tamanho": "Gigante",
        "imagem": "img/best_canibal.jpg",
        "descricao": "O mais terrível dos dragões selvagens de Pedra do Dragão. Negro como carvão com olhos verdes venenosos, recebeu o seu nome por devorar dragões mortos e recém-nascidos. Nunca foi domado."
    },
    {
        "id": "fantasma",
        "nome": "Fantasma (Ghost)",
        "categoria": "Lobo Gigante",
        "tamanho": "Grande",
        "imagem": "img/best_fantasma.jpg",
        "descricao": "O lobo gigante albino de Jon Snow. Diferente dos seus irmãos, Fantasma nunca emite som, caçando em silêncio absoluto. Feroz e intensamente leal, acompanhou Jon Além da Muralha."
    },
    {
        "id": "vento-cinzento",
        "nome": "Vento Cinzento",
        "categoria": "Lobo Gigante",
        "tamanho": "Grande",
        "imagem": "img/batalha_bosque.jpg",
        "descricao": "O temível companheiro de Robb Stark. Tornou-se numa lenda aterrorizante, arrancando braços e matando cavalos em batalha. Morreu de forma trágica nas Gêmeas."
    },
    {
        "id": "nymeria",
        "nome": "Nymeria",
        "categoria": "Lobo Gigante",
        "tamanho": "Enorme",
        "imagem": "img/best_nymeria.jpg",
        "descricao": "A loba de Arya Stark. Após morder Joffrey, foi enxotada para a floresta para não ser morta. Sobreviveu nas Terras Fluviais, tornando-se a alfa colossal de uma gigantesca alcateia."
    },
    {
        "id": "caminhantes",
        "nome": "Caminhantes Brancos",
        "categoria": "Magia Negra",
        "tamanho": "Humanoide",
        "imagem": "img/best_caminhantes.jpg",
        "descricao": "Demónios de gelo criados na Era da Aurora pelas Crianças da Floresta. A sua presença traz o frio absoluto, e as suas lâminas de cristal quebram o aço comum num piscar de olhos."
    },
    {
        "id": "wights",
        "nome": "Criaturas (Wights)",
        "categoria": "Magia Negra",
        "tamanho": "Variável",
        "imagem": "img/best_wights.jpg",
        "descricao": "Cadáveres reanimados pela magia do Rei da Noite. Podem ser humanos, ursos ou dragões. Têm olhos azul-incandescentes e apenas podem ser destruídos por fogo, vidro de dragão ou aço valiriano."
    },
    {
        "id": "sombra",
        "nome": "Sombra Assassina",
        "categoria": "Magia Negra",
        "tamanho": "Humanoide",
        "imagem": "img/best_sombra.jpg",
        "descricao": "Entidades demoníacas de fumaça e escuridão conjuradas por Sacerdotes Vermelhos. Nascidas de magia de sangue e essência vital, deslizam pelas sombras para assassinar alvos específicos, como aconteceu com Renly Baratheon."
    },
    {
        "id": "aranhas-gelo",
        "nome": "Aranhas de Gelo Gigantes",
        "categoria": "Magia Negra",
        "tamanho": "Enorme",
        "imagem": "img/best_aranhas_gelo.jpg",
        "descricao": "Lendas aterrorizantes partilhadas pela Velha Ama e pelos Selvagens. Conta-se que, durante a primeira Longa Noite, os Caminhantes Brancos caçavam homens cavalgando aranhas de gelo pálidas e gigantescas como cães de caça infernais."
    },
    {
        "id": "homens-pedra",
        "nome": "Homens de Pedra",
        "categoria": "Aberração",
        "tamanho": "Humanoide",
        "imagem": "img/best_homens_pedra.jpg",
        "descricao": "Vítimas no estágio terminal da letal doença Escamagris. A sua pele torna-se cinzenta, dura e rachada como pedra. Habitam as ruínas enevoadas e amaldiçoadas de Valíria, enlouquecidos pela dor e altamente contagiosos ao menor toque."
    },
    {
        "id": "gigantes",
        "nome": "Gigantes",
        "categoria": "Raças Antigas",
        "tamanho": "Colossal",
        "imagem": "img/best_gigantes.jpg",
        "descricao": "Criaturas humanoides maciças e peludas que habitam o Extremo Norte. Montam mamutes e empunham troncos de árvores inteiras. Wun Wun foi um dos últimos e mais heroicos aliados do Povo Livre e de Jon Snow."
    },
    {
        "id": "criancas-floresta",
        "nome": "Crianças da Floresta",
        "categoria": "Raças Antigas",
        "tamanho": "Pequeno",
        "imagem": "img/best_criancas.jpg",
        "descricao": "Os habitantes originais de Westeros. Pequenos, com olhos felinos e dotados de profunda magia da terra. Foram eles que esculpiram os misteriosos rostos nas árvores de represeiro."
    },
    {
        "id": "krakens",
        "nome": "Krakens",
        "categoria": "Feras Exóticas",
        "tamanho": "Colossal",
        "imagem": "img/best_kraken.jpg",
        "descricao": "Monstros marinhos lendários que habitam as profundezas dos oceanos. Armados com tentáculos maciços, as lendas afirmam que podem afundar e estilhaçar galeões inteiros. São o orgulhoso e temido símbolo da Casa Greyjoy."
    },
    {
        "id": "manticora",
        "nome": "Mantícora",
        "categoria": "Feras Exóticas",
        "tamanho": "Pequeno",
        "imagem": "img/best_manticora.jpg",
        "descricao": "Um inseto monstruoso originário das Ilhas do Mar de Jade. Assemelha-se a um escaravelho escuro, mas ao abrir as asas, revela um rosto humanoide maligno. O seu ferrão contém um veneno poderoso e fatal, frequentemente usado por assassinos furtivos em Essos."
    }
]

with open('../bestiario.json', 'w', encoding='utf-8') as f:
    json.dump(bestiario_westeros, f, ensure_ascii=False, indent=4)

print("bestiario.json forjado com sucesso! A fauna letal foi registada.")