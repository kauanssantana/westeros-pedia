import json

religioes_westeros = [
    {
        "id": "deuses-antigos",
        "nome": "Os Deuses Antigos",
        "deidade": "Inúmeros espíritos da terra, pedra e árvore",
        "clerigos": "Nenhum (Videntes Verdes no passado)",
        "centro": "O Norte e Além da Muralha",
        "imagem": "img/rel_antigos.jpg",
        "lema": '"Os deuses não têm voz, exceto o farfalhar das folhas."',
        "descricao": "A fé mais antiga de Westeros, venerada pelos Primeiros Homens e pelas Crianças da Floresta. Não possuem templos de pedra, escrituras ou sacerdotes. A adoração ocorre ao ar livre, nos Bosques Sagrados, diante das majestosas árvores de represeiro. Acredita-se que os deuses observam o mundo através dos olhos chorosos de seiva vermelha esculpidos nos troncos brancos."
    },
    {
        "id": "fe-dos-sete",
        "nome": "A Fé dos Sete",
        "deidade": "Um Deus com Sete Faces",
        "clerigos": "Septões, Septãs e a Fé Militante",
        "centro": "O Sul de Westeros (Grande Septo de Baelor)",
        "imagem": "img/rel_sete.jpg",
        "lema": '"Sete deuses, sete infernos, sete reinos."',
        "descricao": "A religião dominante em Westeros, trazida pelos invasores Ândalos. Veneram uma única divindade com sete aspetos: O Pai, a Mãe, o Guerreiro, a Velha, o Ferreiro, a Donzela e o Estranho (a Morte). As suas orações são feitas em imensos Septos adornados com cristais e luz, regidos por regras morais rigorosas e cânticos de adoração."
    },
    {
        "id": "senhor-da-luz",
        "nome": "R'hllor, o Senhor da Luz",
        "deidade": "R'hllor (O Deus Vermelho)",
        "clerigos": "Sacerdotes e Sacerdotisas Vermelhas",
        "centro": "Essos (Asshai e Volantis)",
        "imagem": "img/rel_rhllor.jpg",
        "lema": '"A noite é escura e cheia de terrores."',
        "descricao": "Uma religião absolutista baseada na dualidade cósmica: R'hllor, o deus do fogo, da luz e da vida, trava uma guerra eterna contra o Grande Outro, deus do gelo, da escuridão e da morte. Os seus sacerdotes olham para as chamas em busca de visões do futuro e são conhecidos por praticar magias poderosas e sombrias, incluindo a ressurreição e a conjuração de sombras."
    },
    {
        "id": "deus-afogado",
        "nome": "O Deus Afogado",
        "deidade": "O Deus Afogado",
        "clerigos": "Homens Afogados (Sacerdotes da Água)",
        "centro": "Ilhas de Ferro",
        "imagem": "img/rel_afogado.jpg",
        "lema": '"O que está morto não pode morrer."',
        "descricao": "A dura religião dos Nascidos do Ferro. Acreditam que o seu deus vive nas profundezas do oceano e os criou para saquear, violar e dominar os fracos. O batismo é um ritual brutal onde a pessoa é afogada no mar e reanimada com massagens cardíacas primitivas. Segundo a sua crença, os bravos banqueteiam eternamente nos salões aquáticos do seu deus após a morte."
    },
    {
        "id": "muitas-faces",
        "nome": "O Deus de Muitas Faces",
        "deidade": "A Morte (A Dádiva)",
        "clerigos": "Os Homens Sem Rosto",
        "centro": "Casa de Preto e Branco (Braavos)",
        "imagem": "img/rel_faces.jpg",
        "lema": '"Valar Morghulis. Todos os homens devem morrer."',
        "descricao": "Nascida nas minas de escravos da antiga Valíria. Esta ordem não vê a morte como um fim cruel, mas como o fim do sofrimento — uma dádiva. Acreditam que todos os deuses das outras religiões são apenas diferentes faces do mesmo Deus da Morte. Os seus sacerdotes são os assassinos mais letais e caros do mundo, capazes de arrancar e vestir o rosto dos mortos."
    },
    {
        "id": "grande-garanhao",
        "nome": "O Grande Garanhão",
        "deidade": "A Montaria Divina",
        "clerigos": "Dosh Khaleen (Velhas Sábias)",
        "centro": "Mar Dothraki (Vaes Dothrak)",
        "imagem": "img/rel_garanhao.jpg",
        "lema": '"Um Khal que não sabe cavalgar não é um Khal."',
        "descricao": "A divindade venerada pelas hordas de guerreiros nómadas Dothraki. É o reflexo da sua cultura equestre, onde cavalgar é a essência da vida. Eles acreditam que o céu noturno é o grande rebanho cósmico e que as estrelas são cavalos de fogo. Uma antiga profecia prevê o nascimento do 'Garanhão Que Monta o Mundo', um conquistador que unirá todos os Khalasars."
    }
]

with open('../religioes.json', 'w', encoding='utf-8') as f:
    json.dump(religioes_westeros, f, ensure_ascii=False, indent=4)

print("religioes.json forjado com sucesso! Os Deuses foram aplacados.")