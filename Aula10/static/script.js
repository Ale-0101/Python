function adicionarAtaque() {
    let listaAtaques = document.getElementById("lista-ataques");
    let index = listaAtaques.querySelectorAll("li").length; // Conta os ataques existentes

    let ataqueContainer = document.createElement("li");

    ataqueContainer.innerHTML = `
        <label><strong>Arma:</strong></label>
        <input type="text" name="ataques[\${index}][arma]" required><br>

        <label><strong>Bônus:</strong></label>
        <input type="number" name="ataques[\${index}][bonos]" required><br>

        <label><strong>Dado:</strong></label>
        <input type="number" name="ataques[\${index}][dado]" required><br>

        <button type="button" onclick="removerAtaque(this)">Remover</button>
    `;

    listaAtaques.appendChild(ataqueContainer);
}

function removerAtaque(botao) {
    botao.parentElement.remove();
}