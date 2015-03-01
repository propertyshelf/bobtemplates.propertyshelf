ps.bob
======

``ps.bob`` provides several `mr.bob`_ template to generate packages for `Propertyshelf`_ projects.

To create a package like ``ps.diazo.mytheme``::

    $ mrbob -O ps.diazo.mytheme ps.bob:diazo_theme


Available Templates
===================

The templates provided by ``ps.bob`` are categorized as follows:

- Plone and Diazo Packages
- Zope Packages (planned)
- Pyramid Packages (planned)
- MLS Packages (planned)

Plone and Diazo Packages
------------------------

diazo_theme
    A installable diazo core theme.
    Those themes are used as a base for most customer themes which extend a core theme.


Options
=======

On creating a package you can choose from the following options. The default value is in [square brackets].

diazo_theme
-----------

Name of the Theme [Example Theme]
    Should be something like 'Example Theme'.

Package Name of the Theme [example]
    Should be something like 'example'.


Features
========

Package created with ``ps.bob`` use the current best-practices when creating an addon.


Plone and Diazo Packages
------------------------

Buildout
    The packages are contained in a buildout that allow you to build Plone with the new package installed for testing-purposes.

Locales
    The packages register a directory for locales.

Profile
    The packages contain a `Generic Setup Profile`_ that installs a browserlayer.

Setuphandler
    The packages contain a `setuphandlers.py`_ where you can add code that is executed on installing the package.

Template-Overrides
    The packages register the folder ``template_overrides`` as a directory where you can drop template-overrides using `z3c.jbot`_.

Tests
    The packages come with a test setup and some `tests`_ for installing the package.
    They also contain a `robot-test`_ for browser testing.
    The buildouts also contains a config to allow testing the package on `travis`_.



Compatibility
=============

Addons created with ``ps.bob`` are tested to work in Plone 4.3.x.
They should also work with other versions but that was not tested.


Installation
============

Use in a buildout
-----------------

::

    [buildout]
    parts += mrbob

    [mrbob]
    recipe = zc.recipe.egg
    eggs =
        mr.bob
        ps.bob

If you want to use the latest development version from GitHub, add ``ps.bob`` to your ``mr.developer`` source section::

    [buildout]
    extensions += mr.developer

    [sources]
    ps.bob git git://github.com/propertyshelf/ps.bob.git


This creates a mrbob-executeable in your bin-directory.
Call it from the ``src``-directory of your project like this.::

    $ ../bin/mrbob -O ps.diazo.mytheme ps.bob:diazo_theme


Installation in a virtualenv
----------------------------

You can also install ``ps.bob`` in a virtualenv.::

    $ pip install ps.bob

You can also install the latest version of ``ps.bob`` directly from GitHub::

    $ pip install -e git://github.com/propertyshelf/ps.bob.git#egg=ps.bob

Now you can use it like this::

    $ mrbob -O ps.diazo.mytheme ps.bob:diazo_theme


.. _`mr.bob`: http://mrbob.readthedocs.org/en/latest/
.. _`Generic Setup Profile`: http://docs.plone.org/develop/addons/components/genericsetup.html
.. _`Propertyshelf`: http://propertyshelf.com
.. _`robot-test`: http://docs.plone.org/external/plone.app.robotframework/docs/source/index.html
.. _`setuphandlers.py`: http://docs.plone.org/develop/addons/components/genericsetup.html?highlight=setuphandler#custom-installer-code-setuphandlers-py
.. _`tests`: http://docs.plone.org/external/plone.app.testing/docs/source/index.html
.. _`travis`: http://travis-ci.org/
.. _`z3c.jbot`: https://pypi.python.org/pypi/z3c.jbot
