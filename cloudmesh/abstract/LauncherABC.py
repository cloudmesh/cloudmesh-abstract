from abc import ABCMeta, abstractmethod


# noinspection PyUnusedLocal
class LauncherABC(metaclass=ABCMeta):

    kind = "abstract"

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def define(self, name=None, spec=None, kind=None):
        """
        define a launch and give it the name

        :param name: the unique launch name
        :return:  The dict representing the launch
        """
        raise NotImplementedError

    @abstractmethod
    def info(self, name=None):
        """
        gets the information of a launch with a given name

        :param name:
        :return: The dict representing the launch including updated status
        """
        raise NotImplementedError


    @abstractmethod
    def start(self, name=None):
        """
        start a launch and give it the name

        :param name: the unique launch name
        :return:  The dict representing the launch
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self, name=None):
        """
        stops the launch with the given name

        :param name:
        :return: The dict representing the launch including updated status
        """
        raise NotImplementedError


    @abstractmethod
    def list(self, **kwargs):
        """
        list all launchers

        :return: an array of dicts representing the launchs
        """
        raise NotImplementedError


    @abstractmethod
    def rename(self, name=None, destination=None):
        """
        rename a launch

        :param destination:
        :param name: the current name
        :return: the dict with the new name
        """
        # if destination is None, increase the name counter and use the new name
        raise NotImplementedError

    def log(self, name=None):
        """
        returns the log of the launch

        :param name:
        :return:
        """
        raise NotImplementedError
        return ""
