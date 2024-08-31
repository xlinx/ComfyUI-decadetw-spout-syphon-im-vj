import array
import base64
import enum
import io
import logging
import random
import subprocess
import pprint
import numpy as np
import requests
from PIL import Image
from itertools import islice, cycle
import time

import SpoutGL
from itertools import islice, cycle
import time
from OpenGL import GL
from random import randint

random_symbol = '\U0001f3b2\ufe0f'  # 🎲️
reuse_symbol = '\u267b\ufe0f'  # ♻️
paste_symbol = '\u2199\ufe0f'  # ↙
refresh_symbol = '\U0001f504'  # 🔄
save_style_symbol = '\U0001f4be'  # 💾
apply_style_symbol = '\U0001f4cb'  # 📋
clear_prompt_symbol = '\U0001f5d1\ufe0f'  # 🗑️
extra_networks_symbol = '\U0001F3B4'  # 🎴
switch_values_symbol = '\U000021C5'  # ⇅
restore_progress_symbol = '\U0001F300'  # 🌀
detect_image_size_symbol = '\U0001F4D0'  # 📐
log = logging.getLogger("[auto-llm]")
# log.setLevel(logging.INFO)
# Logging


TARGET_FPS = 30

SENDER_NAME = "IMSDVJ"


def randcolor():
    return randint(0, 255)


def tensor_to_pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def call_SpoutGL_sender(is_realtime_enable, image_to_realtime,
                        text_prompt_postive, text_prompt_negative,
                        before_action_cmd_feedback_type, before_action_cmd,
                        post_action_cmd_feedback_type, post_action_cmd, ):
    print("[][IM-VJ][call_SpoutGL_sender]")
    pil_image = tensor_to_pil(image_to_realtime)
    SEND_WIDTH = pil_image.width
    SEND_HEIGHT = pil_image.height
    with SpoutGL.SpoutSender() as sender:
        sender.setSenderName(SENDER_NAME)
        # while is_realtime_enable:
        for i in range(33 * 3):
            print("[][IM-VJ][while True]")
            # Generating bytes in Python is very slow; ideally you should pass in a buffer obtained elsewhere
            # or re-use an already allocated array instead of allocating one on the fly
            # pixels = bytes(islice(cycle([randcolor(), randcolor(), randcolor(), 255]), SEND_WIDTH * SEND_HEIGHT * 4))
            # pixels = image_to_byte_array(pil_image)
            #bytesarray = bytes(Image.fromarray(bytesarray.reshape((SEND_WIDTH, SEND_HEIGHT, 3))).tobytes())
            # sender.sendImage(pixels, SEND_WIDTH, SEND_HEIGHT, GL.GL_RGBA, False, 0)
            result = sender.sendImage(pil_image.tobytes("raw"), SEND_WIDTH, SEND_HEIGHT, GL.GL_RGB, False, 0)
            # Indicate that a frame is ready to read
            sender.setFrameSync(SENDER_NAME)
            # Wait for next send attempt
            time.sleep(1. / TARGET_FPS)
        return image_to_realtime, "", "",


def image_to_byte_array(image: Image) -> bytes:
    # BytesIO is a file-like buffer stored in memory
    imgByteArr = io.BytesIO()
    # image.save expects a file-like as a argument
    image.save(imgByteArr, format='PNG')
    # Turn the BytesIO object back into a bytes object
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def tensor_to_pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def image_to_base64(image):
    pli_image = tensor_to_pil(image)
    image_data = io.BytesIO()
    pli_image.save(image_data, format='PNG', pnginfo=None)
    image_data_bytes = image_data.getvalue()
    encoded_image = "data:image/png;base64," + base64.b64encode(image_data_bytes).decode('utf-8')
    # log.warning("[][image_to_base64][]"+encoded_image)
    # if not str(base64_image).startswith("data:image"):
    #     base64_image = f"data:image/jpeg;base64,{base64_image}"
    return encoded_image


