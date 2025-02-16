document.getElementById("formPlano").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    let plano = {
        escola: document.getElementById("escola").value,
        professor: document.getElementById("professor").value,
        serie: document.getElementById("serie").value,
        disciplina: document.getElementById("disciplina").value,
        objetivos: document.getElementById("objetivos").value,
        recursos: "Livros, Quadro, Giz",
        metodologia: "Aulas expositivas e interativas",
        atividades: "Exercícios e discussões",
        avaliacao: "Provas e trabalhos",
        competencias: ["Competência BNCC 1", "Competência BNCC 2"],
        data: new Date().toLocaleDateString()
    };

    let response = await fetch("https://plano-aula.onrender.com/gerar_plano", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(plano)
    });

    let data = await response.json();
    document.getElementById("resultado").innerText = "Plano gerado com sucesso! Baixe em: " + data.pdf;
});
