import argparse

from aw_core.log import setup_logging

from aw_watcher_cli.cli import CLIWatcher


def main():
    # Set up argparse
    parser = argparse.ArgumentParser(
        ("A watcher that can be invoked manually to write events to AW."))
    parser.add_argument("-v", "--verbose", dest='verbose',
                        action="store_true", help="run with verbose logging")
    parser.add_argument("--testing", action="store_true",
                        help='run in testing mode')
    parser.add_argument("-b", "--bucket",
                        help="The name of the bucket to store events in.",
                        default="aw-watcher-cli")
    parser.add_argument("-d", "--data",
                        help="The JSON-Formatted Event data to store.",
                        required=True)
    parser.add_argument("-D", "--duration",
                        help=" The duration of the event, in seconds.",
                        default=0)
    parser.add_argument("-t", "--eventtype",
                        help="The 'type' of the event to store.",
                        default="awclistatus")

    args = parser.parse_args()

    setup_logging("aw-aw_watcher_cli", testing=args.testing,
                  verbose=args.verbose, log_stderr=True, log_file=True)

    watcher = CLIWatcher(testing=args.testing,
                         bucket=args.bucket,
                         etype=args.eventtype)
    watcher.run()
    watcher.updateLastEvent()
    watcher.addStringEvent(args.data, args.duration)


if __name__ == "__main__":
    main()
