# Storm Survival Farmland Compat

Independent Minecraft 1.20.1 datapack for Fabric. It adds the verified Regions Unexplored farmland blocks to the Let's Do Brewery farmland tag.

This project is not affiliated with or endorsed by the authors of Regions Unexplored, Farm & Charm, or Brewery.

## Compatibility

Adds:

- `regions_unexplored:peat_farmland`
- `regions_unexplored:silt_farmland`

to:

- `#farm_and_charm:farmland`

This makes Brewery hops compatible with those two Regions Unexplored farmland blocks. It is designed and tested against the exact versions below. Other Minecraft 1.20.1 releases may also work if the relevant block IDs and farmland tag behavior remain unchanged, but they are not guaranteed.

Tested with:

- Minecraft 1.20.1
- Regions Unexplored 0.5.6+1.20.1
- Farm & Charm 1.0.14
- Brewery 2.0.6

## Supported compatibility

- Brewery hops on `regions_unexplored:peat_farmland`.
- Brewery hops on `regions_unexplored:silt_farmland`.

The change extends `#farm_and_charm:farmland` with `replace: false`, preserving the third-party tag's existing values.

## Installation

Copy the contents of the release ZIP, or the `datapack/` directory contents, into the target world's `datapacks/` directory. Run `/reload` or restart the world/server, then verify with `/datapack list`.

## Limitations

Farm & Charm's ordinary crops and HerbalBrews crops use vanilla crop placement behavior and cannot be made universally compatible with arbitrary RU farmland by adding a tag. Vinery grapes use bush/vine/pot support logic rather than farmland. The Farm & Charm tomato family has custom rope/body/head logic and needs separate runtime verification before any broader change.

This pack does not change growth speed, seasons, hydration, moisture, recipes, world generation, or third-party JARs.

## Versioning

Releases use `vMAJOR.MINOR.PATCH+mcM.M.P` tags. The current release is `v0.1.0+mc1.20.1`.

## License

Project-owned datapack JSON, scripts, and documentation are licensed under the MIT License. See [LICENSE](LICENSE).
