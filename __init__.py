"""
    .___                        .___           __
  __| _/____   ____ _____     __| _/____     _/  |___  _  __
 / __ |/ __ \_/ ___\\__  \   / __ |/ __ \    \   __\ \/ \/ /
/ /_/ \  ___/\  \___ / __ \_/ /_/ \  ___/     |  |  \     /
\____ |\___  >\___  >____  /\____ |\___  > /\ |__|   \/\_/
     \/    \/     \/     \/      \/    \/  \/
   _____          __           .____    .____       _____
  /  _  \  __ ___/  |_  ____   |    |   |    |     /     \
 /  /_\  \|  |  \   __\/  _ \  |    |   |    |    /  \ /  \
/    |    \  |  /|  | (  <_> ) |    |___|    |___/    Y    \
\____|__  /____/ |__|  \____/  |_______ \_______ \____|__  /
        \/                             \/       \/       \/
· -—+ auto-prompt-llm-text-vision Extension for ComfyUI +—- ·
trigger more detail using AI render AI
https://decade.tw
https://docs.comfy.org/essentials/custom_node_more_on_inputs#prompt
https://registry.comfy.org/nodes
"""

from .im_sd_vj import *
# import launch
#
# if not launch.is_installed("OpenAI"):
#     launch.run_pip(f"install OpenAI", "OpenAI")

NODE_CLASS_MAPPINGS = {
    "Im-SD-VJ-SPOUT": Im_SD_VJ_SPOUT,
    "Im-SD-VJ-SYPHON": Im_SD_VJ_SPOUT,

}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Im-SD-VJ-SPOUT": "✨ Im-SD-VJ-SPOUT",
    "Im-SD-VJ-SYPHON":"✨ Im-SD-VJ-SYPHON",

}
# WEB_DIRECTORY = "./js"
# __all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]
