
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from djangoProject.scripts import traversal
from ..html import *


def shit_to_int(N):
    for i in range(len(N)):
        for j in range(len(N)):
            if N[i][j] is None:
                N[i][j] = 0
            else:
                N[i][j] = 1
    return N


@csrf_exempt
def routesearcher(request):
    if request.method == 'POST':
        #do shit
        x00 = request.POST.get('x00')
        x01 = request.POST.get('x01')
        print(x01)
        x02 = request.POST.get('x02')
        x03 = request.POST.get('x03')
        x04 = request.POST.get('x04')
        x05 = request.POST.get('x05')
        x06 = request.POST.get('x06')
        x07 = request.POST.get('x07')
        x08 = request.POST.get('x08')
        x09 = request.POST.get('x09')

        x10 = request.POST.get('x10')
        x11 = request.POST.get('x11')
        x12 = request.POST.get('x12')
        x13 = request.POST.get('x13')
        x14 = request.POST.get('x14')
        x15 = request.POST.get('x15')
        x16 = request.POST.get('x16')
        x17 = request.POST.get('x17')
        x18 = request.POST.get('x18')
        x19 = request.POST.get('x19')

        x20 = request.POST.get('x20')
        x21 = request.POST.get('x21')
        x22 = request.POST.get('x22')
        x23 = request.POST.get('x23')
        x24 = request.POST.get('x24')
        x25 = request.POST.get('x25')
        x26 = request.POST.get('x26')
        x27 = request.POST.get('x27')
        x28 = request.POST.get('x28')
        x29 = request.POST.get('x29')

        x30 = request.POST.get('x30')
        x31 = request.POST.get('x31')
        x32 = request.POST.get('x32')
        x33 = request.POST.get('x33')
        x34 = request.POST.get('x34')
        x35 = request.POST.get('x35')
        x36 = request.POST.get('x36')
        x37 = request.POST.get('x37')
        x38 = request.POST.get('x38')
        x39 = request.POST.get('x39')

        x40 = request.POST.get('x40')
        x41 = request.POST.get('x41')
        x42 = request.POST.get('x42')
        x43 = request.POST.get('x43')
        x44 = request.POST.get('x44')
        x45 = request.POST.get('x45')
        x46 = request.POST.get('x46')
        x47 = request.POST.get('x47')
        x48 = request.POST.get('x48')
        x49 = request.POST.get('x49')

        x50 = request.POST.get('x50')
        x51 = request.POST.get('x51')
        x52 = request.POST.get('x52')
        x53 = request.POST.get('x53')
        x54 = request.POST.get('x54')
        x55 = request.POST.get('x55')
        x56 = request.POST.get('x56')
        x57 = request.POST.get('x57')
        x58 = request.POST.get('x58')
        x59 = request.POST.get('x59')

        x60 = request.POST.get('x60')
        x61 = request.POST.get('x61')
        x62 = request.POST.get('x62')
        x63 = request.POST.get('x63')
        x64 = request.POST.get('x64')
        x65 = request.POST.get('x65')
        x66 = request.POST.get('x66')
        x67 = request.POST.get('x67')
        x68 = request.POST.get('x68')
        x69 = request.POST.get('x69')

        x70 = request.POST.get('x70')
        x71 = request.POST.get('x71')
        x72 = request.POST.get('x72')
        x73 = request.POST.get('x73')
        x74 = request.POST.get('x74')
        x75 = request.POST.get('x75')
        x76 = request.POST.get('x76')
        x77 = request.POST.get('x77')
        x78 = request.POST.get('x78')
        x79 = request.POST.get('x79')

        x80 = request.POST.get('x80')
        x81 = request.POST.get('x81')
        x82 = request.POST.get('x82')
        x83 = request.POST.get('x83')
        x84 = request.POST.get('x84')
        x85 = request.POST.get('x85')
        x86 = request.POST.get('x86')
        x87 = request.POST.get('x87')
        x88 = request.POST.get('x88')
        x89 = request.POST.get('x89')

        x90 = request.POST.get('x90')
        x91 = request.POST.get('x91')
        x92 = request.POST.get('x92')
        x93 = request.POST.get('x93')
        x94 = request.POST.get('x94')
        x95 = request.POST.get('x95')
        x96 = request.POST.get('x96')
        x97 = request.POST.get('x97')
        x98 = request.POST.get('x98')
        x99 = request.POST.get('x99')

        N= [
            [x00, x01, x02, x03, x04, x05, x06, x07, x08, x09],
            [x10, x11, x12, x13, x14, x15, x16, x17, x18, x19],
            [x20, x21, x22, x23, x24, x25, x26, x27, x28, x29],
            [x30, x31, x32, x33, x34, x35, x36, x37, x38, x39],
            [x40, x41, x42, x43, x44, x45, x46, x47, x48, x49],
            [x50, x51, x52, x53, x54, x55, x56, x57, x58, x59],
            [x60, x61, x62, x63, x64, x65, x66, x67, x68, x69],
            [x70, x71, x72, x73, x74, x75, x76, x77, x78, x79],
            [x80, x81, x82, x83, x84, x85, x86, x87, x88, x89],
            [x90, x91, x92, x93, x94, x95, x96, x97, x98, x99],
        ]
        a=int(request.POST.get('a_node'))
        b=int(request.POST.get('b_node'))
        N=shit_to_int(N)
        path=traversal.traversal_wrapper(N, a, b)
        pathlol=""
        if path is not False:
            for i in range(len(path)):
                pathlol += str(path[i]) + " "
        else:
            pathlol = "Пути нет"
        #pathlol="0 1 "
        print(pathlol)
        #return HttpResponse(path)
        return render(request, 'mainpage.html', {'pathlol': pathlol})
    else:
        return render(request, 'mainpage.html')