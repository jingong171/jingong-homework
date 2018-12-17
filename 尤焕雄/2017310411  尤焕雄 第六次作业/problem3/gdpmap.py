from country_code import gdpmap

import pygal


gdpmap1={}
gdpmap2={}
gdpmap3={}
##按照GDP的值分为三个组
for k,v in gdpmap.items():
    if v<=100000000000:
        gdpmap1[k]=v
    elif v<=1000000000000:
        gdpmap2[k]=v
    else:
        gdpmap3[k]=v

##把地图画出来并保存
wm=pygal.maps.world.World()
wm.add('<=100tri',gdpmap1)
wm.add('100tri-1000tri',gdpmap2)
wm.add('>1000tri',gdpmap3)
wm.render_to_file('gdpmap.svg')
