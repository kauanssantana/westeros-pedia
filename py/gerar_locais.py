import json

locais_westeros = [
    {
        "id": "castle-black",
        "nome": "Castelo Negro",
        "regiao": "A Muralha",
        "casa": "Patrulha da Noite",
        "top": "8.5%",   
        "left": "52.5%", 
        "descricao": "Castle Black é uma fortaleza antiga e isolada localizada aos pés da Muralha, no extremo norte de Westeros, servindo como base principal da Patrulha da Noite, uma ordem formada por guerreiros, criminosos perdoados e exilados que dedicam suas vidas a vigiar e proteger o reino contra ameaças vindas das terras selvagens e geladas além da Muralha, sendo um lugar marcado pelo frio extremo, disciplina rígida, vida difícil e constante sensação de perigo iminente.",
        "imagem": "img/castle_black.jpg"
    },
    {
        "id": "winterfell",
        "nome": "Winterfell",
        "regiao": "O Norte",
        "casa": "Casa Stark",
        "top": "22%",
        "left": "43.5%",
        "descricao": "Winterfell é uma antiga e imponente fortaleza localizada no Norte de Westeros, sede da Casa Stark, conhecida por sua arquitetura robusta, muralhas altas e pátios amplos aquecidos por fontes termais naturais que permitem suportar os invernos rigorosos da região, funcionando não apenas como castelo, mas como o centro político, militar e cultural do Norte, simbolizando tradição, honra e resistência diante das constantes ameaças e do clima implacável.",
        "imagem": "img/winterfell.jpg"
    },
    {
        "id": "the-twins",
        "nome": "As Gêmeas",
        "regiao": "As Terras Fluviais",
        "casa": "Casa Frey",
        "top": "44.5%",
        "left": "42.5%",
        "descricao": "As Gêmeas são duas fortalezas idênticas localizadas em lados opostos do Rio Verde, conectadas por uma ponte estratégica e controladas pela Casa Frey, servindo como um dos pontos de travessia mais importantes do Norte, onde viajantes e exércitos precisam pedir permissão para cruzar, tornando o local politicamente valioso, conhecido por sua posição estratégica, arquitetura funcional e atmosfera tensa marcada por alianças frágeis e interesses próprios.",
        "imagem": "img/twins.jpg"
    },
    {
        "id": "the-eyrie",
        "nome": "Ninho da Águia",
        "regiao": "O Vale",
        "casa": "Casa Arryn",
        "top": "48.4%",   # Subiu (estava 52%). Deve voltar para o topo da montanha.
        "left": "59.5%", 
        "descricao": "Ninho da Águia é uma fortaleza construída no topo de uma montanha nas Montanhas da Lua, sede da Casa Arryn, conhecida por seu acesso extremamente difícil, alcançado apenas por trilhas estreitas e perigosas, tornando-a uma das fortalezas mais seguras do continente, com torres brancas elegantes, salões altos e uma vista vertiginosa que transmite isolamento, poder e quase invulnerabilidade contra invasores.",
        "imagem": "img/eyrie.jpg"
    },
    {
        "id": "pyke",
        "nome": "Pyke",
        "regiao": "Ilhas de Ferro",
        "casa": "Casa Greyjoy",
        "top": "48.5%",
        "left": "25.5%",
        "descricao": "Pyke é uma fortaleza construída sobre formações rochosas nas Ilhas de Ferro, sede da Casa Greyjoy, composta por torres separadas erguidas em pilares de pedra ligados por pontes estreitas sobre um mar violento, marcada por ventos fortes, clima hostil e arquitetura áspera, refletindo a cultura dura e guerreira dos habitantes das ilhas, que valorizam força, conquistas e a vida no mar.",
        "imagem": "img/pyke.jpg"
    },
    {
        "id": "harrenhal",
        "nome": "Harrenhal",
        "regiao": "As Terras Fluviais",
        "casa": "Desconhecida (Amaldiçoada)",
        "top": "53.5%",
        "left": "46.5%",
        "descricao": "Harrenhal é o maior castelo de Westeros, localizado próximo ao Olho de Deus, conhecido por suas enormes muralhas, torres gigantescas e aparência parcialmente destruída após ser queimado durante a Conquista de Aegon, tornando-se um lugar sombrio, difícil de manter e cercado por histórias de maldição, onde diversas casas tentaram governar sem sucesso, criando a reputação de uma fortaleza grandiosa, porém decadente e assombrada.",
        "imagem": "img/harrenhal.jpg"
    },
    {
        "id": "dragonstone",
        "nome": "Pedra do Dragão",
        "regiao": "Terras da Coroa",
        "casa": "Casa Targaryen",
        "top": "57.5%",  
        "left": "68%", 
        "descricao": "Dragonstone é uma fortaleza construída em uma ilha vulcânica no mar estreito, antiga sede da Casa Targaryen, conhecida por sua arquitetura sombria com torres em forma de dragões, muralhas esculpidas em pedra negra e posição estratégica próxima à capital, sendo um castelo austero e imponente, cercado por mares agitados e falésias íngremes, simbolizando poder, conquista e a antiga presença dos senhores dos dragões.",
        "imagem": "img/dragonstone.jpg"
    },
    {
        "id": "kings-landing",
        "nome": "Porto Real",
        "regiao": "Terras da Coroa",
        "casa": "O Trono de Ferro",
        "top": "60.5%",  
        "left": "59.5%", 
        "descricao": "Porto real é a capital de Westeros, localizada na costa da Baía da Água Negra, sendo a maior e mais populosa cidade do reino, onde ficam a Fortaleza Vermelha, sede do poder político, e o Trono de Ferro, marcada por grande desigualdade social, ruas movimentadas, intrigas políticas constantes e uma mistura de riqueza, corrupção e perigo, funcionando como o principal centro de poder, comércio e disputas pelo controle do reino.",
        "imagem": "img/porto_real.jpg"
    },
    {
        "id": "pentos",
        "nome": "Pentos",
        "regiao": "Essos",
        "casa": "Magísteres",
        "top": "60.5%",  
        "left": "83.5%", 
        "descricao": "Pentos é uma das Cidades Livres localizada no continente de Essos, conhecida por seus palácios luxuosos, muralhas fortes e grande atividade comercial, governada por príncipes mercadores e magísteres ricos que controlam a política e o comércio, sendo uma cidade próspera e elegante, marcada por riqueza, intrigas políticas e forte dependência de acordos comerciais e alianças para manter sua segurança e influência.",
        "imagem": "img/pentos.jpg"
    },
    {
        "id": "dorne",
        "nome": "Lançassolar (Dorne)",
        "regiao": "Dorne",
        "casa": "Casa Martell",
        "top": "82%",  
        "left": "50%", 
        "descricao": "Dorne é a região mais ao sul de Westeros, governada pela Casa Martell, conhecida por seu clima quente e desértico, cidades construídas em meio a montanhas e oásis, cultura distinta e mais liberal que o restante do continente, além de uma forte tradição de independência, guerreiros habilidosos e uma política marcada por orgulho, paciência e vingança.",
        "imagem": "img/dorne.jpg"
    },

{
        "id": "casterly-rock",
        "nome": "Rochedo Casterly",
        "regiao": "Terras Ocidentais",
        "casa": "Casa Lannister",
        "top": "58.46%",  
        "left": "25.5%", 
        "descricao": "Casterly Rock é uma imensa fortaleza construída dentro de uma montanha rochosa na costa oeste de Westeros, sede da Casa Lannister, conhecida por suas ricas minas de ouro, defesas naturais quase impenetráveis e estrutura gigantesca esculpida na própria rocha, sendo um símbolo de riqueza, poder e influência política, além de uma das fortalezas mais difíceis de conquistar do continente.",
        "imagem": "img/casterly_rock.jpg"
    }

]

with open('locais.json', 'w', encoding='utf-8') as f:
    json.dump(locais_westeros, f, ensure_ascii=False, indent=4)

print("Ajuste final: Subimos os pinos fujões!")