document.addEventListener("DOMContentLoaded", function() {
  const marketItems = document.getElementById("marketItems");

  fetch("http://127.0.0.1:8000/api/market/")
    .then(response => response.json())
    .then(data => {
      data.forEach(item => {
        const card = document.createElement("div");
        card.className = "col-lg-4 col-md-6 mb-4";
        card.innerHTML = `
          <div class="card">
            <img src="${item.image}" class="card-img-top" alt="Artículo">
            <div class="card-body">
              <h5 class="card-title">${item.nameSkin}</h5>
              <p class="card-text">Precio: ${item.price}</p>
              <p class="card-text">Vendedor: ${item.seller}</p>
              <p class="card-text">Condición: ${item.condition}</p>
              <p class="card-text">Descripción: ${item.description}</p>
            </div>
          </div>
        `;
        marketItems.appendChild(card);
      });
    })
    .catch(error => {
      console.log("Error:", error);
    });
});