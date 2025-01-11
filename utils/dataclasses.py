from utils.registers import Armor, ArmorElement, TrimMaterial
from utils.conts import DEFAULT_NAMESPACE


class MCTrimMaterials:
    QUARTZ: TrimMaterial = TrimMaterial(id_="quartz")
    IRON: TrimMaterial = TrimMaterial(id_="iron", darker_id="iron_darker")
    NETHERITE: TrimMaterial = TrimMaterial(id_="netherite", darker_id="netherite_darker")
    REDSTONE: TrimMaterial = TrimMaterial(id_="redstone")
    COPPER: TrimMaterial = TrimMaterial(id_="copper")
    GOLD: TrimMaterial = TrimMaterial(id_="gold", darker_id="gold_darker")
    EMERALD: TrimMaterial = TrimMaterial(id_="emerald")
    DIAMOND: TrimMaterial = TrimMaterial(id_="diamond", darker_id="diamond_darker")
    LAPIS: TrimMaterial = TrimMaterial(id_="lapis")
    AMETHYST: TrimMaterial = TrimMaterial(id_="amethyst")
    RESIN: TrimMaterial = TrimMaterial(id_="resin")


class EquipmentType:
    HELMET: str = "helmet"
    CHESTPLATE: str = "chestplate"
    LEGGINGS: str = "leggings"
    BOOTS: str = "boots"


class Materials:
    LEATHER: str = "leather"
    CHAINMAIL: str = "chainmail"
    IRON: str = "iron"
    GOLDEN: str = "golden"
    DIAMOND: str = "diamond"
    NETHERITE: str = "netherite"
    TURTLE_SCUTE: str = "turtle_scute"


class MCArmors:
    LEATHER: Armor = Armor(
        Materials.LEATHER,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="leather_helmet", type_=EquipmentType.HELMET),
        ArmorElement(id_="leather_chestplate", type_=EquipmentType.CHESTPLATE),
        ArmorElement(id_="leather_leggings", type_=EquipmentType.LEGGINGS),
        ArmorElement(id_="leather_boots", type_=EquipmentType.BOOTS)
    )
    CHAINMAIL: Armor = Armor(
        Materials.CHAINMAIL,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="chainmail_helmet", type_=EquipmentType.HELMET),
        ArmorElement(id_="chainmail_chestplate", type_=EquipmentType.CHESTPLATE),
        ArmorElement(id_="chainmail_leggings", type_=EquipmentType.LEGGINGS),
        ArmorElement(id_="chainmail_boots", type_=EquipmentType.BOOTS)
    )
    IRON: Armor = Armor(
        Materials.IRON,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="iron_helmet", type_=EquipmentType.HELMET),
        ArmorElement(id_="iron_chestplate", type_=EquipmentType.CHESTPLATE),
        ArmorElement(id_="iron_leggings", type_=EquipmentType.LEGGINGS),
        ArmorElement(id_="iron_boots", type_=EquipmentType.BOOTS)
    )
    GOLDEN: Armor = Armor(
        Materials.GOLDEN,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="golden_helmet", type_=EquipmentType.HELMET),
        ArmorElement(id_="golden_chestplate", type_=EquipmentType.CHESTPLATE),
        ArmorElement(id_="golden_leggings", type_=EquipmentType.LEGGINGS),
        ArmorElement(id_="golden_boots", type_=EquipmentType.BOOTS)
    )
    DIAMOND: Armor = Armor(
        Materials.DIAMOND,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="diamond_helmet", type_=EquipmentType.HELMET),
        ArmorElement(id_="diamond_chestplate", type_=EquipmentType.CHESTPLATE),
        ArmorElement(id_="diamond_leggings", type_=EquipmentType.LEGGINGS),
        ArmorElement(id_="diamond_boots", type_=EquipmentType.BOOTS)
    )
    NETHERITE: Armor = Armor(
        Materials.NETHERITE,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="netherite_helmet", type_=EquipmentType.HELMET),
        ArmorElement(id_="netherite_chestplate", type_=EquipmentType.CHESTPLATE),
        ArmorElement(id_="netherite_leggings", type_=EquipmentType.LEGGINGS),
        ArmorElement(id_="netherite_boots", type_=EquipmentType.BOOTS)
    )
    TURTLE: Armor = Armor(
        Materials.TURTLE_SCUTE,
        DEFAULT_NAMESPACE,
        ArmorElement(id_="turtle_helmet", type_=EquipmentType.HELMET)
    )
