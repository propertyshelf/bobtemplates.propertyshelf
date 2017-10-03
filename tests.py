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
        p = 'ps.diazo.example'
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
            p_src + '/example',
            p_src + '/example/Extensions',
            p_src + '/example/Extensions/install.py',
            p_src + '/example/__init__.py',
            p_src + '/example/config.py',
            p_src + '/example/configure.zcml',
            p_src + '/example/theme',
            p_src + '/example/theme/favicon.ico',
            p_src + '/example/theme/index.html',
            p_src + '/example/theme/install',
            p_src + '/example/theme/install/.gitkeep',
            p_src + '/example/theme/install/registry.xml',
            p_src + '/example/theme/manifest.cfg',
            p_src + '/example/theme/package.json',
            p_src + '/example/theme/preview.png',
            p_src + '/example/theme/rules',
            p_src + '/example/theme/rules.xml',
            p_src + '/example/theme/rules/content.xml',
            p_src + '/example/theme/rules/core.xml',
            p_src + '/example/theme/rules/footer.xml',
            p_src + '/example/theme/rules/header.xml',
            p_src + '/example/theme/rules/transformations.xml',
            p_src + '/example/theme/static',
            p_src + '/example/theme/static/main.css',
            p_src + '/example/theme/static/main.js',
            p_src + '/example/theme/uninstall',
            p_src + '/example/theme/uninstall/.gitkeep',
            p_src + '/example/theme/uninstall/registry.xml',
            p_src + '/example/theme-custom',
            p_src + '/example/theme-custom/custom.css',
            p_src + '/example/theme-custom/custom.js',
            p_src + '/example/theme-custom/manifest.cfg',
            p_src + '/example/theme-custom/preview.png',
            p_src + '/example/theme-custom/rules.xml',
            p_src + '/example/interfaces.py',
            p_src + '/example/locales',
            p_src + '/example/locales/en',
            p_src + '/example/locales/en/LC_MESSAGES',
            p_src + '/example/locales/en/LC_MESSAGES/ps.diazo.example.po',
            p_src + '/example/locales/manual.pot',
            p_src + '/example/locales/plone.pot',
            p_src + '/example/locales/ps.diazo.example.pot',
            p_src + '/example/migration.py',
            p_src + '/example/profiles',
            p_src + '/example/profiles.zcml',
            p_src + '/example/profiles/default',
            p_src + '/example/profiles/default/browserlayer.xml',
            p_src + '/example/profiles/default/metadata.xml',
            p_src + '/example/profiles/default/psdiazoexample_marker.txt',
            p_src + '/example/profiles/default/theme.xml',
            p_src + '/example/profiles/testfixture',
            p_src + '/example/profiles/testfixture/metadata.xml',
            p_src + '/example/profiles/uninstall',
            p_src + '/example/profiles/uninstall/browserlayer.xml',
            p_src + '/example/profiles/uninstall/theme.xml',
            p_src + '/example/setuphandlers.py',
            p_src + '/example/template_overrides',
            p_src + '/example/template_overrides/README',
            p_src + '/example/testing.py',
            p_src + '/example/tests',
            p_src + '/example/tests/__init__.py',
            p_src + '/example/tests/robot',
            p_src + '/example/tests/robot/keywords.robot',
            p_src + '/example/tests/robot/test_setup.robot',
            p_src + '/example/tests/test_robot.py',
            p_src + '/example/tests/test_setup.py',
        ]
        self.assertItemsEqual(result.files_created.keys(), expected)
