class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self._status = False  # TV is off by default
        self._mute = False  # TV is not muted by default
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        # Toggle TV status
        self._status = not self._status

    def mute(self):
        # Toggle mute status
        if self._status:
            self._mute = not self._mute

    def channel_up(self):
        # Increase the channel
        if self._status:
            self._channel = self.MIN_CHANNEL if self._channel == self.MAX_CHANNEL else self._channel + 1

    def channel_down(self):
        # Decrease the channel
        if self._status:
            self._channel = self.MAX_CHANNEL if self._channel == self.MIN_CHANNEL else self._channel - 1

    def volume_up(self):
        # Increase the volume
        if self._status:
            if self._mute:
                self._mute = False  # Unmute when changing the volume
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        # Decrease the volume
        if self._status:
            if self._mute:
                self._mute = False  # Unmute when changing the volume
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self):
        # Return the TV details
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
