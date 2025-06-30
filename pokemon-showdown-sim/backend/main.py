from fastapi import FastAPI, Form, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"
POKEAPI_TYPE_URL = "https://pokeapi.co/api/v2/type"

@app.get("/types")
async def get_types():
    async with httpx.AsyncClient() as client:
        res = await client.get(POKEAPI_TYPE_URL)
        data = res.json()
        types = [t["name"] for t in data["results"]]
        return {"types": types}

@app.get("/get-pokemons")
async def get_pokemons(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    name: str = Query("", alias="name"),
    type_: str = Query("", alias="type_")
):
    offset = (page - 1) * limit

    async with httpx.AsyncClient() as client:
        pokemons = []

        if type_:
            # Consulta por tipo
            res = await client.get(f"{POKEAPI_TYPE_URL}/{type_.lower()}")
            if res.status_code != 200:
                return {"total": 0, "pokemons": []}
            data = res.json()
            all_pokemons = [p["pokemon"] for p in data.get("pokemon", [])]
        else:
            # Consulta general
            res = await client.get(f"{POKEAPI_URL}?limit=1000")
            data = res.json()
            all_pokemons = data.get("results", [])

        # Filtrado por nombre si aplica
        if name:
            all_pokemons = [p for p in all_pokemons if name.lower() in p["name"]]

        total = len(all_pokemons)
        paginated = all_pokemons[offset:offset + limit]

        for p in paginated:
            poke_res = await client.get(p["url"])
            poke_data = poke_res.json()
            pokemons.append({
                "name": poke_data["name"].capitalize(),
                "image": poke_data["sprites"]["front_default"],
                "id": poke_data["id"],
                "types": [t["type"]["name"] for t in poke_data["types"]]
            })

        return {"total": total, "pokemons": pokemons}

# Estado de batalla temporal
battle_state = {
    "pokemon1": None,
    "pokemon2": None,
    "hp1": 0,
    "hp2": 0,
    "turn": 1,
}

@app.post("/start-battle")
async def start_battle(pokemon1: str = Form(...), pokemon2: str = Form(...)):
    async with httpx.AsyncClient() as client:
        res1 = await client.get(f"{POKEAPI_URL}/{pokemon1.lower()}")
        res2 = await client.get(f"{POKEAPI_URL}/{pokemon2.lower()}")
        poke1 = res1.json()
        poke2 = res2.json()

        battle_state["pokemon1"] = {
            "name": poke1["name"].capitalize(),
            "hp": poke1["stats"][0]["base_stat"],
            "attack": poke1["stats"][1]["base_stat"],
            "defense": poke1["stats"][2]["base_stat"],
            "image": poke1["sprites"]["front_default"]
        }
        battle_state["pokemon2"] = {
            "name": poke2["name"].capitalize(),
            "hp": poke2["stats"][0]["base_stat"],
            "attack": poke2["stats"][1]["base_stat"],
            "defense": poke2["stats"][2]["base_stat"],
            "image": poke2["sprites"]["front_default"]
        }
        battle_state["hp1"] = battle_state["pokemon1"]["hp"]
        battle_state["hp2"] = battle_state["pokemon2"]["hp"]
        battle_state["turn"] = 1

        return {"message": "Batalla iniciada", "battle_state": battle_state}
