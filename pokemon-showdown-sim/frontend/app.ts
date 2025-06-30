document.addEventListener("DOMContentLoaded", () => {
  const API_URL = "http://127.0.0.1:8000";

  const pokemonList = document.getElementById("pokemon-list")!;
  const startBattleBtn = document.getElementById("start-battle-btn")!;
  const battleArea = document.getElementById("battle-area")!;
  const name1 = document.getElementById("name1")!;
  const name2 = document.getElementById("name2")!;
  const hp1 = document.getElementById("hp1")!;
  const hp2 = document.getElementById("hp2")!;
  const img1 = document.getElementById("img1") as HTMLImageElement;
  const img2 = document.getElementById("img2") as HTMLImageElement;

  const searchInput = document.getElementById("search-name") as HTMLInputElement;
  const typeSelect = document.getElementById("filter-type") as HTMLSelectElement;
  const paginationDiv = document.getElementById("pagination")!;

  const PAGE_SIZE = 20;
  let currentPage = 1;
  let totalPokemons = 0;

  let selectedPokemons: string[] = [];

  // Cargar lista de tipos
  async function loadTypes() {
    try {
      const res = await fetch(`${API_URL}/types`);
      const data = await res.json();
      const types: string[] = data.types;

      typeSelect.innerHTML = `<option value="">Filtrar por tipo</option>`;
      types.forEach(type => {
        const option = document.createElement("option");
        option.value = type;
        option.textContent = type.charAt(0).toUpperCase() + type.slice(1);
        typeSelect.appendChild(option);
      });
    } catch (e) {
      console.error("Error cargando tipos:", e);
    }
  }

  // Cargar pokémones paginados y filtrados
  async function loadPokemons(page = 1) {
    const nameFilter = searchInput.value.trim();
    const typeFilter = typeSelect.value;

    const params = new URLSearchParams();
    params.append("page", page.toString());
    params.append("limit", PAGE_SIZE.toString());
    if (nameFilter) params.append("name", nameFilter);
    if (typeFilter) params.append("type_", typeFilter);

    try {
      const res = await fetch(`${API_URL}/get-pokemons?${params.toString()}`);
      const data = await res.json();

      totalPokemons = data.total;
      renderPokemons(data.pokemons);
      renderPagination(page, Math.ceil(totalPokemons / PAGE_SIZE));
    } catch (e) {
      console.error("Error cargando pokemons:", e);
    }
  }

  // Mostrar lista de pokémones
  function renderPokemons(pokemons: any[]) {
    pokemonList.innerHTML = "";

    pokemons.forEach(pokemon => {
      const col = document.createElement("div");
      col.className = "col";
      col.innerHTML = `
        <div class="card h-100 text-center shadow-sm" style="cursor:pointer;" data-name="${pokemon.name}">
          <img src="${pokemon.image}" class="card-img-top mx-auto mt-2" style="width: 96px; height: 96px;">
          <div class="card-body p-2">
            <h6 class="card-title mb-0">${pokemon.name}</h6>
          </div>
        </div>
      `;
      pokemonList.appendChild(col);

      col.addEventListener("click", () => selectPokemon(pokemon.name));
    });
  }

  // Paginación
  function renderPagination(current: number, totalPages: number) {
    paginationDiv.innerHTML = "";

    function createBtn(label: string | number, page?: number, active = false) {
      const btn = document.createElement("button");
      btn.textContent = label.toString();
      btn.className = "btn btn-outline-primary m-1";
      if (active) btn.classList.add("active");
      if (page !== undefined) {
        btn.addEventListener("click", () => {
          currentPage = page;
          loadPokemons(currentPage);
        });
      }
      return btn;
    }

    if (current > 1) {
      paginationDiv.appendChild(createBtn("« Anterior", current - 1));
    }

    let startPage = Math.max(1, current - 2);
    let endPage = Math.min(totalPages, current + 2);

    for (let i = startPage; i <= endPage; i++) {
      paginationDiv.appendChild(createBtn(i, i, i === current));
    }

    if (current < totalPages) {
      paginationDiv.appendChild(createBtn("Siguiente »", current + 1));
    }
  }

  // Seleccionar pokémon
  function selectPokemon(name: string) {
    if (selectedPokemons.includes(name)) {
      alert(`${name} ya está seleccionado.`);
      return;
    }
    if (selectedPokemons.length < 2) {
      selectedPokemons.push(name);
      alert(`${name} seleccionado.`);

      if (selectedPokemons.length === 2) {
        startBattleBtn.removeAttribute("disabled");
      }
    } else {
      alert("Ya seleccionaste 2 Pokémon.");
    }
  }

  // Evento para iniciar batalla
  startBattleBtn.addEventListener("click", async () => {
    const formData = new URLSearchParams();
    formData.append("pokemon1", selectedPokemons[0]);
    formData.append("pokemon2", selectedPokemons[1]);

    try {
      const res = await fetch(`${API_URL}/start-battle`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData.toString(),
      });
      const data = await res.json();
      const battleState = data.battle_state;

      const modalName1 = document.getElementById("modal-name1")!;
      const modalName2 = document.getElementById("modal-name2")!;
      const modalHp1 = document.getElementById("modal-hpbar1")!;
      const modalHp2 = document.getElementById("modal-hpbar2")!;
      const modalImg1 = document.getElementById("modal-img1") as HTMLImageElement;
      const modalImg2 = document.getElementById("modal-img2") as HTMLImageElement;
      const modalStatus = document.getElementById("modal-status")!;

      modalStatus.textContent = "¡La batalla ha comenzado!";
      modalName1.textContent = battleState.pokemon1.name;
      modalName2.textContent = battleState.pokemon2.name;
      modalHp1.textContent = battleState.hp1;
      modalHp2.textContent = battleState.hp2;
      modalImg1.src = battleState.pokemon1.image;
      modalImg2.src = battleState.pokemon2.image;

      // Mostrar modal
      const battleModal = new bootstrap.Modal(document.getElementById("battleModal")!);
      battleModal.show();
      simulateBattle(battleState, battleModal);

    } catch (e) {
      alert("Error iniciando batalla.");
      console.error(e);
    }
  });

  async function simulateBattle(battleState: any, modal: any) {
    const hpBar1 = document.getElementById("modal-hpbar1") as HTMLElement;
    const hpBar2 = document.getElementById("modal-hpbar2") as HTMLElement;
    const modalStatus = document.getElementById("modal-status") as HTMLElement;

    let hp1 = battleState.hp1;
    let hp2 = battleState.hp2;
    const attack1 = battleState.pokemon1.attack;
    const attack2 = battleState.pokemon2.attack;
    const defense1 = battleState.pokemon1.defense;
    const defense2 = battleState.pokemon2.defense;

    const maxHp1 = hp1;
    const maxHp2 = hp2;

    let turn = 1;

    modalStatus.textContent = "¡La batalla ha comenzado!";

    while (hp1 > 0 && hp2 > 0) {
      await new Promise(resolve => setTimeout(resolve, 1000)); // 1 segundo entre turnos

      if (turn % 2 !== 0) {
        // Pokémon 1 ataca
        const damage = Math.max(1, attack1 - Math.floor(defense2 / 2));
        hp2 = Math.max(0, hp2 - damage);
        modalStatus.textContent = `${battleState.pokemon1.name} ataca y causa ${damage} de daño.`;
      } else {
        // Pokémon 2 ataca
        const damage = Math.max(1, attack2 - Math.floor(defense1 / 2));
        hp1 = Math.max(0, hp1 - damage);
        modalStatus.textContent = `${battleState.pokemon2.name} ataca y causa ${damage} de daño.`;
      }

      // Actualizar barras de vida
      const percentHp1 = (hp1 / maxHp1) * 100;
      const percentHp2 = (hp2 / maxHp2) * 100;
      hpBar1.style.width = `${percentHp1}%`;
      hpBar2.style.width = `${percentHp2}%`;
      hpBar1.textContent = `${hp1} HP`;
      hpBar2.textContent = `${hp2} HP`;

      // Cambiar color de barra según porcentaje
      hpBar1.classList.toggle('bg-danger', percentHp1 <= 30);
      hpBar2.classList.toggle('bg-danger', percentHp2 <= 30);

      turn++;
    }

    await new Promise(resolve => setTimeout(resolve, 1500));

    if (hp1 > 0) {
      modalStatus.textContent = `¡${battleState.pokemon1.name} ha ganado! 🎉`;
    } else {
      modalStatus.textContent = `¡${battleState.pokemon2.name} ha ganado! 🎉`;
    }
  }

  // Eventos para búsqueda y filtro
  searchInput.addEventListener("input", () => {
    currentPage = 1;
    loadPokemons(currentPage);
  });
  typeSelect.addEventListener("change", () => {
    currentPage = 1;
    loadPokemons(currentPage);
  });

  // Inicialización
  (async function init() {
    await loadTypes();
    await loadPokemons();
  })();
});
