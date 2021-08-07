from hockeysim.database import migrate
from click.testing import CliRunner


def test_database_migration():
    runner = CliRunner()
    result = runner.invoke(migrate)
    assert result.output == "Migration completed\n"