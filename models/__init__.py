from glob import glob

__all__ = []

for i in glob("models/*.py"):
    __all__.append(i[7:-3])
else:
    __all__.remove('__init__')

    for i in __all__:
        from . import i


__name__ = 'models'
__package__ = 'models'
