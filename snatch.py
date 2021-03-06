#!/usr/bin/env python3
from __future__ import unicode_literals
import youtube_dl
import argparse


class Logger(object):
    """
    Logging Class
    """
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def snatch_config(args):
    """
    Dynamic Config
    """

    ydl_opts: dict = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': args.mode or 'mp3',
            'preferredquality': str(args.bitrate) or '192',
        }],
        'logger': Logger(),
        'progress_hooks': [snatch_hook],
        'verbose': args.verbose or False,
    }
    return ydl_opts


def snatch_hook(data):
    """
    Hook for displaying progress
    """
    if data['status'] == 'downloading':
        print('.', end='', flush=True)
    if data['status'] == 'finished':
        print(f' ')
        file_name = data['filename'].rsplit(".", 1)[0] + f'.{t_mode}'
        file_size = data['_total_bytes_str']
        print(f'==> DOWNLOAD Complete: {file_name}, Bytes: {file_size}, conversion processing ...')


def snatch(args):
    """
    The Snatch Function
    """
    global t_mode
    t_mode = args.mode

    with youtube_dl.YoutubeDL(snatch_config(args)) as ydl:
        print(f'Fetching: {args.url}')
        ydl.download([args.url])


def main(args):
    """
    The Main Function
    """

    print(f"File format: {args.mode}")
    snatch(args)


def create_parser():
    """
    Create the command line parser.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands')

    # mp3 options
    subparser = subparsers.add_parser(
        'mp3',
        help=f'Instructs snatch that you are requesting output format to be mp3'
    )
    subparser.add_argument(
        '-u',
        '--url',
        help='--url <http://www.youtube.com/watch?v=NaW_semoZie>',
        default="true",
        required=True
    )
    subparser.add_argument(
        '-v',
        '--verbose',
        help='--verbose (True|False)',
        default=False,
        required=False
    )
    subparser.add_argument(
        '-b',
        '--bitrate',
        help='--bitrate encoding bitrate, default: 192',
        default='192',
        required=False
    )
    subparser.set_defaults(mode='mp3')

    # m4a options
    subparser = subparsers.add_parser(
        'm4a',
        help=f'Instructs snatch that you are requesting output format to be m4a'
    )
    subparser.add_argument(
        '-u',
        '--url',
        help='--url <http://www.youtube.com/watch?v=NaW_semoZie>',
        default="true",
        required=True
    )
    subparser.add_argument(
        '-v',
        '--verbose',
        help='--verbose (True|False)',
        default=False,
        required=False
    )
    subparser.add_argument(
        '-b',
        '--bitrate',
        help='--bitrate encoding bitrate, default: 192',
        default='192',
        required=False
    )
    subparser.set_defaults(mode='m4a')

    # flac options
    subparser = subparsers.add_parser(
        'flac',
        help=f'Instructs snatch that you are requesting output format to be flac'
    )
    subparser.add_argument(
        '-u',
        '--url',
        help='--url <http://www.youtube.com/watch?v=NaW_semoZie>',
        default="true",
        required=True
    )
    subparser.add_argument(
        '-v',
        '--verbose',
        help='--verbose (True|False)',
        default=False,
        required=False
    )
    subparser.add_argument(
        '-b',
        '--bitrate',
        help='--bitrate encoding bitrate, default: 192',
        default='192',
        required=False
    )
    subparser.set_defaults(mode='flac')

    # wav options
    subparser = subparsers.add_parser(
        'wav',
        help=f'Instructs snatch that you are requesting output format to be wav'
    )
    subparser.add_argument(
        '-u',
        '--url',
        help='--url <http://www.youtube.com/watch?v=NaW_semoZie>',
        default="true",
        required=True
    )
    subparser.add_argument(
        '-v',
        '--verbose',
        help='--verbose (True|False)',
        default=False,
        required=False
    )
    subparser.add_argument(
        '-b',
        '--bitrate',
        help='--bitrate encoding bitrate, default: 192',
        default='192',
        required=False
    )
    subparser.set_defaults(mode='wav')

    return parser


def parse_args_and_run(argv=None):
    """
    Wrapper for command-line execution.
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    main(args)


if __name__ == '__main__':
    parse_args_and_run()
