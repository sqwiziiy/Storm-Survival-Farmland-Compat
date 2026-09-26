# Phase A — Regions Unexplored farmland discovery

Target artifact: `RegionsUnexploredFabric-0.5.6+1.20.1.jar` from the Storm Survival 1.20.1 server.

## Verified inventory

| Registry ID | Class | Properties | Registration location | Existing block tags | Normal crop placement |
|---|---|---|---|---|---|
| `regions_unexplored:peat_farmland` | `io.github.uhq_games.regions_unexplored.world.level.block.forest_dirt.PeatFarmBlock` | `moisture=0..7`; farmland-shaped collision/visual state; reverts to `peat_dirt` when unsupported or dry | `io.github.uhq_games.regions_unexplored.block.RuBlocks` static initializer (`<clinit>`), registration string `peat_farmland`; implementation extends vanilla `FarmlandBlock` | `c:farmland`, `c:farmlands`, `regions_unexplored:crop_plantable_blocks` | Vanilla/Farm & Charm `CropBlock` rules do not accept arbitrary farmland blocks; tag-aware Brewery hops can accept it after the compatibility tag extension |
| `regions_unexplored:silt_farmland` | `io.github.uhq_games.regions_unexplored.world.level.block.plains_dirt.SiltFarmBlock` | `moisture=0..7`; custom support check; reverts to `silt_dirt` when unsupported or dry | `io.github.uhq_games.regions_unexplored.block.RuBlocks` static initializer (`<clinit>`), registration string `silt_farmland` | `c:farmland`, `c:farmlands`, `regions_unexplored:crop_plantable_blocks` | Vanilla/Farm & Charm `CropBlock` rules do not accept arbitrary farmland blocks; tag-aware Brewery hops can accept it after the compatibility tag extension |

No other RU block in the exact JAR was classified as genuinely tilled farmland. The two IDs above are also explicitly present in RU's bundled `c:farmland`, `c:farmlands`, and `regions_unexplored:crop_plantable_blocks` tags.

## Evidence notes

- `RuBlocks` declares `PEAT_FARMLAND` and `SILT_FARMLAND` and registers the exact IDs in its static initializer.
- `PeatFarmBlock` extends the vanilla farmland implementation.
- `SiltFarmBlock` is a custom block with farmland-like moisture and support behavior; its bundled RU crop-plantable tag is the authoritative indication that RU intends it as crop soil.
- No gameplay result is claimed here; the manual planting test remains pending.
