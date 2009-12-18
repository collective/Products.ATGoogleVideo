## Script (Python) "getUFOJSCodeFromVideo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=video_id,quality,auto_play,div_id='video'
##title=
##

""" returns UFO Javascript code """

code = """
    /* <![CDATA[ */
    var FO = { %s };
    UFO.create(FO, '%s');
    /* ]]> */
"""

majorversion = 9
build = 28
params = "movie:'%s', width:'%s', height:'%s', majorversion:'%s', build:'%s', flashvars:'%s', quality:'%s', wmode:'transparent', setcontainercss:'true'"

if video_id[1:].isdigit():
    # is Google Video
    movie = 'http://video.google.com/googleplayer.swf?docId=%s' % video_id
    width = 400
    height = 326
    flashvars = test(auto_play,'autoplay=true','')

else:
    # is YouTube
    movie = 'http://www.youtube.com/v/%s%s' % (video_id, test(auto_play,'&amp;autoplay=1',''))
    width = 425
    height = 350
    flashvars = ''

params = params % (movie, width, height, majorversion, build, flashvars, quality)
return code % (params, div_id)
