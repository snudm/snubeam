# -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.sentences(u'저는 대학생이구요. 소프트웨어 관련학과 입니다.'))
[저는 대학생이구요., 소프트웨어 관련학과 입니다.]
