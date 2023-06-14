fetch('http://127.0.0.1:8000/api/teams/')
  .then(response => response.json())
  .then(data => {
    const teamsContainer = document.getElementById('teams-container');
    data.forEach(teams => {
      const card = document.createElement('div');
      card.classList.add('card');
      card.classList.add('my-custom-card');
      card.classList.add('random-class-1');
      card.classList.add('random-class-2');

      // Agregar estilo en línea con la imagen del logo como fondo
      card.style.backgroundImage = `url(${teams.logo})`;
      card.style.backgroundSize = 'cover';
      card.style.backgroundPosition = 'center';

      const cardBody = document.createElement('div');
      cardBody.classList.add('card-body');

      const cardTitle = document.createElement('h5');
      cardTitle.classList.add('card-title');
      cardTitle.innerText = teams.nameTeam;

      const cardContent = document.createElement('p');
      cardContent.classList.add('card-text');
      cardContent.innerText = `Ranking: ${teams.ranking}`;

      cardBody.appendChild(cardTitle);
      cardBody.appendChild(cardContent);
      card.appendChild(cardBody);

      teamsContainer.appendChild(card);
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