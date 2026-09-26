# Final audit — Phase A

Exact RU farmland IDs:

- `regions_unexplored:peat_farmland` — `PeatFarmBlock`
- `regions_unexplored:silt_farmland` — `SiltFarmBlock`

Datapack-fixable crop families:

- Brewery hops, through the installed `#farm_and_charm:farmland` tag.

Not datapack-fixable:

- Farm & Charm ordinary crops and HerbalBrews crops use vanilla block-specific crop placement.
- Vinery grapes are bush/vine/pot crops, not farmland crops.
- Farm & Charm tomato is custom rope/body/head logic and is not included without a dedicated runtime test.

Tag files created:

- `data/farm_and_charm/tags/blocks/farmland.json` (`replace: false`)

Validation: PASS

Minecraft manual test: PASS

Release ZIP: `releases/storm-survival-farmland-compat-0.1.0+mc1.20.1.zip`

SHA-256: `0fee6f3d026e61fbfd45dbf5f4265bc71f2108e63edd23d5fe170f94cfb9399f`

Java mod required for remaining compatibility: YES
