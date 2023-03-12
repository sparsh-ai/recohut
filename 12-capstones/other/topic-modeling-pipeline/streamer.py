#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Ansible playbook runner with access to environment variables."""

# pylint: disable=invalid-name


import argparse
import os
import shlex
import subprocess

from dotenv import find_dotenv, load_dotenv

import src.ansible.playbook_utils as pbu


def run_cmd(cmd: str) -> None:
    """Run a shell command using Python."""
    print(cmd)
    process = subprocess.Popen(
        shlex.split(cmd), shell=False, stdout=subprocess.PIPE
    )
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            print(str(output.strip(), "utf-8"))
    _ = process.poll()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tag",
        type=str,
        dest="tag",
        default="start",
        help="whether to start or stop streaming",
    )
    parser.add_argument(
        "--target-type",
        type=str,
        dest="target_type",
        default="localhost",
        help="whether to run the streaming code on localhost or ec2 instance",
    )
    args = parser.parse_args()

    if os.path.exists("../.env"):
        load_dotenv(find_dotenv())

    print("Will run twitter streaming code using orchestration.")
    pbu.set_nb_target_host_type("stream_twitter.yml", args.target_type)
    pbu.set_path_to_streamer_script("stream_twitter.yml", args.target_type)

    run_cmd(
        "ansible-playbook -i inventories/production stream_twitter.yml "
        f"--extra-vars '@variables_run.yaml' --tags {args.tag}"
    )
