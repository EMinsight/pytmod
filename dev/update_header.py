# Authors: Benjamin Vial
# This file is part of pytmod
# License: GPLv3
# See the documentation at bvial.info/pytmod


from __future__ import annotations

import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

header = """# Authors: Benjamin Vial
# This file is part of pytmod
# License: GPLv3
# See the documentation at bvial.info/pytmod
"""


DIR = Path(__file__).parents[1].resolve()


def rep_header(python_file, header):
    with Path.open(python_file) as f:
        lines = f.readlines()
    i = 0
    current_header = []
    for line in lines:
        if line.startswith("#"):
            current_header.append(line)
            i += 1
        else:
            break

    new_header = header.splitlines()
    new_header = [h + "\n" for h in new_header]
    if new_header != current_header:
        new_header = "".join(new_header)
        data = new_header + "".join(lines[i:])
        with Path.open(python_file, "w") as f:
            f.write(data)


def update(directory):
    for root, _dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_file = Path(Path(root) / file).resolve()
                logging.info("Updating header in %s ...", python_file)
                rep_header(python_file, header)


for directory in [DIR]:
    update(directory)
