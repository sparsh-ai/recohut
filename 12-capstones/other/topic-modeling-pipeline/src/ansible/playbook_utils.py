#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Utilities to support running Ansible Playbooks."""

# pylint: disable=invalid-name,dangerous-default-value,unspecified-encoding


import argparse
import io
from typing import Union


def set_nb_target_host_type(
    nb_fpath: str, target_host_type: str, verbose: bool = False
) -> None:
    """Set target host type in Ansible inventory."""
    locale_enc = getattr(io, "LOCALE_ENCODING", None)
    with open(nb_fpath, mode="r", encoding=locale_enc) as f:
        lines = f.readlines()
    if target_host_type == "ec2":
        hosts_list = [
            "  # connection: local",
            "  # hosts: localhost",
            "  hosts: ec2host",
        ]
    else:
        hosts_list = [
            "  connection: local",
            "  hosts: localhost",
            "  # hosts: ec2host",
        ]
    line_start, line_end = [2, 4 + 1]
    if lines[line_start:line_end] == [hl + "\n" for hl in hosts_list]:
        print(
            f"Previously changed to use {target_host_type} as target host. "
            "Did nothing."
        )
    else:
        lines[line_start:line_end] = [hl + "\n" for hl in hosts_list]
        print(f"Changed to use {target_host_type} as target host.")
    with open(nb_fpath, "w", encoding=locale_enc) as f:
        f.writelines(lines)
    if verbose:
        show_file_contents(nb_fpath)


def set_path_to_streamer_script(
    nb_fpath: str, target_host_type: str, verbose: bool = False
) -> None:
    """Set target host type in Ansible inventory."""
    locale_enc = getattr(io, "LOCALE_ENCODING", None)
    with open(nb_fpath, mode="r", encoding=locale_enc) as f:
        lines = f.readlines()
    prefix_str = "          nohup python3 "
    if target_host_type == "ec2":
        cmd_str = prefix_str + "{{ ansible_env.HOME }}/twitter_s3.py \\"
    else:
        cmd_str = f"{prefix_str}twitter_s3.py \\"
    if lines[39] == cmd_str + "\n":
        print(
            "Previously changed to use specified path to script. Did nothing."
        )
    else:
        lines[39] = cmd_str + "\n"
        print("Changed to use specified path to script.")
    with open(nb_fpath, "w", encoding=locale_enc) as f:
        f.writelines(lines)
    if verbose:
        show_file_contents(nb_fpath)


def replace_inventory_host_ip(
    inv_host_vars_fpath: str, remote_ec2_host_ip: str
) -> None:
    """Replace target host address in Ansible inventory."""
    locale_enc = getattr(io, "LOCALE_ENCODING", None)
    with open(inv_host_vars_fpath, mode="r", encoding=locale_enc) as f:
        lines = f.readlines()
    if remote_ec2_host_ip in lines[0]:
        print("Previously changed to use specified IP address. Did nothing.")
    else:
        lines[0] = f"ansible_host: {remote_ec2_host_ip}\n"
        print("Changed to use specified IP address.")
        with open(inv_host_vars_fpath, "w", encoding=locale_enc) as f:
            f.writelines(lines)
        show_file_contents(inv_host_vars_fpath)


def replace_inventory_python_version(
    inv_host_vars_fpath: str, python_version: str = "3"
) -> None:
    """Replace target Python path in Ansible inventory."""
    locale_enc = getattr(io, "LOCALE_ENCODING", None)
    with open(inv_host_vars_fpath, mode="r", encoding=locale_enc) as f:
        lines = f.readlines()
    if python_version in lines[3]:
        print(
            f"Previously changed to use Python {python_version}. Did nothing."
        )
    else:
        new_line_contents = (
            f"ansible_python_interpreter: /usr/bin/python{python_version}\n"
        )
        lines[3] = new_line_contents
        print(f"Changed to use Python {python_version}.")
        with open(inv_host_vars_fpath, "w", encoding=locale_enc) as f:
            f.writelines(lines)
        show_file_contents(inv_host_vars_fpath)


def show_file_contents(
    inv_host_vars_filepath: str, num_lines_to_show: Union[None, int] = None
) -> None:
    """Show contents of a text file."""
    locale_enc = getattr(io, "LOCALE_ENCODING", None)
    with open(inv_host_vars_filepath, mode="r", encoding=locale_enc) as f:
        lines = lines = f.readlines()
    lines_to_show = num_lines_to_show if num_lines_to_show else len(lines)
    for line in lines[:lines_to_show]:
        print(line.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--python-version",
        type=str,
        dest="python_version",
        default="2.7",
        help="remote version of python",
    )
    args = parser.parse_args()

    inventory_host_vars_filepath = "inventories/production/host_vars/ec2host"

    replace_inventory_python_version(
        inventory_host_vars_filepath, args.python_version
    )
