import json

guerras_westeros = [
    {
        "id": "conquista",
        "nome": "A Conquista de Aegon",
        "ano": "2 a.C. - 1 d.C.",
        "combatentes": "Casa Targaryen vs. Os Sete Reinos Independentes",
        "desfecho": "Unificação de Westeros sob o Trono de Ferro",
        "imagem": "img/aegon.jpg",
        "descricao": "Aegon Targaryen e as suas irmãs-esposas, Visenya e Rhaenys, desembarcaram em Westeros com um exército pequeno, mas acompanhados pelo poder supremo: três dragões imensos. Durante a campanha, o impenetrável castelo de Harrenhal foi derretido por Balerion, exércitos combinados foram transformados em cinzas no brutal Campo de Fogo, e reis orgulhosos, como Torrhen Stark, ajoelharam-se para evitar a aniquilação. Foi o evento que unificou o continente, reiniciou o calendário do mundo e forjou o Trono de Ferro a partir do fogo negro e das espadas dos derrotados."
    },
    {
        "id": "degraus",
        "nome": "A Guerra nos Degraus",
        "ano": "106 d.C. - 109 d.C.",
        "combatentes": "Daemon Targaryen e Casa Velaryon vs. A Triarquia",
        "desfecho": "Vitória de Daemon; coroado Rei do Mar Estreito",
        "imagem": "img/batalha_degraus.jpg",
        "descricao": "Buscando glória longe da sombra do irmão e irritado com as taxas comerciais abusivas que prejudicavam Derivamarca, o Príncipe Daemon Targaryen e Lorde Corlys Velaryon iniciaram uma guerra brutal nas ilhas dos Degraus. A Triarquia utilizou táticas de guerrilha e cavernas para anular o poder do dragão Caraxes. O conflito atingiu o seu clímax sangrento quando Daemon fingiu uma rendição suicida para atrair Craghas Drahar, o temido Engorda Caranguejo, para fora das cavernas, cortando-o literalmente ao meio com a espada Irmã Sombria."
    },
    {
        "id": "pouso-gralhas",
        "nome": "A Batalha de Pouso de Gralhas",
        "ano": "129 d.C.",
        "combatentes": "Rhaenys Targaryen (Pretos) vs. Aegon II e Aemond (Verdes)",
        "desfecho": "Vitória dos Verdes; morte de Rhaenys e Meleys",
        "imagem": "img/batalha_pouso_gralhas.jpg",
        "descricao": "Uma emboscada meticulosamente orquestrada por Sor Criston Cole e um dos combates aéreos mais brutais da história. A Princesa Rhaenys, a 'Rainha Que Nunca Foi', atendeu ao pedido de socorro do castelo voando na sua experiente dragão Meleys. No entanto, foi surpreendida pelos irmãos Aegon II (em Sunfyre) e Aemond (na colossal Vhagar). Apesar da sua bravura inigualável e de ter ferido o Rei Aegon e Sunfyre quase mortalmente, o peso de Vhagar prevaleceu. Rhaenys e Meleys caíram dos céus em chamas e glória, marcando uma perda devastadora para a facção Negra."
    },
    {
        "id": "danca",
        "nome": "A Dança dos Dragões",
        "ano": "129 d.C. - 131 d.C.",
        "combatentes": "Os Pretos (Rhaenyra) vs. Os Verdes (Aegon II)",
        "desfecho": "Morte de quase todos os dragões e ruína da dinastia",
        "imagem": "img/guerra_danca.jpg",
        "descricao": "A guerra civil mais devastadora da dinastia Targaryen, iniciada após a morte do Rei Viserys I, quando o Conselho Verde usurpou o trono que pertencia por direito a Rhaenyra. O reino foi rasgado ao meio. Castelos foram incendiados, grandes casas foram dizimadas e a capital assistiu à sangrenta invasão do Fosso dos Dragões pela população enfurecida. O conflito fratricida resultou na extinção quase total das feras aladas e deixou a Casa Targaryen numa sombra do que outrora foi, culminando na coroação do traumatizado Aegon III."
    },
    {
        "id": "blackfyre",
        "nome": "A Primeira Rebelião Blackfyre",
        "ano": "196 d.C.",
        "combatentes": "Coroa Targaryen (Daeron II) vs. Rebeldes Blackfyre (Daemon I)",
        "desfecho": "Vitória Targaryen e exílio dos sobreviventes Blackfyre",
        "imagem": "img/guerra_blackfyre.jpg",
        "descricao": "O péssimo Rei Aegon IV legitimou todos os seus bastardos no leito de morte e entregou a espada ancestral 'Blackfyre' a Daemon, plantando as sementes para a maior revolta do século. Argumentando que Daeron II era ilegítimo e focado nos dorneses, Daemon Blackfyre ergueu os seus estandartes do dragão negro. O reino sangrou até à Batalha do Campo do Capim Vermelho, onde um mar de homens pereceu e a rebelião foi esmagada pelas flechas de represeiro do feiticeiro Corvo de Sangue, forçando os sobreviventes a fugir para Essos."
    },
    {
        "id": "rebeliao",
        "nome": "A Rebelião de Robert",
        "ano": "282 d.C. - 283 d.C.",
        "combatentes": "Aliança Rebelde (Baratheon, Stark, Arryn, Tully) vs. Coroa Targaryen",
        "desfecho": "Fim da Dinastia Targaryen e Coroação de Robert",
        "imagem": "img/rebeliao_robert.jpg",
        "descricao": "Desencadeada pelo desaparecimento de Lyanna Stark com Rhaegar Targaryen e pela atrocidade do Rei Louco, que queimou Lorde Rickard Stark vivo e estrangulou o seu herdeiro. Jon Arryn recusou-se a entregar as cabeças de Robert e Ned, erguendo as suas bandeiras em revolta. O conflito culminou no lendário vau do Tridente, onde o martelo de guerra de Robert Baratheon esmagou as pedras preciosas da armadura de Rhaegar, e foi finalizado pelo cruel Saque de Porto Real, onde Tywin Lannister traiu a coroa e exterminou a linhagem real."
    },
    {
        "id": "bosque-murmurios",
        "nome": "A Batalha do Bosque dos Murmúrios",
        "ano": "298 d.C.",
        "combatentes": "Exército do Norte (Robb Stark) vs. Exército Lannister (Jaime)",
        "desfecho": "Vitória Stark; Jaime Lannister capturado",
        "imagem": "img/batalha_bosque.jpg",
        "descricao": "O momento em que Robb Stark provou ser um génio tático. Enganando Tywin Lannister ao enviar uma força menor para o Tridente, Robb desceu com a sua cavalaria em segredo e armou uma emboscada noturna perfeita. O exército de Jaime Lannister foi pego desprevenido no bosque. Mesmo percebendo a derrota, o Regicida lutou furiosamente para tentar matar Robb num combate direto, mas as suas espadas falharam e o orgulhoso Leão Dourado foi feito prisioneiro do Jovem Lobo."
    },
    {
        
        "id": "cinco-reis",
        "nome": "A Guerra dos Cinco Reis",
        "ano": "298 d.C. - 300 d.C.",
        "combatentes": "Lannister vs. Stark vs. Baratheon (Stannis) vs. Baratheon (Renly) vs. Greyjoy",
        "desfecho": "Vitória Lannister (com alianças de Tyrell, Bolton e Frey)",
        "imagem": "img/guerra_cinco_reis.jpg",
        "descricao": "O continente foi lançado no mais puro caos após a caçada fatal de Robert Baratheon e a execução injusta de Ned Stark por Joffrey. Robb Stark foi coroado Rei do Norte, enquanto Stannis e Renly Baratheon disputavam o Sul, e Balon Greyjoy atacava as costas. A guerra viu o brilhantismo tático de Robb desfazer-se perante quebras de promessas, culminando no traiçoeiro Casamento Vermelho, orquestrado por Tywin Lannister, Roose Bolton e Walder Frey, redefinindo o conceito de honra em Westeros."
    },
    {
        "id": "agua-negra",
        "nome": "A Batalha da Água Negra",
        "ano": "299 d.C.",
        "combatentes": "Defensores Lannister/Tyrell vs. Frota de Stannis Baratheon",
        "desfecho": "Vitória da Coroa; Frota de Stannis dizimada pelo fogo vivo",
        "imagem": "img/batalha_agua_negra.jpg",
        "descricao": "O maior cerco anfíbio da Guerra dos Cinco Reis. Stannis Baratheon trouxe uma frota massiva para tomar Porto Real e depor o seu sobrinho bastardo. Graças ao génio tático da Mão do Rei, Tyrion Lannister, um navio carregado com a instável e mágica substância verde conhecida como Fogo Vivo foi lançado na baía, incinerando metade da armada inimiga numa explosão dantesca. As forças de Stannis quase tomaram os muros, mas foram esmagadas pela chegada de última hora da aliança Lannister-Tyrell."
    },
    {
        "id": "castelo-negro",
        "nome": "A Batalha de Castelo Negro",
        "ano": "300 d.C.",
        "combatentes": "Patrulha da Noite vs. Exército do Povo Livre (Selvagens)",
        "desfecho": "Vitória da Patrulha com a chegada surpresa de Stannis",
        "imagem": "img/batalha_castelo_negro.jpg",
        "descricao": "Impulsionados pelo medo dos mortos-vivos, cem mil selvagens unidos por Mance Rayder atacaram a Muralha com gigantes montados em mamutes e alpinistas mortíferos. Com a liderança superior ausente, o jovem patrulheiro Jon Snow assumiu o comando da defesa desesperada. A Patrulha resistiu usando barris inflamáveis e flechas na escuridão, sofrendo perdas dolorosas como a da guerreira Ygritte. Quando a Muralha parecia prestes a cair, a cavalaria de Stannis Baratheon emergiu da floresta, derrotando o Rei Próximo à Muralha."
    },
    {
        "id": "durolar",
        "nome": "O Massacre de Durolar (Hardhome)",
        "ano": "301 d.C.",
        "combatentes": "Povo Livre e Patrulha da Noite vs. O Exército dos Mortos",
        "desfecho": "Aniquilação quase total dos vivos; Retirada desesperada",
        "imagem": "img/batalha_durolar.jpg",
        "descricao": "Mais do que uma batalha, foi um aviso aterrorizante para os vivos. O Senhor Comandante Jon Snow viajou à baía gelada de Durolar para evacuar os selvagens restantes. Subitamente, um frio antinatural desceu das montanhas, trazendo consigo uma avalanche de mortos-vivos incontroláveis. Milhares foram massacrados. Jon Snow descobriu que o aço valiriano podia destruir Caminhantes Brancos, mas foi forçado a fugir nos barcos, assistindo em pânico absoluto ao Rei da Noite a erguer os braços e a ressuscitar todos os caídos."
    },
    {
        "id": "bastardos",
        "nome": "A Batalha dos Bastardos",
        "ano": "303 d.C.",
        "combatentes": "Exército Stark (Jon Snow) vs. Exército Bolton (Ramsay)",
        "desfecho": "Vitória Stark, retomada de Winterfell e morte de Ramsay",
        "imagem": "img/batalha_bastardos.jpg",
        "descricao": "Um confronto visceral e claustrofóbico que decidiu o destino do Norte. O sádico Ramsay Bolton utilizou o jovem Rickon Stark como isca, provocando Jon Snow a abandonar a sua estratégia e a liderar uma carga suicida. As forças Stark viram-se esmagadas sob uma parede de escudos e lanças dos Bolton, formando uma montanha asfixiante de cadáveres e lama. Quando a esperança parecia totalmente perdida, os Cavaleiros do Vale, convocados por Sansa Stark, romperam as linhas inimigas, permitindo que a bandeira do Lobo Gigante voltasse a hastear em Winterfell."
    },
    {
        "id": "estrada-ouro",
        "nome": "A Batalha da Estrada de Ouro (Espólios de Guerra)",
        "ano": "304 d.C.",
        "combatentes": "Exército Targaryen/Dothraki vs. Forças Lannister/Tarly",
        "desfecho": "Massacre das forças Lannister por Daenerys e Drogon",
        "imagem": "img/batalha_estrada_ouro.jpg",
        "descricao": "Após o saque bem-sucedido de Jardim de Cima, Jaime Lannister e os seus exércitos marchavam triunfantes com o ouro da Campina. O ar de tranquilidade foi quebrado pelo som de milhares de cascos: os temíveis senhores dos cavalos Dothraki. Mas o verdadeiro terror emergiu das nuvens. Daenerys Targaryen montada em Drogon varreu a linha de defesa Lannister num mar de chamas ardentes. Nem mesmo as balistas desenhadas por Qyburn impediram o massacre que provou aos Lordes de Westeros que a era dos Dragões não era apenas um mito distante."
    },
    {
        "id": "longa-noite",
        "nome": "A Batalha de Winterfell (A Longa Noite)",
        "ano": "305 d.C.",
        "combatentes": "Os Vivos (Aliança Stark-Targaryen) vs. O Exército dos Mortos",
        "desfecho": "Destruição do Rei da Noite e dos Caminhantes Brancos",
        "imagem": "img/guerra_longa_noite.jpg",
        "descricao": "A maior convergência de poder na história contra a ameaça apocalíptica. O Rei da Noite rompeu a Muralha com o seu dragão reanimado e lançou um manto de trevas sobre Winterfell. A formidável carga Dothraki foi extinta em segundos na escuridão. O castelo foi invadido e até as criptas provaram ser letais quando os Starks mortos despertaram. Com o fogo de dragão a provar ser ineficaz contra o Rei da Noite, foi necessário que Arya Stark aplicasse os seus treinos letais com uma adaga de aço valiriano para quebrar o Rei do Inverno e desintegrar todo o seu exército de uma só vez."
    },
    {
        "id": "porto-real",
        "nome": "O Saque de Porto Real (Os Sinos)",
        "ano": "305 d.C.",
        "combatentes": "Daenerys Targaryen (Drogon) e Imaculados vs. Defesas de Cersei",
        "desfecho": "Destruição completa da cidade e da Fortaleza Vermelha",
        "imagem": "img/batalha_porto_real.jpg",
        "descricao": "O momento final e devastador pelo Trono de Ferro. Apesar do exército Lannister e da Companhia Dourada terem soado os sinos em sinal de rendição, Daenerys Targaryen, impulsionada pela dor de inúmeras perdas e traições, cedeu à fúria. Drogon incinerou as defesas, os civis e a Fortaleza Vermelha quarteirão por quarteirão. Nas ruas, o caos reinou enquanto os exércitos invasores executavam os rendidos. Cersei e Jaime Lannister morreram esmagados sob o castelo, no dia em que a 'Quebradora de Correntes' se tornou a Rainha das Cinzas."
    }
]

# Volta uma pasta para salvar na raiz do projeto!
with open('../guerras.json', 'w', encoding='utf-8') as f:
    json.dump(guerras_westeros, f, ensure_ascii=False, indent=4)

print("guerras.json forjado com sucesso! As cinzas e o sangue foram registados.")