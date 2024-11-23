import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    tv.power()
    assert tv._status is True
    tv.power()
    assert tv._status is False

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._mute is True
    tv.mute()
    assert tv._mute is False

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._channel == 1
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv._channel == 0  # Wrap around to the minimum

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._channel == 3  # Wrap around to the maximum
    tv.channel_down()
    tv.channel_down()
    tv.channel_down()
    assert tv._channel == 0

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._volume == 1
    tv.volume_up()
    assert tv._volume == 2
    tv.volume_up()
    assert tv._volume == 2  # Stay at MAX_VOLUME

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv._volume == 0
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._volume == 1
    tv.volume_down()
    tv.volume_down()
    assert tv._volume == 0  # Stay at MIN_VOLUME

def test_volume_unmute():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert tv._mute is False  # Volume change unmutes the TV
    assert tv._volume == 1
