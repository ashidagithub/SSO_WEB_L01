from django.http import HttpResponse


def vdhello(request):
    '直接返回一串字符，作为网页显示'
    return HttpResponse("Hello world ! ")


def vdhtml1(request):
    '直接返回一个 HTML 文本（包装成字符串形式）'

    '''
    <!DOCTYPE html> 声明为 HTML5 文档
    <html> 元素是 HTML 页面的根元素
    <head> 元素包含了文档的元（meta）数据，如 <meta charset="utf-8"> 定义网页编码格式为 utf-8。
    <title> 元素描述了文档的标题
    <body> 元素包含了可见的页面内容
    <h1> 元素定义一个大标题
    <p> 元素定义一个段落
    '''

    str = ' <!DOCTYPE html> \
            <html> \
            <head> \
            <meta charset="utf-8"> \
            <title>良爸教程2019</title> \
            </head> \
            <body> \
                <h1>我的第一个标题</h1> \
                <p>我的第一个段落</p> \
                <h2>我的第二个标题</h2> \
                <p>我的第二个段落</p> \
            </body> \
            </html> '

    return HttpResponse(str)


def vdhtml2(request):
    '分段式返回一个 HTML 文本'

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'
    s_body = '<h3>我的第三个标题</h3><p>我的第三个段落</p>\n'
    s_body += '<h4>我的第四个标题</h4><p>我的第四个段落</p>\n'
    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)


def vdhtml3(request):
    '分段式返回一个 HTML 文本 + href 新标签'

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'

    s_body = '<h3>练习链接</h3>'
    s_body += '<p><a href="http://www.baidu.com">点击这里</a></p>\n'

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)

'''
def index(request):
    '将 vi1-3 html 放进目录'

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'

    s_body = '<h3>目录</h3>'
    s_body += '<p><a href="/vdhtml1">第一个练习</a></p>\n'
    s_body += '<p><a href="/vdhtml2">第二个练习</a></p>\n'
    s_body += '<p><a href="/vdhtml3">外部链接练习</a></p>\n'
    s_body += '<p><a href="/vihtml1">图片练习一</a></p>\n'
    s_body += '<p><a href="/vihtml2">图片练习二（带外部链接）</a></p>\n'
    s_body += '<p><a href="/vihtml3">图片练习三（分区域链接）</a></p>\n'

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)
'''
