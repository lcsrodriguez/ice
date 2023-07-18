import requests


class ICE:
    def __init__(self) -> None:
        pass

    def searchContracts(self) -> None:
        raise NotImplemented

    def getContractList(self) -> None:
        raise NotImplemented

    def getIntraday(self) -> None:
        # TODO: Add warning (as log)
        print("Be careful ! Delayed data")
        raise NotImplemented

    def getHistorical(self) -> None:
        # TODO: Add warning (as log)
        print("Be careful ! Delayed data")
        raise NotImplemented
