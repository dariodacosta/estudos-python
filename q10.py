#!/usr/bin/env python
# -*- coding: utf-8 -*-

quantidade=int(input('por dia'))
anos=int(input('anos de fumo'))
cigarros=quantidade*(anos*365)
minutos=cigarros*10
vida=(minutos/60)/24

print('vida',vida)