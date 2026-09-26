# Phase B — crop placement discovery

Target artifacts are the exact installed Storm Survival 1.20.1 JARs.

## Findings

| Crop / family | Implementation and placement rule | Classification |
|---|---|---|
| Brewery hops (`brewery:hops_crop` family) | `net.satisfy.brewery.core.block.HopsCropBlock.mayPlaceOn(BlockState)` checks `state.is(TagRegistry.FARMLAND)`, where the installed Farm & Charm registry maps `FARMLAND` to `#farm_and_charm:farmland` | `TAG_BASED`; fixable |
| Farm & Charm barley, corn, lettuce, oat, onion, strawberry | `BarleyCropBlock`, `CornCropBlock`, `LettuceCropBlock`, `OatCropBlock`, `OnionCropBlock`, and `StrawberryCropBlock` extend vanilla `CropBlock`. The Farm & Charm mixin only adds `fertilized_farmland` as an extra accepted block; it does not replace vanilla farmland placement with the `farm_and_charm:farmland` tag | `VANILLA_FARMLAND_HARDCODED`; not fixable with a tag-only RU addition |
| Farm & Charm tomato | `TomatoCropBlock.mayPlaceOn(BlockState)` checks the Farm & Charm farmland tag, so this is tag-based in principle. However, the tomato family is a custom rope/body/head crop whose complete placement and growth behavior is not equivalent to a simple ordinary crop block; it is not included in this minimal tag change without an in-game test of the full family | `CUSTOM_BLOCK_CHECK`; document/test separately |
| Vinery grape bushes/vines and grapevine pots | `GrapeBush`, `GrapeVineBlock`, and `GrapevinePotBlock` use bush/vine/pot support logic, not farmland acceptance | `NOT_A_FARMLAND_CROP` |
| HerbalBrews coffee, rooibos, tea, yerba mate | `CoffeeCropBlock`, `RooibosCropBlock`, `TeaCropBlock`, and `YerbaMateCropBlock` extend vanilla `CropBlock` and do not expose a mod farmland tag in their crop classes | `VANILLA_FARMLAND_HARDCODED` |
| Brewery barley/oat/wheat/nettle/haley entries | These are Brewery crop/ingredient content entries, not additional installed farmland crop block families; the placeable farmland crop family found in the Brewery classes is hops | `NOT_A_FARMLAND_CROP` |

## Classification table

| Crop / family | Current accepted soil | RU farmland desired | Datapack-fixable? | Exact tag to extend | Reason |
|---|---|---|---|---|---|
| Brewery hops | `#farm_and_charm:farmland` | peat and silt farmland | `FIXABLE_WITH_TAG` | `#farm_and_charm:farmland` | Exact installed `HopsCropBlock.mayPlaceOn` reads the tag |
| Farm & Charm ordinary crops | vanilla `minecraft:farmland`, plus the mod's special fertilized block through its mixin | peat and silt farmland | `NOT_FIXABLE_WITH_DATAPACK` | none | Vanilla placement is block-specific; extending an unused tag would not change it |
| Farm & Charm tomato family | Farm & Charm farmland tag plus custom rope/body/head rules | peat and silt farmland | `NOT_FIXABLE_WITH_DATAPACK` for this phase | none | Custom family requires separate full placement/runtime verification |
| Vinery grapes | bush/vine/pot support blocks | not farmland | `NOT_A_FARMLAND_CROP` | none | No farmland soil check |
| HerbalBrews crops | vanilla farmland behavior | peat and silt farmland | `NOT_FIXABLE_WITH_DATAPACK` | none | No consumed compatibility farmland tag |

The datapack deliberately makes only the Brewery hops fix. It does not add RU blocks to unrelated tags or alter Java behavior.
