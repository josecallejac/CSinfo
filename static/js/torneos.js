document.addEventListener("DOMContentLoaded", function() {
  const torneosCards = document.getElementById("torneosCards");

  fetch("http://127.0.0.1:8000/api/torneo/")
    .then(response => response.json())
    .then(data => {
      data.forEach(torneos => {
        const card = document.createElement("div");
        card.className = "col-lg-4 col-md-6 mb-4";
        card.innerHTML = `
          <div class="card">
            <img src="${torneos.imgTorneo}" class="card-img-top" alt="Torneo">
            <div class="card-body">
              <h5 class="card-title">${torneos.nombreTorneo}</h5>
              
              <p class="card-text">Ubicación: ${torneos.locacionTorneo}</p>
              <p class="card-text">Premio: ${torneos.premio}</p>
              <p class="card-text">Equipos Participantes: ${torneos.teamsParticipando}</p>
              
              
<!-- Modal toggle -->
<button data-modal-target="defaultModal" data-modal-toggle="defaultModal" class=" btn btn-primary btn-lg btn-block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
  Detalles del torneo
</button>

<!-- Main modal -->
<div id="defaultModal" tabindex="-1" aria-hidden="true" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative w-full max-w-2xl max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <!-- Modal header -->
            <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
                <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                ${torneos.nombreTorneo}
                </h3>
                
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="defaultModal">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="p-6 space-y-6">
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                
                <p class="card-text">Desde: ${torneos.fechaInicio}</p>
                <p class="card-text">Hasta: ${torneos.fechaTermino}</p>
                <p class="card-text">Top player: ${torneos.topPlayer}</p>
                </p>
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    AQUI TAMBIEN
                </p>
            </div>
            <!-- Modal footer -->
            <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                <button data-modal-hide="defaultModal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 btn btn-primary btn-lg btn-block">Cerrar detalles</button>
                
            </div>
        </div>
    </div>
</div>

            </div>
          </div>
        `;
        torneosCards.appendChild(card);
      });
    })
    .catch(error => {
      console.log("Error:", error);
    });
});