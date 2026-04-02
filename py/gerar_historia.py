import json

historia_westeros = [
    {
        "id": "origem-caminhantes",
        "ano": "~ 8000 a.C.",
        "titulo": "A Criação do Rei da Noite",
        "foco": "A Era da Aurora",
        "imagem": "img/hist_caminhantes.jpg",
        "descricao": "O maior erro da história mágica. Desesperadas e a perder a guerra contra a invasão dos Primeiros Homens, as Crianças da Floresta capturaram um homem e cravaram uma adaga de vidro de dragão no seu coração junto a uma árvore de represeiro. O feitiço transformou-o no primeiro Caminhante Branco, uma arma de gelo e morte que eventualmente se viraria contra os seus próprios criadores."
    },
    {
        "id": "perdicao-valiria",
        "ano": "114 a.C.",
        "titulo": "A Perdição de Valíria",
        "foco": "O Fim da Magia",
        "imagem": "img/hist_valiria.jpg",
        "descricao": "O cataclismo que destruiu o maior império que o mundo já conheceu. Num único dia, os vulcões conhecidos como 'Os Quatorze Fogos' explodiram simultaneamente, engolindo os temíveis senhores de dragões, as suas torres de vidro e a sua magia em fogo e cinzas. Apenas a Casa Targaryen sobreviveu graças a uma visão profética de Daenys, a Sonhadora, fugindo a tempo para a remota ilha de Pedra do Dragão."
    },
    {
        "id": "conquista-aegon",
        "ano": "1 d.C.",
        "titulo": "A Conquista de Aegon",
        "foco": "O Nascimento de um Império",
        "imagem": "img/hist_aegon.jpg",
        "descricao": "Montados em três dragões colossais, Aegon Targaryen e as suas irmãs, Visenya e Rhaenys, forçaram a submissão dos Sete Reinos independentes de Westeros. Castelos derreteram sob o fogo de Balerion, o Terror Negro, e espadas rendidas foram fundidas no fogo místico para criar o assento mais perigoso do mundo: o Trono de Ferro."
    },
    {
        "id": "morte-lucerys",
        "ano": "129 d.C.",
        "titulo": "A Morte de Lucerys Velaryon",
        "foco": "Dança dos Dragões",
        "imagem": "img/hist_lucerys.jpg",
        "descricao": "O ponto sem retorno da guerra civil. O jovem Príncipe Lucerys foi a Ponta Tempestade como mensageiro pacífico, mas encontrou o seu tio Aemond. No meio de uma tempestade aterrorizante acima da Baía dos Naufrágios, a colossal Vhagar desobedeceu aos comandos de Aemond e devorou Lucerys e o seu pequeno dragão Arrax. Com esta mordida, a diplomacia morreu."
    },
    {
        "id": "sangue-queijo",
        "ano": "129 d.C.",
        "titulo": "Sangue e Queijo",
        "foco": "Um Filho por um Filho",
        "imagem": "img/hist_sangue_queijo.jpg",
        "descricao": "A vingança sombria de Daemon Targaryen pela morte de Lucerys. Dois assassinos, conhecidos apenas como Sangue e Queijo, infiltraram-se na Fortaleza Vermelha. Eles obrigaram a Rainha Helaena a escolher qual dos seus filhos seria executado, antes de decapitarem brutalmente o pequeno Príncipe Jaehaerys, mergulhando os Verdes no desespero absoluto."
    },
    {
        "id": "morte-baelor",
        "ano": "209 d.C.",
        "titulo": "A Morte de Baelor Quebra-Lanças",
        "foco": "O Julgamento dos Sete",
        "imagem": "img/hist_baelor.jpg",
        "descricao": "Durante o Torneio de Vaufreixo, o humilde cavaleiro andante Sor Duncan, o Alto, exigiu um Julgamento por Combate para provar a sua inocência de ter agredido um príncipe. O Príncipe Herdeiro, Baelor Targaryen, aclamado como o melhor cavaleiro do reino, surpreendeu a todos ao lutar a favor de Dunk, contra a sua própria família. Após a vitória de Dunk, Baelor retirou o seu capacete arruinado e revelou um ferimento fatal desferido pela maça do seu irmão Maekar, tombando morto na terra. O reino chorou aquele que teria sido um dos maiores reis da história."
    },
    {
        "id": "solarestival",
        "ano": "259 d.C.",
        "titulo": "A Tragédia de Solarestival",
        "foco": "O Preço da Magia",
        "imagem": "img/hist_solarestival.jpg",
        "descricao": "O Rei Aegon V (Egg) tentou realizar o milagre de chocar ovos de dragão petrificados no palácio de verão da Casa Targaryen. O ritual com fogo vivo saiu terrivelmente do controle, resultando num incêndio catastrófico que matou o rei, o Príncipe Duncan e o lendário Senhor Comandante Sor Duncan, o Alto. Das cinzas e lágrimas dessa noite, nasceu o Príncipe Rhaegar Targaryen."
    },
    {
        "id": "torneio-harrenhal",
        "ano": "281 d.C.",
        "titulo": "O Torneio de Harrenhal",
        "foco": "A Coroa de Inverno",
        "imagem": "img/hist_harrenhal.jpg",
        "descricao": "O evento que plantou as sementes da destruição dos Targaryen. Após vencer o maior torneio da época, o Príncipe Rhaegar Targaryen chocou todos os Sete Reinos: em vez de coroar a sua esposa, a Princesa Elia Martell, ele cavalgou até Lyanna Stark e depositou uma coroa de rosas azuis de inverno no seu colo. Naquele dia silencioso e tenso, a faísca da Rebelião de Robert foi acesa."
    },
    {
        "id": "regicida",
        "ano": "283 d.C.",
        "titulo": "A Ascensão do Regicida",
        "foco": "A Queda do Rei Louco",
        "imagem": "img/hist_regicida.jpg",
        "descricao": "Enquanto o exército rebelde de Robert Baratheon vencia no Tridente, Tywin Lannister invadiu e saqueou Porto Real. Recusando-se a render, o Rei Louco Aerys II ordenou aos piromantes que queimassem toda a cidade com estoques secretos de fogo vivo. Para salvar milhões de inocentes, o jovem Sor Jaime Lannister quebrou os seus votos, degolou os piromantes e cravou a sua espada dourada nas costas do seu próprio rei."
    },
    {
        "id": "torre-alegria",
        "ano": "283 d.C.",
        "titulo": "O Segredo da Torre da Alegria",
        "foco": "A Promessa de Gelo e Fogo",
        "imagem": "img/hist_torre_alegria.jpg",
        "descricao": "O fim sangrento da Rebelião de Robert guardava o maior segredo de Westeros. Após derrotar Sor Arthur Dayne, Ned Stark encontrou a sua irmã Lyanna a morrer num leito de sangue. Com o seu último suspiro, ela implorou 'Promete-me, Ned', entregando-lhe o seu filho recém-nascido com Rhaegar Targaryen. Para proteger a criança da ira de Robert, Ned assumiu-o como o seu próprio bastardo: Jon Snow."
    },
    {
        "id": "queda-bran",
        "ano": "298 d.C.",
        "titulo": "A Queda de Bran Stark",
        "foco": "As Coisas Feitas por Amor",
        "imagem": "img/hist_queda_bran.png",
        "descricao": "A faísca que incendiou a Guerra dos Cinco Reis. O jovem Bran Stark, ao escalar uma das torres de Winterfell, testemunhou o segredo mais obscuro da rainha: o incesto entre Cersei e Jaime Lannister. Para proteger a coroa, Jaime empurrou o rapaz da janela. Bran sobreviveu paralisado, iniciando a sua jornada para se tornar o Corvo de Três Olhos."
    },
    {
        "id": "morte-ned",
        "ano": "298 d.C.",
        "titulo": "A Execução de Eddard Stark",
        "foco": "Game of Thrones",
        "imagem": "img/hist_ned.jpg",
        "descricao": "O momento em que Westeros perdeu a sua inocência. Ned Stark, a Mão do Rei e o homem mais honrado dos Sete Reinos, confessou falsamente traição para salvar as suas filhas. No entanto, o cruel e imprevisível Rei Joffrey ignorou o conselho da sua mãe e ordenou a decapitação de Ned nas escadarias do Grande Septo de Baelor."
    },
    {
        "id": "nascimento-dragoes",
        "ano": "299 d.C.",
        "titulo": "O Renascimento dos Dragões",
        "foco": "A Mãe de Dragões",
        "imagem": "img/hist_dragoes.jpg",
        "descricao": "A magia havia abandonado o mundo há séculos. Nas terras desoladas de Essos, Daenerys Targaryen entrou na pira funerária em chamas do seu marido Khal Drogo, carregando três ovos petrificados. Ao amanhecer, as cinzas revelaram o impossível: Daenerys estava ilesa, e três pequenos dragões haviam nascido."
    },
    {
        "id": "astapor",
        "ano": "299 d.C.",
        "titulo": "A Libertação de Astapor",
        "foco": "Dracarys",
        "imagem": "img/hist_astapor.jpg",
        "descricao": "A transição de Daenerys de sobrevivente para rainha conquistadora. Fingindo vender o seu dragão Drogon em troca do formidável exército de Imaculados, Daenerys revelou fluência em Alto Valiriano. Com uma única e letal palavra — 'Dracarys' —, ela incinerou os cruéis Mestres Escravagistas e cedeu aos Imaculados a sua liberdade, forjando a sua maior aliança."
    },
    {
        "id": "casamento-vermelho",
        "ano": "299 d.C.",
        "titulo": "O Casamento Vermelho",
        "foco": "A Maior Traição",
        "imagem": "img/hist_casamento.jpg",
        "descricao": "O evento mais chocante da história de Westeros. Sob a melodia sombria de 'As Chuvas de Castamere', Lorde Walder Frey e Roose Bolton traíram a sagrada lei da hospitalidade. O Rei do Norte, Robb Stark, a sua esposa grávida Talisa e a sua mãe Catelyn foram brutalmente assassinados num banquete, extinguindo a rebelião do Norte num mar de sangue."
    },
    {
        "id": "casamento-purpura",
        "ano": "300 d.C.",
        "titulo": "O Casamento Púrpura",
        "foco": "A Morte de um Tirano",
        "imagem": "img/hist_joffrey.jpg",
        "descricao": "A justiça finalmente alcançou o sádico Joffrey. Durante o seu suntuoso banquete de casamento com Margaery Tyrell, o rei bebeu vinho envenenado com 'O Estrangulador'. Diante de toda a corte, o jovem tirano asfixiou-se até à morte, com o rosto roxo e a sangrar. A culpa recaiu sobre Tyrion, mas a arquiteta oculta foi Olenna Tyrell."
    },
    {
        "id": "julgamento-tyrion",
        "ano": "300 d.C.",
        "titulo": "O Julgamento de Tyrion",
        "foco": "Eu Exijo um Julgamento por Combate!",
        "imagem": "img/hist_tyrion.jpg",
        "descricao": "Acusado injustamente de envenenar Joffrey, Tyrion suportou a farsa de um julgamento até ver a mulher que amava, Shae, mentir contra ele. Num acesso de fúria e dor absoluta, proferiu o discurso mais marcante da capital, confessando apenas o 'crime de ser anão' e exigindo um julgamento por combate."
    },
    {
        "id": "caminhada-cersei",
        "ano": "301 d.C.",
        "titulo": "A Caminhada da Expiação",
        "foco": "Vergonha!",
        "imagem": "img/hist_cersei_shame.jpg",
        "descricao": "Uma rainha orgulhosa reduzida ao chão. O fanático Alto Pardal, a quem Cersei Lannister entregou poder ingenuamente, virou as suas forças contra ela. Despida das suas sedas, com os cabelos cortados e rodeada pelos gritos de 'Vergonha!' de milhares de plebeus, Cersei foi forçada a caminhar ensanguentada pelas ruas da capital."
    },
    {
        "id": "ressurreicao-jon",
        "ano": "302 d.C.",
        "titulo": "A Ressurreição de Jon Snow",
        "foco": "O Senhor da Luz",
        "imagem": "img/hist_ressurreicao_jon.jpg",
        "descricao": "Após ser brutalmente apunhalado e traído pelos seus próprios irmãos da Patrulha da Noite, Jon Snow foi encontrado morto. A Sacerdotisa Vermelha, Melisandre, realizando um ritual desesperado, clamou ao Senhor da Luz. Contra todas as leis da natureza, Jon abriu os olhos e o seu dever na Patrulha foi encerrado pela morte."
    },
    {
        "id": "sacrificio-hodor",
        "ano": "303 d.C.",
        "titulo": "O Segredo de Hodor",
        "foco": "Hold the Door",
        "imagem": "img/hist_hodor.jpg",
        "descricao": "Um dos paradoxos mais trágicos da magia em Westeros. Enquanto fugiam dos Caminhantes Brancos, Bran Stark usou as suas visões para entrar na mente de Hodor no presente e do jovem Wylis no passado simultaneamente. O eco de Meera Reed a gritar 'Segura a porta!' quebrou a mente do menino Wylis, ditando o seu destino trágico para salvar Bran."
    },
    {
        "id": "explosao-septo",
        "ano": "303 d.C.",
        "titulo": "A Explosão do Grande Septo",
        "foco": "O Fogo Vivo de Cersei",
        "imagem": "img/hist_septo.jpg",
        "descricao": "Encurralada pela Fé Militante e pela astúcia da Casa Tyrell, Cersei Lannister optou pela aniquilação total. Em vez de comparecer ao seu julgamento, incendiou os estoques secretos de Fogo Vivo sob o Grande Septo de Baelor. Uma explosão verde colossal vaporizou o Alto Pardal e a Rainha Margaery, eliminando todos os inimigos num único instante."
    },
    {
        "id": "queda-muralha",
        "ano": "304 d.C.",
        "titulo": "A Queda da Muralha",
        "foco": "O Inverno Chegou",
        "imagem": "img/hist_muralha.jpg",
        "descricao": "A estrutura de gelo maciço que protegeu os reinos dos homens por oito mil anos finalmente cedeu. Montado no dragão ressuscitado Viserion, o Rei da Noite cuspiu chamas de fogo azul intenso, derretendo Atalaialeste-do-Mar. Pelos escombros desabados, o exército de mais de cem mil mortos-vivos marchou livremente para o Sul."
    },
    {
        "id": "derretimento-trono",
        "ano": "305 d.C.",
        "titulo": "O Fim do Trono de Ferro",
        "foco": "Um Sonho de Primavera",
        "imagem": "img/hist_trono.jpg",
        "descricao": "O ato que encerrou o Jogo dos Tronos. Após Jon Snow assassinar Daenerys Targaryen, Drogon emitiu um rugido de dor que abalou a destruída Fortaleza Vermelha. Ignorando Jon, o dragão virou o seu fogo para o Trono de Ferro, derretendo o assento pelo qual milhares morreram, reduzindo-o a uma poça de escória incandescente."
    }
]

with open('../historia.json', 'w', encoding='utf-8') as f:
    json.dump(historia_westeros, f, ensure_ascii=False, indent=4)

print("historia.json forjado com sucesso! As 22 lendas essenciais da História foram registadas.")