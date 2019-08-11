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
    s_body += '    <tr>'
    s_body += '        <th>课程</th>'
    s_body += '        <th>练习内容说明</th>'
    s_body += '    </tr>'
    s_body += '    <tr>'
    s_body += '        <td>课程一</td>'
    s_body += '        <td>直接返回一个 HTML 文本（包装成字符串形式）</td>'
    s_body += '    </tr>'
    s_body += '    <tr>'
    s_body += '        <td>课程二</td>'
    s_body += '        <td>分段式返回一个 HTML 文本</td>'
    s_body += '    </tr>'
    s_body += '    <tr>'
    s_body += '        <td>课程三</td>'
    s_body += '        <td>分段式返回一个 HTML 文本 + href 新标签</td>'
    s_body += '    </tr>'
    s_body += '</table>'

    # ----- 学习表格 ▲ ----------------------------------

    s_body_suffix = '</body>\n'
    s_html_suffix = '</html>\n'

    s_total = s0 + s_html_prefix + s_head + s_body_prefix + \
        s_body + s_body_suffix + s_html_suffix

    return HttpResponse("Table ! ")
