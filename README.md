### Quick Links
* I'm SD-VJ. (share SD-generating-process in realtime by gpu) 
    * SD-WEB-UI: https://github.com/xlinx/sd-webui-decadetw-spout-syphon-im-vj
    * ComfyUI:   https://github.com/xlinx/ComfyUI-decadetw-spout-syphon-im-vj
* Auto prompt by LLM and LLM-Vision (Trigger more details out inside model) 
    * SD-WEB-UI: https://github.com/xlinx/sd-webui-decadetw-auto-prompt-llm
    * ComfyUI:   https://github.com/xlinx/ComfyUI-decadetw-auto-prompt-llm
* Auto msg to ur mobile  (LINE | Telegram | Discord)
  * SD-WEB-UI :https://github.com/xlinx/sd-webui-decadetw-auto-messaging-realtime
  * ComfyUI:  https://github.com/xlinx/ComfyUI-decadetw-auto-messaging-realtime
* CivitAI Info|discuss:
  * https://civitai.com/articles/6988/extornode-using-llm-trigger-more-detail-that-u-never-thought
  * https://civitai.com/articles/6989/extornode-sd-image-auto-msg-to-u-mobile-realtime
<hr/>

# SD-WEB-UI | ComfyUI | decadetw-spout-syphon-im-vj

<hr/>
<p align="center">
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fxlinx%2Fsd-webui-decadetw-auto-prompt-llm&count_bg=%2379C83D&title_bg=%23555555&icon=codeforces.svg&icon_color=%23E7E7E7&title=sd-webui-decadetw-auto-prompt-llm&edge_flat=true" alt=""/>
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fxlinx%2FComfyUI-decadetw-auto-prompt-llm&count_bg=%2379C83D&title_bg=%23555555&icon=codeforces.svg&icon_color=%23E7E7E7&title=ComfyUI-decadetw-auto-prompt-llm&edge_flat=true" alt=""/>
</p>
<p align="center">
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fxlinx%2Fsd-webui-decadetw-auto-messaging-realtime&count_bg=%2379C83D&title_bg=%23555555&icon=codeforces.svg&icon_color=%23E7E7E7&title=sd-webui-decadetw-auto-messaging-realtime&edge_flat=true" alt=""/>
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fxlinx%2FComfyUI-decadetw-auto-messaging-realtime&count_bg=%2379C83D&title_bg=%23555555&icon=codeforces.svg&icon_color=%23E7E7E7&title=ComfyUI-decadetw-auto-messaging-realtime&edge_flat=true" alt=""/>
</p>
<p align="center">  
<a href="https://github.com/feross/standard">
    <img src="https://img.shields.io/badge/code%20style-standard-green.svg?style=flat-square" alt="">
  </a>
  <a href="https://github.com/xlinx/sd-webui-decadetw-auto-prompt-llm/releases">
    <img src="https://img.shields.io/github/downloads/xlinx/sd-webui-decadetw-auto-prompt-llm/total.svg?style=flat-square" alt="">
  </a>
   <a href="https://travis-ci.org/xlinx/sd-webui-decadetw-auto-prompt-llm/builds">
    <img src="https://img.shields.io/travis/xlinx/sd-webui-decadetw-auto-prompt-llm.svg?style=flat-square" alt="">
  </a>
  <a href="https://github.com/xlinx/sd-webui-decadetw-auto-prompt-llm/releases/latest">
    <img src="https://img.shields.io/github/release/xlinx/sd-webui-decadetw-auto-prompt-llm?style=flat-square" alt="">
  </a>
<a href="https://github.com/xlinx/sd-webui-decadetw-auto-prompt-llm/issues">
    <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square" alt="">
</a> 
</p>

#### Update Log
  * [add|202400822] | 🟢 spout support
  * [add|2024008xx] | 🟠 syphon support
  * [add|2024008xx] | 🟠 ofxNDI
  * 🟢 SD-Image(latent space) -> Spout(win)|(mac)Syphon -> GPU Memory -> Other Software (Ultra-fast-access)
  * 🟠 SD-Inpainting use <- GPU Memory <- Spout(win)|(mac)Syphon <- Other Software

