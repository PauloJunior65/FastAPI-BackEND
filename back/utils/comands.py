from fastapi_babel import BabelCli
from typing import Optional
from utils.babel import babel

def Comands():
    babel_cli = BabelCli(babel)
    from click import echo, group, option

    @group(
        "cmd",
        help="""
        First Step to extracting messages:\n

            1- extract -d/--dir {watch_dir}\n
            2- init -l/--lang {lang}\n
            3- add your custome translation to your lang `.po` file for example FA dir {./lang/fa}. \n
            4- compile.\n

            Example: \n
                1- extract -d .\n
                2- init -l fa\n
                3- go to ./lang/Fa/.po and add your translations.\n
                4- compile\n

        If you have already extracted messages and you have an existing `.po` and `.mo` file
        follow this steps:\n
            1- extract -d/--dir {watch_dir} \n
            2- update -d/--dir {lang_dir} defaults is ./lang \n
            3- add your custome to your lang `.po` file for example FA dir {./lang/fa}. \n
            4- compile.

            Example: \n
                1- extract -d .\n
                2- update -d lang\n
                3- go to ./lang/Fa/.po and add your translations.\n
                4- compile\n
    """,  # noqa
    )
    def cmd():
        pass

    @cmd.command(
        "extract",
        help="""extract all messages that annotated using gettext/_
            in the specified directory.

            for first time will create messages.pot file into the root
            directory.""",
    )
    @option("-d", "--dir", "dir", help="watch dir")
    def extract(dir):
        try:
            babel_cli.extract(dir)
        except Exception as err:
            echo(err)

    @cmd.command(
        "init",
        help="""Initialized lacale directory for first time.
            if there is already exists the directory, notice that your
            all comiled and initialized messages will remove, in this
            condition has better to use `update` command""",
    )
    @option(
        "-l",
        "--lang",
        "lang",
        help="locale directory name and path, default is fa",
        default="fa",
    )
    def init(lang: Optional[str] = None):
        try:
            babel_cli.init(lang)
        except Exception as err:
            echo(err)

    @cmd.command(
        "compile",
        help="""compile all messages from translation directory in .PO to .MO file and is
            a binnary text file.""",
    )
    def compile():
        try:
            babel_cli.compile()
        except Exception as err:
            echo(err)

    @cmd.command(
        "update",
        help="""update the extracted messages after init command/initialized directory
            , Default is `./lang`""",
    )
    @option("-d", "--dir", "dir", help="locale directory name and path")
    def update(dir: Optional[str] = None):
        try:
            babel_cli.update(dir)
        except Exception as err:
            echo(err)
            
    @cmd.command(
        "teste",
        help="""teste 123""",
    )
    def teste(dir: Optional[str] = None):
        try:
            echo("teste")
        except Exception as err:
            echo(err)

    cmd()