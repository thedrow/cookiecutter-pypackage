import os

from nose2.tools import such

from tests.acceptance.support.setuputils import run_setup_command, SUCCESS
from tests.common.layers import AcceptanceTestsLayer


with such.A('Project Documentation') as it:
    it.uses(AcceptanceTestsLayer)

    @it.should('be able to build the docs')
    def test_should_build_docs():
        script = run_setup_command('build_sphinx --source-dir ./docs/source/ --build-dir %s --dry-run' % os.path.join(
            os.path.dirname(__file__), 'support/build'))

        script.expect_exit(SUCCESS)

    it.createTests(globals())
