from django.http import HttpResponse


def index(request):
    '直接返回一个表格，链接到过去所做过的页面'

    s0 = '<!DOCTYPE html>\n'
    s_html_prefix = '<html>\n'
    s_head = '<head><meta charset="utf-8"><title>良爸教程2019</title></head>\n'
    s_body_prefix = '<body>\n'

    # ----- 学习表格 ▼----------------------------------
    s_body = '<h3>练习表格</h3>\n'

    s_body += '<table border="1">'

    # ----- 添加最初的 HTML 练习
    s_body += '    <tr>'
    s_body += '        <th>No</th>'
    s_body += '        <th>练习内容说明</th>'
    s_body += '    </tr>'

    a_link = '<a href="/vdhtml1/">之前的练习一</a>'
    s_body += '    <tr>'
    s_body += '        <td>%s</td>' % a_link
    s_body += '        <td>直接返回一个 HTML 文本（包装成字符串形式）</td>'
    s_body += '    </tr>'

    a_link = '<a href="/vdhtml2/">之前的练习二</a>'
    s_body += '    <tr>'
    s_body += '        <td>%s</td>' % a_link
    s_body += '        <td>分段式返回一个 HTML 文本</td>'
    s_body += '    </tr>'

    a_link = '<a href="/vdhtml3/">之前的练习三</a>'
    s_body += '    <tr>'
    s_body += '        <td>%s</td>' % a_link
    s_body += '        <td>分段式返回一个 HTML 文本 + href 新标签</td>'
    s_body += '    </tr>'

    # ----- 添加图像链接练习
    a_link = '<a href="/vihtml1/">图片练习一</a>'
    s_body += '    <tr>'
    s_body += '        <td>%s</td>' % a_link
    s_body += '        <td>显示一张指定的静态图片并调整大小</td>'
    s_body += '    </tr>'

    a_link = '<a href="/vihtml2/">图片练习二</a>'
    s_body += '    <tr>'
    s_body += '        <td>%s</td>' % a_link
    s_body += '        <td>练习带链接的图片</td>'
    s_body += '    </tr>'

    a_link = '<a href="/vihtml3/">图片练习三</a>'
    s_body += '    <tr>'
    s_body += '        <td>%s</td>' % a_link
    s_body += '        <td>上海市地图，分区域创造链接-图像映射技术</td>'
    s_body += '    </tr>'


    s_body += '</table>'

    # ----- 学习表格 ▲ ----------------------------------

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse(s_total)
