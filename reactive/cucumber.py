from charms.reactive import when, when_not, set_state

# interrogate config, and discern if a config option has
# changed
from charmhelpers.core.hookenv import config, status_set
from charmhelpers.fetch.archiveurl import ArchiveUrlFetchHandler as auf

# reactive works with synethetic states
@when_not('cucumber.installed')
def install_cucumber():
    # User messaging, that the charm is not configured
    if not config('rebacca_url'):
        status_set('blocked', 'rebacca_url not configured')
        return
    if not config('rebacca_sum'):
        status_set('blocked', 'rebacca_sum not configured')
        return

    # curl's the file passed as first argument, and verifies with
    # second argument
    fetcher = auf()
    fetcher.install(config('rebacca_url'), checksum=config('rebacca_sum'),
                    hash_type='sha256')
    set_state('cucumber.installed')


@when('cucumber.installed')
def probe_nfv():
    # kick off the nfv evaluation
    pass
