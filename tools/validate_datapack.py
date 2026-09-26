#!/usr/bin/env python3
"""Validate the small Storm Survival 1.20.1 compatibility datapack."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATAPACK = ROOT / "datapack"
MODS = Path("/home/mentality/Games/Minecraft-Servers/Java/Fabric/1.20.1/storm-survival/mods")
RU_JAR = MODS / "RegionsUnexploredFabric-0.5.6+1.20.1.jar"
HOPS_JAR = MODS / "letsdo-brewery-fabric-2.0.6.jar"
TAG = DATAPACK / "data/farm_and_charm/tags/blocks/farmland.json"
IDS = ["regions_unexplored:peat_farmland", "regions_unexplored:silt_farmland"]
NAMESPACE = re.compile(r"^[a-z0-9_.-]+$")
PATH = re.compile(r"^[a-z0-9_./-]+$")


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    mcmeta = json.loads((DATAPACK / "pack.mcmeta").read_text())
    fail("pack_format must be 15 for Minecraft 1.20.1") if mcmeta["pack"]["pack_format"] != 15 else None
    tag = json.loads(TAG.read_text())
    fail("compatibility tag must use replace=false") if tag.get("replace") is not False else None
    values = tag.get("values")
    fail("tag values must be a non-empty list") if not isinstance(values, list) or not values else None
    fail("tag contains duplicate values") if len(values) != len(set(values)) else None
    fail("tag values differ from the verified RU inventory") if values != IDS else None

    for path in DATAPACK.rglob("*"):
        if path.is_file():
            rel = path.relative_to(DATAPACK).as_posix()
            parts = rel.split("/")
            fail(f"invalid namespace/path: {rel}") if len(parts) > 1 and (not NAMESPACE.match(parts[1]) or not PATH.match("/".join(parts[2:])) ) else None
    allowed = {"pack.mcmeta", "data/farm_and_charm/tags/blocks/farmland.json"}
    actual = {p.relative_to(DATAPACK).as_posix() for p in DATAPACK.rglob("*") if p.is_file()}
    fail(f"unexpected datapack files: {sorted(actual - allowed)}") if actual != allowed else None

    with zipfile.ZipFile(RU_JAR) as jar:
        names = set(jar.namelist())
        for value in IDS:
            namespace, block = value.split(":", 1)
            fail(f"missing exact RU block resource: {value}") if f"assets/{namespace}/blockstates/{block}.json" not in names else None
        for bundled in (
            "data/c/tags/blocks/farmland.json",
            "data/c/tags/blocks/farmlands.json",
            "data/regions_unexplored/tags/blocks/crop_plantable_blocks.json",
        ):
            data = json.loads(jar.read(bundled))
            fail(f"RU evidence tag missing an expected ID: {bundled}") if any(i not in data["values"] for i in IDS) else None

    with zipfile.ZipFile(HOPS_JAR) as jar:
        class_bytes = jar.read("net/satisfy/brewery/core/block/HopsCropBlock.class")
        fail("installed hops implementation does not show the farmland tag reference") if b"FARMLAND" not in class_bytes else None
        fail("installed hops implementation class is missing") if not class_bytes else None

    print("PASS: datapack JSON, paths, exact RU IDs, tag preservation, and Brewery tag consumption verified")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, FileNotFoundError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
