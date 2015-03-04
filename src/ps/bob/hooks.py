# -*- coding: utf-8 -*-
"""Pre- and Post-Render Hooks for mr.bob."""

# python imports
from mrbob.bobexceptions import ConfigurationError


def prepare_diazo_render(configurator):
    """Some variables to make templating easier."""

    theme_type = configurator.variables['theme.type']
    if theme_type == 'core':
        namespace = 'ps'
        namespace2 = 'diazo'
    elif theme_type == 'customer':
        namespace = 'customer'
        namespace2 = 'diazo'
    else:
        raise ConfigurationError('The theme type was not defined.')

    dottedname = '.'.join([
        namespace,
        namespace2,
        configurator.variables['package.name'],
    ])
    configurator.variables['package.dottedname'] = dottedname
    configurator.variables['package.namespace'] = namespace
    configurator.variables['package.namespace2'] = namespace2

    # package.uppercasename = 'PS_DIAZO_MYTHEME'
    configurator.variables['package.uppercasename'] = \
        dottedname.replace('.', '_').upper()

    camelcasename = dottedname.replace('.', ' ').title()\
        .replace(' ', '')\
        .replace('_', '')
    browserlayer = "{0}Layer".format(camelcasename)

    # package.testlayer = 'PsDiazoMythemeLayer'
    configurator.variables['package.testlayer'] = browserlayer

    # package.longname = 'psdiazomytheme'
    configurator.variables['package.longname'] = camelcasename.lower()
