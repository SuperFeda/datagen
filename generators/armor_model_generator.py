import json
import os

from utils.conts import DEFAULT_NAMESPACE
from utils.registers import Armor, ArmorElement, TrimMaterial
from utils.dataclasses import (
    EquipmentType,
    MCTrimMaterials,
    MCArmors
)


class ArmorModelGenerator:
    def __init__(self, mod_id: str, json_indent: int = 4):
        super().__init__()
        self.__mod_id = mod_id
        self.json_indent = json_indent

        self.__armor_types: tuple = (
            EquipmentType.HELMET,
            EquipmentType.CHESTPLATE,
            EquipmentType.LEGGINGS,
            EquipmentType.BOOTS
        )

        self.__mc_armors: tuple = (
            MCArmors.IRON,
            MCArmors.GOLDEN,
            MCArmors.DIAMOND,
            MCArmors.CHAINMAIL,
            MCArmors.LEATHER,
            MCArmors.NETHERITE,
            MCArmors.TURTLE
        )
        self.__mod_armors: list = []
        self.__armors: tuple = (*self.__mc_armors, *self.__mod_armors)

        self.__mc_trim_materials: tuple = (
            MCTrimMaterials.QUARTZ,
            MCTrimMaterials.IRON,
            MCTrimMaterials.NETHERITE,
            MCTrimMaterials.REDSTONE,
            MCTrimMaterials.COPPER,
            MCTrimMaterials.GOLD,
            MCTrimMaterials.EMERALD,
            MCTrimMaterials.DIAMOND,
            MCTrimMaterials.LAPIS,
            MCTrimMaterials.AMETHYST,
            MCTrimMaterials.RESIN
        )
        self.__mod_trim_materials: list = []
        self.__trim_materials: tuple = (*self.__mc_trim_materials, *self.__mod_trim_materials)

    def append_mod_armor_materials(self, materials: list[Armor]) -> bool:
        """

        :param materials:
        :return:
        """
        self.__mod_armors.extend(materials)

        self.__armors = (*self.__mc_armors, *self.__mod_armors)  # for update of data

        return True

    def append_mod_trim_materials(self, materials: list[TrimMaterial]) -> bool:
        """

        :param materials:
        :return:
        """
        self.__mod_trim_materials.extend(materials)

        self.__trim_materials = (*self.__mc_trim_materials, *self.__mod_trim_materials)  # for update of data

        return True

    def generate_models_for_new_armor(self) -> None:
        """

        :return: None
        """
        for armor in self.__mod_armors:
            for i in range(len(armor)):
                for trim in self.__mc_trim_materials:
                    self.__armor_item_model_with_trim_layer(namespace=self.__mod_id, armor_element=armor.get_element(i), armor=armor, trim=trim)
                self.__armor_itemstate(armor_element=armor.get_element(i), armor=armor)  # itemstate
                self.__default_armor_item_model(namespace=self.__mod_id, armor_element_id=armor.get_element(i).get_id())  # default (fallback) model

    def generate_models_for_new_trim_materials(self) -> None:
        """

        :return: None
        """
        for armor in self.__armors:
            for i in range(len(armor)):
                for trim in self.__mod_trim_materials:
                    self.__armor_item_model_with_trim_layer(namespace=self.__mod_id, armor_element=armor.get_element(i), armor=armor, trim=trim)
                self.__armor_itemstate(armor=armor, armor_element=armor.get_element(i))  # itemstate

    def __armor_item_model_with_trim_layer(self, armor: Armor, armor_element: ArmorElement, trim: TrimMaterial, namespace: str = None) -> None:
        os.makedirs(f"gen/assets/{namespace}/models/item/", exist_ok=True)

        armor_type = armor_element.get_type_()
        element_id = armor_element.get_id()

        with open(f"gen/assets/{namespace}/models/item/{element_id}_{trim.get_id()}.json", "w") as file:
            json.dump({
                "parent": "minecraft:item/generated",
                "textures": {
                    "layer0": f"{armor.get_namespace()}:item/{element_id}",
                    "layer1": f"minecraft:trims/items/{armor_type}_trim_{trim.get_darker_id() if armor.get_material() == trim.get_id() and trim.has_darker_texture() else trim.get_id()}"
                }
            }, file, indent=self.json_indent)

    def __default_armor_item_model(self, namespace: str, armor_element_id: str) -> None:
        os.makedirs(f"gen/assets/{namespace}/models/item/", exist_ok=True)
        with open(f"gen/assets/{namespace}/models/item/{armor_element_id}.json", "w") as file:
            json.dump({
                "parent": "minecraft:item/generated",
                "textures": {
                    "layer0": f"{namespace}:item/{armor_element_id}",
                }
            }, file, indent=self.json_indent)

    def __armor_itemstate(self, armor: Armor, armor_element: ArmorElement, custom_tints: dict = None) -> None:
        namespace_for_model = armor.get_namespace()
        element_id = armor_element.get_id()

        os.makedirs(f"gen/assets/{namespace_for_model}/items/", exist_ok=True)
        with open(f"gen/assets/{namespace_for_model}/items/{element_id}.json", "w") as file:
            data: dict = {
                "model": {
                    "type": "minecraft:select",
                    "cases": [
                        *({
                            "model": {
                                "type": "minecraft:model",
                                "model": f"{DEFAULT_NAMESPACE if trim_material not in self.__mod_trim_materials and armor not in self.__mod_armors else self.__mod_id}:item/{element_id}_{trim_material.get_id()}_trim",
                            },
                            "when": f"{trim_material.get_namespace()}:{trim_material.get_id()}"
                        } for trim_material in self.__trim_materials),
                    ],
                    "fallback": {
                        "type": "minecraft:model",
                        "model": f"{namespace_for_model}:item/{element_id}",
                    },
                    "property": "minecraft:trim_material"
                }
            }

            if armor is MCArmors.LEATHER:
                data = self.__add_tints(data, {"tints":[{"type": "minecraft:dye","default": -6265536}]})

            if custom_tints is not None:
                data = self.__add_tints(data, custom_tints)

            json.dump(data, file, indent=self.json_indent)

    def __add_tints(self, itemstate: dict, tints: dict) -> dict:
        for i in itemstate["model"]["cases"]:
            i["model"].update(tints)
        itemstate["model"]["fallback"].update(tints)

        return itemstate
