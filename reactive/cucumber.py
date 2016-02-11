from charms.reactive import when, when_not, set_state

# interrogate config, and discern if a config option has
# changed
from charmhelpers.core.hookenv import config
from charmhelpers.fetch import install_remote

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
   install_remote(config('rebacca_url'),checksum=config('rebacca_sum'))
 
   set_state('cucumber.installed')

@when('cucumber.installed')
def probe_nfv():
   # kick off teh nfv evaluation
   
