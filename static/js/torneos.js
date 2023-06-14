fetch('http://127.0.0.1:8000/api/torneo/')  // Ruta a tu endpoint de la API
  .then(response => response.json())
  .then(data => {
    const torneoContainer = document.getElementById('torneo-container');
    data.forEach(torneo => {
      const card = document.createElement('div');
      card.classList.add('card');
      card.classList.add('my-custom-card');

    /*   const cardImage = document.createElement('img');
      cardImage.classList.add('card-img-top');
      cardImage.src = news.image;  // URL de la imagen de la noticia */

      const cardBody = document.createElement('div');
      cardBody.classList.add('card-body');

      const cardTitle = document.createElement('h5');
      cardTitle.classList.add('card-title');
      cardTitle.innerText = torneo.nombreTorneo;
      

      const cardContent = document.createElement('p');
      cardContent.classList.add('card-text');
      cardContent.innerText = torneo.locacionTorneo;

      
      cardBody.appendChild(cardTitle);
      cardBody.appendChild(cardContent);
      card.appendChild(cardBody);
      
      torneoContainer.appendChild(card);
    });
  })
  .catch(error => console.log(error));


  /* <div class="card-header">Featured</div>
        <div class="card-body">
          <h5 class="card-title">Special title treatment</h5>
          <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          <a href="#" class="btn btn-primary">Button</a>
        </div>
        <div class="card-footer text-muted">2 days ago</div>
      </div> */