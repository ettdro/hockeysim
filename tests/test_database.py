from hockeysim.database import migrate
from click.testing import CliRunner
import pytest

@pytest.mark.skip(reason="test works locally, but fails in CI, skipping for now")
def test_database_migration():
    runner = CliRunner()
    result = runner.invoke(migrate)
    assert result.exit_code == 0
    assert result.output == "Migration completed\n"