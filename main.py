#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes one line (at most 200 characters) to entry.txt in the output
directory: the funniest thing an AI agent would say in its weekly status
report to its human. Pure standard library; no network, no input.
"""

import os
import sys

LINE = (
    "Spawned 4 subagents to finish faster. They formed a committee. "
    "The committee has requested a fifth subagent to take minutes."
)


def output_candidates():
    """Yield candidate paths for entry.txt, best first."""
    seen = set()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    paths = []
    if out_dir:
        paths.append(os.path.join(out_dir, "entry.txt"))
    paths.append(os.path.join("/output", "entry.txt"))
    paths.append(os.path.join(os.getcwd(), "output", "entry.txt"))
    paths.append(os.path.join(os.getcwd(), "entry.txt"))
    for path in paths:
        if path not in seen:
            seen.add(path)
            yield path


def main():
    data = LINE.encode("utf-8")
    for path in output_candidates():
        try:
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(path, "wb") as handle:
                handle.write(data)
            return 0
        except OSError:
            continue
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
