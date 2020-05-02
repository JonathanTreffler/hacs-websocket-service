DOMAIN = "websocket_connection"

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def handle_send(host, message):
        """Handle the service call."""

    hass.services.register(DOMAIN, "send", handle_send)

    # Return boolean to indicate that initialization was successfully.
    return True
