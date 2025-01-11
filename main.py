from api.sfs_logger import Logger
from providers.model_provider import ModelProvider


def main():
    MOD_ID: str = "beautifulworld"
    LOGGER = Logger()

    model_provider = ModelProvider(MOD_ID, LOGGER)
    model_provider.generate()


if __name__ == "__main__":
    main()
