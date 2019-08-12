from django.shortcuts import render

import random


def vw_temp1(request):
    '用模板方式显示一个含照片的 HTML'

    context = {}
    context['var_title'] = 'Hello World! - replaced'
    context['var_img_path'] = '\\static\\images\\helloworld.jpg'

    return render(request, 'temp1.html', context)


def vw_temp2(request):
    '用模板方式显示小学课程表（一）- 单个变量'

    context = {}
    context['var_title'] = '小学课程表（一）- 单个变量'

    all_lessons = ('语文', '数学', '英语', '美术', '思品', '手工', '体育', '科学', '书法',)

    context['var_no'] = '第1节课'
    context['var_lesson11'] = random.choice(all_lessons)
    context['var_lesson21'] = random.choice(all_lessons)
    context['var_lesson31'] = random.choice(all_lessons)
    context['var_lesson41'] = random.choice(all_lessons)
    context['var_lesson51'] = random.choice(all_lessons)

    return render(request, 'temp2.html', context)


def vw_temp3(request):
    '用模板方式显示小学课程表（二）-循环标签-单个变量'

    context = {}
    context['var_title'] = '小学课程表（二）-循环标签-单个变量循环'

    var_numbers = []
    for row in range(1,6):
        var_numbers.append(row)

    context['var_numbers'] = var_numbers

    return render(request, 'temp3.html', context)


def vw_temp4(request):
    '用模板方式显示小学课程表（三）-循环标签-表格-多个变量同时循环'


    all_lessons = ('语文', '数学', '英语', '美术', '思品', '手工', '体育', '科学', '书法',)

    context = {}
    context['var_title'] = '小学课程表（三）-循环标签-表格-多个变量同时循环'

    var_lessons = []
    for row in range(1,7):
        row_data = []
        for col in range(1,3):
            if col == 1:
                row_data.append(row)
            else:
                row_data.append(random.choice(all_lessons))
                row_data.append(random.choice(all_lessons))
                row_data.append(random.choice(all_lessons))
                row_data.append(random.choice(all_lessons))
                row_data.append(random.choice(all_lessons))
            #print(row_data)
        var_lessons.append(row_data)

    context['var_lessons'] = var_lessons

    return render(request, 'temp4.html', context)
