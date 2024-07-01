class Server:
    """Class Config is used to set the main logical operations required for the application to work propperly."""

    def __init__(self) -> None:
        self.little_endian: bool = True
        self.threaded: bool = True
        self.locale_nosql: bool = False
        self.store_nets: bool = False

    def use_le(self) -> None:
        self.little_endian = True

    def use_be(self) -> None:
        self.little_endian = False

    def use_threads(self) -> None:
        self.threaded = True

    def dont_use_threads(self) -> None:
        self.threaded = False

    def use_locale_nosql(self) -> None:
        self.locale_nosql = True

    def use_remote_nosql(self) -> None:
        self.locale_nosql = False

    def do_store_nets(self) -> None:
        self.store_nets = True

    def dont_store_nets(self) -> None:
        self.store_nets = False


conf: Server = Server()
