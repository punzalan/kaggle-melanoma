import argparse
import shlex
import subprocess as sp
import time

import kaggle


def run(task_name):

    cmd = "kaggle kernels status punzalan/{}".format(task_name)

    # TODO: Expose increment as parameter
    increment = 60
    acc = 0

    while True:
        response = sp.run(shlex.split(cmd), stdout=sp.PIPE, stderr=sp.PIPE)
        print(response.stdout.decode("utf-8"))
        is_running = any(
            map(
                lambda elem: elem in response.stdout.decode("utf-8"),
                ["running", "queued"],
            )
        )
        if not is_running:
            break

        # TODO: Expose sleep increment as parameter
        time.sleep(5)
        acc += 5
        if acc >= increment:
            acc = 0
            print("slept {} seconds".format(increment))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--task_name")
    args = parser.parse_args()

    run(args.task_name)
