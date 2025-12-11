from datetime import datetime

class CreditApproveAccountPayload(object):
    def view(self, acno=None):
        if not acno:
            acno = ''
        payload = {
            "acno": acno
        }
        return payload

    def simple_search(self, search_text=None, page_size=None, page_index=None):
        if not search_text:
            search_text = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "search_text": search_text,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def advanced_search(self, acno=None, acname=None, ccrcd=None, customerid=None, catcd=None, crdtype=None, tntype=None, crdsts=None, refid=None, splcd=None, aprsts=None, page_index=None, page_size=None):
        if not acno:
            acno = ''
        if not acname:
            acname = ''
        if not ccrcd:
            ccrcd = ''
        if not customerid:
            customerid = None
        if not catcd:
            catcd = ''
        if not crdtype:
            crdtype = ''
        if not tntype:
            tntype = ''
        if not crdsts:
            crdsts = ''
        if not refid:
            refid = ''
        if not splcd:
            splcd = ''
        if not aprsts:
            aprsts = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "acno": acno,
            "acname": acname,
            "ccrcd": ccrcd,
            "customerid": customerid,
            "catcd": catcd,
            "crdtype": crdtype,
            "tntype": tntype,
            "crdsts": crdsts,
            "refid": refid,
            "splcd": splcd,
            "aprsts": aprsts,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, txrefid=None, txdt=None, aprsts=None, defacno=None, acno=None, aplcd=None, branchid=None, ccrcd=None, acname=None, customerid=None, ctmtype=None, catid=None, sccrcd=None, crdtype=None, tntype=None, issyn=None, intmode=None, sectype=None, secrate=None, prtn=None, prtnun=None, inttn=None, inttnun=None, fntn=None, fntnun=None, crdprp=None, crdcls=None, crdfacility=None, dcrate=None, rdcrate=None, dbmode=None, prgrpr=None, intgrpr=None, fngrpr=None, isprv=None, prvtn=None, prvtnun=None, rllovr=None, restruct=None, hdinttnr=None, hdprntnr=None, hdfntnr=None, crlimit=None, opcrlimit=None, emklimit=None, lfrdt=None, ltodt=None, olimit=None, oolimit=None, dbamt=None, balance=None, namt=None, oamt=None, pamt=None, oiamt=None, pfstdt=None, pday=None, lamt=None, insamt=None, damt=None, mavgamt=None, qavgamt=None, havgamt=None, yavgamt=None, intamt=None, intpaid=None, intpre=None, intpbl=None, intdue=None, intovd=None, intspamt=None, fnamt=None, fnpaid=None, intfstdt=None, iday=None, lintamt=None, ramt=None, riamt=None, woamt=None, woiamt=None, wopamt=None, woipamt=None, ppamt=None, ipamt=None, fpamt=None, opndt=None, clsdt=None, frdt=None, todt=None, lastmkdt=None, lastdt=None, crdsts=None, clsts=None, rlsts=None, rksts=None, trfcd=None, wdr=None, wcr=None, mdr=None, mcr=None, qdr=None, qcr=None, hdr=None, hcr=None, ydr=None, ycr=None, usrid=None, apuser=None, crmid=None, rmkfld=None, refid=None, udfield1=None, splcd=None, acrt=None, plrt=None, splrt=None, isrestruct=None, prv_p_rate0=None, prv_p_rate1=None, prv_p_rate2=None, prv_p_rate3=None, prv_p_rate4=None, prv_i_rate0=None, prv_i_rate1=None, prv_i_rate2=None, prv_i_rate3=None, prv_i_rate4=None, subproduct=None, offbsdt=None, isiccd=None):
        if not txrefid:
            txrefid = ''
        if not txdt:
            txdt = ''
        if not aprsts:
            aprsts = ''
        if not defacno:
            defacno = ''
        if not acno:
            acno = ''
        if not aplcd:
            aplcd = ''
        if not branchid:
            branchid = 0
        if not ccrcd:
            ccrcd = ''
        if not acname:
            acname = ''
        if not customerid:
            customerid = 0
        if not ctmtype:
            ctmtype = ''
        if not catid:
            catid = 0
        if not sccrcd:
            sccrcd = ''
        if not crdtype:
            crdtype = ''
        if not tntype:
            tntype = ''
        if not issyn:
            issyn = ''
        if not intmode:
            intmode = ''
        if not sectype:
            sectype = ''
        if not secrate:
            secrate = 0
        if not prtn:
            prtn = 0
        if not prtnun:
            prtnun = ''
        if not inttn:
            inttn = 0
        if not inttnun:
            inttnun = ''
        if not fntn:
            fntn = 0
        if not fntnun:
            fntnun = ''
        if not crdprp:
            crdprp = ''
        if not crdcls:
            crdcls = ''
        if not crdfacility:
            crdfacility = ''
        if not dcrate:
            dcrate = 0
        if not rdcrate:
            rdcrate = 0
        if not dbmode:
            dbmode = ''
        if not prgrpr:
            prgrpr = 0
        if not intgrpr:
            intgrpr = 0
        if not fngrpr:
            fngrpr = 0
        if not isprv:
            isprv = ''
        if not prvtn:
            prvtn = 0
        if not prvtnun:
            prvtnun = ''
        if not rllovr:
            rllovr = ''
        if not restruct:
            restruct = ''
        if not hdinttnr:
            hdinttnr = 0
        if not hdprntnr:
            hdprntnr = 0
        if not hdfntnr:
            hdfntnr = 0
        if not crlimit:
            crlimit = 0
        if not opcrlimit:
            opcrlimit = 0
        if not emklimit:
            emklimit = 0
        if not lfrdt:
            lfrdt = ''
        if not ltodt:
            ltodt = ''
        if not olimit:
            olimit = 0
        if not oolimit:
            oolimit = 0
        if not dbamt:
            dbamt = 0
        if not balance:
            balance = 0
        if not namt:
            namt = 0
        if not oamt:
            oamt = 0
        if not pamt:
            pamt = 0
        if not oiamt:
            oiamt = 0
        if not pfstdt:
            pfstdt = ''
        if not pday:
            pday = 0
        if not lamt:
            lamt = 0
        if not insamt:
            insamt = 0
        if not damt:
            damt = 0
        if not mavgamt:
            mavgamt = 0
        if not qavgamt:
            qavgamt = 0
        if not havgamt:
            havgamt = 0
        if not yavgamt:
            yavgamt = 0
        if not intamt:
            intamt = 0
        if not intpaid:
            intpaid = 0
        if not intpre:
            intpre = 0
        if not intpbl:
            intpbl = 0
        if not intdue:
            intdue = 0
        if not intovd:
            intovd = 0
        if not intspamt:
            intspamt = 0
        if not fnamt:
            fnamt = 0
        if not fnpaid:
            fnpaid = 0
        if not intfstdt:
            intfstdt = ''
        if not iday:
            iday = 0
        if not lintamt:
            lintamt = 0
        if not ramt:
            ramt = 0
        if not riamt:
            riamt = 0
        if not woamt:
            woamt = 0
        if not woiamt:
            woiamt = 0
        if not wopamt:
            wopamt = 0
        if not woipamt:
            woipamt = 0
        if not ppamt:
            ppamt = 0
        if not ipamt:
            ipamt = 0
        if not fpamt:
            fpamt = 0
        if not opndt:
            opndt = ''
        if not clsdt:
            clsdt = ''
        if not frdt:
            frdt = ''
        if not todt:
            todt = ''
        if not lastmkdt:
            lastmkdt = ''
        if not lastdt:
            lastdt = ''
        if not crdsts:
            crdsts = ''
        if not clsts:
            clsts = ''
        if not rlsts:
            rlsts = ''
        if not rksts:
            rksts = ''
        if not trfcd:
            trfcd = 0
        if not wdr:
            wdr = 0
        if not wcr:
            wcr = 0
        if not mdr:
            mdr = 0
        if not mcr:
            mcr = 0
        if not qdr:
            qdr = 0
        if not qcr:
            qcr = 0
        if not hdr:
            hdr = 0
        if not hcr:
            hcr = 0
        if not ydr:
            ydr = 0
        if not ycr:
            ycr = 0
        if not usrid:
            usrid = 0
        if not apuser:
            apuser = 0
        if not crmid:
            crmid = 0
        if not rmkfld:
            rmkfld = ''
        if not refid:
            refid = ''
        if not udfield1:
            udfield1 = ''
        if not splcd:
            splcd = ''
        if not acrt:
            acrt = 0
        if not plrt:
            plrt = 0
        if not splrt:
            splrt = 0
        if not isrestruct:
            isrestruct = ''
        if not prv_p_rate0:
            prv_p_rate0 = 0
        if not prv_p_rate1:
            prv_p_rate1 = 0
        if not prv_p_rate2:
            prv_p_rate2 = 0
        if not prv_p_rate3:
            prv_p_rate3 = 0
        if not prv_p_rate4:
            prv_p_rate4 = 0
        if not prv_i_rate0:
            prv_i_rate0 = 0
        if not prv_i_rate1:
            prv_i_rate1 = 0
        if not prv_i_rate2:
            prv_i_rate2 = 0
        if not prv_i_rate3:
            prv_i_rate3 = 0
        if not prv_i_rate4:
            prv_i_rate4 = 0
        if not subproduct:
            subproduct = ''
        if not offbsdt:
            offbsdt = ''
        if not isiccd:
            isiccd = ''
        payload = {
            "txrefid": txrefid,
            "txdt": txdt,
            "aprsts": aprsts,
            "defacno": defacno,
            "acno": acno,
            "aplcd": aplcd,
            "branchid": branchid,
            "ccrcd": ccrcd,
            "acname": acname,
            "customerid": customerid,
            "ctmtype": ctmtype,
            "catid": catid,
            "sccrcd": sccrcd,
            "crdtype": crdtype,
            "tntype": tntype,
            "issyn": issyn,
            "intmode": intmode,
            "sectype": sectype,
            "secrate": secrate,
            "prtn": prtn,
            "prtnun": prtnun,
            "inttn": inttn,
            "inttnun": inttnun,
            "fntn": fntn,
            "fntnun": fntnun,
            "crdprp": crdprp,
            "crdcls": crdcls,
            "crdfacility": crdfacility,
            "dcrate": dcrate,
            "rdcrate": rdcrate,
            "dbmode": dbmode,
            "prgrpr": prgrpr,
            "intgrpr": intgrpr,
            "fngrpr": fngrpr,
            "isprv": isprv,
            "prvtn": prvtn,
            "prvtnun": prvtnun,
            "rllovr": rllovr,
            "restruct": restruct,
            "hdinttnr": hdinttnr,
            "hdprntnr": hdprntnr,
            "hdfntnr": hdfntnr,
            "crlimit": crlimit,
            "opcrlimit": opcrlimit,
            "emklimit": emklimit,
            "lfrdt": lfrdt,
            "ltodt": ltodt,
            "olimit": olimit,
            "oolimit": oolimit,
            "dbamt": dbamt,
            "balance": balance,
            "namt": namt,
            "oamt": oamt,
            "pamt": pamt,
            "oiamt": oiamt,
            "pfstdt": pfstdt,
            "pday": pday,
            "lamt": lamt,
            "insamt": insamt,
            "damt": damt,
            "mavgamt": mavgamt,
            "qavgamt": qavgamt,
            "havgamt": havgamt,
            "yavgamt": yavgamt,
            "intamt": intamt,
            "intpaid": intpaid,
            "intpre": intpre,
            "intpbl": intpbl,
            "intdue": intdue,
            "intovd": intovd,
            "intspamt": intspamt,
            "fnamt": fnamt,
            "fnpaid": fnpaid,
            "intfstdt": intfstdt,
            "iday": iday,
            "lintamt": lintamt,
            "ramt": ramt,
            "riamt": riamt,
            "woamt": woamt,
            "woiamt": woiamt,
            "wopamt": wopamt,
            "woipamt": woipamt,
            "ppamt": ppamt,
            "ipamt": ipamt,
            "fpamt": fpamt,
            "opndt": opndt,
            "clsdt": clsdt,
            "frdt": frdt,
            "todt": todt,
            "lastmkdt": lastmkdt,
            "lastdt": lastdt,
            "crdsts": crdsts,
            "clsts": clsts,
            "rlsts": rlsts,
            "rksts": rksts,
            "trfcd": trfcd,
            "wdr": wdr,
            "wcr": wcr,
            "mdr": mdr,
            "mcr": mcr,
            "qdr": qdr,
            "qcr": qcr,
            "hdr": hdr,
            "hcr": hcr,
            "ydr": ydr,
            "ycr": ycr,
            "usrid": usrid,
            "apuser": apuser,
            "crmid": crmid,
            "rmkfld": rmkfld,
            "refid": refid,
            "udfield1": udfield1,
            "splcd": splcd,
            "acrt": acrt,
            "plrt": plrt,
            "splrt": splrt,
            "isrestruct": isrestruct,
            "prv_p_rate0": prv_p_rate0,
            "prv_p_rate1": prv_p_rate1,
            "prv_p_rate2": prv_p_rate2,
            "prv_p_rate3": prv_p_rate3,
            "prv_p_rate4": prv_p_rate4,
            "prv_i_rate0": prv_i_rate0,
            "prv_i_rate1": prv_i_rate1,
            "prv_i_rate2": prv_i_rate2,
            "prv_i_rate3": prv_i_rate3,
            "prv_i_rate4": prv_i_rate4,
            "subproduct": subproduct,
            "offbsdt": offbsdt,
            "isiccd": isiccd
        }
        return payload

    def update(self, id=None, txrefid=None, txdt=None, aprsts=None, defacno=None, acno=None, aplcd=None, branchid=None, ccrcd=None, acname=None, customerid=None, ctmtype=None, catid=None, sccrcd=None, crdtype=None, tntype=None, issyn=None, intmode=None, sectype=None, secrate=None, prtn=None, prtnun=None, inttn=None, inttnun=None, fntn=None, fntnun=None, crdprp=None, crdcls=None, crdfacility=None, dcrate=None, rdcrate=None, dbmode=None, prgrpr=None, intgrpr=None, fngrpr=None, isprv=None, prvtn=None, prvtnun=None, rllovr=None, restruct=None, hdinttnr=None, hdprntnr=None, hdfntnr=None, crlimit=None, opcrlimit=None, emklimit=None, lfrdt=None, ltodt=None, olimit=None, oolimit=None, dbamt=None, balance=None, namt=None, oamt=None, pamt=None, oiamt=None, pfstdt=None, pday=None, lamt=None, insamt=None, damt=None, mavgamt=None, qavgamt=None, havgamt=None, yavgamt=None, intamt=None, intpaid=None, intpre=None, intpbl=None, intdue=None, intovd=None, intspamt=None, fnamt=None, fnpaid=None, intfstdt=None, iday=None, lintamt=None, ramt=None, riamt=None, woamt=None, woiamt=None, wopamt=None, woipamt=None, ppamt=None, ipamt=None, fpamt=None, opndt=None, clsdt=None, frdt=None, todt=None, lastmkdt=None, lastdt=None, crdsts=None, clsts=None, rlsts=None, rksts=None, trfcd=None, wdr=None, wcr=None, mdr=None, mcr=None, qdr=None, qcr=None, hdr=None, hcr=None, ydr=None, ycr=None, usrid=None, apuser=None, crmid=None, rmkfld=None, refid=None, udfield1=None, splcd=None, acrt=None, plrt=None, splrt=None, isrestruct=None, prv_p_rate0=None, prv_p_rate1=None, prv_p_rate2=None, prv_p_rate3=None, prv_p_rate4=None, prv_i_rate0=None, prv_i_rate1=None, prv_i_rate2=None, prv_i_rate3=None, prv_i_rate4=None, subproduct=None, offbsdt=None, isiccd=None):
        if not id:
            id = 0
        if not txrefid:
            txrefid = ''
        if not txdt:
            txdt = ''
        if not aprsts:
            aprsts = ''
        if not defacno:
            defacno = ''
        if not acno:
            acno = ''
        if not aplcd:
            aplcd = ''
        if not branchid:
            branchid = 0
        if not ccrcd:
            ccrcd = ''
        if not acname:
            acname = ''
        if not customerid:
            customerid = 0
        if not ctmtype:
            ctmtype = ''
        if not catid:
            catid = 0
        if not sccrcd:
            sccrcd = ''
        if not crdtype:
            crdtype = ''
        if not tntype:
            tntype = ''
        if not issyn:
            issyn = ''
        if not intmode:
            intmode = ''
        if not sectype:
            sectype = ''
        if not secrate:
            secrate = 0
        if not prtn:
            prtn = 0
        if not prtnun:
            prtnun = ''
        if not inttn:
            inttn = 0
        if not inttnun:
            inttnun = ''
        if not fntn:
            fntn = 0
        if not fntnun:
            fntnun = ''
        if not crdprp:
            crdprp = ''
        if not crdcls:
            crdcls = ''
        if not crdfacility:
            crdfacility = ''
        if not dcrate:
            dcrate = 0
        if not rdcrate:
            rdcrate = 0
        if not dbmode:
            dbmode = ''
        if not prgrpr:
            prgrpr = 0
        if not intgrpr:
            intgrpr = 0
        if not fngrpr:
            fngrpr = 0
        if not isprv:
            isprv = ''
        if not prvtn:
            prvtn = 0
        if not prvtnun:
            prvtnun = ''
        if not rllovr:
            rllovr = ''
        if not restruct:
            restruct = ''
        if not hdinttnr:
            hdinttnr = 0
        if not hdprntnr:
            hdprntnr = 0
        if not hdfntnr:
            hdfntnr = 0
        if not crlimit:
            crlimit = 0
        if not opcrlimit:
            opcrlimit = 0
        if not emklimit:
            emklimit = 0
        if not lfrdt:
            lfrdt = ''
        if not ltodt:
            ltodt = ''
        if not olimit:
            olimit = 0
        if not oolimit:
            oolimit = 0
        if not dbamt:
            dbamt = 0
        if not balance:
            balance = 0
        if not namt:
            namt = 0
        if not oamt:
            oamt = 0
        if not pamt:
            pamt = 0
        if not oiamt:
            oiamt = 0
        if not pfstdt:
            pfstdt = ''
        if not pday:
            pday = 0
        if not lamt:
            lamt = 0
        if not insamt:
            insamt = 0
        if not damt:
            damt = 0
        if not mavgamt:
            mavgamt = 0
        if not qavgamt:
            qavgamt = 0
        if not havgamt:
            havgamt = 0
        if not yavgamt:
            yavgamt = 0
        if not intamt:
            intamt = 0
        if not intpaid:
            intpaid = 0
        if not intpre:
            intpre = 0
        if not intpbl:
            intpbl = 0
        if not intdue:
            intdue = 0
        if not intovd:
            intovd = 0
        if not intspamt:
            intspamt = 0
        if not fnamt:
            fnamt = 0
        if not fnpaid:
            fnpaid = 0
        if not intfstdt:
            intfstdt = ''
        if not iday:
            iday = 0
        if not lintamt:
            lintamt = 0
        if not ramt:
            ramt = 0
        if not riamt:
            riamt = 0
        if not woamt:
            woamt = 0
        if not woiamt:
            woiamt = 0
        if not wopamt:
            wopamt = 0
        if not woipamt:
            woipamt = 0
        if not ppamt:
            ppamt = 0
        if not ipamt:
            ipamt = 0
        if not fpamt:
            fpamt = 0
        if not opndt:
            opndt = ''
        if not clsdt:
            clsdt = ''
        if not frdt:
            frdt = ''
        if not todt:
            todt = ''
        if not lastmkdt:
            lastmkdt = ''
        if not lastdt:
            lastdt = ''
        if not crdsts:
            crdsts = ''
        if not clsts:
            clsts = ''
        if not rlsts:
            rlsts = ''
        if not rksts:
            rksts = ''
        if not trfcd:
            trfcd = 0
        if not wdr:
            wdr = 0
        if not wcr:
            wcr = 0
        if not mdr:
            mdr = 0
        if not mcr:
            mcr = 0
        if not qdr:
            qdr = 0
        if not qcr:
            qcr = 0
        if not hdr:
            hdr = 0
        if not hcr:
            hcr = 0
        if not ydr:
            ydr = 0
        if not ycr:
            ycr = 0
        if not usrid:
            usrid = 0
        if not apuser:
            apuser = 0
        if not crmid:
            crmid = 0
        if not rmkfld:
            rmkfld = ''
        if not refid:
            refid = ''
        if not udfield1:
            udfield1 = ''
        if not splcd:
            splcd = ''
        if not acrt:
            acrt = 0
        if not plrt:
            plrt = 0
        if not splrt:
            splrt = 0
        if not isrestruct:
            isrestruct = ''
        if not prv_p_rate0:
            prv_p_rate0 = 0
        if not prv_p_rate1:
            prv_p_rate1 = 0
        if not prv_p_rate2:
            prv_p_rate2 = 0
        if not prv_p_rate3:
            prv_p_rate3 = 0
        if not prv_p_rate4:
            prv_p_rate4 = 0
        if not prv_i_rate0:
            prv_i_rate0 = 0
        if not prv_i_rate1:
            prv_i_rate1 = 0
        if not prv_i_rate2:
            prv_i_rate2 = 0
        if not prv_i_rate3:
            prv_i_rate3 = 0
        if not prv_i_rate4:
            prv_i_rate4 = 0
        if not subproduct:
            subproduct = ''
        if not offbsdt:
            offbsdt = ''
        if not isiccd:
            isiccd = ''
        payload = {
            "id": id,
            "txrefid": txrefid,
            "txdt": txdt,
            "aprsts": aprsts,
            "defacno": defacno,
            "acno": acno,
            "aplcd": aplcd,
            "branchid": branchid,
            "ccrcd": ccrcd,
            "acname": acname,
            "customerid": customerid,
            "ctmtype": ctmtype,
            "catid": catid,
            "sccrcd": sccrcd,
            "crdtype": crdtype,
            "tntype": tntype,
            "issyn": issyn,
            "intmode": intmode,
            "sectype": sectype,
            "secrate": secrate,
            "prtn": prtn,
            "prtnun": prtnun,
            "inttn": inttn,
            "inttnun": inttnun,
            "fntn": fntn,
            "fntnun": fntnun,
            "crdprp": crdprp,
            "crdcls": crdcls,
            "crdfacility": crdfacility,
            "dcrate": dcrate,
            "rdcrate": rdcrate,
            "dbmode": dbmode,
            "prgrpr": prgrpr,
            "intgrpr": intgrpr,
            "fngrpr": fngrpr,
            "isprv": isprv,
            "prvtn": prvtn,
            "prvtnun": prvtnun,
            "rllovr": rllovr,
            "restruct": restruct,
            "hdinttnr": hdinttnr,
            "hdprntnr": hdprntnr,
            "hdfntnr": hdfntnr,
            "crlimit": crlimit,
            "opcrlimit": opcrlimit,
            "emklimit": emklimit,
            "lfrdt": lfrdt,
            "ltodt": ltodt,
            "olimit": olimit,
            "oolimit": oolimit,
            "dbamt": dbamt,
            "balance": balance,
            "namt": namt,
            "oamt": oamt,
            "pamt": pamt,
            "oiamt": oiamt,
            "pfstdt": pfstdt,
            "pday": pday,
            "lamt": lamt,
            "insamt": insamt,
            "damt": damt,
            "mavgamt": mavgamt,
            "qavgamt": qavgamt,
            "havgamt": havgamt,
            "yavgamt": yavgamt,
            "intamt": intamt,
            "intpaid": intpaid,
            "intpre": intpre,
            "intpbl": intpbl,
            "intdue": intdue,
            "intovd": intovd,
            "intspamt": intspamt,
            "fnamt": fnamt,
            "fnpaid": fnpaid,
            "intfstdt": intfstdt,
            "iday": iday,
            "lintamt": lintamt,
            "ramt": ramt,
            "riamt": riamt,
            "woamt": woamt,
            "woiamt": woiamt,
            "wopamt": wopamt,
            "woipamt": woipamt,
            "ppamt": ppamt,
            "ipamt": ipamt,
            "fpamt": fpamt,
            "opndt": opndt,
            "clsdt": clsdt,
            "frdt": frdt,
            "todt": todt,
            "lastmkdt": lastmkdt,
            "lastdt": lastdt,
            "crdsts": crdsts,
            "clsts": clsts,
            "rlsts": rlsts,
            "rksts": rksts,
            "trfcd": trfcd,
            "wdr": wdr,
            "wcr": wcr,
            "mdr": mdr,
            "mcr": mcr,
            "qdr": qdr,
            "qcr": qcr,
            "hdr": hdr,
            "hcr": hcr,
            "ydr": ydr,
            "ycr": ycr,
            "usrid": usrid,
            "apuser": apuser,
            "crmid": crmid,
            "rmkfld": rmkfld,
            "refid": refid,
            "udfield1": udfield1,
            "splcd": splcd,
            "acrt": acrt,
            "plrt": plrt,
            "splrt": splrt,
            "isrestruct": isrestruct,
            "prv_p_rate0": prv_p_rate0,
            "prv_p_rate1": prv_p_rate1,
            "prv_p_rate2": prv_p_rate2,
            "prv_p_rate3": prv_p_rate3,
            "prv_p_rate4": prv_p_rate4,
            "prv_i_rate0": prv_i_rate0,
            "prv_i_rate1": prv_i_rate1,
            "prv_i_rate2": prv_i_rate2,
            "prv_i_rate3": prv_i_rate3,
            "prv_i_rate4": prv_i_rate4,
            "subproduct": subproduct,
            "offbsdt": offbsdt,
            "isiccd": isiccd
        }
        return payload

    def approve(self, txrefid=None, acno=None):
        if not txrefid:
            txrefid = ''
        if not acno:
            acno = ''
        payload = {
            "txrefid": txrefid,
            "acno": acno
        }
        return payload

    def reject(self, txrefid=None, acno=None):
        if not txrefid:
            txrefid = ''
        if not acno:
            acno = ''
        payload = {
            "txrefid": txrefid,
            "acno": acno
        }
        return payload