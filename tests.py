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
            'project': self.project,
            'answers_file': self.answers_file,
        }
        return self.env.run(
            '{dir}/bin/mrbob -O {project} --config '
            '{dir}/{answers_file} {dir}/src/ps/bob/{template}'.format(
                **options
            )
        )
        # return self.env.run(
        #     '%(dir)s/bin/mrbob -O %(project)s --config '
        #     '%(dir)s/%(answers_file)s %(dir)s/src/ps/bob/%(template)s'
        #     % options)


class DiazoThemeTest(BaseTemplateTest):
    """Test case for the `diazo_theme` template."""
    template = 'diazo_theme'
    project = 'ps.diazo.mytheme'
    answers_file = 'test_answers/diazo_theme.ini'

    def test_plone_addon_template(self):
        """Test the `plone_addon` template.
        Generate a project from a template, test which files were created
        and run all te)sts in the generated package.
        """
        self.maxDiff = None
        result = self.create_template()
        p = self.project
        p_src = p + '/src/ps/diazo'
        expected = [
            p,
            p + '/.csslintrc',
            p + '/.gitignore',
            p + '/.jshintignore',
            p + '/CHANGES.rst',
            p + '/README.rst',
            p + '/bootstrap.py',
            p + '/buildout.cfg',
            p + '/docs',
            p + '/docs/README',
            p + '/docs/source',
            p + '/docs/source/_static',
            p + '/docs/source/_static/logo.png',
            p + '/docs/source/_templates',
            p + '/docs/source/_templates/empty',
            p + '/docs/source/conf.py',
            p + '/docs/source/index.rst',
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
            p_src + '/mytheme/diazo_resources',
            p_src + '/mytheme/diazo_resources/favicon.ico',
            p_src + '/mytheme/diazo_resources/index.html',
            p_src + '/mytheme/diazo_resources/manifest.cfg',
            p_src + '/mytheme/diazo_resources/preview.png',
            p_src + '/mytheme/diazo_resources/rules.xml',
            p_src + '/mytheme/diazo_resources/static',
            p_src + '/mytheme/diazo_resources/static/main.css',
            p_src + '/mytheme/diazo_resources/static/main.js',
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
            p_src + '/mytheme/profiles/default/theme.xml',
            p_src + '/mytheme/profiles/uninstall',
            p_src + '/mytheme/profiles/uninstall/browserlayer.xml',
            p_src + '/mytheme/profiles/uninstall/theme.xml',
            p_src + '/mytheme/template_overrides',
            p_src + '/mytheme/template_overrides/README',
        ]
        self.assertItemsEqual(result.files_created.keys(), expected)
