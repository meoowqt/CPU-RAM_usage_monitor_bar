import psutil as pt


class CpuBar:
    def __init__(self) -> None:
        self.cpu_count = pt.cpu_count(logical=False)  # количество ядер
        self.cpu_count_logical = pt.cpu_count()  # количество потоков
