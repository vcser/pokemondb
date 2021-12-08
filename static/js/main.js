var data;
// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var content = document.getElementsByClassName("modal-content")[0];

function get_info_pokemon() {
    fetch(window.origin + "/_info_pokemon", { method: "GET" }).then(
        function (response) {
            response.json().then((value) => {
                data = value.data;
                grid = document.getElementById("card-grid");
                data.forEach(element => {
                    add_card(grid, element);
                });
                // console.log(data);
            }
            )
        }
    );
}

function add_card(grid, pokemon) {
    const div = document.createElement("div");
    div.className = "card";
    div.id = pokemon.num_pokedex;
    div.innerHTML = `
        <span class="card-pokemon-id">#${pokemon.num_pokedex}</span>
        <div class="card-img-container">
            <img class="card-pokemon-img" src="/static/img/pokemon-card/${pokemon.num_pokedex}.png">
        </div>
        <h3 class="card-pokemon-name">${pokemon.nombre}</h3>
    `;
    div.addEventListener("click", () => {
        show_info(pokemon);
    })
    grid.appendChild(div);
}

function search_pokemon() {
    const input = document.getElementById("search");
    const filter = input.value.toUpperCase();
    const grid = document.getElementById("card-grid");
    const cards = grid.getElementsByClassName("card");
    for (let i = 0; i < cards.length; i++) {
        const number = cards[i].id;
        const name = cards[i].getElementsByClassName("card-pokemon-name")[0].innerHTML;
        if (name.toUpperCase().indexOf(filter) > -1 || number.indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

function show_info(pokemon) {
    console.log(pokemon);
    const img = content.getElementsByTagName("img")[0];
    const name = content.getElementsByClassName("name")[0];
    const description = content.getElementsByClassName("description")[0];
    const height = content.getElementsByClassName("height")[0];
    const weight = content.getElementsByClassName("weight")[0];
    const elemental = content.getElementsByClassName("elemental")[0];
    img.src = "/static/img/pokemon-card/" + pokemon.num_pokedex + ".png";
    name.innerHTML = "Nombre: " + pokemon.nombre;
    description.innerHTML = pokemon.descripcion;
    height.innerHTML = "Altura: " + pokemon.altura + " m";
    weight.innerHTML = "Peso: " + pokemon.peso + " kg";
    elemental.innerHTML = pokemon.tipo_elemental1 + ", " + pokemon.tipo_elemental2;
    modal.style.display = "block";
}

window.onload = get_info_pokemon;
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}
