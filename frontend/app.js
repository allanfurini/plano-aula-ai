document.getElementById("formPlano").addEventListener("submit", async function(event) {
    event.preventDefault();

    let plano = {
        escola: document.getElementById("escola").value,
        professor: document.getElementById("professor").value,
        serie: document.getElementById("serie").value,
        disciplina: document.getElementById("disciplina").value,
        objetivos: document.getElementById("objetivos").value,
        recursos: document.getElementById("recursos").value,
        metodologia: document.getElementById("metodologia").value,
        atividades: document.getElementById("atividades").value,
        avaliacao: document.getElementById("avaliacao").value,
        competencias: document.getElementById("competencias").value.split(","),
        data: new Date().toLocaleDateString()
    };

    let response = await fetch("https://plano-aula-ai.onrender.com/gerar_plano", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(plano)
    });

    if (response.ok) {
        let blob = await response.blob();
        let link = document.createElement("a");
        link.href = window.URL.createObjectURL(blob);
        link.download = "plano_aula.pdf";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        document.getElementById("resultado").innerText = "Plano de aula gerado e baixado com sucesso!";
    } else {
        document.getElementById("resultado").innerText = "Erro ao gerar o plano de aula.";
    }
});
