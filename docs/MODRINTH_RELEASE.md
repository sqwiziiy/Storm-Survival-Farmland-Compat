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
- SHA-256: `0fee6f3d026e61fbfd45dbf5f4265bc71f2108e63edd23d5fe170f94cfb9399f`

## Required dependencies

Verified Modrinth projects:

- Regions Unexplored
  - slug: `regions-unexplored`
  - project ID: `Tkikq67H`
  - exact tested Fabric version: `A-0.5.6+1.20.1`
  - exact tested version ID: `rhE8MT9Z`
- [Let's Do] Farm & Charm
  - slug: `lets-do-farm-charm`
  - project ID: `HJetCzWo`
  - exact tested Fabric version: `1.0.14`
  - exact tested version ID: `sMjnKy5B`
- [Let's Do] Brewery - Farm&Charm Compat
  - slug: `lets-do-brewery-farmcharm-compat`
  - project ID: `b7NV2plI`
  - exact tested Fabric version: `2.0.6`
  - exact tested version ID: `W2QrBsrL`

Use the project-level dependencies as REQUIRED. The exact version IDs above document the tested environment; do not imply that only those exact versions can ever work.

## Description

Adds `regions_unexplored:peat_farmland` and `regions_unexplored:silt_farmland` to `#farm_and_charm:farmland`, making Brewery hops compatible with those two Regions Unexplored farmland blocks.

Designed and tested against Minecraft 1.20.1 with Regions Unexplored 0.5.6+1.20.1, Farm & Charm 1.0.14, and Brewery 2.0.6. Other 1.20.1 versions may work if the relevant block IDs and farmland-tag behavior remain unchanged, but they are not guaranteed.

The datapack does not provide universal RU farmland support and does not change crop growth speed, recipes, seasons, hydration, moisture, or world generation.

## Installation

Place the ZIP in a world's `datapacks/` directory, reload or restart, and verify with `/datapack list`.

## Changelog

- Adds RU peat and silt farmland to `#farm_and_charm:farmland` for Brewery hops.
- No third-party assets or binaries are bundled.
- Validation PASS.
- Manual Minecraft test PASS.

## Content-disclosure / publication gate

Modrinth's current rules require accurate generative-AI disclosure when a substantial portion of code, assets, design/functionality, or project-page publishing relies on generative AI. Modrinth also states that projects may not be public if the project contents are primarily or entirely a product of generative-AI output.

This project was developed with AI-assisted analysis/tooling and its publication text was AI-assisted. Before submitting publicly:

1. enable the appropriate `Contains AI-generated content` disclosure;
2. review the actual datapack files and project description yourself;
3. do not submit if the resulting project would still be primarily/entirely AI-generated under Modrinth's current rules;
4. do not use an AI-generated project icon, gallery image, or banner.

GitHub source/release publication is independent of this Modrinth moderation gate.
