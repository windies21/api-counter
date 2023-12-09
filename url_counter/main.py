"""Simple Url Counter Main"""
from collections import defaultdict, Counter

import click
import json
import pprint
import re
from datetime import datetime
from pathlib import Path
from yirgachefe import logger


def url_counter(file) -> dict:
    url_count = defaultdict(int)
    for i in file:
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        for url in ["".join(x) for x in re.findall(regex, i)]:
            url_count[url] += 1

    return url_count


def make_result_file(targets: list, counter: list):
    result_file_name = f"result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    result = {'targets': targets, 'result': counter}
    with open(result_file_name, "w") as file:
        json.dump(result, file, indent=4)


def pretty(json_obj) -> str:
    return f"\n{pprint.PrettyPrinter(indent=4, sort_dicts=False).pformat(json_obj)}\n"


@click.command()
@click.argument("files", nargs=-1, type=click.File('r'))
@click.option('-d', '--folder', type=click.Path(exists=False), default="", help="Target Json Folder.")
@click.option('-f', '--makefile', is_flag=True, show_default=True, default=False, help="Make Result File.")
@click.option('-r', '--recursive', is_flag=True,
              show_default=True, default=False, help="Includes Sub folders recursively.")
def main(files, folder, makefile, recursive):
    counter = Counter()
    file_list = None
    targets = []

    if files:
        logger.info('Run with files')
        file_list = files
    elif folder:
        directory_path = Path(folder)
        if recursive:
            logger.info(f'Run in path({folder}) recursively.')
            files_ = directory_path.glob('**/*')
        else:
            logger.info(f'Run in path({folder}).')
            files_ = directory_path.glob('*')

        file_list = (open(file, "r") for file in files_ if file.suffix == ".json" and file.name[:7] != "result_")

    if file_list:
        for file in file_list:
            targets.append(file.name)
            count = url_counter(file)
            counter.update(Counter(count))

    result = [{item[0]:item[1]} for item in counter.most_common()]
    if makefile:
        make_result_file(targets, result)

    logger.info(f'URL Count {pretty(result)}')
