#!/usr/bin/env python
# -*- coding: utf-8 -*-

mercadoria1=float(input('preco da mercadoria'))
percentual2=float(input('desconto'))
valordesconto=mercadoria1*(percentual2/100)
novovalor=mercadoria1-valordesconto
print('valor desconto', valordesconto)
print(novovalor)