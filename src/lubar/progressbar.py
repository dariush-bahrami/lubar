import datetime
import sys


class ProgressBar:
    def __init__(
        self,
        iterations,
        size=37,
        description="",
        file=sys.stdout,
        progressed_char="#",
        remained_char=".",
        enclosing_chars=("[", "]"),
        join_char="  ",
    ):
        self.iterations = iterations
        self.size = size
        self.description = description
        self.file = file
        self.progressed_char = progressed_char
        self.remained_char = remained_char
        self.enclosing_chars = enclosing_chars
        self.join_char = join_char
        self.__last_bar_length = 0

    def __calculate_progress(self, idx):
        progressed = int(self.size * idx / self.iterations)
        remained = self.size - progressed
        return progressed, remained

    def __construct_progress_section(self, progressed, remained):
        progress_section_parts = [
            self.enclosing_chars[0],
            self.progressed_char * progressed,
            self.remained_char * remained,
            self.enclosing_chars[1],
        ]
        return "".join(progress_section_parts)

    def __construct_elapsed_iteration_section(self, idx):
        return f"{idx}/{self.iterations}"

    def __construct_elapsed_time_section(self, elapsed_time):
        h, m, s = [int(float(i)) for i in str(elapsed_time).split(":")]
        return f"{h:02}:{m:02}:{s:02}"

    def show(self, idx, elapsed_time):
        progressed, remained = self.__calculate_progress(idx)
        progress_section = self.__construct_progress_section(progressed, remained)
        elapsed_iterations_section = self.__construct_elapsed_iteration_section(idx)
        elapsed_time_section = self.__construct_elapsed_time_section(elapsed_time)

        bar_parts = [
            self.description,
            progress_section,
            elapsed_iterations_section,
            elapsed_time_section,
        ]
        bar = self.join_char.join(bar_parts)
        self.file.write("\r")
        self.file.write(" " * self.__last_bar_length)
        self.file.write("\r")
        self.file.write(bar)
        self.file.flush()
        self.__last_bar_length = len(bar)

    def __call__(self, iterable):
        start_time = datetime.datetime.now()
        for idx, item in enumerate(iterable):
            current_time = datetime.datetime.now()
            elapsed_time = current_time - start_time
            self.show(idx + 1, elapsed_time)
            yield item
        self.file.write("\n")
        self.file.flush()
