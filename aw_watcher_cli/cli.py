import logging
from datetime import datetime, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

logger = logging.getLogger(__name__)


class CLIWatcher:
    def __init__(self, bucket, etype, testing=False):
        self.client = ActivityWatchClient("aw-watcher-cli", testing=testing)
        self.bucketname = bucket
        self.etype = etype
        self.client.create_bucket(self.bucketname, event_type=self.etype)

    def run(self):
        logger.info("aw-watcher-cli started for bucket '%s' containing events of type '%s'"
                    % (self.bucketname, self.etype))

    def updateLastEvent(self):
        logger.info("Updating previous event duration.")
        try:
            last = self.client.get_events(bucket_id=self.bucketname, limit=1)[0]
        except IndexError:
            logger.info("No previous event found.")
            return

        duration = abs((datetime.now(timezone.utc)-last.timestamp).seconds)
        logger.info("Previous event '%s' occurred at %s. Duration since: %ss"
                    % (last.data, last.timestamp.strftime("%Y-%m-%d %T%z"), duration))
        last.duration = duration
        self.client.insert_event(self.bucketname, last)

    def addStringEvent(self, eventString, duration):
        logger.info("Adding event %s (duration: %s) to bucket %s" %
                    (eventString, duration, self.bucketname))
        data = {"label": eventString}
        event = Event(timestamp=datetime.now(timezone.utc),
                      data=data,
                      duration=duration)
        inserted_event = self.client.insert_event(self.bucketname, event)

        assert inserted_event.id is not None
