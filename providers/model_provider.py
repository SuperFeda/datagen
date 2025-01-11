from api.sfs_logger import Logger
from generators.armor_model_generator import ArmorModelGenerator
from generators.item_model_generator import ItemModelGenerator
from generators.block_model_generator import BlockModelGenerator
from utils.dataclasses import EquipmentType
from utils.registers import Armor, ArmorElement, TrimMaterial


class ModelProvider:
    def __init__(self, mod_id: str, logger: Logger):
        super().__init__()
        self.__mod_id = mod_id
        self.__logger = logger

    def generate_item_models(self, generator: ItemModelGenerator):
        ...

    def generate_armor_models(self, generator: ArmorModelGenerator):
        # reg new armor
        OVERLOUD = Armor(
            armor_material="overloud",
            namespace=self.__mod_id,
            helmet=ArmorElement(id_="overloud_helmet", type_=EquipmentType.HELMET),
            chestplate=ArmorElement(id_="overloud_chestplate", type_=EquipmentType.CHESTPLATE),
            leggings=ArmorElement(id_="overloud_leggings", type_=EquipmentType.LEGGINGS),
            boots=ArmorElement(id_="overloud_boots", type_=EquipmentType.BOOTS),
        )

        # reg new trims
        RHODIUM = TrimMaterial(id_="rhodium", darker_id="rhodium_darker", namespace=self.__mod_id)

        # adding new armor material and new trim material
        generator.append_mod_armor_materials([OVERLOUD])
        generator.append_mod_trim_materials([RHODIUM])

        generator.generate_models_for_new_armor()
        generator.generate_models_for_new_trim_materials()

    def generate_block_models(self, generator: BlockModelGenerator):
        ...

    def generate(self):
        self.generate_item_models(ItemModelGenerator(self.__mod_id))
        self.__logger.info("Generation of item models complete")

        self.generate_armor_models(ArmorModelGenerator(self.__mod_id))
        self.__logger.info("Generation of armor models complete")

        self.generate_block_models(BlockModelGenerator(self.__mod_id))
        self.__logger.info("Generation of block models complete")
