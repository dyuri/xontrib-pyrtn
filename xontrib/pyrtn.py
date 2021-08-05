from xonsh.events import events


__all__ = ("Out", "In")

PYRTNS = []


@events.on_postcommand
def store_pyrtn(cmd, rtn, out, ts):
    PYRTNS.append(
        (
            cmd,
            _ if _ is not PYRTNS else None,
        )
    )


def In(n=None):
    if n is not None:
        return PYRTNS[n][0]
    return list(map(lambda pyrtn: pyrtn[0], PYRTNS))


def Out(n=None):
    if n is not None:
        return PYRTNS[n][1]
    return list(map(lambda pyrtn: pyrtn[1], PYRTNS))


__xonsh__.env["PROMPT_FIELDS"]["pyhistnum"] = lambda: len(PYRTNS)
