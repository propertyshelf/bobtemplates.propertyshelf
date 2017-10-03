# -*- coding: utf-8 -*-
"""Pre- and Post-Render Hooks for mr.bob."""


def prepare_diazo_render(configurator):
    """Some variables to make templating easier."""
    namespace = 'ps'
    namespace2 = 'diazo'

    dottedname = '.'.join([
        namespace,
        namespace2,
        configurator.variables['package.name'],
    ])
    configurator.variables['package.dottedname'] = dottedname
    configurator.variables['package.namespace'] = namespace
    configurator.variables['package.namespace2'] = namespace2

    # package.uppercasename = 'PS_DIAZO_EXAMPLE'
    configurator.variables['package.uppercasename'] = \
        dottedname.replace('.', '_').upper()

    camelcasename = dottedname.replace('.', ' ').title()\
        .replace(' ', '')\
        .replace('_', '')
    testlayer = '{0}Layer'.format(camelcasename)

    # package.testlayer = 'PsDiazoExampleLayer'
    configurator.variables['package.testlayer'] = testlayer

    browserlayer = 'I{0}'.format(testlayer)
    # package.browserlayer = 'IPsDiazoExampleLayer'
    configurator.variables['package.browserlayer'] = browserlayer

    # package.longname = 'psdiazoexample'
    configurator.variables['package.longname'] = camelcasename.lower()
