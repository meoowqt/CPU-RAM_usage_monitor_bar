import psutil as pt


class CpuBar:
    def __init__(self) -> None:
        self.cpu_count = pt.cpu_count(logical=False)  # количество ядер
        self.cpu_count_logical = pt.cpu_count()  # количество потоков

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)

    def ram_usage(self):
        return pt.virtual_memory()
