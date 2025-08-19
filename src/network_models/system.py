# System settings

from pydantic import BaseModel


class System(BaseModel):
    """
    System settings for device
    """
    ddm: bool = False