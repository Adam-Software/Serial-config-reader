from serial_config_reader.Models.Joint import Joint


class Motor:
    name: str
    joint: Joint

    def __init__(self, name: str, joint: Joint) -> None:
        self.name = name
        self.joint = joint