## Motivation💡
* Live Performances & ...and show control cues.
  * QLab https://qlab.app/
  * vjdj | madmapper | processing | JAVA ....etc.,
  * https://madmapper.com/
  * https://processing.org/

* Enjoy ur party or project 
* I'm VJ(Visual Jockey)
* Interface, middle-ware between SD and Spout lib (https://spoutgl-site.netlify.app/#CClass:Spout)
* SD-Image to OpenGL in realtime 

##  Web-UI | Forge | ComfyUI preview
<table style="border-width:0px" >
<tr>
    <td>
        <img width=90% src="images/webui_imDJ.png" alt=""/>
    </td>
    <td>
       <img width=90% src="images/comfyui_spout_syphon_workflow.png" alt=""/>
    </td>
 </tr>
</table>

<table style="border-width:0px" >
<tr>
    <td>
        <b style="font-size:20px">Input</b>
    </td>
    <td>
       <b style="font-size:20px">Output</b>
    </td>
 </tr>
 <tr>
    <td> 
        <b style="font-size:30px">Spout / Win </b> 
        <hr/>
        <li style="font-size:14px">Tx </li>
            <li style="font-size:14px; text-indent: 1em;">SD-Image -> 3rd software</li>
        <li style="font-size:14px">Rx </li>
        <li style="font-size:14px; text-indent: 1em;">3rd software (maybe webcam) -> SD-Img2Img</li>
    </td>
    <td>
        <img width="700" src="images/web-ui-user.png" alt=""/>
            <hr/>
        <img width="700" src="images/comfyui_spout_win.png" alt=""/>
    </td>
 </tr>
 <tr>
    <td> 
        <b style="font-size:20px">Syphon / Mac</b> 
        <hr/>
        <b style="font-size:14px">@Mac using Syphon (later. finding M series mac ing...)</b>
    </td>
    <td>
        <img width="400" src="images/ui.png" alt=""/>
    </td>
 </tr>

</table>

## Installtion

* You need install Spout or Syphon Client first.
  * https://github.com/leadedge/Spout2/releases/download/2.007.015/SPOUT_2007-015.zip
  * https://spout.zeal.co/

## Reference

* re-compiler for SD python env 3.10 | 3.11 
  * SpoutGL https://github.com/jlai/Python-SpoutGL/tree/main/VS2019

## How to show high-quality previews?
* Edit the "run_nvidia_gpu.bat" file with "--preview-method auto" on the end.
* If you have ComfyUI Manager Menu installed and just change on "Preview method"
* Use --preview-method auto to enable previews.

* The default installation includes a fast latent preview method that's low-resolution. To enable higher-quality previews with TAESD, download the taesd_decoder.pth, taesdxl_decoder.pth, taesd3_decoder.pth and taef1_decoder.pth and place them in the models/vae_approx folder. Once they're installed, restart ComfyUI and launch it with --preview-method taesd to enable high-quality previews.

##  Suggestion software info list

* https://syphon.github.io/ (Mac)
  * https://github.com/Syphon/Syphon-Framework
* https://spout.zeal.co/ (Win)
  * https://github.com/leadedge/Spout2
* https://github.com/leadedge/ofxNDI (Net)

<div align="right" style="margin-bottom:20px; margin-top:20px">
<a href="https://www.arkaos.com/products/vjdj"><img src="https://syphon.github.io/app_icons/GrandVJ_128.png" width="99" height="99" style="padding:10px"></a>
<a href="http://madmapper.net"><img src="https://syphon.github.io/app_icons/MadMapper_128.png" width="99" height="99" style="padding:10px"></a>
<a href="https://millumin.com/v4/index.php"><img src="https://syphon.github.io/app_icons/Millumin_128.png" width="99" height="99" style="padding:10px"></a>
<a href="http://Modul8.us"><img src="https://syphon.github.io/app_icons/Modul8_128.png" width="99" height="99" style="padding:10px"></a>
<a href="http://vidvox.net"><img src="https://syphon.github.io/app_icons/VDMX_128.png" width="99" height="99" style="padding:10px"></a>
</div>
<div align="right" style="margin-bottom:20px; margin-top:20px">
<a href="http://www.2v-p.tv/" title="2V-P"><img src="https://syphon.github.io/app_icons/2v-p_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://neuromixer.com/" title="AVmixer"><img src="https://syphon.github.io/app_icons/AVmixer_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/Syphon/Syphon-Transmit/" title="Adobe After Effects via Syphon-Transmit"><img src="https://syphon.github.io/app_icons/adobe_after_effects_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/Syphon/Syphon-Transmit/" title="Adobe Character Animator via Syphon-Transmit"><img src="https://syphon.github.io/app_icons/adobe_character_animator_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/Syphon/Syphon-Transmit/" title="Adobe Premiere Pro via Syphon-Transmit"><img src="https://syphon.github.io/app_icons/adobe_premiere_pro_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://appologics.com/airbeam" title="Airbeam"><img src="https://syphon.github.io/app_icons/AirBeam_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://bazik-vj.com/" title="Bazik"><img src="https://syphon.github.io/app_icons/Bazik_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://vdmx.vidvox.net/blog/black-syphon" title="BlackSyphon"><img src="https://syphon.github.io/app_icons/Black_Syphon_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.blendydomevj.com" title="Blendy Dome VJ"><img src="https://syphon.github.io/app_icons/Blendy_Dome_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://blendyvj.com/" title="Blendy VJ"><img src="https://syphon.github.io/app_icons/Blendy_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.hypertonal.net/cathodemer/" title="Cathodemer"><img src="https://syphon.github.io/app_icons/Cathodemer_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://lividinstruments.com/news/cell-cell-dna-vj-software/" title="Cell DNA"><img src="https://syphon.github.io/app_icons/cellDNA_32.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/astellato/Cinder-Syphon" title="Cinder"><img src="https://syphon.github.io/app_icons/Cinder_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://cogevj.hu/" title="CoGe"><img src="https://syphon.github.io/app_icons/CoGe_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://www.dragonframe.com" title="Dragonframe"><img src="https://syphon.github.io/app_icons/Dragonframe_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://sat.qc.ca/en/logiciels/domeport" title="DomePort"><img src="https://syphon.github.io/app_icons/DomePort_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.discobrick.com" title="DiscoBrick"><img src="https://syphon.github.io/app_icons/DiscoBrick_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.pawfal.org/fluxus/packages/" title="Fluxus"><img src="https://syphon.github.io/app_icons/Fluxus_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/Syphon/FreeFrameGL/" title="FreeFrame GL"><img src="https://syphon.github.io/app_icons/Generic_plugin_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.bigfug.com/software/fugio/" title="Fugio"><img src="https://syphon.github.io/app_icons/Fugio_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://glypheo.com/" title="Glypheo"><img src="https://syphon.github.io/app_icons/Glypheo_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://heavym.net/" title="Heavy M"><img src="https://syphon.github.io/app_icons/HeavyM_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/bakercp/IPCAM2SYPHON" title="IPCAM2SYPHON"><img src="https://syphon.github.io/app_icons/IPCAM2SYPHON_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://troikatronix.com/" title="Isadora"><img src="https://syphon.github.io/app_icons/Isadora_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/Syphon/Java" title="Java"><img src="https://syphon.github.io/app_icons/java_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://hv-a.com/lpmt/" title="Little Projection Mapping Tool"><img src="https://syphon.github.io/app_icons/LPMT_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://lumen-app.com" title="Lumen"><img src="https://syphon.github.io/app_icons/Lumen_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.prg.com/prg-products/media-servers/mbox-media-server" title="MBOX"><img src="https://syphon.github.io/app_icons/MBOX_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.mxwendler.net/" title="MXWendler"><img src="https://syphon.github.io/app_icons/MXWendler_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://magicmusicvisuals.com" title="Magic"><img src="https://syphon.github.io/app_icons/Magic_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/Syphon/Jitter/releases/" title="Max/MSP"><img src="https://syphon.github.io/app_icons/Max6_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.arkaos.net/product/index.php?catid=2&amp;pid=10031&amp;iid=74" title="MediaMaster"><img src="https://syphon.github.io/app_icons/MediaMaster_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://imimot.com/mitti/" title="Mitti"><img src="https://syphon.github.io/app_icons/Mitti_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.inklen.com/mixemergency" title="Mix Emergency"><img src="https://syphon.github.io/app_icons/MixEmergency_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.omnido.me" title="Omnidome"><img src="https://syphon.github.io/app_icons/Omnidome_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/astellato/ofxSyphon" title="OpenFrameworks"><img src="https://syphon.github.io/app_icons/OF_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.bigfug.com/software/painting-with-light/" title="Painting With Light"><img src="https://syphon.github.io/app_icons/PaintingWithLight_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://pixelconduit.com/index.html" title="PixelConduit"><img src="https://syphon.github.io/app_icons/PixelConduit_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.plask.org/" title="Plask"><img src="https://syphon.github.io/app_icons/plask_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.renewedvision.com/propresenter.php" title="ProPresenter"><img src="https://syphon.github.io/app_icons/ProPresenter_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/Syphon/Processing/releases" title="Processing"><img src="https://syphon.github.io/app_icons/Processing_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://vdmx.vidvox.net/blog/projectmilksyphon" title="ProjectMilkSyphon"><img src="https://syphon.github.io/app_icons/ProjectMilkSyphon_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://github.com/Syphon/PureData/" title="PureData / GEM"><img src="https://syphon.github.io/app_icons/Puredata_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://figure53.com/qlab/" title="QLab"><img src="https://syphon.github.io/app_icons/QLab_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/Syphon/Quartz-Composer" title="Quartz Composer"><img src="https://syphon.github.io/app_icons/QC_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/Dewb/radome" title="Radome"><img src="https://syphon.github.io/app_icons/Radome_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://mixvibes.com/remixvideo" title="RemixVideo"><img src="https://syphon.github.io/app_icons/Remixvideo_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://resolume.com/" title="Resolume"><img src="https://syphon.github.io/app_icons/Resolume_Arena_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://tecartlab.com/" title="SPARCK"><img src="https://syphon.github.io/app_icons/SPARCK_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://serato.com/video" title="Serato Video"><img src="https://syphon.github.io/app_icons/Serato_Video_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.signalculture.org/appclub.html" title="Signal Culture App Club"><img src="https://syphon.github.io/app_icons/SignalCulture_32.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/paperManu/splash" title="Splash!"><img src="https://syphon.github.io/app_icons/Splash_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://synesthesia.live" title="Synesthesia"><img src="https://syphon.github.io/app_icons/Synesthesia_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://andreacremaschi.github.io/Syphon1394/" title="Syphon1394"><img src="https://syphon.github.io/app_icons/Syphon1394_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/rsodre/SyphonC4D" title="SyphonC4D"><img src="https://syphon.github.io/app_icons/C4D_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="/recorder" title="Syphon Recorder"><img src="https://syphon.github.io/app_icons/Syphon_Recorder_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://andreacremaschi.github.io/Syphon-virtual-screen/" title="Syphon Virtual Screen"><img src="https://syphon.github.io/app_icons/SyphonVirtualScreen_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.sigmasix.ch/syphoner/" title="Syphoner"><img src="https://syphon.github.io/app_icons/Syphoner_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://derivative.ca/" title="Touch Designer"><img src="https://syphon.github.io/app_icons/TouchDesigner_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.ultragrid.cz" title="UltraGrid"><img src="https://syphon.github.io/app_icons/UltraGrid_48.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://github.com/keijiro/KlakSyphon" title="Unity3D"><img src="https://syphon.github.io/app_icons/Unity_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://hcgilje.wordpress.com/vpt/" title="VPT"><img src="https://syphon.github.io/app_icons/VPT_32.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://non-lethal-applications.com/products/video-sync-5/video-sync-5-pro" title="Video Sync Pro"><img src="https://syphon.github.io/app_icons/Video_Slave_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://pixlwave.uk/vidue.html" title="Vidue Stack"><img src="https://syphon.github.io/app_icons/Vidue_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://vuo.org" title="Vuo"><img src="https://syphon.github.io/app_icons/Vuo_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.weiv.co/" title="Weiv"><img src="https://syphon.github.io/app_icons/weiv_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://www.telestream.net/wirecast/" title="Wirecast"><img src="https://syphon.github.io/app_icons/Wirecast_32.png" width="45px" height="45px" style="padding:0px"></a>
<a href="https://z-vector.com" title="Z-Vector"><img src="https://syphon.github.io/app_icons/ZVector_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.zwobotmax.com" title="Zwobot"><img src="https://syphon.github.io/app_icons/Zwobot_128.png" width="45px" height="45px" style="padding:0px"></a>
<a href="http://www.adrienm.net/emotion/eMotion.html" title="eMotion"><img src="https://syphon.github.io/app_icons/eMotion_32.png" width="45px" height="45px" style="padding:0px"></a>



</div>

### Suggestion LLM Model in VJ mode

* LLM-text (normal, chat, assistant)
    * 4B VRAM<2G
        * CHE-72/Qwen1.5-4B-Chat-Q2_K-GGUF/qwen1.5-4b-chat-q2_k.gguf
            * https://huggingface.co/CHE-72/Qwen1.5-4B-Chat-Q2_K-GGUF
    * 7B VRAM<8G
        * ccpl17/Llama-3-Taiwan-8B-Instruct-GGUF/Llama-3-Taiwan-8B-Instruct.Q2_K.gguf
        * Lewdiculous/L3-8B-Stheno-v3.2-GGUF-IQ-Imatrix/L3-8B-Stheno-v3.2-IQ3_XXS-imat.gguf
    * Google-Gemma
        * https://huggingface.co/bartowski/gemma-2-9b-it-GGUF
        * bartowski/gemma-2-9b-it-GGUF/gemma-2-9b-it-IQ2_M.gguf
            * small and good for SD-Prompt

* LLM-vision 👀 (work with SDXL, VRAM >=8G is better )
    * https://huggingface.co/xtuner/llava-phi-3-mini-gguf
        * llava-phi-3-mini-mmproj-f16.gguf (600MB,vision adapter)
        * ⭐⭐⭐llava-phi-3-mini-f16.gguf (7G, main model)
    * https://huggingface.co/FiditeNemini/Llama-3.1-Unhinged-Vision-8B-GGUF
        * llava-llama-3.1-8b-mmproj-f16.gguf
        * ⭐⭐⭐Llama-3.1-Unhinged-Vision-8B-Q8.0.gguf
    * https://huggingface.co/Lewdiculous/Eris_PrimeV4-Vision-32k-7B-GGUF-IQ-Imatrix#quantization-information
      * quantization_options = ["Q4_K_M", "Q4_K_S", "IQ4_XS", "Q5_K_M", "Q5_K_S","Q6_K", "Q8_0", "IQ3_M", "IQ3_S", "IQ3_XXS"]
      * ⭐⭐⭐⭐⭐for low VRAM <font color=#FFD700>**super small**</font>: IQ3_XXS (2.83G)
      * in fact, it's enough uses.

        
## Fixing Spout Post-Build
    By default the spout build config will try to copy to a non-existent Binaries/x64 folder. Fix this by:
    Clicking on SpoutSDK in the Visual Studio Solutions Explorer, and choosing Properties
    Choose BuildEvents->Post-Build Event
    Delete the Command Line option
    Click Apply

## Buy me a Coca cola ☕

https://buymeacoffee.com/xxoooxx


## Colophon

Made for fun. I hope if brings you great joy, and perfect hair forever. Contact me with questions and comments, but not
threats, please. And feel free to contribute! Pull requests and ideas in Discussions or Issues will be taken quite
seriously!
--- https://decade.tw

