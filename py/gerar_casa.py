import json

casas_westeros = [
    {
        "id": "stark",
        "nome": "Casa Stark",
        "lema": "O Inverno Está Chegando",
        "sede": "Winterfell",
        "regiao": "O Norte",
        "brasao": "img/sigil_stark.jpg",
        "historia": "Os antigos Reis do Inverno. Descendentes diretos dos Primeiros Homens, a Casa Stark governou o vasto e gélido Norte de Westeros por milhares de anos antes da Conquista de Aegon. Eles são reverenciados por sua honra inabalável, justiça severa e uma profunda resiliência contra o frio implacável. Diferente de outras casas que buscam poder pelo poder, os Stark são os guardiões do reino contra as verdadeiras ameaças que espreitam Além da Muralha.",
        "personagens_memoraveis": "Eddard (Ned) Stark, Robb Stark, Arya Stark, Jon Snow."
    },
    {
        "id": "targaryen",
        "nome": "Casa Targaryen",
        "lema": "Fogo e Sangue",
        "sede": "Pedra do Dragão / Porto Real",
        "regiao": "Terras da Coroa",
        "brasao": "img/sigil_targaryen.jpg",
        "historia": "Os senhores dos dragões que sobreviveram à Perdição de Valíria. Sob o comando de Aegon, o Conquistador, e suas irmãs-esposas, eles unificaram os Sete Reinos usando o terror e a majestade de seus dragões. Possuem uma afinidade lendária com fogo e magia, além de costumes de linhagem pura que frequentemente os levam à linha tênue entre a grandeza absoluta e a loucura incontrolável.",
        "personagens_memoraveis": "Aegon o Conquistador, Daenerys Targaryen, Aemon o Cavaleiro do Dragão."
    },
    {
        "id": "lannister",
        "nome": "Casa Lannister",
        "lema": "Ouça-me Rugir!",
        "sede": "Rochedo Casterly",
        "regiao": "Terras Ocidentais",
        "brasao": "img/sigil_lannister.jpg",
        "historia": "Descendentes de Lann, o Esperto, os Lannister formam a casa mais rica e politicamente astuta de Westeros, construída sobre montanhas inesgotáveis de ouro. Embora seu lema oficial evoque o orgulho dos leões, a força da casa se apoia na fama de sua crueldade tática e no lema não oficial que ecoa por todo o reino: 'Um Lannister sempre paga suas dívidas', seja com ouro ou com sangue.",
        "personagens_memoraveis": "Tywin Lannister, Jaime Lannister, Tyrion Lannister, Cersei Lannister."
    },
    {
        "id": "baratheon",
        "nome": "Casa Baratheon",
        "lema": "Nossa é a Fúria",
        "sede": "Ponta Tempestade",
        "regiao": "Terras da Tempestade",
        "brasao": "img/sigil_baratheon.jpg",
        "historia": "A mais jovem das Grandes Casas, nascida durante a Conquista de Aegon através de Orys Baratheon. Eles ascenderam ao Trono de Ferro após a rebelião liderada por Robert Baratheon, que esmagou a dinastia Targaryen. São conhecidos por sua força bruta formidável, temperamento explosivo e uma determinação teimosa que se assemelha às violentas tempestades que castigam sua fortaleza.",
        "personagens_memoraveis": "Robert Baratheon, Stannis Baratheon, Renly Baratheon."
    },
    {
        "id": "greyjoy",
        "nome": "Casa Greyjoy",
        "lema": "Nós Não Semeamos",
        "sede": "Pyke",
        "regiao": "Ilhas de Ferro",
        "brasao": "img/sigil_greyjoy.jpg",
        "historia": "Mestres do mar e senhores das Ilhas de Ferro. Os Greyjoy seguem a implacável 'Antiga Doutrina' e adoram o Deus Afogado. Rejeitando a agricultura e o comércio pacífico, eles acreditam que o verdadeiro valor de um homem é medido por sua capacidade de tomar o que deseja através do 'preço de ferro', promovendo pilhagens e saques implacáveis pelas costas de Westeros.",
        "personagens_memoraveis": "Balon Greyjoy, Euron Olho-de-Corvo, Theon Greyjoy, Asha (Yara) Greyjoy."
    },
    {
        "id": "tyrell",
        "nome": "Casa Tyrell",
        "lema": "Crescendo Fortes",
        "sede": "Jardim de Cima",
        "regiao": "A Campina",
        "brasao": "img/sigil_tyrell.jpg",
        "historia": "Os Protetores do Sul controlam as terras mais férteis e populosas do continente, permitindo-lhes reunir o maior exército de Westeros. Originalmente meros intendentes da Casa Gardener, os Tyrell ascenderam ao poder por sua capacidade de adaptação. Sob uma fachada de rosas floridas, beleza estonteante e cavalheirismo cortesão, escondem uma ambição política implacável e altamente estratégica.",
        "personagens_memoraveis": "Olenna Tyrell (Rainha dos Espinhos), Margaery Tyrell, Loras Tyrell."
    },
    {
        "id": "martell",
        "nome": "Casa Martell",
        "lema": "Insubmissos, Não Curvados, Não Quebrados",
        "sede": "Lançassolar",
        "regiao": "Dorne",
        "brasao": "img/sigil_martell.jpg",
        "historia": "Os príncipes governantes do deserto de Dorne. Fortemente influenciados pela imigração dos Roinares, os Martell foram os únicos em toda Westeros a resistir aos dragões de Aegon com sucesso, juntando-se aos Sete Reinos séculos depois apenas através de tratados de casamento. Possuem costumes igualitários únicos, onde o filho mais velho herda, independentemente de ser homem ou mulher.",
        "personagens_memoraveis": "Doran Martell, Oberyn Martell (A Víbora Vermelha), Elia Martell."
    },
    {
        "id": "tully",
        "nome": "Casa Tully",
        "lema": "Família, Dever, Honra",
        "sede": "Correrrio",
        "regiao": "As Terras Fluviais",
        "brasao": "img/sigil_tully.jpg",
        "historia": "Senhores Supremos das Terras Fluviais, uma região estrategicamente vital, mas amaldiçoada por sua geografia plana e central, tornando-a o campo de batalha de todas as grandes guerras. Os Tully nunca foram reis, mas mantêm seu poder através de fortes alianças matrimoniais, diplomacia cuidadosa e uma dedicação inquestionável à honra e aos juramentos familiares.",
        "personagens_memoraveis": "Hoster Tully, Catelyn Stark (nascida Tully), Brynden Tully (O Peixe Negro)."
    },
    {
        "id": "arryn",
        "nome": "Casa Arryn",
        "lema": "Tão Alto Como a Honra",
        "sede": "Ninho da Águia",
        "regiao": "O Vale",
        "brasao": "img/brasao_arryn.jpg",
        "historia": "Considerada a mais antiga e pura linhagem da nobreza Ândala. Os Arryn governam suas terras a partir de uma fortaleza nas nuvens, considerada totalmente inexpugnável por meios convencionais. Devido à proteção natural das Montanhas da Lua, o Vale frequentemente adota uma postura isolacionista, observando os conflitos dos Sete Reinos de cima antes de decidir quando — e se — intervir.",
        "personagens_memoraveis": "Jon Arryn, Lysa Arryn, Robin Arryn."
    },
    {
        "id": "bolton",
        "nome": "Casa Bolton",
        "lema": "Nossas Lâminas São Afiadas",
        "sede": "Forte do Pavor",
        "regiao": "O Norte",
        "brasao": "img/brasao_bolton.jpg",
        "historia": "Antigos Reis Vermelhos e os maiores rivais históricos da Casa Stark. Por séculos, os Bolton aterrorizaram o Norte com sua macabra tradição de esfolar seus inimigos vivos, usando as peles como troféus. Frios, calculistas e implacáveis, eles são mestres na tortura física e psicológica, sempre à espreita de uma oportunidade para usurpar o domínio do Norte.",
        "personagens_memoraveis": "Roose Bolton, Ramsay Bolton."
    },
    {
        "id": "mormont",
        "nome": "Casa Mormont",
        "lema": "Aqui Permanecemos",
        "sede": "Ilha dos Ursos",
        "regiao": "O Norte",
        "brasao": "img/brasao_mormont.jpg",
        "historia": "Uma casa orgulhosa e feroz governando uma ilha isolada e pobre no gelado Mar Poente. Devido à constante ameaça de invasores Nascidos do Ferro e Selvagens, tanto os homens quanto as mulheres Mormont são treinados como guerreiros mortais desde a infância. São vassalos de lealdade fanática aos Stark e guerreiros lendários nos campos de batalha.",
        "personagens_memoraveis": "Jeor Mormont (O Velho Urso), Jorah Mormont, Lyanna Mormont."
    },
    {
        "id": "hightower",
        "nome": "Casa Hightower",
        "lema": "Nós Iluminamos o Caminho",
        "sede": "Torralta",
        "regiao": "A Campina",
        "brasao": "img/brasao_hightower.jpg",
        "historia": "Uma das casas mais antigas, ricas e orgulhosas de Westeros. Senhores de Vilavelha, o principal centro acadêmico e religioso do continente. Eles preferem o comércio, o conhecimento e o patronato (tanto da Fé dos Sete quanto dos meistres da Cidadela) em vez da guerra, mas são capazes de convocar espadas suficientes para rivalizar com as Grandes Casas quando provocados.",
        "personagens_memoraveis": "Otto Hightower, Alicent Hightower, Leyton Hightower."
    },
    {
        "id": "velaryon",
        "nome": "Casa Velaryon",
        "lema": "Os Antigos, os Verdadeiros, os Bravos",
        "sede": "Derivamarca",
        "regiao": "Terras da Coroa",
        "brasao": "img/brasao_velaryon.jpg",
        "historia": "Com raízes na Antiga Valíria, os Velaryon chegaram a Westeros antes mesmo dos Targaryen. Embora não sejam montadores de dragões natos, eles dominam as marés com a maior frota naval do mundo. Historicamente, são os aliados e consortes mais frequentes da Casa Targaryen, controlando o poderio marítimo do reino e trazendo riquezas incalculáveis de Essos.",
        "personagens_memoraveis": "Corlys Velaryon (A Serpente Marinha), Laenor Velaryon, Addam de Casco."
    },
    {
        "id": "frey",
        "nome": "Casa Frey",
        "lema": "Nós Permanecemos Juntos",
        "sede": "As Gêmeas",
        "regiao": "As Terras Fluviais",
        "brasao": "img/brasao_frey.jpg",
        "historia": "Uma casa 'nova' que rapidamente enriqueceu extorquindo pedágios daqueles que precisavam cruzar o Ramo Verde através de sua ponte fortificada. Famosos por sua enorme fertilidade e falta de modos nobres, os Frey são desprezados pelas casas mais antigas. Eles reescreveram a história de Westeros ao quebrar o antigo e sagrado direito de hospitalidade no infame Casamento Vermelho.",
        "personagens_memoraveis": "Walder Frey, Lothar Frey (O Coxo), Walder Negro."
    },
    {
        "id": "redwyne",
        "nome": "Casa Redwyne",
        "lema": "Amadurecidos para a Vitória",
        "sede": "A Árvore",
        "regiao": "A Campina",
        "brasao": "img/brasao_redwyne.jpg",
        "historia": "Senhores da próspera ilha da Árvore, localizada ao sul do continente. Os Redwyne dominam o mercado com a produção do melhor e mais caro vinho doce de Westeros. Mais do que meros comerciantes, eles possuem uma armada gigantesca e formidável, essencial para proteger a costa oeste do reino contra os saques constantes das lulas gigantes das Ilhas de Ferro.",
        "personagens_memoraveis": "Paxter Redwyne, Olenna Tyrell (nascida Redwyne)."
    },
    {
        "id": "dayne",
        "nome": "Casa Dayne",
        "lema": "A Espada da Manhã",
        "sede": "Tombastela",
        "regiao": "Dorne",
        "brasao": "img/brasao_dayne.jpg",
        "historia": "Uma das casas mais antigas e místicas de Westeros. Seu castelo, Tombastela, foi erguido no local exato onde um meteorito mágico caiu na terra. Daquele metal estelar, forjaram a lendária espada Alvorada. Diferente do aço valiriano escuro, ela é pálida como vidro leitoso. O título de 'Espada da Manhã' só é concedido a um cavaleiro Dayne considerado verdadeiramente digno de empunhá-la.",
        "personagens_memoraveis": "Arthur Dayne (A Espada da Manhã), Ashara Dayne, Gerold Dayne (Estrela Negra)."
    },
    {
        "id": "tarly",
        "nome": "Casa Tarly",
        "lema": "Primeiros em Batalha",
        "sede": "Monte Chifre",
        "regiao": "A Campina",
        "brasao": "img/brasao_tarly.jpg",
        "historia": "A principal força militar da Campina e uma das casas guerreiras mais respeitadas dos Sete Reinos. Possuem terras férteis na fronteira e empunham a lendária espada de montante de aço valiriano chamada Veneno do Coração. Suas tradições são extremamente marciais e severas, formando comandantes brilhantes nas artes da guerra.",
        "personagens_memoraveis": "Randyll Tarly, Samwell Tarly, Dickon Tarly."
    },
    {
        "id": "blackwood",
        "nome": "Casa Blackwood",
        "lema": "Sangue Antigo, Deuses Antigos",
        "sede": "Solar de Corvarbor",
        "regiao": "As Terras Fluviais",
        "brasao": "img/brasao_blackwood.jpg",
        "historia": "Uma casa ancestral com raízes que remontam diretamente aos Primeiros Homens. Curiosamente, é uma das únicas casas ao sul do Gargalo que ainda cultua os Deuses Antigos. O pátio de seu castelo abriga uma colossal e morta árvore represeiro, que atrai milhares de corvos ao entardecer. São ferozmente leais e mantêm uma rivalidade milenar e sangrenta com a vizinha Casa Bracken.",
        "personagens_memoraveis": "Brynden Rivers (Corvo de Três Olhos), Tytos Blackwood, Alysanne Blackwood."
    },
    {
        "id": "manderly",
        "nome": "Casa Manderly",
        "lema": "A Promessa foi Feita",
        "sede": "Porto Branco",
        "regiao": "O Norte",
        "brasao": "img/brasao_manderly.jpg",
        "historia": "Originais da Campina, foram exilados há mais de mil anos e acolhidos pela Casa Stark. Em profunda gratidão, juraram lealdade inabalável a Winterfell. Hoje, são a casa mais rica e comercial do Norte, controlando a única grande cidade da região: Porto Branco. É a única família nortenha de destaque a seguir a Fé dos Sete e manter as tradições cavaleirescas andalas do sul.",
        "personagens_memoraveis": "Wyman Manderly, Wylla Manderly, Wendel Manderly."
    },
    {
        "id": "blackfyre",
        "nome": "Casa Blackfyre",
        "lema": "Sangue e Fogo",
        "sede": "Exilados (Companhia Dourada)",
        "regiao": "Essos",
        "brasao": "img/brasao_blackfyre.jpg",
        "historia": "Uma ramificação bastarda da Casa Targaryen, fundada pelo lendário guerreiro Daemon Blackfyre após receber a espada de aço valiriano do próprio Aegon, o Conquistador. O brasão inverte as cores de seus ancestrais: um dragão negro em fundo vermelho. A casa foi responsável por cinco sangrentas rebeliões na tentativa de usurpar o Trono de Ferro. Oficialmente, a linhagem masculina foi extinta nos Degraus, mas rumores sobre sobreviventes ainda sussurram no leste.",
        "personagens_memoraveis": "Daemon I Blackfyre, Aegor Rivers (Açomargo), Maelys o Monstruoso."
    },
    {
        "id": "reyne",
        "nome": "Casa Reyne",
        "lema": "Desconhecido (Imortalizada em 'As Chuvas de Castamere')",
        "sede": "Castamere (Ruínas)",
        "regiao": "Terras Ocidentais",
        "brasao": "img/brasao_reyne.jpg",
        "historia": "O outrora poderoso Leão Vermelho de Castamere. A Casa Reyne era a segunda família mais rica das Terras Ocidentais, rivalizando com os próprios Lannister. Sua soberba e rebelião resultaram em uma retaliação brutal liderada por um jovem Tywin Lannister, que exterminou toda a linhagem, inundou seu castelo subterrâneo e transformou a casa em uma canção de aviso para toda Westeros.",
        "personagens_memoraveis": "Roger Reyne (O Leão Vermelho), Reynard Reyne, Ellyn Reyne."
    }
]

# O "../" avisa o Python para voltar uma pasta e salvar na raiz do projeto!
with open('../casas.json', 'w', encoding='utf-8') as f:
    json.dump(casas_westeros, f, ensure_ascii=False, indent=4)

print("casas.json forjado com sucesso (21 Casas Lendárias) e salvo na raiz do projeto!")