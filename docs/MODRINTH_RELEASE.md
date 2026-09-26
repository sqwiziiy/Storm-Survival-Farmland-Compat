# Modrinth release metadata

## Project

- Project title: Storm Survival Farmland Compat
- Summary: Minecraft 1.20.1 datapack adding Regions Unexplored farmland compatibility for Brewery hops.
- Project type: datapack
- License: MIT
- Source: https://github.com/sqwiziiy/storm-survival-farmland-compat

## Version

- Version number: `0.1.0`
- Version name: `Storm Survival Farmland Compat 0.1.0 — Minecraft 1.20.1`
- Game version: `1.20.1`
- Release type: release
- File: `storm-survival-farmland-compat-0.1.0+mc1.20.1.zip`

## Required dependencies

- Regions Unexplored
- Farm & Charm
- Brewery

Dependency project slugs/IDs must be verified in Modrinth during manual project setup; none are guessed in this document.

## Description

Adds `regions_unexplored:peat_farmland` and `regions_unexplored:silt_farmland` to `#farm_and_charm:farmland`, making Brewery hops compatible with those two RU farmland blocks.

Designed and tested against Minecraft 1.20.1 with Regions Unexplored 0.5.6+1.20.1, Farm & Charm 1.0.14, and Brewery 2.0.6. It does not provide universal RU farmland support and does not change crop growth speed, recipes, seasons, hydration, moisture, or world generation.

## Installation

Place the ZIP in a world's `datapacks/` directory, reload or restart, and verify with `/datapack list`.

## Changelog

- Adds RU peat and silt farmland to `#farm_and_charm:farmland` for Brewery hops.
- No third-party assets or binaries are bundled.
