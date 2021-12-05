import platform


def get_instruction_type():
    return platform.machine()


def get_platform_version():
    return platform.version()


def get_platform():
    return platform.platform()


def get_system():
    return platform.system()


def get_processor():
    return platform.processor()