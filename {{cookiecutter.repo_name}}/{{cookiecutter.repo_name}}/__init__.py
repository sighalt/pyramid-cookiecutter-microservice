from datetime import datetime
from pyramid.config import Configurator
from pyramid.interfaces import IRendererFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    json_renderer = config.registry.getUtility(IRendererFactory, name="json")
    json_renderer.add_adapter(datetime, lambda o, r: o.isoformat())

    config.add_route("home", "/")
    config.include("pyramid_json_hyperschema")

    config.scan()
    return config.make_wsgi_app()
