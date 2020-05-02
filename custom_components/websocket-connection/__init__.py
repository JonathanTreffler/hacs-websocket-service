DOMAIN = "websocket_connection"

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def handle_send(host, message):
        """Handle the service call."""
        uri = "ws://"+host
        async with websockets.connect(uri) as websocket:
            await websocket.send(input(message))

    hass.services.register(DOMAIN, "send", handle_send)

    return True
