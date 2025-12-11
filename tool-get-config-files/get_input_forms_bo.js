//requiring path and fs modules
const path = require("path");
const fs = require("fs");
const folderRawForms = "./raw_forms/bo";
const folderInputForms = "./input_forms/bo";
const pathRawForms = path.join(__dirname, folderRawForms);
const pathInputForms = path.join(__dirname, folderInputForms);


/**
 * Checks if a given `formId` represents a valid file type FO.
 *
 * @param {string} formId - The form id want to validate.
 * @returns {boolean} - `true` if the `formId` is considered a valid form type (i.e., it's NOT in the list of invalid types);
 * `false` if the `formId` is found in the list of invalid types.
 */
function isValidFormBO(formId) {
    const invalidformTypeArray = [
        "lookup",
        "posting",
        "O9_FEE",
        "ifccd",
        "pgoacc",
        "cibnk",
        "pgacc",
        "cifccd",
        "cbrcdc",
        "cctmcd",
        "cncat",
        "isiccd",
        "spl",
        "actgrp",
        "plcd",
        "usrcd",
        "sacno",
        "pdacc",
        "crnum",
        "pdoacc",
        "pdmacc",
        "ctlid",
        "Posting",
        "cbrid",
        "management",
        "crbank",
        "msgcode",
        "racno",
        "cnostro",
        "crbank3",
        "ctxg3",
        "ctxg4",
        "dlid",
        "pcacc",
        "benefbnk",
        "catcd",
        "ctrcd",
        "hcacc",
        "paybnk",
        "recacc",
        "rembnk",
        "payacc",
        "ifc",
        "cfrbnk",
        "issbnk",
        "splnm",
        "newhcacc",
        "advbnk",
        "pmtacc",
        "_SO",
        "_so"
    ]
    const containsInvalidType = invalidformTypeArray.some(invalidType => formId.includes(invalidType));
    return !containsInvalidType;
}

const formDataChange = fs
    .readdirSync(pathRawForms, { withFileTypes: true })
    .map((el) => el.name);
formDataChange.forEach(function (file) {
    let fileContents = fs.readFileSync(pathRawForms + "/" + file).toString();
    try {
        const jsonFileContents = JSON.parse(fileContents);
        const formContents = jsonFileContents[2].data[0];
        const formId = formContents.form_id;
        if (isValidFormBO(formId)) {
            const myArray = [formContents]
                
            fs.writeFile(pathInputForms + "/" + formId + ".json", JSON.stringify(myArray, null, 4), function (err) {
                if (err) throw err;
            });
        }
    } catch (error) {
        console.error("Error: ", error);
    }
});

console.info("Input Forms BO converted!");