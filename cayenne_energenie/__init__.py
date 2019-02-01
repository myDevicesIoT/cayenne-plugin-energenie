"""
This module provides a class for interfacing with Energenie Pi-mote Control devices.
"""
from gpiozero import Energenie
from myDevices.utils.logger import info


class CayenneEnergenie():
    """Class for interacting with a socket on an Energenie Pi-mote Control device."""

    def __init__(self, socket, initial_state):
        """Initializes Energenie socket.

        Arguments:
        socket: The socket on the Energenie device
        initial_state: The initial state of the socket
        """
        self.energenie = Energenie(socket, initial_state)

    def get_state(self):
        """Gets the state of the Energenie socket."""
        return (int(self.energenie.value), 'digital_actuator')

    def set_state(self, state):
        """Sets the state of the Energenie socket."""
        if state:
            self.energenie.on()
        else:
            self.energenie.off()
