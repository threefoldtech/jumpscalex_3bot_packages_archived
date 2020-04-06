from Jumpscale import j


class TFDirectoryFactory(j.baseclasses.threebot_factory):

    __jslocation__ = "j.threebot_factories.package.directory"

    def test(self, name=""):
        """
        test the directory
        """

        # FIXME: server is already running
        
        self._tests_run(name=name, die=True)
