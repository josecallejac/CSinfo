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

      const additionalInfo = document.createElement('p');
      additionalInfo.classList.add('card-text');
      additionalInfo.innerText = `Otra información: ${teams.otraInformacion}`;

      cardBody.appendChild(cardTitle);
      cardBody.appendChild(cardContent);
      cardBody.appendChild(additionalInfo);
      card.appendChild(cardBody);

      teamsContainer.appendChild(card);
    });
  })
  .catch(error => console.log(error));

  