def encodeX(clip, text):
    print("[][Auto-LLM][clip-encode-text] text=", text)
    tokens = clip.tokenize(text)
    output = clip.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
    cond = output.pop("cond")
    return [[cond, output]]


def print_obj_x(obj):
    for attr in dir(obj):
        if not attr.startswith("__"):
            print(attr + "==>", getattr(obj, attr))


class dict_2_class:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)


class dict_2_class_pass:
    pass


class default_openai_completion_class:
    choices = [{"message": {"content": "Missing LLM Server"}}]


class EnumCmdReturnType(enum.Enum):
    PASS = 'Pass'
    JUST_CALL = 'just-call'
    LLM_USER_PROMPT = 'USER-PROMPT'
    LLM_VISION_IMG_PATH = 'VISION-IMG_PATH'

    @classmethod
    def values(cls):
        return [e.value for e in cls]


class AnyTypeX(str):
    """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

    def __eq__(self, _) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False


def call_syphon():
    return None, None, None,


# def call_spout(is_realtime_enable, image_to_realtime,
#                text_prompt_postive, text_prompt_negative,
#                before_action_cmd_feedback_type, before_action_cmd,
#                post_action_cmd_feedback_type, post_action_cmd, ):
#     print("[][IM-VJ][call_spout]")
#
#     return call_SpoutGL_sender(is_realtime_enable, image_to_realtime,
#                         text_prompt_postive, text_prompt_negative,
#                         before_action_cmd_feedback_type, before_action_cmd,
#                         post_action_cmd_feedback_type, post_action_cmd, )


class Im_SD_VJ_SPOUT:
    # @classmethod
    # def IS_CHANGED(s, image_to_realtime):
    #     if image_to_realtime:
    #         return random.random()
    #     else:
    #         return 0

    @classmethod
    def INPUT_TYPES(cls):
        return {
            #https://docs.comfy.org/essentials/custom_node_more_on_inputs#hidden-inputs
            "hidden": {
            },
            "optional": {
                # "trigger_any_type": ("IMAGE",),
            },
            "required": {
                "is_realtime_enable": ("BOOLEAN", {"default": True, "label_off": "OFF", "label_on": "ON"}),
                "image_to_realtime": ("IMAGE",),
                "before_action_cmd_feedback_type": (EnumCmdReturnType.values(),),
                "before_action_cmd": ("STRING", {"multiline": False, "default": ""}),
                "post_action_cmd_feedback_type": (EnumCmdReturnType.values(),),
                "post_action_cmd": (
                    "STRING", {"multiline": False,
                               "default": ""}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING", "STRING",)
    RETURN_NAMES = (
        "🌀before_action_cmd_output",
        "🌀post_action_cmd_output")
    FUNCTION = "call_all"
    CATEGORY = "🧩 IM-VJ"

    def call_all(self, is_realtime_enable=True, image_to_realtime=None,
                 text_prompt_postive=None, text_prompt_negative=None,
                 before_action_cmd_feedback_type=None, before_action_cmd=None,
                 post_action_cmd_feedback_type=None, post_action_cmd=None,
                 ):
        print("[][IM-VJ][call_spout]")
        return call_SpoutGL_sender(is_realtime_enable, image_to_realtime,
                                   text_prompt_postive, text_prompt_negative,
                                   before_action_cmd_feedback_type, before_action_cmd,
                                   post_action_cmd_feedback_type, post_action_cmd, )


# Unit test
if __name__ == "__main__":
    node = Im_SD_VJ_SPOUT()

    result = call_SpoutGL_sender(is_realtime_enable=None, image_to_realtime=None,
                                 text_prompt_postive=None, text_prompt_negative=None,
                                 before_action_cmd_feedback_type=None, before_action_cmd=None,
                                 post_action_cmd_feedback_type=None, post_action_cmd=None,
                                 )
    print("Result:", result)
