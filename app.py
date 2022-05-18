from asyncio.windows_events import NULL
from sre_constants import SRE_FLAG_IGNORECASE
from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import datetime
import random
import string
import os
#--
from tabulate import tabulate
from numpy.matrixlib.defmatrix import matrix
import numpy as np
import pandas as pd
import math as mt
#---
import proced
from proced import prin
"""
from proced import cambio
from proced import encabezados
from proced import igualdad
from proced import artificial
from proced import add_artif
from proced import add_art_enc
from proced import solucion
"""

global matriz
matriz = []
#global decision
#decision = 0

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    restr = request.form.get("restr", "")
    var = request.form.get("var", "")
    opt = request.form.get("opt", "")
    zx1 = request.form.get("zx1", "")
    zx2 = request.form.get("zx2", "")
    zx3 = request.form.get("zx3", "")
    zx4 = request.form.get("zx4", "")
    zx5 = request.form.get("zx5", "")
    rx11 = request.form.get("rx11", "")
    rx12 = request.form.get("rx12", "")
    rx13 = request.form.get("rx13", "")
    rx14 = request.form.get("rx14", "")
    rx15 = request.form.get("rx15", "")
    rx21 = request.form.get("rx21", "")
    rx22 = request.form.get("rx22", "")
    rx23 = request.form.get("rx23", "")
    rx24 = request.form.get("rx24", "")
    rx25 = request.form.get("rx25", "")
    rx31 = request.form.get("rx31", "")
    rx32 = request.form.get("rx32", "")
    rx33 = request.form.get("rx33", "")
    rx34 = request.form.get("rx34", "")
    rx35 = request.form.get("rx35", "")
    rx41 = request.form.get("rx41", "")
    rx42 = request.form.get("rx42", "")
    rx43 = request.form.get("rx43", "")
    rx44 = request.form.get("rx44", "")
    rx45 = request.form.get("rx45", "")
    rx51 = request.form.get("rx51", "")
    rx52 = request.form.get("rx52", "")
    rx53 = request.form.get("rx53", "")
    rx54 = request.form.get("rx54", "")
    rx55 = request.form.get("rx55", "")
    r1 = [rx11, rx12, rx13, rx14, rx15]
    r2 = [rx21, rx22, rx23, rx24, rx25]
    r3 = [rx31, rx32, rx33, rx34, rx35]
    r4 = [rx41, rx42, rx43, rx44, rx45]
    r5= [rx51, rx52, rx53, rx54, rx55]
    signo1 = request.form.get("signo1", "")
    signo2 = request.form.get("signo2", "")
    signo3 = request.form.get("signo3", "")
    signo4 = request.form.get("signo4", "")
    signo5 = request.form.get("signo5", "")
    res1 = request.form.get("res1", "")
    res2 = request.form.get("res2", "")
    res3 = request.form.get("res3", "")
    res4 = request.form.get("res4", "")
    res5 = request.form.get("res5", "")
    topt = request.form.get("topt", "")
    funcionZ=[]
    signos=[]
    res=[]
    rs1=[]
    rs2=[]
    rs3=[]
    rs4=[]
    rs5=[]
    for i in range(0, len(r1)):
        if r1[i] != '':
            rs1.append(int(r1[i]))
    for i in range(0, len(r2)):
        if r2[i] != '':
            rs2.append(int(r2[i]))
    for i in range(0, len(r3)):
        if r3[i] != '':
            rs3.append(int(r3[i]))
    for i in range(0, len(r4)):
        if r4[i] != '':
            rs4.append(int(r4[i]))
    for i in range(0, len(r5)):
        if r5[i] != '':
            rs5.append(int(r5[i]))
    if zx1 != "":
        funcionZ.append(int(zx1))
    if zx2 != "":
        funcionZ.append(int(zx2))
    if zx3 != "":
        funcionZ.append(int(zx3))
    if zx4 != "":
        funcionZ.append(int(zx4))
    if zx5 != "":
        funcionZ.append(int(zx5))
    if signo1 != "":
        signos.append(int(signo1))
    if signo2 != "":
        signos.append(int(signo2))
    if signo3 != "":
        signos.append(int(signo3))
    if signo4 != "":
        signos.append(int(signo4))
    if signo5 != "":
        signos.append(int(signo5))
    if res1 != "":
        res.append(int(res1))
    if res2 != "":
        res.append(int(res2))
    if res3 != "":
        res.append(int(res3))
    if res4 != "":
        res.append(int(res4))
    if res5 != "":
        res.append(int(res5))

    matriz = np.zeros((len(res)+1, len(funcionZ)+2))
    for i in range(0, len(funcionZ)):
        matriz[-1,i] = funcionZ[i]
    for i in range(0, len(res)):
        matriz[i,-1] = res[i]
    for i in range(0, len(signos)):
        matriz[i,-2] = signos[i]

    if len(rs1)>0:
        for i in range(0, len(rs1)):
            matriz[0,i] = rs1[i]
    if len(rs2)>0:
        for i in range(0, len(rs2)):
            matriz[1,i] = rs2[i]
    if len(rs3)>0:
        for i in range(0, len(rs3)):
            matriz[2,i] = rs3[i]
    if len(rs4)>0:
        for i in range(0, len(rs4)):
            matriz[3,i] = rs4[i]
    if len(rs5)>0:
        for i in range(0, len(rs5)):
            matriz[4,i] = rs5[i]
    print(matriz)

    decision = []
    if topt != "":
        if topt == "1":
            decision = 1
        if topt == "2":
            decision = 2

    np.savetxt('A.txt', matriz, fmt='%d')
    #np.savetxt('B.txt', decision, fmt='%d')
    primal, dual, solprimal, soldual = prin(matriz, decision)
    solprimal = primal[-1,-1]
    soldual = dual[-1,-1]


    print(solprimal)

    template = env.get_template('index.html')
    return template.render(restr=restr, var=var, opt=opt, zx1=zx1, zx2=zx2, zx3=zx3, zx4=zx4, zx5=zx5, 
            rx11=rx11, rx12=rx12, rx13=rx13, rx14=rx14, rx15=rx15, 
            rx21=rx21, rx22=rx22, rx23=rx23, rx24=rx24, rx25=rx25, 
            rx31=rx31, rx32=rx32, rx33=rx33, rx34=rx34, rx35=rx35, 
            rx41=rx41, rx42=rx42, rx43=rx43, rx44=rx44, rx45=rx45, 
            rx51=rx51, rx52=rx52, rx53=rx53, rx54=rx54, rx55=rx55,
            signo1=signo1, signo2=signo2, signo3=signo3, signo4=signo4, signo5=signo5,
            res1=res1, res2=res2, res3=res3, res4=res4, res5=res5,
            topt=topt, soldual=soldual, solprimal=solprimal, primal=primal, dual=dual)

@app.route('/definition')
def result():
    template = env.get_template('definition.html')
    return template.render()


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug = True)