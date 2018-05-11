from glob import glob


__all__ = []

for i in glob("routes/api/*_api.py"):
    __all__.append(i[11:-3])
else:
    for i in __all__:
        from . import i

__name__ = 'routes.api'
__package__ = 'routes.api'
