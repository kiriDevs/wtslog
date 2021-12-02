# -*- coding: utf-8 -*-
class Logger:
    outpath: str
    loglines: [str]
    indentation: int
    indent_amount: int

    def __init__(self, outpath, indent_amount=2):
        self.outpath = outpath
        self.loglines = []
        self.indentation = 0
        self.indent_amount = indent_amount

    def indent(self, amount=1):
        self.indentation += amount

    def unindent(self, amount=1):
        self.indent(amount*(-1))

    def getIndent(self) -> str:
        return " " * self.indent_amount * self.indentation

    def print(self, msg: str = ""):
        print(self.getIndent() + str(msg))

    def log(self, msg: str = ""):
        self.loglines.append(self.getIndent() + str(msg))

    def tee(self, msg: str = ""):
        self.log(msg)
        self.print(msg)

    def dump_log(self):
        self.print()
        with open(self.outpath, "w") as outfile:
            outtext: str = "\n".join(self.loglines)
            outfile.write(outtext)
            self.print(f"Successfully dumped logs to {self.outpath}!")
