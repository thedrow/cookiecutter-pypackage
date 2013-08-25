import os
from nose2.tools import such

import setup
from tests.acceptance.support.setuputils import run_setup_command, SUCCESS
from tests.common.layers import AcceptanceTestsLayer


with such.A('Setup Script') as it:
    it.uses(AcceptanceTestsLayer)

    @it.should('be able to install testsuite')
    def test_should_install():
        script = run_setup_command('install --dry-run')

        script.expect_exit(SUCCESS)

    @it.should('have all the required metadata')
    def test_should_have_all_required_metadata():
        script = run_setup_command('check --metadata --restructuredtext --strict')

        script.expect_exit(SUCCESS)

    @it.should('be able to register the package to PyPi')
    def test_should_be_able_to_register_package():
        script = run_setup_command('register --strict --dry-run')

        script.expect_exit(SUCCESS)

    @it.should('be able to upload the package to PyPi')
    def test_should_be_able_to_upload_package():
        script = run_setup_command('sdist upload --dry-run')

        script.expect_exit(SUCCESS)

    @it.should('be able to create a source distribution')
    def test_should_be_able_to_create_source_distribution():
        script = run_setup_command('build sdist clean')

        script.expect_exit(SUCCESS)

    @it.should('specify all the common requirements')
    def test_should_specify_all_common_requirements(case):
        case.assertTrue(os.path.exists('./requirements/common.txt'), 'common requirements file does not exist')

        expected = [requirement.strip() for requirement in open('./requirements/common.txt').readlines()]
        actual = setup.config.get('install_requires', None)

        case.assertEquals(actual, expected)

    @it.should('specify all the dependencies that are required for testing')
    def test_should_specify_all_testing_requirements(case):
        case.assertTrue(os.path.exists('./requirements/testing.txt'),
                        "testing requirements file does not exist")

        expected = [requirement.strip() for requirement in
                    open('./requirements/testing.txt').readlines()
                    + open('./requirements/testing/unit.txt').readlines()
                    + open('./requirements/testing/functional.txt').readlines()
                    + open('./requirements/testing/integration.txt').readlines()
                    + open('./requirements/testing/acceptance.txt').readlines()
                    if not requirement.strip().startswith('-r')]

        actual = setup.config.get('tests_requires', None)

        case.assertEquals(actual, expected)

    @it.should('specify all the dependencies that are required for setup')
    def test_should_specify_all_setup_requirements(case):
        expected = ['setuptools']
        actual = setup.config.get('setup_requires', None)

        case.assertEquals(actual, expected)

    @it.should('use the README.rst file as the long description')
    def test_should_use_readme_file(case):
        expected = open('README.rst').read()
        actual = setup.config.get('long_description', None)

        case.assertEquals(actual, expected)

    it.createTests(globals())
