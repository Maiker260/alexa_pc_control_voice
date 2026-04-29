# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
from ask_sdk_core.skill_builder import SkillBuilder

from handlers.default.launch import LaunchRequestHandler
from handlers.default.help import HelpIntentHandler
from handlers.default.cancel_or_stop import CancelOrStopIntentHandler
from handlers.default.fallback import FallbackIntentHandler
from handlers.default.session_ended import SessionEndedRequestHandler
from handlers.default.intent_reflector import IntentReflectorHandler
from handlers.default.catch_all_exception import CatchAllExceptionHandler

from handlers.config.setup import SetupHandler
from handlers.config.link_code import LinkCodeHandler
from handlers.config.check_user_data import CheckUserDataHandler

from handlers.system_process.restart_pc import RestartPcHandler
from handlers.system_process.shutdown_pc import ShutdownPcHandler

from handlers.application.play_lolito import PlayLolitoHandler
from handlers.application.open_application import OpenApplicationHandler

from handlers.music.play_music import PlayMusicHandler
from handlers.music.play_playlist import PlayPlaylistHandler
from handlers.music.resume_music import ResumeMusicHandler
from handlers.music.pause_music import PauseMusicHandler
from handlers.music.skip_music import SkipMusicHandler
from handlers.music.stop_music import StopMusicHandler
from handlers.music.vol_control.vol_up import VolUpHandler
from handlers.music.vol_control.vol_down import VolDownHandler
from handlers.music.vol_control.set_vol import SetVolHandler


# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())

sb.add_request_handler(SetupHandler())
sb.add_request_handler(LinkCodeHandler())
sb.add_request_handler(CheckUserDataHandler())

sb.add_request_handler(RestartPcHandler())
sb.add_request_handler(ShutdownPcHandler())

sb.add_request_handler(PlayLolitoHandler())
sb.add_request_handler(OpenApplicationHandler())

sb.add_request_handler(PlayMusicHandler())
sb.add_request_handler(PlayPlaylistHandler())
sb.add_request_handler(ResumeMusicHandler())
sb.add_request_handler(PauseMusicHandler())
sb.add_request_handler(SkipMusicHandler())
sb.add_request_handler(StopMusicHandler())
sb.add_request_handler(VolUpHandler())
sb.add_request_handler(VolDownHandler())
sb.add_request_handler(SetVolHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()