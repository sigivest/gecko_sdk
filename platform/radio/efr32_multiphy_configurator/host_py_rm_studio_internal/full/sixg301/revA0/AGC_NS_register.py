
# -*- coding: utf-8 -*-

from . static import Base_RM_Register
from . AGC_NS_field import *


class RM_Register_AGC_NS_IPVERSION(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_IPVERSION, self).__init__(rmio, label,
            0xb020c000, 0x000,
            'IPVERSION', 'AGC_NS.IPVERSION', 'read-only',
            u"",
            0x00000006, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.IPVERSION = RM_Field_AGC_NS_IPVERSION_IPVERSION(self)
        self.zz_fdict['IPVERSION'] = self.IPVERSION
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_EN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_EN, self).__init__(rmio, label,
            0xb020c000, 0x004,
            'EN', 'AGC_NS.EN', 'read-write',
            u"",
            0x00000000, 0x00000001,
            0x00001000, 0x00002000,
            0x00003000)

        self.EN = RM_Field_AGC_NS_EN_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_STATUS0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_STATUS0, self).__init__(rmio, label,
            0xb020c000, 0x008,
            'STATUS0', 'AGC_NS.STATUS0', 'read-only',
            u"",
            0x00000000, 0x07FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.GAININDEX = RM_Field_AGC_NS_STATUS0_GAININDEX(self)
        self.zz_fdict['GAININDEX'] = self.GAININDEX
        self.RFPKDLOWLAT = RM_Field_AGC_NS_STATUS0_RFPKDLOWLAT(self)
        self.zz_fdict['RFPKDLOWLAT'] = self.RFPKDLOWLAT
        self.RFPKDHILAT = RM_Field_AGC_NS_STATUS0_RFPKDHILAT(self)
        self.zz_fdict['RFPKDHILAT'] = self.RFPKDHILAT
        self.IFPKDLOLAT = RM_Field_AGC_NS_STATUS0_IFPKDLOLAT(self)
        self.zz_fdict['IFPKDLOLAT'] = self.IFPKDLOLAT
        self.IFPKDHILAT = RM_Field_AGC_NS_STATUS0_IFPKDHILAT(self)
        self.zz_fdict['IFPKDHILAT'] = self.IFPKDHILAT
        self.CCA = RM_Field_AGC_NS_STATUS0_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.GAINOK = RM_Field_AGC_NS_STATUS0_GAINOK(self)
        self.zz_fdict['GAINOK'] = self.GAINOK
        self.PGAINDEX = RM_Field_AGC_NS_STATUS0_PGAINDEX(self)
        self.zz_fdict['PGAINDEX'] = self.PGAINDEX
        self.LNAINDEX = RM_Field_AGC_NS_STATUS0_LNAINDEX(self)
        self.zz_fdict['LNAINDEX'] = self.LNAINDEX
        self.PNINDEX = RM_Field_AGC_NS_STATUS0_PNINDEX(self)
        self.zz_fdict['PNINDEX'] = self.PNINDEX
        self.ADCINDEX = RM_Field_AGC_NS_STATUS0_ADCINDEX(self)
        self.zz_fdict['ADCINDEX'] = self.ADCINDEX
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_STATUS1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_STATUS1, self).__init__(rmio, label,
            0xb020c000, 0x00C,
            'STATUS1', 'AGC_NS.STATUS1', 'read-only',
            u"",
            0x00000000, 0x3FFFFEFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CHPWR = RM_Field_AGC_NS_STATUS1_CHPWR(self)
        self.zz_fdict['CHPWR'] = self.CHPWR
        self.FASTLOOPSTATE = RM_Field_AGC_NS_STATUS1_FASTLOOPSTATE(self)
        self.zz_fdict['FASTLOOPSTATE'] = self.FASTLOOPSTATE
        self.CFLOOPSTATE = RM_Field_AGC_NS_STATUS1_CFLOOPSTATE(self)
        self.zz_fdict['CFLOOPSTATE'] = self.CFLOOPSTATE
        self.RSSISTATE = RM_Field_AGC_NS_STATUS1_RSSISTATE(self)
        self.zz_fdict['RSSISTATE'] = self.RSSISTATE
        self.RFPKDLOWLATCNT = RM_Field_AGC_NS_STATUS1_RFPKDLOWLATCNT(self)
        self.zz_fdict['RFPKDLOWLATCNT'] = self.RFPKDLOWLATCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_STATUS2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_STATUS2, self).__init__(rmio, label,
            0xb020c000, 0x010,
            'STATUS2', 'AGC_NS.STATUS2', 'read-only',
            u"",
            0x00000000, 0xFFFF4FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RFPKDHILATCNT = RM_Field_AGC_NS_STATUS2_RFPKDHILATCNT(self)
        self.zz_fdict['RFPKDHILATCNT'] = self.RFPKDHILATCNT
        self.PNDWNUP = RM_Field_AGC_NS_STATUS2_PNDWNUP(self)
        self.zz_fdict['PNDWNUP'] = self.PNDWNUP
        self.RFPKDPRDCNT = RM_Field_AGC_NS_STATUS2_RFPKDPRDCNT(self)
        self.zz_fdict['RFPKDPRDCNT'] = self.RFPKDPRDCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_RSSI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_RSSI, self).__init__(rmio, label,
            0xb020c000, 0x018,
            'RSSI', 'AGC_NS.RSSI', 'read-only',
            u"",
            0x00008000, 0x0000FFC0,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIFRAC = RM_Field_AGC_NS_RSSI_RSSIFRAC(self)
        self.zz_fdict['RSSIFRAC'] = self.RSSIFRAC
        self.RSSIINT = RM_Field_AGC_NS_RSSI_RSSIINT(self)
        self.zz_fdict['RSSIINT'] = self.RSSIINT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_FRAMERSSI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_FRAMERSSI, self).__init__(rmio, label,
            0xb020c000, 0x01C,
            'FRAMERSSI', 'AGC_NS.FRAMERSSI', 'read-only',
            u"",
            0x00008000, 0x0000FFC0,
            0x00001000, 0x00002000,
            0x00003000)

        self.FRAMERSSIFRAC = RM_Field_AGC_NS_FRAMERSSI_FRAMERSSIFRAC(self)
        self.zz_fdict['FRAMERSSIFRAC'] = self.FRAMERSSIFRAC
        self.FRAMERSSIINT = RM_Field_AGC_NS_FRAMERSSI_FRAMERSSIINT(self)
        self.zz_fdict['FRAMERSSIINT'] = self.FRAMERSSIINT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL0, self).__init__(rmio, label,
            0xb020c000, 0x020,
            'CTRL0', 'AGC_NS.CTRL0', 'read-write',
            u"",
            0x2132727F, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PWRTARGET = RM_Field_AGC_NS_CTRL0_PWRTARGET(self)
        self.zz_fdict['PWRTARGET'] = self.PWRTARGET
        self.MODE = RM_Field_AGC_NS_CTRL0_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RSSISHIFT = RM_Field_AGC_NS_CTRL0_RSSISHIFT(self)
        self.zz_fdict['RSSISHIFT'] = self.RSSISHIFT
        self.DISCFLOOPADJ = RM_Field_AGC_NS_CTRL0_DISCFLOOPADJ(self)
        self.zz_fdict['DISCFLOOPADJ'] = self.DISCFLOOPADJ
        self.CFLOOPNFADJ = RM_Field_AGC_NS_CTRL0_CFLOOPNFADJ(self)
        self.zz_fdict['CFLOOPNFADJ'] = self.CFLOOPNFADJ
        self.CFLOOPNEWCALC = RM_Field_AGC_NS_CTRL0_CFLOOPNEWCALC(self)
        self.zz_fdict['CFLOOPNEWCALC'] = self.CFLOOPNEWCALC
        self.DISRESETCHPWR = RM_Field_AGC_NS_CTRL0_DISRESETCHPWR(self)
        self.zz_fdict['DISRESETCHPWR'] = self.DISRESETCHPWR
        self.ADCATTENMODE = RM_Field_AGC_NS_CTRL0_ADCATTENMODE(self)
        self.zz_fdict['ADCATTENMODE'] = self.ADCATTENMODE
        self.INRXRSTEN = RM_Field_AGC_NS_CTRL0_INRXRSTEN(self)
        self.zz_fdict['INRXRSTEN'] = self.INRXRSTEN
        self.ADCATTENCODE = RM_Field_AGC_NS_CTRL0_ADCATTENCODE(self)
        self.zz_fdict['ADCATTENCODE'] = self.ADCATTENCODE
        self.ENRSSIRESET = RM_Field_AGC_NS_CTRL0_ENRSSIRESET(self)
        self.zz_fdict['ENRSSIRESET'] = self.ENRSSIRESET
        self.DSADISCFLOOP = RM_Field_AGC_NS_CTRL0_DSADISCFLOOP(self)
        self.zz_fdict['DSADISCFLOOP'] = self.DSADISCFLOOP
        self.DISPNGAINUP = RM_Field_AGC_NS_CTRL0_DISPNGAINUP(self)
        self.zz_fdict['DISPNGAINUP'] = self.DISPNGAINUP
        self.DISPNDWNCOMP = RM_Field_AGC_NS_CTRL0_DISPNDWNCOMP(self)
        self.zz_fdict['DISPNDWNCOMP'] = self.DISPNDWNCOMP
        self.AGCRST = RM_Field_AGC_NS_CTRL0_AGCRST(self)
        self.zz_fdict['AGCRST'] = self.AGCRST
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL1, self).__init__(rmio, label,
            0xb020c000, 0x024,
            'CTRL1', 'AGC_NS.CTRL1', 'read-write',
            u"",
            0x04001300, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CCATHRSH = RM_Field_AGC_NS_CTRL1_CCATHRSH(self)
        self.zz_fdict['CCATHRSH'] = self.CCATHRSH
        self.RSSIPERIOD = RM_Field_AGC_NS_CTRL1_RSSIPERIOD(self)
        self.zz_fdict['RSSIPERIOD'] = self.RSSIPERIOD
        self.PWRPERIOD = RM_Field_AGC_NS_CTRL1_PWRPERIOD(self)
        self.zz_fdict['PWRPERIOD'] = self.PWRPERIOD
        self.CCAMODE = RM_Field_AGC_NS_CTRL1_CCAMODE(self)
        self.zz_fdict['CCAMODE'] = self.CCAMODE
        self.CCAMODE3LOGIC = RM_Field_AGC_NS_CTRL1_CCAMODE3LOGIC(self)
        self.zz_fdict['CCAMODE3LOGIC'] = self.CCAMODE3LOGIC
        self.CCASWCTRL = RM_Field_AGC_NS_CTRL1_CCASWCTRL(self)
        self.zz_fdict['CCASWCTRL'] = self.CCASWCTRL
        self.DISRSTONPREDET = RM_Field_AGC_NS_CTRL1_DISRSTONPREDET(self)
        self.zz_fdict['DISRSTONPREDET'] = self.DISRSTONPREDET
        self.CFLOOPINCREQMODE = RM_Field_AGC_NS_CTRL1_CFLOOPINCREQMODE(self)
        self.zz_fdict['CFLOOPINCREQMODE'] = self.CFLOOPINCREQMODE
        self.ENRSSIINITGAINCHG = RM_Field_AGC_NS_CTRL1_ENRSSIINITGAINCHG(self)
        self.zz_fdict['ENRSSIINITGAINCHG'] = self.ENRSSIINITGAINCHG
        self.DISPWRERRCOMP = RM_Field_AGC_NS_CTRL1_DISPWRERRCOMP(self)
        self.zz_fdict['DISPWRERRCOMP'] = self.DISPWRERRCOMP
        self.ENAGCRSTALL = RM_Field_AGC_NS_CTRL1_ENAGCRSTALL(self)
        self.zz_fdict['ENAGCRSTALL'] = self.ENAGCRSTALL
        self.RSSIVALIDMODE = RM_Field_AGC_NS_CTRL1_RSSIVALIDMODE(self)
        self.zz_fdict['RSSIVALIDMODE'] = self.RSSIVALIDMODE
        self.RSSIINITGAINSTEPTHR = RM_Field_AGC_NS_CTRL1_RSSIINITGAINSTEPTHR(self)
        self.zz_fdict['RSSIINITGAINSTEPTHR'] = self.RSSIINITGAINSTEPTHR
        self.INRXRSSIGATING = RM_Field_AGC_NS_CTRL1_INRXRSSIGATING(self)
        self.zz_fdict['INRXRSSIGATING'] = self.INRXRSSIGATING
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL2, self).__init__(rmio, label,
            0xb020c000, 0x028,
            'CTRL2', 'AGC_NS.CTRL2', 'read-write',
            u"",
            0x0000610A, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DMASEL = RM_Field_AGC_NS_CTRL2_DMASEL(self)
        self.zz_fdict['DMASEL'] = self.DMASEL
        self.SAFEMODE = RM_Field_AGC_NS_CTRL2_SAFEMODE(self)
        self.zz_fdict['SAFEMODE'] = self.SAFEMODE
        self.SAFEMODETHD = RM_Field_AGC_NS_CTRL2_SAFEMODETHD(self)
        self.zz_fdict['SAFEMODETHD'] = self.SAFEMODETHD
        self.REHICNTTHD = RM_Field_AGC_NS_CTRL2_REHICNTTHD(self)
        self.zz_fdict['REHICNTTHD'] = self.REHICNTTHD
        self.RELOTHD = RM_Field_AGC_NS_CTRL2_RELOTHD(self)
        self.zz_fdict['RELOTHD'] = self.RELOTHD
        self.RELBYCHPWR = RM_Field_AGC_NS_CTRL2_RELBYCHPWR(self)
        self.zz_fdict['RELBYCHPWR'] = self.RELBYCHPWR
        self.RELTARGETPWR = RM_Field_AGC_NS_CTRL2_RELTARGETPWR(self)
        self.zz_fdict['RELTARGETPWR'] = self.RELTARGETPWR
        self.RSSICCASUB = RM_Field_AGC_NS_CTRL2_RSSICCASUB(self)
        self.zz_fdict['RSSICCASUB'] = self.RSSICCASUB
        self.DEBCNTRST = RM_Field_AGC_NS_CTRL2_DEBCNTRST(self)
        self.zz_fdict['DEBCNTRST'] = self.DEBCNTRST
        self.PRSDEBUGEN = RM_Field_AGC_NS_CTRL2_PRSDEBUGEN(self)
        self.zz_fdict['PRSDEBUGEN'] = self.PRSDEBUGEN
        self.DISRFPKD = RM_Field_AGC_NS_CTRL2_DISRFPKD(self)
        self.zz_fdict['DISRFPKD'] = self.DISRFPKD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL3, self).__init__(rmio, label,
            0xb020c000, 0x02C,
            'CTRL3', 'AGC_NS.CTRL3', 'read-write',
            u"",
            0x5140A800, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.IFPKDDEB = RM_Field_AGC_NS_CTRL3_IFPKDDEB(self)
        self.zz_fdict['IFPKDDEB'] = self.IFPKDDEB
        self.IFPKDDEBTHD = RM_Field_AGC_NS_CTRL3_IFPKDDEBTHD(self)
        self.zz_fdict['IFPKDDEBTHD'] = self.IFPKDDEBTHD
        self.IFPKDDEBPRD = RM_Field_AGC_NS_CTRL3_IFPKDDEBPRD(self)
        self.zz_fdict['IFPKDDEBPRD'] = self.IFPKDDEBPRD
        self.IFPKDDEBRST = RM_Field_AGC_NS_CTRL3_IFPKDDEBRST(self)
        self.zz_fdict['IFPKDDEBRST'] = self.IFPKDDEBRST
        self.RFPKDDEB = RM_Field_AGC_NS_CTRL3_RFPKDDEB(self)
        self.zz_fdict['RFPKDDEB'] = self.RFPKDDEB
        self.RFPKDDEBTHD = RM_Field_AGC_NS_CTRL3_RFPKDDEBTHD(self)
        self.zz_fdict['RFPKDDEBTHD'] = self.RFPKDDEBTHD
        self.RFPKDDEBPRD = RM_Field_AGC_NS_CTRL3_RFPKDDEBPRD(self)
        self.zz_fdict['RFPKDDEBPRD'] = self.RFPKDDEBPRD
        self.RFPKDDEBRST = RM_Field_AGC_NS_CTRL3_RFPKDDEBRST(self)
        self.zz_fdict['RFPKDDEBRST'] = self.RFPKDDEBRST
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL4, self).__init__(rmio, label,
            0xb020c000, 0x030,
            'CTRL4', 'AGC_NS.CTRL4', 'read-write',
            u"",
            0x0000000E, 0xBF80FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PERIODRFPKD = RM_Field_AGC_NS_CTRL4_PERIODRFPKD(self)
        self.zz_fdict['PERIODRFPKD'] = self.PERIODRFPKD
        self.DISRFPKDCNTRST = RM_Field_AGC_NS_CTRL4_DISRFPKDCNTRST(self)
        self.zz_fdict['DISRFPKDCNTRST'] = self.DISRFPKDCNTRST
        self.DISRSTCONDI = RM_Field_AGC_NS_CTRL4_DISRSTCONDI(self)
        self.zz_fdict['DISRSTCONDI'] = self.DISRSTCONDI
        self.RFPKDPRDGEAR = RM_Field_AGC_NS_CTRL4_RFPKDPRDGEAR(self)
        self.zz_fdict['RFPKDPRDGEAR'] = self.RFPKDPRDGEAR
        self.RFPKDSYNCSEL = RM_Field_AGC_NS_CTRL4_RFPKDSYNCSEL(self)
        self.zz_fdict['RFPKDSYNCSEL'] = self.RFPKDSYNCSEL
        self.RFPKDSEL = RM_Field_AGC_NS_CTRL4_RFPKDSEL(self)
        self.zz_fdict['RFPKDSEL'] = self.RFPKDSEL
        self.RFPKDCNTEN = RM_Field_AGC_NS_CTRL4_RFPKDCNTEN(self)
        self.zz_fdict['RFPKDCNTEN'] = self.RFPKDCNTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL5, self).__init__(rmio, label,
            0xb020c000, 0x034,
            'CTRL5', 'AGC_NS.CTRL5', 'read-write',
            u"",
            0x00000000, 0xC0FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PNUPDISTHD = RM_Field_AGC_NS_CTRL5_PNUPDISTHD(self)
        self.zz_fdict['PNUPDISTHD'] = self.PNUPDISTHD
        self.PNUPRELTHD = RM_Field_AGC_NS_CTRL5_PNUPRELTHD(self)
        self.zz_fdict['PNUPRELTHD'] = self.PNUPRELTHD
        self.SEQPNUPALLOW = RM_Field_AGC_NS_CTRL5_SEQPNUPALLOW(self)
        self.zz_fdict['SEQPNUPALLOW'] = self.SEQPNUPALLOW
        self.SEQRFPKDEN = RM_Field_AGC_NS_CTRL5_SEQRFPKDEN(self)
        self.zz_fdict['SEQRFPKDEN'] = self.SEQRFPKDEN
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL6, self).__init__(rmio, label,
            0xb020c000, 0x038,
            'CTRL6', 'AGC_NS.CTRL6', 'read-write',
            u"",
            0x0003AAA8, 0x7FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DUALRFPKDDEC = RM_Field_AGC_NS_CTRL6_DUALRFPKDDEC(self)
        self.zz_fdict['DUALRFPKDDEC'] = self.DUALRFPKDDEC
        self.ENDUALRFPKD = RM_Field_AGC_NS_CTRL6_ENDUALRFPKD(self)
        self.zz_fdict['ENDUALRFPKD'] = self.ENDUALRFPKD
        self.GAINDETTHD = RM_Field_AGC_NS_CTRL6_GAINDETTHD(self)
        self.zz_fdict['GAINDETTHD'] = self.GAINDETTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL7, self).__init__(rmio, label,
            0xb020c000, 0x03C,
            'CTRL7', 'AGC_NS.CTRL7', 'read-write',
            u"",
            0x00000000, 0x01FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SUBDEN = RM_Field_AGC_NS_CTRL7_SUBDEN(self)
        self.zz_fdict['SUBDEN'] = self.SUBDEN
        self.SUBINT = RM_Field_AGC_NS_CTRL7_SUBINT(self)
        self.zz_fdict['SUBINT'] = self.SUBINT
        self.SUBNUM = RM_Field_AGC_NS_CTRL7_SUBNUM(self)
        self.zz_fdict['SUBNUM'] = self.SUBNUM
        self.SUBPERIOD = RM_Field_AGC_NS_CTRL7_SUBPERIOD(self)
        self.zz_fdict['SUBPERIOD'] = self.SUBPERIOD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_RSSISTEPTHR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_RSSISTEPTHR, self).__init__(rmio, label,
            0xb020c000, 0x040,
            'RSSISTEPTHR', 'AGC_NS.RSSISTEPTHR', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.POSSTEPTHR = RM_Field_AGC_NS_RSSISTEPTHR_POSSTEPTHR(self)
        self.zz_fdict['POSSTEPTHR'] = self.POSSTEPTHR
        self.NEGSTEPTHR = RM_Field_AGC_NS_RSSISTEPTHR_NEGSTEPTHR(self)
        self.zz_fdict['NEGSTEPTHR'] = self.NEGSTEPTHR
        self.STEPPER = RM_Field_AGC_NS_RSSISTEPTHR_STEPPER(self)
        self.zz_fdict['STEPPER'] = self.STEPPER
        self.DEMODRESTARTPER = RM_Field_AGC_NS_RSSISTEPTHR_DEMODRESTARTPER(self)
        self.zz_fdict['DEMODRESTARTPER'] = self.DEMODRESTARTPER
        self.DEMODRESTARTTHR = RM_Field_AGC_NS_RSSISTEPTHR_DEMODRESTARTTHR(self)
        self.zz_fdict['DEMODRESTARTTHR'] = self.DEMODRESTARTTHR
        self.RSSIFAST = RM_Field_AGC_NS_RSSISTEPTHR_RSSIFAST(self)
        self.zz_fdict['RSSIFAST'] = self.RSSIFAST
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_MANGAIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_MANGAIN, self).__init__(rmio, label,
            0xb020c000, 0x044,
            'MANGAIN', 'AGC_NS.MANGAIN', 'read-write',
            u"",
            0x00000000, 0x0001FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.MANGAINEN = RM_Field_AGC_NS_MANGAIN_MANGAINEN(self)
        self.zz_fdict['MANGAINEN'] = self.MANGAINEN
        self.MANGAINIFPGA = RM_Field_AGC_NS_MANGAIN_MANGAINIFPGA(self)
        self.zz_fdict['MANGAINIFPGA'] = self.MANGAINIFPGA
        self.MANGAINLNA = RM_Field_AGC_NS_MANGAIN_MANGAINLNA(self)
        self.zz_fdict['MANGAINLNA'] = self.MANGAINLNA
        self.MANGAINPN = RM_Field_AGC_NS_MANGAIN_MANGAINPN(self)
        self.zz_fdict['MANGAINPN'] = self.MANGAINPN
        self.MANRFLATRST = RM_Field_AGC_NS_MANGAIN_MANRFLATRST(self)
        self.zz_fdict['MANRFLATRST'] = self.MANRFLATRST
        self.MANIFLOLATRST = RM_Field_AGC_NS_MANGAIN_MANIFLOLATRST(self)
        self.zz_fdict['MANIFLOLATRST'] = self.MANIFLOLATRST
        self.MANIFHILATRST = RM_Field_AGC_NS_MANGAIN_MANIFHILATRST(self)
        self.zz_fdict['MANIFHILATRST'] = self.MANIFHILATRST
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_IF, self).__init__(rmio, label,
            0xb020c000, 0x048,
            'IF', 'AGC_NS.IF', 'read-write',
            u"",
            0x00000000, 0x0003FF7D,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIVALID = RM_Field_AGC_NS_IF_RSSIVALID(self)
        self.zz_fdict['RSSIVALID'] = self.RSSIVALID
        self.CCA = RM_Field_AGC_NS_IF_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.RSSIPOSSTEP = RM_Field_AGC_NS_IF_RSSIPOSSTEP(self)
        self.zz_fdict['RSSIPOSSTEP'] = self.RSSIPOSSTEP
        self.RSSINEGSTEP = RM_Field_AGC_NS_IF_RSSINEGSTEP(self)
        self.zz_fdict['RSSINEGSTEP'] = self.RSSINEGSTEP
        self.RSSIDONE = RM_Field_AGC_NS_IF_RSSIDONE(self)
        self.zz_fdict['RSSIDONE'] = self.RSSIDONE
        self.SHORTRSSIPOSSTEP = RM_Field_AGC_NS_IF_SHORTRSSIPOSSTEP(self)
        self.zz_fdict['SHORTRSSIPOSSTEP'] = self.SHORTRSSIPOSSTEP
        self.RFPKDPRDDONE = RM_Field_AGC_NS_IF_RFPKDPRDDONE(self)
        self.zz_fdict['RFPKDPRDDONE'] = self.RFPKDPRDDONE
        self.RFPKDCNTDONE = RM_Field_AGC_NS_IF_RFPKDCNTDONE(self)
        self.zz_fdict['RFPKDCNTDONE'] = self.RFPKDCNTDONE
        self.RSSIHIGH = RM_Field_AGC_NS_IF_RSSIHIGH(self)
        self.zz_fdict['RSSIHIGH'] = self.RSSIHIGH
        self.RSSILOW = RM_Field_AGC_NS_IF_RSSILOW(self)
        self.zz_fdict['RSSILOW'] = self.RSSILOW
        self.CCANODET = RM_Field_AGC_NS_IF_CCANODET(self)
        self.zz_fdict['CCANODET'] = self.CCANODET
        self.GAINBELOWGAINTHD = RM_Field_AGC_NS_IF_GAINBELOWGAINTHD(self)
        self.zz_fdict['GAINBELOWGAINTHD'] = self.GAINBELOWGAINTHD
        self.GAINUPDATEFRZ = RM_Field_AGC_NS_IF_GAINUPDATEFRZ(self)
        self.zz_fdict['GAINUPDATEFRZ'] = self.GAINUPDATEFRZ
        self.PNATTEN = RM_Field_AGC_NS_IF_PNATTEN(self)
        self.zz_fdict['PNATTEN'] = self.PNATTEN
        self.COLLDETRSSIMAPRE = RM_Field_AGC_NS_IF_COLLDETRSSIMAPRE(self)
        self.zz_fdict['COLLDETRSSIMAPRE'] = self.COLLDETRSSIMAPRE
        self.COLLDETRSSIMASYNC = RM_Field_AGC_NS_IF_COLLDETRSSIMASYNC(self)
        self.zz_fdict['COLLDETRSSIMASYNC'] = self.COLLDETRSSIMASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_IEN, self).__init__(rmio, label,
            0xb020c000, 0x04C,
            'IEN', 'AGC_NS.IEN', 'read-write',
            u"",
            0x00000000, 0x0003FF7D,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIVALID = RM_Field_AGC_NS_IEN_RSSIVALID(self)
        self.zz_fdict['RSSIVALID'] = self.RSSIVALID
        self.CCA = RM_Field_AGC_NS_IEN_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.RSSIPOSSTEP = RM_Field_AGC_NS_IEN_RSSIPOSSTEP(self)
        self.zz_fdict['RSSIPOSSTEP'] = self.RSSIPOSSTEP
        self.RSSINEGSTEP = RM_Field_AGC_NS_IEN_RSSINEGSTEP(self)
        self.zz_fdict['RSSINEGSTEP'] = self.RSSINEGSTEP
        self.RSSIDONE = RM_Field_AGC_NS_IEN_RSSIDONE(self)
        self.zz_fdict['RSSIDONE'] = self.RSSIDONE
        self.SHORTRSSIPOSSTEP = RM_Field_AGC_NS_IEN_SHORTRSSIPOSSTEP(self)
        self.zz_fdict['SHORTRSSIPOSSTEP'] = self.SHORTRSSIPOSSTEP
        self.RFPKDPRDDONE = RM_Field_AGC_NS_IEN_RFPKDPRDDONE(self)
        self.zz_fdict['RFPKDPRDDONE'] = self.RFPKDPRDDONE
        self.RFPKDCNTDONE = RM_Field_AGC_NS_IEN_RFPKDCNTDONE(self)
        self.zz_fdict['RFPKDCNTDONE'] = self.RFPKDCNTDONE
        self.RSSIHIGH = RM_Field_AGC_NS_IEN_RSSIHIGH(self)
        self.zz_fdict['RSSIHIGH'] = self.RSSIHIGH
        self.RSSILOW = RM_Field_AGC_NS_IEN_RSSILOW(self)
        self.zz_fdict['RSSILOW'] = self.RSSILOW
        self.CCANODET = RM_Field_AGC_NS_IEN_CCANODET(self)
        self.zz_fdict['CCANODET'] = self.CCANODET
        self.GAINBELOWGAINTHD = RM_Field_AGC_NS_IEN_GAINBELOWGAINTHD(self)
        self.zz_fdict['GAINBELOWGAINTHD'] = self.GAINBELOWGAINTHD
        self.GAINUPDATEFRZ = RM_Field_AGC_NS_IEN_GAINUPDATEFRZ(self)
        self.zz_fdict['GAINUPDATEFRZ'] = self.GAINUPDATEFRZ
        self.PNATTEN = RM_Field_AGC_NS_IEN_PNATTEN(self)
        self.zz_fdict['PNATTEN'] = self.PNATTEN
        self.COLLDETRSSIMAPRE = RM_Field_AGC_NS_IEN_COLLDETRSSIMAPRE(self)
        self.zz_fdict['COLLDETRSSIMAPRE'] = self.COLLDETRSSIMAPRE
        self.COLLDETRSSIMASYNC = RM_Field_AGC_NS_IEN_COLLDETRSSIMASYNC(self)
        self.zz_fdict['COLLDETRSSIMASYNC'] = self.COLLDETRSSIMASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CMD, self).__init__(rmio, label,
            0xb020c000, 0x050,
            'CMD', 'AGC_NS.CMD', 'write-only',
            u"",
            0x00000000, 0x00000001,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSISTART = RM_Field_AGC_NS_CMD_RSSISTART(self)
        self.zz_fdict['RSSISTART'] = self.RSSISTART
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_GAINRANGE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_GAINRANGE, self).__init__(rmio, label,
            0xb020c000, 0x054,
            'GAINRANGE', 'AGC_NS.GAINRANGE', 'read-write',
            u"",
            0x00813187, 0x7FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAINDEXBORDER = RM_Field_AGC_NS_GAINRANGE_LNAINDEXBORDER(self)
        self.zz_fdict['LNAINDEXBORDER'] = self.LNAINDEXBORDER
        self.PGAINDEXBORDER = RM_Field_AGC_NS_GAINRANGE_PGAINDEXBORDER(self)
        self.zz_fdict['PGAINDEXBORDER'] = self.PGAINDEXBORDER
        self.GAININCSTEP = RM_Field_AGC_NS_GAINRANGE_GAININCSTEP(self)
        self.zz_fdict['GAININCSTEP'] = self.GAININCSTEP
        self.PNGAINSTEP = RM_Field_AGC_NS_GAINRANGE_PNGAINSTEP(self)
        self.zz_fdict['PNGAINSTEP'] = self.PNGAINSTEP
        self.LATCHEDHISTEP = RM_Field_AGC_NS_GAINRANGE_LATCHEDHISTEP(self)
        self.zz_fdict['LATCHEDHISTEP'] = self.LATCHEDHISTEP
        self.HIPWRTHD = RM_Field_AGC_NS_GAINRANGE_HIPWRTHD(self)
        self.zz_fdict['HIPWRTHD'] = self.HIPWRTHD
        self.PNINDEXBORDER = RM_Field_AGC_NS_GAINRANGE_PNINDEXBORDER(self)
        self.zz_fdict['PNINDEXBORDER'] = self.PNINDEXBORDER
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_AGCPERIOD0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_AGCPERIOD0, self).__init__(rmio, label,
            0xb020c000, 0x058,
            'AGCPERIOD0', 'AGC_NS.AGCPERIOD0', 'read-write',
            u"",
            0xD607020E, 0xFFFF03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PERIODHI = RM_Field_AGC_NS_AGCPERIOD0_PERIODHI(self)
        self.zz_fdict['PERIODHI'] = self.PERIODHI
        self.PERIODHISTL = RM_Field_AGC_NS_AGCPERIOD0_PERIODHISTL(self)
        self.zz_fdict['PERIODHISTL'] = self.PERIODHISTL
        self.MAXHICNTTHD = RM_Field_AGC_NS_AGCPERIOD0_MAXHICNTTHD(self)
        self.zz_fdict['MAXHICNTTHD'] = self.MAXHICNTTHD
        self.SETTLETIMEIF = RM_Field_AGC_NS_AGCPERIOD0_SETTLETIMEIF(self)
        self.zz_fdict['SETTLETIMEIF'] = self.SETTLETIMEIF
        self.SETTLETIMERF = RM_Field_AGC_NS_AGCPERIOD0_SETTLETIMERF(self)
        self.zz_fdict['SETTLETIMERF'] = self.SETTLETIMERF
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_AGCPERIOD1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_AGCPERIOD1, self).__init__(rmio, label,
            0xb020c000, 0x05C,
            'AGCPERIOD1', 'AGC_NS.AGCPERIOD1', 'read-write',
            u"",
            0x00000037, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PERIODLOW = RM_Field_AGC_NS_AGCPERIOD1_PERIODLOW(self)
        self.zz_fdict['PERIODLOW'] = self.PERIODLOW
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_HICNTREGION0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_HICNTREGION0, self).__init__(rmio, label,
            0xb020c000, 0x060,
            'HICNTREGION0', 'AGC_NS.HICNTREGION0', 'read-write',
            u"",
            0x06050403, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.HICNTREGION0 = RM_Field_AGC_NS_HICNTREGION0_HICNTREGION0(self)
        self.zz_fdict['HICNTREGION0'] = self.HICNTREGION0
        self.HICNTREGION1 = RM_Field_AGC_NS_HICNTREGION0_HICNTREGION1(self)
        self.zz_fdict['HICNTREGION1'] = self.HICNTREGION1
        self.HICNTREGION2 = RM_Field_AGC_NS_HICNTREGION0_HICNTREGION2(self)
        self.zz_fdict['HICNTREGION2'] = self.HICNTREGION2
        self.HICNTREGION3 = RM_Field_AGC_NS_HICNTREGION0_HICNTREGION3(self)
        self.zz_fdict['HICNTREGION3'] = self.HICNTREGION3
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_HICNTREGION1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_HICNTREGION1, self).__init__(rmio, label,
            0xb020c000, 0x064,
            'HICNTREGION1', 'AGC_NS.HICNTREGION1', 'read-write',
            u"",
            0x00000008, 0x000000FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.HICNTREGION4 = RM_Field_AGC_NS_HICNTREGION1_HICNTREGION4(self)
        self.zz_fdict['HICNTREGION4'] = self.HICNTREGION4
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_STEPDWN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_STEPDWN, self).__init__(rmio, label,
            0xb020c000, 0x068,
            'STEPDWN', 'AGC_NS.STEPDWN', 'read-write',
            u"",
            0x00036D10, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.STEPDWN0 = RM_Field_AGC_NS_STEPDWN_STEPDWN0(self)
        self.zz_fdict['STEPDWN0'] = self.STEPDWN0
        self.STEPDWN1 = RM_Field_AGC_NS_STEPDWN_STEPDWN1(self)
        self.zz_fdict['STEPDWN1'] = self.STEPDWN1
        self.STEPDWN2 = RM_Field_AGC_NS_STEPDWN_STEPDWN2(self)
        self.zz_fdict['STEPDWN2'] = self.STEPDWN2
        self.STEPDWN3 = RM_Field_AGC_NS_STEPDWN_STEPDWN3(self)
        self.zz_fdict['STEPDWN3'] = self.STEPDWN3
        self.STEPDWN4 = RM_Field_AGC_NS_STEPDWN_STEPDWN4(self)
        self.zz_fdict['STEPDWN4'] = self.STEPDWN4
        self.STEPDWN5 = RM_Field_AGC_NS_STEPDWN_STEPDWN5(self)
        self.zz_fdict['STEPDWN5'] = self.STEPDWN5
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_GAINSTEPLIM0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_GAINSTEPLIM0, self).__init__(rmio, label,
            0xb020c000, 0x06C,
            'GAINSTEPLIM0', 'AGC_NS.GAINSTEPLIM0', 'read-write',
            u"",
            0x00003144, 0x01FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CFLOOPSTEPMAX = RM_Field_AGC_NS_GAINSTEPLIM0_CFLOOPSTEPMAX(self)
        self.zz_fdict['CFLOOPSTEPMAX'] = self.CFLOOPSTEPMAX
        self.CFLOOPDEL = RM_Field_AGC_NS_GAINSTEPLIM0_CFLOOPDEL(self)
        self.zz_fdict['CFLOOPDEL'] = self.CFLOOPDEL
        self.HYST = RM_Field_AGC_NS_GAINSTEPLIM0_HYST(self)
        self.zz_fdict['HYST'] = self.HYST
        self.MAXPWRVAR = RM_Field_AGC_NS_GAINSTEPLIM0_MAXPWRVAR(self)
        self.zz_fdict['MAXPWRVAR'] = self.MAXPWRVAR
        self.TRANRSTAGC = RM_Field_AGC_NS_GAINSTEPLIM0_TRANRSTAGC(self)
        self.zz_fdict['TRANRSTAGC'] = self.TRANRSTAGC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_GAINSTEPLIM1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_GAINSTEPLIM1, self).__init__(rmio, label,
            0xb020c000, 0x070,
            'GAINSTEPLIM1', 'AGC_NS.GAINSTEPLIM1', 'read-write',
            u"",
            0x0000F1BA, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAINDEXMAX = RM_Field_AGC_NS_GAINSTEPLIM1_LNAINDEXMAX(self)
        self.zz_fdict['LNAINDEXMAX'] = self.LNAINDEXMAX
        self.PGAINDEXMAX = RM_Field_AGC_NS_GAINSTEPLIM1_PGAINDEXMAX(self)
        self.zz_fdict['PGAINDEXMAX'] = self.PGAINDEXMAX
        self.PNINDEXMAX = RM_Field_AGC_NS_GAINSTEPLIM1_PNINDEXMAX(self)
        self.zz_fdict['PNINDEXMAX'] = self.PNINDEXMAX
        self.PNINDEXADC0 = RM_Field_AGC_NS_GAINSTEPLIM1_PNINDEXADC0(self)
        self.zz_fdict['PNINDEXADC0'] = self.PNINDEXADC0
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT0, self).__init__(rmio, label,
            0xb020c000, 0x074,
            'PNRFATT0', 'AGC_NS.PNRFATT0', 'read-write',
            u"",
            0x00200400, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT1 = RM_Field_AGC_NS_PNRFATT0_LNAMIXRFATT1(self)
        self.zz_fdict['LNAMIXRFATT1'] = self.LNAMIXRFATT1
        self.LNAMIXRFATT2 = RM_Field_AGC_NS_PNRFATT0_LNAMIXRFATT2(self)
        self.zz_fdict['LNAMIXRFATT2'] = self.LNAMIXRFATT2
        self.LNAMIXRFATT3 = RM_Field_AGC_NS_PNRFATT0_LNAMIXRFATT3(self)
        self.zz_fdict['LNAMIXRFATT3'] = self.LNAMIXRFATT3
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT1, self).__init__(rmio, label,
            0xb020c000, 0x078,
            'PNRFATT1', 'AGC_NS.PNRFATT1', 'read-write',
            u"",
            0x00801804, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT4 = RM_Field_AGC_NS_PNRFATT1_LNAMIXRFATT4(self)
        self.zz_fdict['LNAMIXRFATT4'] = self.LNAMIXRFATT4
        self.LNAMIXRFATT5 = RM_Field_AGC_NS_PNRFATT1_LNAMIXRFATT5(self)
        self.zz_fdict['LNAMIXRFATT5'] = self.LNAMIXRFATT5
        self.LNAMIXRFATT6 = RM_Field_AGC_NS_PNRFATT1_LNAMIXRFATT6(self)
        self.zz_fdict['LNAMIXRFATT6'] = self.LNAMIXRFATT6
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT2, self).__init__(rmio, label,
            0xb020c000, 0x07C,
            'PNRFATT2', 'AGC_NS.PNRFATT2', 'read-write',
            u"",
            0x01203C0B, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT7 = RM_Field_AGC_NS_PNRFATT2_LNAMIXRFATT7(self)
        self.zz_fdict['LNAMIXRFATT7'] = self.LNAMIXRFATT7
        self.LNAMIXRFATT8 = RM_Field_AGC_NS_PNRFATT2_LNAMIXRFATT8(self)
        self.zz_fdict['LNAMIXRFATT8'] = self.LNAMIXRFATT8
        self.LNAMIXRFATT9 = RM_Field_AGC_NS_PNRFATT2_LNAMIXRFATT9(self)
        self.zz_fdict['LNAMIXRFATT9'] = self.LNAMIXRFATT9
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT3, self).__init__(rmio, label,
            0xb020c000, 0x080,
            'PNRFATT3', 'AGC_NS.PNRFATT3', 'read-write',
            u"",
            0x02107C18, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT10 = RM_Field_AGC_NS_PNRFATT3_LNAMIXRFATT10(self)
        self.zz_fdict['LNAMIXRFATT10'] = self.LNAMIXRFATT10
        self.LNAMIXRFATT11 = RM_Field_AGC_NS_PNRFATT3_LNAMIXRFATT11(self)
        self.zz_fdict['LNAMIXRFATT11'] = self.LNAMIXRFATT11
        self.LNAMIXRFATT12 = RM_Field_AGC_NS_PNRFATT3_LNAMIXRFATT12(self)
        self.zz_fdict['LNAMIXRFATT12'] = self.LNAMIXRFATT12
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT4, self).__init__(rmio, label,
            0xb020c000, 0x084,
            'PNRFATT4', 'AGC_NS.PNRFATT4', 'read-write',
            u"",
            0x06E0FC2F, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT13 = RM_Field_AGC_NS_PNRFATT4_LNAMIXRFATT13(self)
        self.zz_fdict['LNAMIXRFATT13'] = self.LNAMIXRFATT13
        self.LNAMIXRFATT14 = RM_Field_AGC_NS_PNRFATT4_LNAMIXRFATT14(self)
        self.zz_fdict['LNAMIXRFATT14'] = self.LNAMIXRFATT14
        self.LNAMIXRFATT15 = RM_Field_AGC_NS_PNRFATT4_LNAMIXRFATT15(self)
        self.zz_fdict['LNAMIXRFATT15'] = self.LNAMIXRFATT15
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT5, self).__init__(rmio, label,
            0xb020c000, 0x088,
            'PNRFATT5', 'AGC_NS.PNRFATT5', 'read-write',
            u"",
            0x0180480F, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT16 = RM_Field_AGC_NS_PNRFATT5_LNAMIXRFATT16(self)
        self.zz_fdict['LNAMIXRFATT16'] = self.LNAMIXRFATT16
        self.LNAMIXRFATT17 = RM_Field_AGC_NS_PNRFATT5_LNAMIXRFATT17(self)
        self.zz_fdict['LNAMIXRFATT17'] = self.LNAMIXRFATT17
        self.LNAMIXRFATT18 = RM_Field_AGC_NS_PNRFATT5_LNAMIXRFATT18(self)
        self.zz_fdict['LNAMIXRFATT18'] = self.LNAMIXRFATT18
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT6, self).__init__(rmio, label,
            0xb020c000, 0x08C,
            'PNRFATT6', 'AGC_NS.PNRFATT6', 'read-write',
            u"",
            0x02F0841F, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT19 = RM_Field_AGC_NS_PNRFATT6_LNAMIXRFATT19(self)
        self.zz_fdict['LNAMIXRFATT19'] = self.LNAMIXRFATT19
        self.LNAMIXRFATT20 = RM_Field_AGC_NS_PNRFATT6_LNAMIXRFATT20(self)
        self.zz_fdict['LNAMIXRFATT20'] = self.LNAMIXRFATT20
        self.LNAMIXRFATT21 = RM_Field_AGC_NS_PNRFATT6_LNAMIXRFATT21(self)
        self.zz_fdict['LNAMIXRFATT21'] = self.LNAMIXRFATT21
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATT7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATT7, self).__init__(rmio, label,
            0xb020c000, 0x090,
            'PNRFATT7', 'AGC_NS.PNRFATT7', 'read-write',
            u"",
            0x07F1B83F, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATT22 = RM_Field_AGC_NS_PNRFATT7_LNAMIXRFATT22(self)
        self.zz_fdict['LNAMIXRFATT22'] = self.LNAMIXRFATT22
        self.LNAMIXRFATT23 = RM_Field_AGC_NS_PNRFATT7_LNAMIXRFATT23(self)
        self.zz_fdict['LNAMIXRFATT23'] = self.LNAMIXRFATT23
        self.LNAMIXRFATT24 = RM_Field_AGC_NS_PNRFATT7_LNAMIXRFATT24(self)
        self.zz_fdict['LNAMIXRFATT24'] = self.LNAMIXRFATT24
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PNRFATTALT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PNRFATTALT, self).__init__(rmio, label,
            0xb020c000, 0x0A4,
            'PNRFATTALT', 'AGC_NS.PNRFATTALT', 'read-write',
            u"",
            0x0000007F, 0x000003FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXRFATTALT = RM_Field_AGC_NS_PNRFATTALT_LNAMIXRFATTALT(self)
        self.zz_fdict['LNAMIXRFATTALT'] = self.LNAMIXRFATTALT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_LNAMIXCODE0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_LNAMIXCODE0, self).__init__(rmio, label,
            0xb020c000, 0x0A8,
            'LNAMIXCODE0', 'AGC_NS.LNAMIXCODE0', 'read-write',
            u"",
            0x15724BBD, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXSLICE1 = RM_Field_AGC_NS_LNAMIXCODE0_LNAMIXSLICE1(self)
        self.zz_fdict['LNAMIXSLICE1'] = self.LNAMIXSLICE1
        self.LNAMIXSLICE2 = RM_Field_AGC_NS_LNAMIXCODE0_LNAMIXSLICE2(self)
        self.zz_fdict['LNAMIXSLICE2'] = self.LNAMIXSLICE2
        self.LNAMIXSLICE3 = RM_Field_AGC_NS_LNAMIXCODE0_LNAMIXSLICE3(self)
        self.zz_fdict['LNAMIXSLICE3'] = self.LNAMIXSLICE3
        self.LNAMIXSLICE4 = RM_Field_AGC_NS_LNAMIXCODE0_LNAMIXSLICE4(self)
        self.zz_fdict['LNAMIXSLICE4'] = self.LNAMIXSLICE4
        self.LNAMIXSLICE5 = RM_Field_AGC_NS_LNAMIXCODE0_LNAMIXSLICE5(self)
        self.zz_fdict['LNAMIXSLICE5'] = self.LNAMIXSLICE5
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_LNAMIXCODE1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_LNAMIXCODE1, self).__init__(rmio, label,
            0xb020c000, 0x0AC,
            'LNAMIXCODE1', 'AGC_NS.LNAMIXCODE1', 'read-write',
            u"",
            0x0518A311, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXSLICE6 = RM_Field_AGC_NS_LNAMIXCODE1_LNAMIXSLICE6(self)
        self.zz_fdict['LNAMIXSLICE6'] = self.LNAMIXSLICE6
        self.LNAMIXSLICE7 = RM_Field_AGC_NS_LNAMIXCODE1_LNAMIXSLICE7(self)
        self.zz_fdict['LNAMIXSLICE7'] = self.LNAMIXSLICE7
        self.LNAMIXSLICE8 = RM_Field_AGC_NS_LNAMIXCODE1_LNAMIXSLICE8(self)
        self.zz_fdict['LNAMIXSLICE8'] = self.LNAMIXSLICE8
        self.LNAMIXSLICE9 = RM_Field_AGC_NS_LNAMIXCODE1_LNAMIXSLICE9(self)
        self.zz_fdict['LNAMIXSLICE9'] = self.LNAMIXSLICE9
        self.LNAMIXSLICE10 = RM_Field_AGC_NS_LNAMIXCODE1_LNAMIXSLICE10(self)
        self.zz_fdict['LNAMIXSLICE10'] = self.LNAMIXSLICE10
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PGACODE0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PGACODE0, self).__init__(rmio, label,
            0xb020c000, 0x0B0,
            'PGACODE0', 'AGC_NS.PGACODE0', 'read-write',
            u"",
            0x76543210, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PGAGAIN1 = RM_Field_AGC_NS_PGACODE0_PGAGAIN1(self)
        self.zz_fdict['PGAGAIN1'] = self.PGAGAIN1
        self.PGAGAIN2 = RM_Field_AGC_NS_PGACODE0_PGAGAIN2(self)
        self.zz_fdict['PGAGAIN2'] = self.PGAGAIN2
        self.PGAGAIN3 = RM_Field_AGC_NS_PGACODE0_PGAGAIN3(self)
        self.zz_fdict['PGAGAIN3'] = self.PGAGAIN3
        self.PGAGAIN4 = RM_Field_AGC_NS_PGACODE0_PGAGAIN4(self)
        self.zz_fdict['PGAGAIN4'] = self.PGAGAIN4
        self.PGAGAIN5 = RM_Field_AGC_NS_PGACODE0_PGAGAIN5(self)
        self.zz_fdict['PGAGAIN5'] = self.PGAGAIN5
        self.PGAGAIN6 = RM_Field_AGC_NS_PGACODE0_PGAGAIN6(self)
        self.zz_fdict['PGAGAIN6'] = self.PGAGAIN6
        self.PGAGAIN7 = RM_Field_AGC_NS_PGACODE0_PGAGAIN7(self)
        self.zz_fdict['PGAGAIN7'] = self.PGAGAIN7
        self.PGAGAIN8 = RM_Field_AGC_NS_PGACODE0_PGAGAIN8(self)
        self.zz_fdict['PGAGAIN8'] = self.PGAGAIN8
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_PGACODE1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_PGACODE1, self).__init__(rmio, label,
            0xb020c000, 0x0B4,
            'PGACODE1', 'AGC_NS.PGACODE1', 'read-write',
            u"",
            0x00000A98, 0x00000FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PGAGAIN9 = RM_Field_AGC_NS_PGACODE1_PGAGAIN9(self)
        self.zz_fdict['PGAGAIN9'] = self.PGAGAIN9
        self.PGAGAIN10 = RM_Field_AGC_NS_PGACODE1_PGAGAIN10(self)
        self.zz_fdict['PGAGAIN10'] = self.PGAGAIN10
        self.PGAGAIN11 = RM_Field_AGC_NS_PGACODE1_PGAGAIN11(self)
        self.zz_fdict['PGAGAIN11'] = self.PGAGAIN11
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_LBT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_LBT, self).__init__(rmio, label,
            0xb020c000, 0x0B8,
            'LBT', 'AGC_NS.LBT', 'read-write',
            u"",
            0x00000000, 0x0000007F,
            0x00001000, 0x00002000,
            0x00003000)

        self.CCARSSIPERIOD = RM_Field_AGC_NS_LBT_CCARSSIPERIOD(self)
        self.zz_fdict['CCARSSIPERIOD'] = self.CCARSSIPERIOD
        self.ENCCARSSIPERIOD = RM_Field_AGC_NS_LBT_ENCCARSSIPERIOD(self)
        self.zz_fdict['ENCCARSSIPERIOD'] = self.ENCCARSSIPERIOD
        self.ENCCAGAINREDUCED = RM_Field_AGC_NS_LBT_ENCCAGAINREDUCED(self)
        self.zz_fdict['ENCCAGAINREDUCED'] = self.ENCCAGAINREDUCED
        self.ENCCARSSIMAX = RM_Field_AGC_NS_LBT_ENCCARSSIMAX(self)
        self.zz_fdict['ENCCARSSIMAX'] = self.ENCCARSSIMAX
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_MIRRORIF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_MIRRORIF, self).__init__(rmio, label,
            0xb020c000, 0x0BC,
            'MIRRORIF', 'AGC_NS.MIRRORIF', 'read-write',
            u"",
            0x00000000, 0x0000000F,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIPOSSTEPM = RM_Field_AGC_NS_MIRRORIF_RSSIPOSSTEPM(self)
        self.zz_fdict['RSSIPOSSTEPM'] = self.RSSIPOSSTEPM
        self.RSSINEGSTEPM = RM_Field_AGC_NS_MIRRORIF_RSSINEGSTEPM(self)
        self.zz_fdict['RSSINEGSTEPM'] = self.RSSINEGSTEPM
        self.SHORTRSSIPOSSTEPM = RM_Field_AGC_NS_MIRRORIF_SHORTRSSIPOSSTEPM(self)
        self.zz_fdict['SHORTRSSIPOSSTEPM'] = self.SHORTRSSIPOSSTEPM
        self.IFMIRRORCLEAR = RM_Field_AGC_NS_MIRRORIF_IFMIRRORCLEAR(self)
        self.zz_fdict['IFMIRRORCLEAR'] = self.IFMIRRORCLEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_SEQIF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_SEQIF, self).__init__(rmio, label,
            0xb020c000, 0x0C0,
            'SEQIF', 'AGC_NS.SEQIF', 'read-write',
            u"",
            0x00000000, 0x0003FF7D,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIVALID = RM_Field_AGC_NS_SEQIF_RSSIVALID(self)
        self.zz_fdict['RSSIVALID'] = self.RSSIVALID
        self.CCA = RM_Field_AGC_NS_SEQIF_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.RSSIPOSSTEP = RM_Field_AGC_NS_SEQIF_RSSIPOSSTEP(self)
        self.zz_fdict['RSSIPOSSTEP'] = self.RSSIPOSSTEP
        self.RSSINEGSTEP = RM_Field_AGC_NS_SEQIF_RSSINEGSTEP(self)
        self.zz_fdict['RSSINEGSTEP'] = self.RSSINEGSTEP
        self.RSSIDONE = RM_Field_AGC_NS_SEQIF_RSSIDONE(self)
        self.zz_fdict['RSSIDONE'] = self.RSSIDONE
        self.SHORTRSSIPOSSTEP = RM_Field_AGC_NS_SEQIF_SHORTRSSIPOSSTEP(self)
        self.zz_fdict['SHORTRSSIPOSSTEP'] = self.SHORTRSSIPOSSTEP
        self.RFPKDPRDDONE = RM_Field_AGC_NS_SEQIF_RFPKDPRDDONE(self)
        self.zz_fdict['RFPKDPRDDONE'] = self.RFPKDPRDDONE
        self.RFPKDCNTDONE = RM_Field_AGC_NS_SEQIF_RFPKDCNTDONE(self)
        self.zz_fdict['RFPKDCNTDONE'] = self.RFPKDCNTDONE
        self.RSSIHIGH = RM_Field_AGC_NS_SEQIF_RSSIHIGH(self)
        self.zz_fdict['RSSIHIGH'] = self.RSSIHIGH
        self.RSSILOW = RM_Field_AGC_NS_SEQIF_RSSILOW(self)
        self.zz_fdict['RSSILOW'] = self.RSSILOW
        self.CCANODET = RM_Field_AGC_NS_SEQIF_CCANODET(self)
        self.zz_fdict['CCANODET'] = self.CCANODET
        self.GAINBELOWGAINTHD = RM_Field_AGC_NS_SEQIF_GAINBELOWGAINTHD(self)
        self.zz_fdict['GAINBELOWGAINTHD'] = self.GAINBELOWGAINTHD
        self.GAINUPDATEFRZ = RM_Field_AGC_NS_SEQIF_GAINUPDATEFRZ(self)
        self.zz_fdict['GAINUPDATEFRZ'] = self.GAINUPDATEFRZ
        self.PNATTEN = RM_Field_AGC_NS_SEQIF_PNATTEN(self)
        self.zz_fdict['PNATTEN'] = self.PNATTEN
        self.COLLDETRSSIMAPRE = RM_Field_AGC_NS_SEQIF_COLLDETRSSIMAPRE(self)
        self.zz_fdict['COLLDETRSSIMAPRE'] = self.COLLDETRSSIMAPRE
        self.COLLDETRSSIMASYNC = RM_Field_AGC_NS_SEQIF_COLLDETRSSIMASYNC(self)
        self.zz_fdict['COLLDETRSSIMASYNC'] = self.COLLDETRSSIMASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_SEQIEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_SEQIEN, self).__init__(rmio, label,
            0xb020c000, 0x0C4,
            'SEQIEN', 'AGC_NS.SEQIEN', 'read-write',
            u"",
            0x00000000, 0x0003FF7D,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIVALID = RM_Field_AGC_NS_SEQIEN_RSSIVALID(self)
        self.zz_fdict['RSSIVALID'] = self.RSSIVALID
        self.CCA = RM_Field_AGC_NS_SEQIEN_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.RSSIPOSSTEP = RM_Field_AGC_NS_SEQIEN_RSSIPOSSTEP(self)
        self.zz_fdict['RSSIPOSSTEP'] = self.RSSIPOSSTEP
        self.RSSINEGSTEP = RM_Field_AGC_NS_SEQIEN_RSSINEGSTEP(self)
        self.zz_fdict['RSSINEGSTEP'] = self.RSSINEGSTEP
        self.RSSIDONE = RM_Field_AGC_NS_SEQIEN_RSSIDONE(self)
        self.zz_fdict['RSSIDONE'] = self.RSSIDONE
        self.SHORTRSSIPOSSTEP = RM_Field_AGC_NS_SEQIEN_SHORTRSSIPOSSTEP(self)
        self.zz_fdict['SHORTRSSIPOSSTEP'] = self.SHORTRSSIPOSSTEP
        self.RFPKDPRDDONE = RM_Field_AGC_NS_SEQIEN_RFPKDPRDDONE(self)
        self.zz_fdict['RFPKDPRDDONE'] = self.RFPKDPRDDONE
        self.RFPKDCNTDONE = RM_Field_AGC_NS_SEQIEN_RFPKDCNTDONE(self)
        self.zz_fdict['RFPKDCNTDONE'] = self.RFPKDCNTDONE
        self.RSSIHIGH = RM_Field_AGC_NS_SEQIEN_RSSIHIGH(self)
        self.zz_fdict['RSSIHIGH'] = self.RSSIHIGH
        self.RSSILOW = RM_Field_AGC_NS_SEQIEN_RSSILOW(self)
        self.zz_fdict['RSSILOW'] = self.RSSILOW
        self.CCANODET = RM_Field_AGC_NS_SEQIEN_CCANODET(self)
        self.zz_fdict['CCANODET'] = self.CCANODET
        self.GAINBELOWGAINTHD = RM_Field_AGC_NS_SEQIEN_GAINBELOWGAINTHD(self)
        self.zz_fdict['GAINBELOWGAINTHD'] = self.GAINBELOWGAINTHD
        self.GAINUPDATEFRZ = RM_Field_AGC_NS_SEQIEN_GAINUPDATEFRZ(self)
        self.zz_fdict['GAINUPDATEFRZ'] = self.GAINUPDATEFRZ
        self.PNATTEN = RM_Field_AGC_NS_SEQIEN_PNATTEN(self)
        self.zz_fdict['PNATTEN'] = self.PNATTEN
        self.COLLDETRSSIMAPRE = RM_Field_AGC_NS_SEQIEN_COLLDETRSSIMAPRE(self)
        self.zz_fdict['COLLDETRSSIMAPRE'] = self.COLLDETRSSIMAPRE
        self.COLLDETRSSIMASYNC = RM_Field_AGC_NS_SEQIEN_COLLDETRSSIMASYNC(self)
        self.zz_fdict['COLLDETRSSIMASYNC'] = self.COLLDETRSSIMASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_RSSIABSTHR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_RSSIABSTHR, self).__init__(rmio, label,
            0xb020c000, 0x0C8,
            'RSSIABSTHR', 'AGC_NS.RSSIABSTHR', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIHIGHTHRSH = RM_Field_AGC_NS_RSSIABSTHR_RSSIHIGHTHRSH(self)
        self.zz_fdict['RSSIHIGHTHRSH'] = self.RSSIHIGHTHRSH
        self.RSSILOWTHRSH = RM_Field_AGC_NS_RSSIABSTHR_RSSILOWTHRSH(self)
        self.zz_fdict['RSSILOWTHRSH'] = self.RSSILOWTHRSH
        self.SIRSSIHIGHTHR = RM_Field_AGC_NS_RSSIABSTHR_SIRSSIHIGHTHR(self)
        self.zz_fdict['SIRSSIHIGHTHR'] = self.SIRSSIHIGHTHR
        self.SIRSSINEGSTEPTHR = RM_Field_AGC_NS_RSSIABSTHR_SIRSSINEGSTEPTHR(self)
        self.zz_fdict['SIRSSINEGSTEPTHR'] = self.SIRSSINEGSTEPTHR
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_ANTDIV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_ANTDIV, self).__init__(rmio, label,
            0xb020c000, 0x0D0,
            'ANTDIV', 'AGC_NS.ANTDIV', 'read-write',
            u"",
            0x00000000, 0x000001FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.GAINMODE = RM_Field_AGC_NS_ANTDIV_GAINMODE(self)
        self.zz_fdict['GAINMODE'] = self.GAINMODE
        self.DEBOUNCECNTTHD = RM_Field_AGC_NS_ANTDIV_DEBOUNCECNTTHD(self)
        self.zz_fdict['DEBOUNCECNTTHD'] = self.DEBOUNCECNTTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_DUALRFPKDTHD0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_DUALRFPKDTHD0, self).__init__(rmio, label,
            0xb020c000, 0x0D4,
            'DUALRFPKDTHD0', 'AGC_NS.DUALRFPKDTHD0', 'read-write',
            u"",
            0x000A0001, 0x0FFF0FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RFPKDLOWTHD0 = RM_Field_AGC_NS_DUALRFPKDTHD0_RFPKDLOWTHD0(self)
        self.zz_fdict['RFPKDLOWTHD0'] = self.RFPKDLOWTHD0
        self.RFPKDLOWTHD1 = RM_Field_AGC_NS_DUALRFPKDTHD0_RFPKDLOWTHD1(self)
        self.zz_fdict['RFPKDLOWTHD1'] = self.RFPKDLOWTHD1
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_DUALRFPKDTHD1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_DUALRFPKDTHD1, self).__init__(rmio, label,
            0xb020c000, 0x0D8,
            'DUALRFPKDTHD1', 'AGC_NS.DUALRFPKDTHD1', 'read-write',
            u"",
            0x00280001, 0x0FFF0FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RFPKDHITHD0 = RM_Field_AGC_NS_DUALRFPKDTHD1_RFPKDHITHD0(self)
        self.zz_fdict['RFPKDHITHD0'] = self.RFPKDHITHD0
        self.RFPKDHITHD1 = RM_Field_AGC_NS_DUALRFPKDTHD1_RFPKDHITHD1(self)
        self.zz_fdict['RFPKDHITHD1'] = self.RFPKDHITHD1
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_SPARE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_SPARE, self).__init__(rmio, label,
            0xb020c000, 0x0DC,
            'SPARE', 'AGC_NS.SPARE', 'read-write',
            u"",
            0x00000000, 0x000000FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SPAREREG = RM_Field_AGC_NS_SPARE_SPAREREG(self)
        self.zz_fdict['SPAREREG'] = self.SPAREREG
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_FLARE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_FLARE, self).__init__(rmio, label,
            0xb020c000, 0x0E0,
            'FLARE', 'AGC_NS.FLARE', 'read-write',
            u"",
            0x00000004, 0x0000001F,
            0x00001000, 0x00002000,
            0x00003000)

        self.PNATTENTHD = RM_Field_AGC_NS_FLARE_PNATTENTHD(self)
        self.zz_fdict['PNATTENTHD'] = self.PNATTENTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_STEPDWNSAFE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_STEPDWNSAFE, self).__init__(rmio, label,
            0xb020c000, 0x0E4,
            'STEPDWNSAFE', 'AGC_NS.STEPDWNSAFE', 'read-write',
            u"",
            0x00036D11, 0x0007FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.STEPDWNSAFE0 = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFE0(self)
        self.zz_fdict['STEPDWNSAFE0'] = self.STEPDWNSAFE0
        self.STEPDWNSAFE1 = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFE1(self)
        self.zz_fdict['STEPDWNSAFE1'] = self.STEPDWNSAFE1
        self.STEPDWNSAFE2 = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFE2(self)
        self.zz_fdict['STEPDWNSAFE2'] = self.STEPDWNSAFE2
        self.STEPDWNSAFE3 = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFE3(self)
        self.zz_fdict['STEPDWNSAFE3'] = self.STEPDWNSAFE3
        self.STEPDWNSAFE4 = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFE4(self)
        self.zz_fdict['STEPDWNSAFE4'] = self.STEPDWNSAFE4
        self.STEPDWNSAFE5 = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFE5(self)
        self.zz_fdict['STEPDWNSAFE5'] = self.STEPDWNSAFE5
        self.STEPDWNSAFEEN = RM_Field_AGC_NS_STEPDWNSAFE_STEPDWNSAFEEN(self)
        self.zz_fdict['STEPDWNSAFEEN'] = self.STEPDWNSAFEEN
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CCADEBUG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CCADEBUG, self).__init__(rmio, label,
            0xb020c000, 0x0E8,
            'CCADEBUG', 'AGC_NS.CCADEBUG', 'read-only',
            u"",
            0x00000000, 0x000003FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DEBUGCCARSSI = RM_Field_AGC_NS_CCADEBUG_DEBUGCCARSSI(self)
        self.zz_fdict['DEBUGCCARSSI'] = self.DEBUGCCARSSI
        self.DEBUGCCAM1 = RM_Field_AGC_NS_CCADEBUG_DEBUGCCAM1(self)
        self.zz_fdict['DEBUGCCAM1'] = self.DEBUGCCAM1
        self.DEBUGCCASIGDET = RM_Field_AGC_NS_CCADEBUG_DEBUGCCASIGDET(self)
        self.zz_fdict['DEBUGCCASIGDET'] = self.DEBUGCCASIGDET
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_TIACODE0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_TIACODE0, self).__init__(rmio, label,
            0xb020c000, 0x0EC,
            'TIACODE0', 'AGC_NS.TIACODE0', 'read-write',
            u"",
            0x00000000, 0x00777777,
            0x00001000, 0x00002000,
            0x00003000)

        self.TIACOMP1 = RM_Field_AGC_NS_TIACODE0_TIACOMP1(self)
        self.zz_fdict['TIACOMP1'] = self.TIACOMP1
        self.TIACOMP2 = RM_Field_AGC_NS_TIACODE0_TIACOMP2(self)
        self.zz_fdict['TIACOMP2'] = self.TIACOMP2
        self.TIACOMP3 = RM_Field_AGC_NS_TIACODE0_TIACOMP3(self)
        self.zz_fdict['TIACOMP3'] = self.TIACOMP3
        self.TIACOMP4 = RM_Field_AGC_NS_TIACODE0_TIACOMP4(self)
        self.zz_fdict['TIACOMP4'] = self.TIACOMP4
        self.TIACOMP5 = RM_Field_AGC_NS_TIACODE0_TIACOMP5(self)
        self.zz_fdict['TIACOMP5'] = self.TIACOMP5
        self.TIACOMP6 = RM_Field_AGC_NS_TIACODE0_TIACOMP6(self)
        self.zz_fdict['TIACOMP6'] = self.TIACOMP6
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_TIACODE1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_TIACODE1, self).__init__(rmio, label,
            0xb020c000, 0x0F0,
            'TIACODE1', 'AGC_NS.TIACODE1', 'read-write',
            u"",
            0x00000000, 0x00077777,
            0x00001000, 0x00002000,
            0x00003000)

        self.TIACOMP7 = RM_Field_AGC_NS_TIACODE1_TIACOMP7(self)
        self.zz_fdict['TIACOMP7'] = self.TIACOMP7
        self.TIACOMP8 = RM_Field_AGC_NS_TIACODE1_TIACOMP8(self)
        self.zz_fdict['TIACOMP8'] = self.TIACOMP8
        self.TIACOMP9 = RM_Field_AGC_NS_TIACODE1_TIACOMP9(self)
        self.zz_fdict['TIACOMP9'] = self.TIACOMP9
        self.TIACOMP10 = RM_Field_AGC_NS_TIACODE1_TIACOMP10(self)
        self.zz_fdict['TIACOMP10'] = self.TIACOMP10
        self.TIACOMP11 = RM_Field_AGC_NS_TIACODE1_TIACOMP11(self)
        self.zz_fdict['TIACOMP11'] = self.TIACOMP11
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_LNAMIXCODE2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_LNAMIXCODE2, self).__init__(rmio, label,
            0xb020c000, 0x0F4,
            'LNAMIXCODE2', 'AGC_NS.LNAMIXCODE2', 'read-write',
            u"",
            0x00000011, 0x0001FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LNAMIXSLICE11 = RM_Field_AGC_NS_LNAMIXCODE2_LNAMIXSLICE11(self)
        self.zz_fdict['LNAMIXSLICE11'] = self.LNAMIXSLICE11
        self.LNAMIXCUREN = RM_Field_AGC_NS_LNAMIXCODE2_LNAMIXCUREN(self)
        self.zz_fdict['LNAMIXCUREN'] = self.LNAMIXCUREN
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_FSWIF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_FSWIF, self).__init__(rmio, label,
            0xb020c000, 0x0F8,
            'FSWIF', 'AGC_NS.FSWIF', 'read-write',
            u"",
            0x00000000, 0x0003FF7D,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIVALID = RM_Field_AGC_NS_FSWIF_RSSIVALID(self)
        self.zz_fdict['RSSIVALID'] = self.RSSIVALID
        self.CCA = RM_Field_AGC_NS_FSWIF_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.RSSIPOSSTEP = RM_Field_AGC_NS_FSWIF_RSSIPOSSTEP(self)
        self.zz_fdict['RSSIPOSSTEP'] = self.RSSIPOSSTEP
        self.RSSINEGSTEP = RM_Field_AGC_NS_FSWIF_RSSINEGSTEP(self)
        self.zz_fdict['RSSINEGSTEP'] = self.RSSINEGSTEP
        self.RSSIDONE = RM_Field_AGC_NS_FSWIF_RSSIDONE(self)
        self.zz_fdict['RSSIDONE'] = self.RSSIDONE
        self.SHORTRSSIPOSSTEP = RM_Field_AGC_NS_FSWIF_SHORTRSSIPOSSTEP(self)
        self.zz_fdict['SHORTRSSIPOSSTEP'] = self.SHORTRSSIPOSSTEP
        self.RFPKDPRDDONE = RM_Field_AGC_NS_FSWIF_RFPKDPRDDONE(self)
        self.zz_fdict['RFPKDPRDDONE'] = self.RFPKDPRDDONE
        self.RFPKDCNTDONE = RM_Field_AGC_NS_FSWIF_RFPKDCNTDONE(self)
        self.zz_fdict['RFPKDCNTDONE'] = self.RFPKDCNTDONE
        self.RSSIHIGH = RM_Field_AGC_NS_FSWIF_RSSIHIGH(self)
        self.zz_fdict['RSSIHIGH'] = self.RSSIHIGH
        self.RSSILOW = RM_Field_AGC_NS_FSWIF_RSSILOW(self)
        self.zz_fdict['RSSILOW'] = self.RSSILOW
        self.CCANODET = RM_Field_AGC_NS_FSWIF_CCANODET(self)
        self.zz_fdict['CCANODET'] = self.CCANODET
        self.GAINBELOWGAINTHD = RM_Field_AGC_NS_FSWIF_GAINBELOWGAINTHD(self)
        self.zz_fdict['GAINBELOWGAINTHD'] = self.GAINBELOWGAINTHD
        self.GAINUPDATEFRZ = RM_Field_AGC_NS_FSWIF_GAINUPDATEFRZ(self)
        self.zz_fdict['GAINUPDATEFRZ'] = self.GAINUPDATEFRZ
        self.PNATTEN = RM_Field_AGC_NS_FSWIF_PNATTEN(self)
        self.zz_fdict['PNATTEN'] = self.PNATTEN
        self.COLLDETRSSIMAPRE = RM_Field_AGC_NS_FSWIF_COLLDETRSSIMAPRE(self)
        self.zz_fdict['COLLDETRSSIMAPRE'] = self.COLLDETRSSIMAPRE
        self.COLLDETRSSIMASYNC = RM_Field_AGC_NS_FSWIF_COLLDETRSSIMASYNC(self)
        self.zz_fdict['COLLDETRSSIMASYNC'] = self.COLLDETRSSIMASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_FSWIEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_FSWIEN, self).__init__(rmio, label,
            0xb020c000, 0x0FC,
            'FSWIEN', 'AGC_NS.FSWIEN', 'read-write',
            u"",
            0x00000000, 0x0003FF7D,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIVALID = RM_Field_AGC_NS_FSWIEN_RSSIVALID(self)
        self.zz_fdict['RSSIVALID'] = self.RSSIVALID
        self.CCA = RM_Field_AGC_NS_FSWIEN_CCA(self)
        self.zz_fdict['CCA'] = self.CCA
        self.RSSIPOSSTEP = RM_Field_AGC_NS_FSWIEN_RSSIPOSSTEP(self)
        self.zz_fdict['RSSIPOSSTEP'] = self.RSSIPOSSTEP
        self.RSSINEGSTEP = RM_Field_AGC_NS_FSWIEN_RSSINEGSTEP(self)
        self.zz_fdict['RSSINEGSTEP'] = self.RSSINEGSTEP
        self.RSSIDONE = RM_Field_AGC_NS_FSWIEN_RSSIDONE(self)
        self.zz_fdict['RSSIDONE'] = self.RSSIDONE
        self.SHORTRSSIPOSSTEP = RM_Field_AGC_NS_FSWIEN_SHORTRSSIPOSSTEP(self)
        self.zz_fdict['SHORTRSSIPOSSTEP'] = self.SHORTRSSIPOSSTEP
        self.RFPKDPRDDONE = RM_Field_AGC_NS_FSWIEN_RFPKDPRDDONE(self)
        self.zz_fdict['RFPKDPRDDONE'] = self.RFPKDPRDDONE
        self.RFPKDCNTDONE = RM_Field_AGC_NS_FSWIEN_RFPKDCNTDONE(self)
        self.zz_fdict['RFPKDCNTDONE'] = self.RFPKDCNTDONE
        self.RSSIHIGH = RM_Field_AGC_NS_FSWIEN_RSSIHIGH(self)
        self.zz_fdict['RSSIHIGH'] = self.RSSIHIGH
        self.RSSILOW = RM_Field_AGC_NS_FSWIEN_RSSILOW(self)
        self.zz_fdict['RSSILOW'] = self.RSSILOW
        self.CCANODET = RM_Field_AGC_NS_FSWIEN_CCANODET(self)
        self.zz_fdict['CCANODET'] = self.CCANODET
        self.GAINBELOWGAINTHD = RM_Field_AGC_NS_FSWIEN_GAINBELOWGAINTHD(self)
        self.zz_fdict['GAINBELOWGAINTHD'] = self.GAINBELOWGAINTHD
        self.GAINUPDATEFRZ = RM_Field_AGC_NS_FSWIEN_GAINUPDATEFRZ(self)
        self.zz_fdict['GAINUPDATEFRZ'] = self.GAINUPDATEFRZ
        self.PNATTEN = RM_Field_AGC_NS_FSWIEN_PNATTEN(self)
        self.zz_fdict['PNATTEN'] = self.PNATTEN
        self.COLLDETRSSIMAPRE = RM_Field_AGC_NS_FSWIEN_COLLDETRSSIMAPRE(self)
        self.zz_fdict['COLLDETRSSIMAPRE'] = self.COLLDETRSSIMAPRE
        self.COLLDETRSSIMASYNC = RM_Field_AGC_NS_FSWIEN_COLLDETRSSIMASYNC(self)
        self.zz_fdict['COLLDETRSSIMASYNC'] = self.COLLDETRSSIMASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CCASUB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CCASUB, self).__init__(rmio, label,
            0xb020c000, 0x100,
            'CCASUB', 'AGC_NS.CCASUB', 'read-write',
            u"",
            0x00004400, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CCASUBPER = RM_Field_AGC_NS_CCASUB_CCASUBPER(self)
        self.zz_fdict['CCASUBPER'] = self.CCASUBPER
        self.CCASUBNUM = RM_Field_AGC_NS_CCASUB_CCASUBNUM(self)
        self.zz_fdict['CCASUBNUM'] = self.CCASUBNUM
        self.CCASUBDEN = RM_Field_AGC_NS_CCASUB_CCASUBDEN(self)
        self.zz_fdict['CCASUBDEN'] = self.CCASUBDEN
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_CTRL8(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_CTRL8, self).__init__(rmio, label,
            0xb020c000, 0x104,
            'CTRL8', 'AGC_NS.CTRL8', 'read-write',
            u"",
            0x00000000, 0x0000000F,
            0x00001000, 0x00002000,
            0x00003000)

        self.EARLYRSSIPERIOD = RM_Field_AGC_NS_CTRL8_EARLYRSSIPERIOD(self)
        self.zz_fdict['EARLYRSSIPERIOD'] = self.EARLYRSSIPERIOD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_STATUS3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_STATUS3, self).__init__(rmio, label,
            0xb020c000, 0x108,
            'STATUS3', 'AGC_NS.STATUS3', 'read-only',
            u"",
            0x00000000, 0x000000FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.IFPKDHICNT = RM_Field_AGC_NS_STATUS3_IFPKDHICNT(self)
        self.zz_fdict['IFPKDHICNT'] = self.IFPKDHICNT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_COLLDETCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_COLLDETCTRL, self).__init__(rmio, label,
            0xb020c000, 0x110,
            'COLLDETCTRL', 'AGC_NS.COLLDETCTRL', 'read-write',
            u"",
            0x00002800, 0x03007F8F,
            0x00001000, 0x00002000,
            0x00003000)

        self.UPONMARSSI = RM_Field_AGC_NS_COLLDETCTRL_UPONMARSSI(self)
        self.zz_fdict['UPONMARSSI'] = self.UPONMARSSI
        self.INPUTSEL = RM_Field_AGC_NS_COLLDETCTRL_INPUTSEL(self)
        self.zz_fdict['INPUTSEL'] = self.INPUTSEL
        self.RSSIINSEL = RM_Field_AGC_NS_COLLDETCTRL_RSSIINSEL(self)
        self.zz_fdict['RSSIINSEL'] = self.RSSIINSEL
        self.OVRTHDSEL = RM_Field_AGC_NS_COLLDETCTRL_OVRTHDSEL(self)
        self.zz_fdict['OVRTHDSEL'] = self.OVRTHDSEL
        self.MALATCHSEL = RM_Field_AGC_NS_COLLDETCTRL_MALATCHSEL(self)
        self.zz_fdict['MALATCHSEL'] = self.MALATCHSEL
        self.MACOMPENSEL = RM_Field_AGC_NS_COLLDETCTRL_MACOMPENSEL(self)
        self.zz_fdict['MACOMPENSEL'] = self.MACOMPENSEL
        self.MATAP = RM_Field_AGC_NS_COLLDETCTRL_MATAP(self)
        self.zz_fdict['MATAP'] = self.MATAP
        self.FLTBYP = RM_Field_AGC_NS_COLLDETCTRL_FLTBYP(self)
        self.zz_fdict['FLTBYP'] = self.FLTBYP
        self.LATCHRSSIEN = RM_Field_AGC_NS_COLLDETCTRL_LATCHRSSIEN(self)
        self.zz_fdict['LATCHRSSIEN'] = self.LATCHRSSIEN
        self.LATCHRSSI = RM_Field_AGC_NS_COLLDETCTRL_LATCHRSSI(self)
        self.zz_fdict['LATCHRSSI'] = self.LATCHRSSI
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_COLLDETTHD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_COLLDETTHD, self).__init__(rmio, label,
            0xb020c000, 0x114,
            'COLLDETTHD', 'AGC_NS.COLLDETTHD', 'read-write',
            u"",
            0x00281606, 0x07FDFF0F,
            0x00001000, 0x00002000,
            0x00003000)

        self.MATHRESHOLD = RM_Field_AGC_NS_COLLDETTHD_MATHRESHOLD(self)
        self.zz_fdict['MATHRESHOLD'] = self.MATHRESHOLD
        self.MINTHRESHOLD = RM_Field_AGC_NS_COLLDETTHD_MINTHRESHOLD(self)
        self.zz_fdict['MINTHRESHOLD'] = self.MINTHRESHOLD
        self.OVRTHRESHOLD = RM_Field_AGC_NS_COLLDETTHD_OVRTHRESHOLD(self)
        self.zz_fdict['OVRTHRESHOLD'] = self.OVRTHRESHOLD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_COLLDETSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_COLLDETSTATUS, self).__init__(rmio, label,
            0xb020c000, 0x118,
            'COLLDETSTATUS', 'AGC_NS.COLLDETSTATUS', 'read-only',
            u"",
            0x00000000, 0x000001FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.MAFLTDOUT = RM_Field_AGC_NS_COLLDETSTATUS_MAFLTDOUT(self)
        self.zz_fdict['MAFLTDOUT'] = self.MAFLTDOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_SETTLINGINDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_SETTLINGINDCTRL, self).__init__(rmio, label,
            0xb020c000, 0x120,
            'SETTLINGINDCTRL', 'AGC_NS.SETTLINGINDCTRL', 'read-write',
            u"",
            0x00010100, 0x003F3F01,
            0x00001000, 0x00002000,
            0x00003000)

        self.EN = RM_Field_AGC_NS_SETTLINGINDCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.POSTHD = RM_Field_AGC_NS_SETTLINGINDCTRL_POSTHD(self)
        self.zz_fdict['POSTHD'] = self.POSTHD
        self.NEGTHD = RM_Field_AGC_NS_SETTLINGINDCTRL_NEGTHD(self)
        self.zz_fdict['NEGTHD'] = self.NEGTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_AGC_NS_SETTLINGINDPER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_AGC_NS_SETTLINGINDPER, self).__init__(rmio, label,
            0xb020c000, 0x124,
            'SETTLINGINDPER', 'AGC_NS.SETTLINGINDPER', 'read-write',
            u"",
            0x02000100, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SETTLEDPERIOD = RM_Field_AGC_NS_SETTLINGINDPER_SETTLEDPERIOD(self)
        self.zz_fdict['SETTLEDPERIOD'] = self.SETTLEDPERIOD
        self.DELAYPERIOD = RM_Field_AGC_NS_SETTLINGINDPER_DELAYPERIOD(self)
        self.zz_fdict['DELAYPERIOD'] = self.DELAYPERIOD
        self.__dict__['zz_frozen'] = True


