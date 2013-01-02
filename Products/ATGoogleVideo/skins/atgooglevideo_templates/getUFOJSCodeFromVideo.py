## Script (Python) "getUFOJSCodeFromVideo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=video_id,quality,auto_play,div_id='video',width='', height=''
##title=
##

""" returns UFO Javascript code """

code = """
    /* <![CDATA[ */
    var FO = { %s };
    UFO.create(FO, '%s');
    /* ]]> */
"""

code_iframe = """
    var tag = document.createElement('script');
    tag.src = "//www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    var player;
    function onYouTubeIframeAPIReady() {
        player = new YT.Player('%s', {
            height: '%s',
            width: '%s',
            videoId: '%s',
            playerVars : {
                'autoplay': %s,
            },
        });
    }
"""

majorversion = 9
build = 28
params = "movie:'%s', width:'%s', height:'%s', majorversion:'%s', build:'%s', flashvars:'%s', quality:'%s', wmode:'transparent', setcontainercss:'true'"

if video_id[1:].isdigit():
    # is Google Video
    movie = 'http://video.google.com/googleplayer.swf?docId=%s' % video_id
    width_swf = width or 400
    height_swf = height or 326
    flashvars = test(auto_play, 'autoplay=true', '')
    params = params % (movie, width_swf, height_swf, majorversion, build, flashvars, quality)
    return code % (params, div_id)

else:
    # is YouTube
    width_swf = width or 425
    height_swf = height or 350
    auto = test(auto_play, 1, 0)
    return code_iframe % (div_id, height_swf, width_swf, video_id, auto)
