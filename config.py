from dataclasses import dataclass
from environs import Env
@dataclass
class TGbot:
    token: str

@dataclass
class Config:
    bot: TGbot

def load_config(path:str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TGbot(
            token=env.str("BOT_TOKEN")
        ),
    )