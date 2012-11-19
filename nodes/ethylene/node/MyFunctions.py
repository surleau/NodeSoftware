# -*- coding: utf-8 -*-
from vamdctap.unitconv import *

######################################################################

#  function rather table->fields for MoleculeChemicalName

def checkChemicalName(restrictable,operator,string):
    value = string.strip('\'"')
    value = value.upper()
    if value in ('C2H4','ETHYLENE','ETHENE') and operator in ('=','=='):
        return Q(pk=F('pk'))
    else:
        return ~Q(pk=F('pk'))

#  function rather table->fields for MoleculeStoichiometricFormula

def checkStoichiometricFormula(restrictable,operator,string):
    value = string.strip('\'"')
    value = value.upper()
    if value == 'C2H4' and operator in ('=','=='):
        return Q(pk=F('pk'))
    else:
        return ~Q(pk=F('pk'))

#  function rather table->fields for EnvironmentTemperature

def checkEnvironmentTemperature(restrictable,operator,string):
    value = string.strip('\'"')
    value = float(value)
    if value == 296. and operator in ('=','==','<=','>='):
        return Q(pk=F('pk'))
    elif value > 296. and operator in ('<','<='):
        return Q(pk=F('pk'))
    elif value < 296. and operator in ('>','>='):
        return Q(pk=F('pk'))
    else:
        return ~Q(pk=F('pk'))

######################################################################

