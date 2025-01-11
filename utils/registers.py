from utils.conts import DEFAULT_NAMESPACE


class TrimMaterial:
    def __init__(self, id_: str, darker_id: str = None, namespace: str = DEFAULT_NAMESPACE) -> None:
        super().__init__()
        self.__id = id_
        self.__darker_id = darker_id
        self.__namespace = namespace

    def __repr__(self):
        return f'<TrimMaterial namespace:{self.__namespace} id:{self.__id}>'

    def get_id(self) -> str:
        return self.__id

    def get_darker_id(self) -> str:
        return self.__darker_id

    def get_namespace(self) -> str:
        return self.__namespace

    def has_darker_texture(self) -> bool:
        return self.__darker_id is not None


class ArmorElement:
    def __init__(self, id_: str, type_: str) -> None:
        super().__init__()
        self.__id = id_
        self.__type = type_

    def __repr__(self):
        return f"<ArmorElement id:{self.__id} type:{self.__type}>"

    def get_id(self) -> str:
        return self.__id

    def get_type_(self) -> str:
        return self.__type


class Armor:
    def __init__(self,
                 armor_material: str,
                 namespace: str = DEFAULT_NAMESPACE,
                 helmet: ArmorElement = None,
                 chestplate: ArmorElement = None,
                 leggings: ArmorElement = None,
                 boots: ArmorElement = None
                 ) -> None:
        super().__init__()
        self.__namespace = namespace
        self.__armor_material = armor_material
        self.__helmet = helmet
        self.__chestplate = chestplate
        self.__leggings = leggings
        self.__boots = boots

    def __repr__(self):
        return f'<Armor namespace:{self.__namespace} material:{self.__armor_material}>'

    def __len__(self) -> int:
        count: int = 0
        if self.__helmet is not None:
            count += 1
        if self.__chestplate is not None:
            count += 1
        if self.__leggings is not None:
            count += 1
        if self.__boots is not None:
            count += 1
        return count

    def get_helmet(self) -> ArmorElement:
        return self.__helmet

    def get_chestplate(self) -> ArmorElement:
        return self.__chestplate

    def get_leggings(self) -> ArmorElement:
        return self.__leggings

    def get_boots(self) -> ArmorElement:
        return self.__boots

    def get_material(self) -> str:
        return self.__armor_material

    def get_namespace(self) -> str:
        return self.__namespace

    def get_element(self, number: int) -> ArmorElement:
        """
        get armor element id by index
        :param number: index
        :return: element id
        """
        if number == 0:
            return self.__helmet
        elif number == 1:
            return self.__chestplate
        elif number == 2:
            return self.__leggings
        elif number == 3:
            return self.__boots

