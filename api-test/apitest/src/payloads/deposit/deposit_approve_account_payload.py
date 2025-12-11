from datetime import datetime

class DepositApproveAccountPayload(object):
    def add(self, id=None, txrefid=None, txdt=None, aprsts=None, defacno=None, acno=None, branch_id=None, currency=None, account_name=None, customer_id=None, customer_type=None, catalog_id=None, secure_currency=None, deposit_tenor=None, deposit_tenor_unit=None, tenor=None, tenorun=None, tenor2=None, tenorun2=None, interest_tenor_unit=None, interest_tenor=None, initial_amount=None, tndptamt=None, minimum_amount=None, mintnr=None, mintnrun=None, multdpt=None, multwdr=None, earlywdr=None, mintenr=None, mintenrun=None, crint=None, crinttnr=None, crinttnrun=None, crintday=None, intacrrt=None, deposit_type=None, dptgrp=None, dptprp=None, dptcls=None, drmpr=None, drmprun=None, rllovr=None, rovcat=None, hdinttnr=None, hdprntnr=None, pbst=None, sttnr=None, sttnrun=None, stfmt=None, dptamt=None, wdramt=None, balance=None, icbal=None, mavgamt=None, qavgamt=None, havgamt=None, yavgamt=None, intamt=None, intpaid=None, intpre=None, intpbl=None, intdue=None, intovd=None, intspamt=None, intnypd=None, inamt=None, examt=None, intpdcd=None, intac=None, rvbalance=None, rvmavgamt=None, rvqavgamt=None, rvhavgamt=None, rvyavgamt=None, rvintamt=None, rintpaid=None, rintpre=None, rvintpbl=None, rvintdue=None, rvintovd=None, rvintspamt=None, rvintnypd=None, opndt=None, clsdt=None, frdt=None, todt=None, lastdt=None, dpt_status=None, psts=None, pbno=None, pbstatus=None, trfcd=None, drmdt=None, lintduedt=None, emkamt=None, wdr=None, wcr=None, mdr=None, mcr=None, qdr=None, qcr=None, hdr=None, hcr=None, ydr=None, ycr=None, trftied=None, usrid=None, apuser=None, crmid=None, rmkfld=None, refid=None, udfield1=None, periodic=None, periodicun=None, blkby=None, acrsd=None, drmamt=None, macno=None, dptsubtype=None, isiccd=None, ldndt=None):
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
        if not branch_id:
            branch_id = 0
        if not currency:
            currency = ''
        if not account_name:
            account_name = ''
        if not customer_id:
            customer_id = 0
        if not customer_type:
            customer_type = ''
        if not catalog_id:
            catalog_id = 0
        if not secure_currency:
            secure_currency = ''
        if not deposit_tenor:
            deposit_tenor = 0
        if not deposit_tenor_unit:
            deposit_tenor_unit = ''
        if not tenor:
            tenor = 0
        if not tenorun:
            tenorun = ''
        if not tenor2:
            tenor2 = 0
        if not tenorun2:
            tenorun2 = ''
        if not interest_tenor_unit:
            interest_tenor_unit = ''
        if not interest_tenor:
            interest_tenor = 0
        if not initial_amount:
            initial_amount = 0
        if not tndptamt:
            tndptamt = 0
        if not minimum_amount:
            minimum_amount = 0
        if not mintnr:
            mintnr = 0
        if not mintnrun:
            mintnrun = ''
        if not multdpt:
            multdpt = ''
        if not multwdr:
            multwdr = ''
        if not earlywdr:
            earlywdr = ''
        if not mintenr:
            mintenr = 0
        if not mintenrun:
            mintenrun = ''
        if not crint:
            crint = ''
        if not crinttnr:
            crinttnr = 0
        if not crinttnrun:
            crinttnrun = ''
        if not crintday:
            crintday = 0
        if not intacrrt:
            intacrrt = 0
        if not deposit_type:
            deposit_type = ''
        if not dptgrp:
            dptgrp = ''
        if not dptprp:
            dptprp = ''
        if not dptcls:
            dptcls = ''
        if not drmpr:
            drmpr = 0
        if not drmprun:
            drmprun = ''
        if not rllovr:
            rllovr = ''
        if not rovcat:
            rovcat = 0
        if not hdinttnr:
            hdinttnr = 0
        if not hdprntnr:
            hdprntnr = 0
        if not pbst:
            pbst = ''
        if not sttnr:
            sttnr = 0
        if not sttnrun:
            sttnrun = ''
        if not stfmt:
            stfmt = ''
        if not dptamt:
            dptamt = 0
        if not wdramt:
            wdramt = 0
        if not balance:
            balance = 0
        if not icbal:
            icbal = 0
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
        if not intnypd:
            intnypd = 0
        if not inamt:
            inamt = 0
        if not examt:
            examt = 0
        if not intpdcd:
            intpdcd = ''
        if not intac:
            intac = ''
        if not rvbalance:
            rvbalance = 0
        if not rvmavgamt:
            rvmavgamt = 0
        if not rvqavgamt:
            rvqavgamt = 0
        if not rvhavgamt:
            rvhavgamt = 0
        if not rvyavgamt:
            rvyavgamt = 0
        if not rvintamt:
            rvintamt = 0
        if not rintpaid:
            rintpaid = 0
        if not rintpre:
            rintpre = 0
        if not rvintpbl:
            rvintpbl = 0
        if not rvintdue:
            rvintdue = 0
        if not rvintovd:
            rvintovd = 0
        if not rvintspamt:
            rvintspamt = 0
        if not rvintnypd:
            rvintnypd = 0
        if not opndt:
            opndt = ''
        if not clsdt:
            clsdt = ''
        if not frdt:
            frdt = ''
        if not todt:
            todt = ''
        if not lastdt:
            lastdt = ''
        if not dpt_status:
            dpt_status = ''
        if not psts:
            psts = ''
        if not pbno:
            pbno = ''
        if not pbstatus:
            pbstatus = ''
        if not trfcd:
            trfcd = 0
        if not drmdt:
            drmdt = ''
        if not lintduedt:
            lintduedt = ''
        if not emkamt:
            emkamt = 0
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
        if not trftied:
            trftied = ''
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
        if not periodic:
            periodic = 0
        if not periodicun:
            periodicun = ''
        if not blkby:
            blkby = ''
        if not acrsd:
            acrsd = ''
        if not drmamt:
            drmamt = 0
        if not macno:
            macno = ''
        if not dptsubtype:
            dptsubtype = ''
        if not isiccd:
            isiccd = ''
        if not ldndt:
            ldndt = ''
        payload = {
            "id": id,
            "txrefid": txrefid,
            "txdt": txdt,
            "aprsts": aprsts,
            "defacno": defacno,
            "acno": acno,
            "branch_id": branch_id,
            "currency": currency,
            "account_name": account_name,
            "customer_id": customer_id,
            "customer_type": customer_type,
            "catalog_id": catalog_id,
            "secure_currency": secure_currency,
            "deposit_tenor": deposit_tenor,
            "deposit_tenor_unit": deposit_tenor_unit,
            "tenor": tenor,
            "tenorun": tenorun,
            "tenor2": tenor2,
            "tenorun2": tenorun2,
            "interest_tenor_unit": interest_tenor_unit,
            "interest_tenor": interest_tenor,
            "initial_amount": initial_amount,
            "tndptamt": tndptamt,
            "minimum_amount": minimum_amount,
            "mintnr": mintnr,
            "mintnrun": mintnrun,
            "multdpt": multdpt,
            "multwdr": multwdr,
            "earlywdr": earlywdr,
            "mintenr": mintenr,
            "mintenrun": mintenrun,
            "crint": crint,
            "crinttnr": crinttnr,
            "crinttnrun": crinttnrun,
            "crintday": crintday,
            "intacrrt": intacrrt,
            "deposit_type": deposit_type,
            "dptgrp": dptgrp,
            "dptprp": dptprp,
            "dptcls": dptcls,
            "drmpr": drmpr,
            "drmprun": drmprun,
            "rllovr": rllovr,
            "rovcat": rovcat,
            "hdinttnr": hdinttnr,
            "hdprntnr": hdprntnr,
            "pbst": pbst,
            "sttnr": sttnr,
            "sttnrun": sttnrun,
            "stfmt": stfmt,
            "dptamt": dptamt,
            "wdramt": wdramt,
            "balance": balance,
            "icbal": icbal,
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
            "intnypd": intnypd,
            "inamt": inamt,
            "examt": examt,
            "intpdcd": intpdcd,
            "intac": intac,
            "rvbalance": rvbalance,
            "rvmavgamt": rvmavgamt,
            "rvqavgamt": rvqavgamt,
            "rvhavgamt": rvhavgamt,
            "rvyavgamt": rvyavgamt,
            "rvintamt": rvintamt,
            "rintpaid": rintpaid,
            "rintpre": rintpre,
            "rvintpbl": rvintpbl,
            "rvintdue": rvintdue,
            "rvintovd": rvintovd,
            "rvintspamt": rvintspamt,
            "rvintnypd": rvintnypd,
            "opndt": opndt,
            "clsdt": clsdt,
            "frdt": frdt,
            "todt": todt,
            "lastdt": lastdt,
            "dpt_status": dpt_status,
            "psts": psts,
            "pbno": pbno,
            "pbstatus": pbstatus,
            "trfcd": trfcd,
            "drmdt": drmdt,
            "lintduedt": lintduedt,
            "emkamt": emkamt,
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
            "trftied": trftied,
            "usrid": usrid,
            "apuser": apuser,
            "crmid": crmid,
            "rmkfld": rmkfld,
            "refid": refid,
            "udfield1": udfield1,
            "periodic": periodic,
            "periodicun": periodicun,
            "blkby": blkby,
            "acrsd": acrsd,
            "drmamt": drmamt,
            "macno": macno,
            "dptsubtype": dptsubtype,
            "isiccd": isiccd,
            "ldndt": ldndt
        }
        return payload

    def update(self, id=None, txrefid=None, txdt=None, aprsts=None, defacno=None, acno=None, branch_id=None, currency=None, account_name=None, customer_id=None, customer_type=None, catalog_id=None, secure_currency=None, deposit_tenor=None, deposit_tenor_unit=None, tenor=None, tenorun=None, tenor2=None, tenorun2=None, interest_tenor_unit=None, interest_tenor=None, initial_amount=None, tndptamt=None, minimum_amount=None, mintnr=None, mintnrun=None, multdpt=None, multwdr=None, earlywdr=None, mintenr=None, mintenrun=None, crint=None, crinttnr=None, crinttnrun=None, crintday=None, intacrrt=None, deposit_type=None, dptgrp=None, dptprp=None, dptcls=None, drmpr=None, drmprun=None, rllovr=None, rovcat=None, hdinttnr=None, hdprntnr=None, pbst=None, sttnr=None, sttnrun=None, stfmt=None, dptamt=None, wdramt=None, balance=None, icbal=None, mavgamt=None, qavgamt=None, havgamt=None, yavgamt=None, intamt=None, intpaid=None, intpre=None, intpbl=None, intdue=None, intovd=None, intspamt=None, intnypd=None, inamt=None, examt=None, intpdcd=None, intac=None, rvbalance=None, rvmavgamt=None, rvqavgamt=None, rvhavgamt=None, rvyavgamt=None, rvintamt=None, rintpaid=None, rintpre=None, rvintpbl=None, rvintdue=None, rvintovd=None, rvintspamt=None, rvintnypd=None, opndt=None, clsdt=None, frdt=None, todt=None, lastdt=None, dpt_status=None, psts=None, pbno=None, pbstatus=None, trfcd=None, drmdt=None, lintduedt=None, emkamt=None, wdr=None, wcr=None, mdr=None, mcr=None, qdr=None, qcr=None, hdr=None, hcr=None, ydr=None, ycr=None, trftied=None, usrid=None, apuser=None, crmid=None, rmkfld=None, refid=None, udfield1=None, periodic=None, periodicun=None, blkby=None, acrsd=None, drmamt=None, macno=None, dptsubtype=None, isiccd=None, ldndt=None):
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
        if not branch_id:
            branch_id = 0
        if not currency:
            currency = ''
        if not account_name:
            account_name = ''
        if not customer_id:
            customer_id = 0
        if not customer_type:
            customer_type = ''
        if not catalog_id:
            catalog_id = 0
        if not secure_currency:
            secure_currency = ''
        if not deposit_tenor:
            deposit_tenor = 0
        if not deposit_tenor_unit:
            deposit_tenor_unit = ''
        if not tenor:
            tenor = 0
        if not tenorun:
            tenorun = ''
        if not tenor2:
            tenor2 = 0
        if not tenorun2:
            tenorun2 = ''
        if not interest_tenor_unit:
            interest_tenor_unit = ''
        if not interest_tenor:
            interest_tenor = 0
        if not initial_amount:
            initial_amount = 0
        if not tndptamt:
            tndptamt = 0
        if not minimum_amount:
            minimum_amount = 0
        if not mintnr:
            mintnr = 0
        if not mintnrun:
            mintnrun = ''
        if not multdpt:
            multdpt = ''
        if not multwdr:
            multwdr = ''
        if not earlywdr:
            earlywdr = ''
        if not mintenr:
            mintenr = 0
        if not mintenrun:
            mintenrun = ''
        if not crint:
            crint = ''
        if not crinttnr:
            crinttnr = 0
        if not crinttnrun:
            crinttnrun = ''
        if not crintday:
            crintday = 0
        if not intacrrt:
            intacrrt = 0
        if not deposit_type:
            deposit_type = ''
        if not dptgrp:
            dptgrp = ''
        if not dptprp:
            dptprp = ''
        if not dptcls:
            dptcls = ''
        if not drmpr:
            drmpr = 0
        if not drmprun:
            drmprun = ''
        if not rllovr:
            rllovr = ''
        if not rovcat:
            rovcat = 0
        if not hdinttnr:
            hdinttnr = 0
        if not hdprntnr:
            hdprntnr = 0
        if not pbst:
            pbst = ''
        if not sttnr:
            sttnr = 0
        if not sttnrun:
            sttnrun = ''
        if not stfmt:
            stfmt = ''
        if not dptamt:
            dptamt = 0
        if not wdramt:
            wdramt = 0
        if not balance:
            balance = 0
        if not icbal:
            icbal = 0
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
        if not intnypd:
            intnypd = 0
        if not inamt:
            inamt = 0
        if not examt:
            examt = 0
        if not intpdcd:
            intpdcd = ''
        if not intac:
            intac = ''
        if not rvbalance:
            rvbalance = 0
        if not rvmavgamt:
            rvmavgamt = 0
        if not rvqavgamt:
            rvqavgamt = 0
        if not rvhavgamt:
            rvhavgamt = 0
        if not rvyavgamt:
            rvyavgamt = 0
        if not rvintamt:
            rvintamt = 0
        if not rintpaid:
            rintpaid = 0
        if not rintpre:
            rintpre = 0
        if not rvintpbl:
            rvintpbl = 0
        if not rvintdue:
            rvintdue = 0
        if not rvintovd:
            rvintovd = 0
        if not rvintspamt:
            rvintspamt = 0
        if not rvintnypd:
            rvintnypd = 0
        if not opndt:
            opndt = ''
        if not clsdt:
            clsdt = ''
        if not frdt:
            frdt = ''
        if not todt:
            todt = ''
        if not lastdt:
            lastdt = ''
        if not dpt_status:
            dpt_status = ''
        if not psts:
            psts = ''
        if not pbno:
            pbno = ''
        if not pbstatus:
            pbstatus = ''
        if not trfcd:
            trfcd = 0
        if not drmdt:
            drmdt = ''
        if not lintduedt:
            lintduedt = ''
        if not emkamt:
            emkamt = 0
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
        if not trftied:
            trftied = ''
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
        if not periodic:
            periodic = 0
        if not periodicun:
            periodicun = ''
        if not blkby:
            blkby = ''
        if not acrsd:
            acrsd = ''
        if not drmamt:
            drmamt = 0
        if not macno:
            macno = ''
        if not dptsubtype:
            dptsubtype = ''
        if not isiccd:
            isiccd = ''
        if not ldndt:
            ldndt = ''
        payload = {
            "id": id,
            "txrefid": txrefid,
            "txdt": txdt,
            "aprsts": aprsts,
            "defacno": defacno,
            "acno": acno,
            "branch_id": branch_id,
            "currency": currency,
            "account_name": account_name,
            "customer_id": customer_id,
            "customer_type": customer_type,
            "catalog_id": catalog_id,
            "secure_currency": secure_currency,
            "deposit_tenor": deposit_tenor,
            "deposit_tenor_unit": deposit_tenor_unit,
            "tenor": tenor,
            "tenorun": tenorun,
            "tenor2": tenor2,
            "tenorun2": tenorun2,
            "interest_tenor_unit": interest_tenor_unit,
            "interest_tenor": interest_tenor,
            "initial_amount": initial_amount,
            "tndptamt": tndptamt,
            "minimum_amount": minimum_amount,
            "mintnr": mintnr,
            "mintnrun": mintnrun,
            "multdpt": multdpt,
            "multwdr": multwdr,
            "earlywdr": earlywdr,
            "mintenr": mintenr,
            "mintenrun": mintenrun,
            "crint": crint,
            "crinttnr": crinttnr,
            "crinttnrun": crinttnrun,
            "crintday": crintday,
            "intacrrt": intacrrt,
            "deposit_type": deposit_type,
            "dptgrp": dptgrp,
            "dptprp": dptprp,
            "dptcls": dptcls,
            "drmpr": drmpr,
            "drmprun": drmprun,
            "rllovr": rllovr,
            "rovcat": rovcat,
            "hdinttnr": hdinttnr,
            "hdprntnr": hdprntnr,
            "pbst": pbst,
            "sttnr": sttnr,
            "sttnrun": sttnrun,
            "stfmt": stfmt,
            "dptamt": dptamt,
            "wdramt": wdramt,
            "balance": balance,
            "icbal": icbal,
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
            "intnypd": intnypd,
            "inamt": inamt,
            "examt": examt,
            "intpdcd": intpdcd,
            "intac": intac,
            "rvbalance": rvbalance,
            "rvmavgamt": rvmavgamt,
            "rvqavgamt": rvqavgamt,
            "rvhavgamt": rvhavgamt,
            "rvyavgamt": rvyavgamt,
            "rvintamt": rvintamt,
            "rintpaid": rintpaid,
            "rintpre": rintpre,
            "rvintpbl": rvintpbl,
            "rvintdue": rvintdue,
            "rvintovd": rvintovd,
            "rvintspamt": rvintspamt,
            "rvintnypd": rvintnypd,
            "opndt": opndt,
            "clsdt": clsdt,
            "frdt": frdt,
            "todt": todt,
            "lastdt": lastdt,
            "dpt_status": dpt_status,
            "psts": psts,
            "pbno": pbno,
            "pbstatus": pbstatus,
            "trfcd": trfcd,
            "drmdt": drmdt,
            "lintduedt": lintduedt,
            "emkamt": emkamt,
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
            "trftied": trftied,
            "usrid": usrid,
            "apuser": apuser,
            "crmid": crmid,
            "rmkfld": rmkfld,
            "refid": refid,
            "udfield1": udfield1,
            "periodic": periodic,
            "periodicun": periodicun,
            "blkby": blkby,
            "acrsd": acrsd,
            "drmamt": drmamt,
            "macno": macno,
            "dptsubtype": dptsubtype,
            "isiccd": isiccd,
            "ldndt": ldndt
        }
        return payload

    def advanced_search(self, txrefid=None, txdt=None, aprsts=None, defacno=None, acno=None, account_name=None, currency_code=None, customer_code=None, customer_type_caption=None, catalog_code=None, dpt_status=None, deposit_type=None, refid=None, page_index=None, page_size=None):
        if not txrefid:
            txrefid = ''
        if not txdt:
            txdt = None
        if not aprsts:
            aprsts = ''
        if not defacno:
            defacno = ''
        if not acno:
            acno = ''
        if not account_name:
            account_name = ''
        if not currency_code:
            currency_code = ''
        if not customer_code:
            customer_code = ''
        if not customer_type_caption:
            customer_type_caption = ''
        if not catalog_code:
            catalog_code = ''
        if not dpt_status:
            dpt_status = ''
        if not deposit_type:
            deposit_type = ''
        if not refid:
            refid = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "txrefid": txrefid,
            "txdt": txdt,
            "aprsts": aprsts,
            "defacno": defacno,
            "acno": acno,
            "account_name": account_name,
            "currency_code": currency_code,
            "customer_code": customer_code,
            "customer_type_caption": customer_type_caption,
            "catalog_code": catalog_code,
            "dpt_status": dpt_status,
            "deposit_type": deposit_type,
            "refid": refid,
            "page_index": page_index,
            "page_size": page_size
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

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload