from django.http import HttpResponse


def vihtml1(request):
    '显示一张指定的静态图片并调整大小'

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'

    s_body = '<h3>练习图片</h3>\n'
    # 要在settings.py 中加上 STATIC_ROOT 和 STATICFILES_DIRS 的设置内容
    img_path = '\\static\\images\\myimg.png'
    s_body += '<p><img src=%s alt="my first image"></p>\n' % img_path

    # 添加尺寸后的比较
    s_body += '<p><img src=%s alt="my first image" width="300" height="400"></p>\n' % img_path

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)


def vihtml2(request):
    '练习带链接的图片'

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'

    s_body = '<h3>练习带链接的图片</h3>\n'
    # 要在settings.py 中加上 STATIC_ROOT 和 STATICFILES_DIRS 的设置内容
    img_path = '\\static\\images\\myimg.png'
    img_link = 'http://www.baidu.com'
    s_body += '<p><a href=%s><img src=%s alt="my first image" \
              width="300" height="400"></p>\n' % (
        img_link, img_path)

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)


def vihtml3(request):
    '上海市地图，分区域创造链接-图像映射技术 '

    '''
    方法：
    1.将图片分割成更小的图片，然后再在网页上拼接起来，为不同部位的图片各自建立一个连接 href
    2.创建图像映射：它可以为某个部位创建一个称为“热点”的区域，每个热点就是一个映射，当用户单
      击不同热点时就可以跳转到不同的网页。相比较于方法1，可以省去很多切割图片和拼合图片的时间。

    概念：
    1.热点：可以是图形上具有某种形状的一块区域或是一个文本，它也是一种超链接。当访问者单击该
    区域或文本时，超链接所指向的文档会显示在浏览器中。热点 的相撞可以使长方形、圆形或多边形。
    （热点在浏览器中是不可见的，但鼠标移动到热点上时就会改变指针状态，从而可以标示这是个链接）

    2.图像映射分为在服务器上分析和在客户端浏览器中分析两种。
    前者称为客户端图像映射，后者称为服务端图像映射。

    使用HTML定义图像映射：
    HTML中实际是map元素和area元素在起作用来定义图像映射的，Dreamweaver只是使创建的过程更简单。
    （1）area元素
    两个属性：shape属性和coords属性。
    shape有四个属性值：default、rect、circle、poly。
    而coords有三个属性值：rect、circle、poly。
    （2）map元素
    map元素用来定义一个客户端图像映射，该元素一般是和另一个元素配合使用，如img元素、
    object元素或者input元素，这些元素一般会在网页上呈现一个图形。
    这些元素会有一个usemap属性，该属性的值与map元素的name属性值匹配，从而建立联系。
    （3）热点重叠
    有热点重叠的地方，在文档中出现较早的热点具有更高的优先级。

    '''

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'

    s_body = '<h3>练习为图片分区域创建链接</h3>\n'
    # 要在settings.py 中加上 STATIC_ROOT 和 STATICFILES_DIRS 的设置内容
    img_path = '\\static\\images\\map_of_shanghai.jpg'
    # 注意 usemap
    s_body += '<p><img src=%s alt="map of Shanghai" \
              width="600" height="688" usemap="#sh_map"></p>\n' % (img_path)
    # 按坐标区域切割 sh_map
    s_body += '<map name="sh_map">\n'
    # set county img link
    img_link = 'https://map.baidu.com/search/%E5%B4%87%E6%98%8E%E5%8C%BA/@13509325.35872504,3676934.38,10.8z?querytype=s&wd=%E5%B4%87%E6%98%8E%E5%8C%BA&c=2908&provider=pc-aladin&pn=0&device_ratio=2&da_src=shareurl'
    s_body += '<area shape="rect" coords="140,10,560,200" alt="崇明" href= %s>\n' % img_link
    img_link = 'https://map.baidu.com/search/%E9%95%BF%E5%85%B4%E5%B2%9B/@13546518.016347198,3661014.8004900003,13.44z?querytype=s&da_src=shareurl&wd=%E9%95%BF%E5%85%B4%E5%B2%9B&c=289&src=0&pn=0&sug=0&l=10&b=(13391654.341827959,3621840.281689708;13626996.37562212,3732028.4783102917)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2'
    s_body += '<area shape="rect" coords="340,200,420,280" alt="崇明" href= %s>\n' % img_link
    img_link = 'https://map.baidu.com/search/%E6%A8%AA%E6%B2%99%E5%B2%9B/@13562330.097486435,3655561.050352622,13.69z?querytype=s&da_src=shareurl&wd=%E6%A8%AA%E6%B2%99%E5%B2%9B&c=289&src=0&pn=0&sug=0&l=13&b=(13527656.035045212,3652183.5361771625;13565379.997649183,3669846.064802838)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2'
    s_body += '<area shape="rect" coords="420,200,560,330" alt="崇明" href= %s>\n' % img_link

    # <area shape="circle" coords="250,140,35" alt="宝山1" href="mercur.htm">
    # <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
    s_body += '</map>\n'

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)
