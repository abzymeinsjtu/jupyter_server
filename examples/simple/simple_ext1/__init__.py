from .application import SimpleApp1


def _jupyter_server_extension_points():
    return [{"module": "simple_ext1.application", "app": SimpleApp1}]
