from xonsh.events import events


__all__ = ("Out", "In")

PYRTNS = []


@events.on_postcommand
def store_pyrtn(cmd, rtn, out, ts):
    retval = _ if "_" in __builtins__ else None
    PYRTNS.append(
        (
            cmd,
            retval,
        )
    )


class PyrtnAccessor:

    def __init__(self, idx, pyhistory=PYRTNS):
        self.__idx = idx
        self.__history = pyhistory

    def __call__(self, histidx=None):
        if histidx is not None:
            return self.__history[histidx][self.__idx]
        return list(map(lambda pyrtn: pyrtn[self.__idx], self.__history))

    def __getitem__(self, idx=None):
        return self(idx)


In = PyrtnAccessor(0)
Out = PyrtnAccessor(1)


__xonsh__.env["PROMPT_FIELDS"]["pyhistnum"] = lambda: len(PYRTNS)
