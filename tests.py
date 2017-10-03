# -*- coding: utf-8 -*-
"""Tests for ps.bob templates."""

# python imports
from scripttest import TestFileEnvironment
import os
import shutil
import tempfile
import unittest2 as unittest


class BaseTemplateTest(unittest.TestCase):
    """Base class for all ps.bob test cases."""

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(
            os.path.join(self.tempdir, 'test-output'),
            ignore_hidden=False,
        )

    def create_template(self):
        """Run mr.bob to create your template."""
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
            'answers_file': self.answers_file,
        }
        return self.env.run(
            '{dir}/bin/mrbob --config '
            '{dir}/{answers_file} {dir}/src/ps/bob/{template}'.format(
                **options
            )
        )


class DiazoThemeTest(BaseTemplateTest):
    """Test case for the `plone_theme` template."""

    template = 'plone_theme'

    def test_template(self):
        """Validate the `plone_theme` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        self.answers_file = 'test_answers/plone_theme.ini'
        result = self.create_template()
        p = 'ps.diazo.mytheme'
        p_src = p + '/src/ps/diazo'
        expected = [
            p,
            p + '/.csslintrc',
            p + '/.editorconfig',
            p + '/.gitignore',
            p + '/.jshintignore',
            p + '/CHANGES.rst',
            p + '/CONTRIBUTORS.rst',
            p + '/Gruntfile.js',
            p + '/README.rst',
            p + '/buildout.cfg',
            p + '/docs',
            p + '/docs/README',
            p + '/docs/_images',
            p + '/docs/_images/README',
            p + '/docs/source',
            p + '/docs/source/_static',
            p + '/docs/source/_static/logo.png',
            p + '/docs/source/_templates',
            p + '/docs/source/_templates/empty',
            p + '/docs/source/conf.py',
            p + '/docs/source/configuration.rst',
            p + '/docs/source/index.rst',
            p + '/package.json',
            p + '/requirements.txt',
            p + '/setup.cfg',
            p + '/setup.py',
            p + '/src',
            p + '/src/ps',
            p + '/src/ps/__init__.py',
            p_src,
            p_src + '/__init__.py',
            p_src + '/mytheme',
            p_src + '/mytheme/Extensions',
            p_src + '/mytheme/Extensions/install.py',
            p_src + '/mytheme/__init__.py',
            p_src + '/mytheme/config.py',
            p_src + '/mytheme/configure.zcml',
            p_src + '/mytheme/theme',
            p_src + '/mytheme/theme/favicon.ico',
            p_src + '/mytheme/theme/index.html',
            p_src + '/mytheme/theme/install',
            p_src + '/mytheme/theme/install/.gitkeep',
            p_src + '/mytheme/theme/install/registry.xml',
            p_src + '/mytheme/theme/manifest.cfg',
            p_src + '/mytheme/theme/package.json',
            p_src + '/mytheme/theme/preview.png',
            p_src + '/mytheme/theme/rules',
            p_src + '/mytheme/theme/rules.xml',
            p_src + '/mytheme/theme/rules/content.xml',
            p_src + '/mytheme/theme/rules/core.xml',
            p_src + '/mytheme/theme/rules/footer.xml',
            p_src + '/mytheme/theme/rules/header.xml',
            p_src + '/mytheme/theme/rules/transformations.xml',
            p_src + '/mytheme/theme/static',
            p_src + '/mytheme/theme/static/main.css',
            p_src + '/mytheme/theme/static/main.js',
            p_src + '/mytheme/theme/uninstall',
            p_src + '/mytheme/theme/uninstall/.gitkeep',
            p_src + '/mytheme/theme/uninstall/registry.xml',
            p_src + '/mytheme/theme-custom',
            p_src + '/mytheme/theme-custom/custom.css',
            p_src + '/mytheme/theme-custom/custom.js',
            p_src + '/mytheme/theme-custom/manifest.cfg',
            p_src + '/mytheme/theme-custom/preview.png',
            p_src + '/mytheme/theme-custom/rules.xml',
            p_src + '/mytheme/interfaces.py',
            p_src + '/mytheme/locales',
            p_src + '/mytheme/locales/en',
            p_src + '/mytheme/locales/en/LC_MESSAGES',
            p_src + '/mytheme/locales/en/LC_MESSAGES/ps.diazo.mytheme.po',
            p_src + '/mytheme/locales/manual.pot',
            p_src + '/mytheme/locales/plone.pot',
            p_src + '/mytheme/locales/ps.diazo.mytheme.pot',
            p_src + '/mytheme/migration.py',
            p_src + '/mytheme/profiles',
            p_src + '/mytheme/profiles.zcml',
            p_src + '/mytheme/profiles/default',
            p_src + '/mytheme/profiles/default/browserlayer.xml',
            p_src + '/mytheme/profiles/default/metadata.xml',
            p_src + '/mytheme/profiles/default/psdiazomytheme_marker.txt',
            p_src + '/mytheme/profiles/default/theme.xml',
            p_src + '/mytheme/profiles/testfixture',
            p_src + '/mytheme/profiles/testfixture/metadata.xml',
            p_src + '/mytheme/profiles/uninstall',
            p_src + '/mytheme/profiles/uninstall/browserlayer.xml',
            p_src + '/mytheme/profiles/uninstall/theme.xml',
            p_src + '/mytheme/setuphandlers.py',
            p_src + '/mytheme/template_overrides',
            p_src + '/mytheme/template_overrides/README',
            p_src + '/mytheme/testing.py',
            p_src + '/mytheme/tests',
            p_src + '/mytheme/tests/__init__.py',
            p_src + '/mytheme/tests/robot',
            p_src + '/mytheme/tests/robot/keywords.robot',
            p_src + '/mytheme/tests/robot/test_setup.robot',
            p_src + '/mytheme/tests/test_robot.py',
            p_src + '/mytheme/tests/test_setup.py',
        ]
        self.assertItemsEqual(result.files_created.keys(), expected)
