//requiring path and fs modules
const path = require("path");
const fs = require("fs");
const folderInputForms = "./input_forms/bo";
const folderConfigFiles = "./config_files";
const pathInputForms = path.join(__dirname, folderInputForms);
const pathConfigFiles = path.join(__dirname, folderConfigFiles);

/**
 * Convert string to string with format snake_case.
 * Example: "Accounting Type" -> "accounting_type", "DPT-Account Information-View" -> "dpt_account_information_view"
 * @param {string} str - string
 * @returns {string} `convertStr` - string with format snake_case.
 */
function toSnakeCase(str) {
    if (!str) return "";
    let convertStr = str.toLowerCase().replaceAll('-', ' ')
    convertStr = convertStr.toLowerCase().replaceAll('/', ' ')
    convertStr = convertStr.toLowerCase().replace(/\s+/g, '_').replace(/[^a-z0-9_]/g, '')
    return convertStr;
}

/**
 * Convert to `field_list` for form type FO
 *
 * @param {string} jsonFileContents - data under node `list_layout`
 * @param {string} transactionCode - value of key `form_id`
 * @returns {Object} `field_list` array object
 */
function convertToFieldListBO(jsonFileContents, transactionCode) {
    let fieldList = []; // Array to store the final list of fields after conversion
    // const fieldListDisable = [];
    // const fieldListEnable = [];
    let configFiles = {};
    let i = 1;
    let formId = "";
    let formTitle = "";
    for (const formContents of jsonFileContents) {
        const listLayout = formContents.list_layout;
        const formInfo = JSON.parse(formContents.info);
        formId = formContents.form_id;
        formTitle = formInfo.title;
        const fieldsDisable = getFieldsDisable(formInfo.ruleStrong);
        const fieldsInvisible = getFieldsInvisible(formInfo.ruleStrong);
        if (!listLayout || typeof listLayout !== 'string') {
            return configFiles;
        }
        let listLayoutObjects;
        // converting a JSON string into a JavaScript object or array.
        try {
            listLayoutObjects = JSON.parse(listLayout);
        } catch (error) {
            console.error("Error during conversion to JS object or array: ", error.message);
            return configFiles;
        }
        const fieldsIsGroupDisable = getFieldsIsGroup(listLayoutObjects, fieldsDisable);
        const fieldsIsGroupInvisible = getFieldsIsGroup(listLayoutObjects, fieldsInvisible);
        // Check listLayoutObjects is an array
        if (!Array.isArray(listLayoutObjects)) {
            console.error("Error: JSON structure is not an array.");
            return configFiles;
        }
        let orderCounter = 1;
        let orderListView = 1;
        let isGroup = "";
        for (const listLayoutObj of listLayoutObjects) {
            // check `list_view` exists and is an array
            if (listLayoutObj?.list_view && Array.isArray(listLayoutObj.list_view)) {
                for (const viewObj of listLayoutObj.list_view) {
                    // check `list_input` exists and is an array
                    let tabName = "";
                    let borderName = "";
                    if (viewObj?.list_input && Array.isArray(viewObj.list_input)) {
                        if ((String(viewObj?.condition) !== "`1`!==`1`") && (String(viewObj?.condition) !== "1!==1")) {
                            if (String(viewObj.isBorder) === "true") {
                                borderName = viewObj.name;
                            }
                            if (String(viewObj.isTab) === "true") {
                                tabName = viewObj.name;
                            }
                            for (const inputItem of viewObj.list_input) {
                                if (hasField(inputItem.default.code, fieldsIsGroupDisable) || hasField(inputItem.default.code, fieldsIsGroupInvisible)) {
                                    isGroup = "y";
                                } else {
                                    isGroup = "";
                                }
                                if (!hasField(inputItem.default.code, fieldsInvisible)) {
                                    if (isValidInputType(inputItem.inputtype)){
                                        if (!hasField(inputItem.default.code, fieldsDisable)) {
                                            const field = getFieldBO(inputItem, "y", borderName, orderCounter, isGroup, tabName);
                                            // fieldListEnable.push(field);
                                            fieldList.push(field);
                                        } else {
                                            const field = getFieldBO(inputItem, "n", borderName, orderCounter, isGroup, tabName);
                                            // fieldListDisable.push(field);
                                            fieldList.push(field);
                                        }
                                    }
                                }
                                orderCounter++;
                            }
                        }
                    } else {
                        console.warn("'list_view' already exists, 'list_input' is not an array or null.");
                    }
                    orderListView++;
                }
            } else {
                console.warn("'list_layout' already exists, 'list_view' is not an array or null.");
            }
        }
        i++;
        if (formId !== formTitle) {
            formId = formId;
            formTitle = formTitle;
        } else {
            formId = "";
            formTitle = "";
        }
    }
    // fieldList = [...fieldListEnable, ...fieldListDisable];
    if (fieldList.length === 0){
        return configFiles;
    } else {
        configFiles = {
            "template": "./ui_test/bo_form_action.sbn",
            "transaction_code": transactionCode,
            "transaction_name": formTitle,
            "form_title": formTitle,
            "field_list": fieldList
        }
        return configFiles;
    }
}

function getFieldBO(inputItem, isEnable, borderName, orderCounter, isGroup, tabName){
    let fieldType = "not_found";
    let fieldTitle = inputItem.default.name;
    let fieldValue = toSnakeCase(fieldTitle.trim());
    let valueInput = "";
    let collapName = "";
    let fieldMethod = "";
    let valueDefault = "";
    let decimalNumber = "";
    let maskType = "";
    let isMulti = "";
    let isRequired = "";
    let isLookup = "";
    let maxLength = "";
    let minLength = "";
    let orderNumber = "";
    let isReplace = "";
    let replaceBy = "";
    let outMethod = "";
    let viewMethod = "";
    let maskMethod = "";

    if (inputItem.inputtype === "cTextInput") {
        if ((String(inputItem.config?.autoWrap) === "true") || (inputItem.config?.is_password !== "true" && inputItem.config?.isSearch !== "true" && inputItem.config?.isLookup !== "true")) {
            fieldType = "text";
            if (fieldTitle === "Description") {
                valueInput = "'AUTO TEST'";
            }
        } else {
            fieldType = "input";
        }
    } else if (inputItem.inputtype === "cTextArea") {
        fieldType = "text_multi";
    } else if (inputItem.inputtype === "jCheckbox") {
        fieldType = "checkbox";
        valueInput = "False";
        if (fieldTitle.startsWith("Caution!") === true) {
            fieldValue = "";
        }
    } else if (inputItem.inputtype === "jRadioBox") {
        fieldType = "radio";
        valueInput = "False";
    } else if (inputItem.inputtype === "jMaskInput") {
        if (inputItem.config?.mask_mode === "default") {
            fieldType = "input";
        } else if (inputItem.config?.mask_mode === "date") {
            fieldType = "date";
        } else if (inputItem.config?.mask_mode === "time") {
            fieldType = "time";
        }
    } else if (inputItem.inputtype === "jCurrency") {
        fieldType = "number";
    } else if (inputItem.inputtype === "jSelect") {
        fieldType = "select";
    } else if (inputItem.inputtype === "jSelectMulti") {
        fieldType = "select_multi";
    } else if (inputItem.inputtype === "jMutiValue") {
        fieldType = "";
        fieldValue = "";
        collapName = fieldTitle;
    } else if (inputItem.inputtype === "jListCheckBox") {
        fieldType = "";
        fieldValue = "";
        collapName = fieldTitle;
    }

    valueDefault = inputItem.config?.data_default ?? "";
    decimalNumber = (inputItem.inputtype === "jCurrency" && inputItem.config?.decimal_length != null) ? inputItem.config.decimal_length : "";
    maskType = inputItem.config?.mask_format ?? "";
    // isMulti = (inputItem.config?.structable.startsWith("muti.") === true) ? "y" : "";
    isRequired = (String(inputItem.validate?.request) === "true") ? "y" : "";
    isLookup = (String(inputItem.config?.isLookup) === "true") ? "y" : "";
    maxLength = inputItem.validate?.max !== undefined && inputItem.validate?.max !== null ? String(inputItem.validate.max) : "";
    minLength = inputItem.validate?.min !== undefined && inputItem.validate?.min !== null ? String(inputItem.validate.min) : "";
    orderNumber = String(orderCounter);

    // switch (true) {
    //     case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bw";
    //         break;
    //     case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bws";
    //         break;
    //     case fieldType === "input" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwg";
    //         break;
    //     case fieldType === "input" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwgs";
    //         break;
    //     case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwm";
    //         break;
    //     case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         fieldMethod = "bwms";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bav";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bavs";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bavg";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bavgs";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         fieldMethod = "bavm";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         fieldMethod = "bavm";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         fieldMethod = "bavb";
    //         break;
    //     case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         fieldMethod = "bavb";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwt";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwts";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwtg";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwtgs";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwtm";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         fieldMethod = "bwtms";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         fieldMethod = "bwtb";
    //         break;
    //     case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         fieldMethod = "bwtb";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bat";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bats";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "batg";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "batgs";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         fieldMethod = "batm";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         fieldMethod = "batm";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         fieldMethod = "batb";
    //         break;
    //     case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         fieldMethod = "batb";
    //         break;
    //     case fieldType === "text_multi" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwtml";
    //         break;
    //     case fieldType === "text_multi" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwtml";
    //         break;
    //     case fieldType === "text_multi" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "batml";
    //         break;
    //     case fieldType === "text_multi" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "batml";
    //         break;
    //     case fieldType === "date" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwd";
    //         break;
    //     case fieldType === "date" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwds";
    //         break;
    //     case fieldType === "date" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bad";
    //         break;
    //     case fieldType === "date" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bads";
    //         break;
    //     case fieldType === "number" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwn";
    //         break;
    //     case fieldType === "number" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwns";
    //         break;
    //     case fieldType === "number" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bwng";
    //         break;
    //     case fieldType === "number" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bwngs";
    //         break;
    //     case fieldType === "number" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bav";
    //         break;
    //     case fieldType === "number" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bavs";
    //         break;
    //     case fieldType === "number" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bavg";
    //         break;
    //     case fieldType === "number" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bavgs";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bs";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bss";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bsg";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bsgs";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         fieldMethod = "bsc";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         fieldMethod = "bsc";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         fieldMethod = "bsb";
    //         break;
    //     case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         fieldMethod = "bsb";
    //         break;
    //     case fieldType === "select" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bas";
    //         break;
    //     case fieldType === "select" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bass";
    //         break;
    //     case fieldType === "select" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "basg";
    //         break;
    //     case fieldType === "select" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "basgs";
    //         break;
    //     case fieldType === "select" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         fieldMethod = "bavb";
    //         break;
    //     case fieldType === "select" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         fieldMethod = "bavb";
    //         break;
    //     case fieldType === "select_multi" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bsm";
    //         break;
    //     case fieldType === "select_multi" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bsm";
    //         break;
    //     case fieldType === "select_multi" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "basm";
    //         break;
    //     case fieldType === "select_multi" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "basm";
    //         break;
    //     case fieldType === "checkbox" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bcc";
    //         break;
    //     case fieldType === "checkbox" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bccs";
    //         break;
    //     case fieldType === "checkbox" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         fieldMethod = "bac";
    //         break;
    //     case fieldType === "checkbox" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         fieldMethod = "bac";
    //         break;
    // }

    // switch (true) {
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgv";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgvs";
    //         break;
    //     case fieldType === "input" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgvg";
    //         break;
    //     case fieldType === "input" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgvgs";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         outMethod = "bgvm";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         outMethod = "bgvm";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         outMethod = "bgvb";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         outMethod = "bgvb";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgv";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgvs";
    //         break;
    //     case fieldType === "number" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgvg";
    //         break;
    //     case fieldType === "number" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgvgs";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         outMethod = "bgvm";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         outMethod = "bgvm";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         outMethod = "bgvb";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         outMethod = "bgvb";
    //         break;
    //     case fieldType === "date" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgd";
    //         break;
    //     case fieldType === "date" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgds";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgs";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgss";
    //         break;
    //     case fieldType === "select" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgsg";
    //         break;
    //     case fieldType === "select" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgsgs";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         outMethod = "bgvb";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         outMethod = "bgvb";
    //         break;
    //     case fieldType === "select_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgsm";
    //         break;
    //     case fieldType === "select_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgsm";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgt";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgts";
    //         break;
    //     case fieldType === "text" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgtg";
    //         break;
    //     case fieldType === "text" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgtgs";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         outMethod = "bgtm";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         outMethod = "bgtm";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         outMethod = "bgtb";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         outMethod = "bgtb";
    //         break;
    //     case fieldType === "text_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         outMethod = "bgtml";
    //         break;
    //     case fieldType === "text_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         outMethod = "bgtml";
    //         break;
    // }

    // switch (true) {
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bav";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bavs";
    //         break;
    //     case fieldType === "input" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bavg";
    //         break;
    //     case fieldType === "input" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bavgs";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         viewMethod = "bavm";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         viewMethod = "bavm";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         viewMethod = "bavb";
    //         break;
    //     case fieldType === "input" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         viewMethod = "bavb";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bav";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bavs";
    //         break;
    //     case fieldType === "number" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bavg";
    //         break;
    //     case fieldType === "number" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bavgs";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         viewMethod = "bavm";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         viewMethod = "bavm";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         viewMethod = "bavb";
    //         break;
    //     case fieldType === "number" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         viewMethod = "bavb";
    //         break;
    //     case fieldType === "date" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bad";
    //         break;
    //     case fieldType === "date" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bads";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bas";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bass";
    //         break;
    //     case fieldType === "select" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "basg";
    //         break;
    //     case fieldType === "select" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "basgs";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         viewMethod = "bavb";
    //         break;
    //     case fieldType === "select" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         viewMethod = "bavb";
    //         break;
    //     case fieldType === "select_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "basm";
    //         break;
    //     case fieldType === "select_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "basm";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bat";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bats";
    //         break;
    //     case fieldType === "text" && isGroup === "y" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "batg";
    //         break;
    //     case fieldType === "text" && isGroup === "y" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "batgs";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "y" && borderName === "" && tabName !== "":
    //         viewMethod = "batm";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "y" && borderName === "" && tabName === "":
    //         viewMethod = "batm";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName !== "" && tabName !== "":
    //         viewMethod = "batb";
    //         break;
    //     case fieldType === "text" && isGroup === "" && isMulti === "" && borderName !== "" && tabName === "":
    //         viewMethod = "batb";
    //         break;
    //     case fieldType === "text_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "batml";
    //         break;
    //     case fieldType === "text_multi" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "batml";
    //         break;
    //     case fieldType === "checkbox" && isGroup === "" && isMulti === "" && borderName === "" && tabName !== "":
    //         viewMethod = "bac";
    //         break;
    //     case fieldType === "checkbox" && isGroup === "" && isMulti === "" && borderName === "" && tabName === "":
    //         viewMethod = "bac";
    //         break;
    // }

    switch (true) {
        case maskType === "$MASK_DEPOSIT_ACNO_FO$":
            maskMethod = "deposit_account_number_mask";
            break;
        case maskType === "99-999-999999-9":
            maskMethod = "deposit_account_number_mask";
            break;
        case maskType === "_-_-______":
            maskMethod = "customer_code_mask";
            break;
        case maskType === "$MASK_CUSTOMERCD$":
            maskMethod = "customer_code_mask";
            break;
        case maskType === "$FO_ACNO_POSTING$":
            maskMethod = "gl_account_number_mask";
            break;
        case maskType === "$MASK_TRS_ACNO$":
            maskMethod = "treasury_account_number_mask";
            break;
        case maskType === "$MASK_TRD_ACNO$":
            maskMethod = "trade_account_number_mask";
            break;
        case maskType === "$$MASK_TRD_ACNO$$":
            maskMethod = "trade_account_number_mask";
            break;
        case maskType === "$MASK_CREDIT_ACNO$":
            maskMethod = "credit_account_number_mask";
            break;
        case maskType === "____-______-_-__":
            maskMethod = "product_limit_code_mask";
            break;
        case maskType === "____-______-_-__-__":
            maskMethod = "sub_product_limit_code_mask";
            break;
        case maskType === "$MASK_STOCK_NO$":
            maskMethod = "stock_number_mask";
            break;
        case maskType === "$MASK_STOCK_NO_PMT$":
            maskMethod = "stock_number_mask";
            break;
        case maskType === "__-__________":
            maskMethod = "stock_number_mask";
            break;
        case maskType === "$MASK_MORTGAGE_ACNO$":
            maskMethod = "mortgage_account_number_mask";
            break;
        case maskType === "$MASK_FAC_ACNO$":
            maskMethod = "fixed_asset_account_number_mask";
            break;
    }

    const field = {
        title: fieldTitle,
        value: fieldValue,
        field_type: fieldType,
        field_method: fieldMethod,
        value_default: valueDefault,
        decimal_number: decimalNumber,
        mask_type: maskType,
        collap_name: collapName,
        border_name: borderName,
        tab_name: tabName,
        is_enable: isEnable,
        is_group: isGroup,
        is_multi: isMulti,
        is_required: isRequired,
        is_lookup: isLookup,
        max_length: maxLength,
        min_length: minLength,
        order_number: orderNumber,
        is_wait: "",
        is_replace: isReplace,
        replace_by: replaceBy,
        return: "",
        out_method: outMethod,
        view_method: viewMethod,
        mask_method: maskMethod,
        value_input: valueInput
    };

    return field;
}

/**
 * Gathers and returns a unique list of field names that are configured as "invisible"
 * (`visible: "false"`) from an input JSON array.
 * This function specifically processes fields from items where 'code' is either "visibility"
 * or "managerComponent" and 'isStart' is true.
 *
 * @param {Array<Object>} jsonArray - An array of JSON objects, data under node `info.ruleStrong`
 * @returns {Array<string>} `fieldsInvisible` - A unique array of strings containing the names of the invisible fields.
 */
function getFieldsInvisible(jsonArray) {
    let fieldsInvisible = []; // Array to store the final list of invisible fields
    if (!Array.isArray(jsonArray)) {
        console.error("Error getFieldsInvisible: jsonArray is not a valid Array.");
        return fieldsInvisible;
    }
    let finalArray = [];
    for (const item of jsonArray) {
        if (String(item.isStart) === "true" && (item.code=="visibility" || item.code== "managerComponent")) {
            if (String(item.config.visible) === "false") {
                const tempArray = item.config.component_result.split(';');
                finalArray = finalArray.concat(tempArray)
            }
        }
    }
    const filteredArray = finalArray.filter(item => item !== "");
    fieldsInvisible = [...new Set(filteredArray)];
    return fieldsInvisible;
}

/**
 * Gathers and returns a unique list of field names that are configured as "disable"
 * (`"ena_dis": "true"`) from an input JSON array.
 * This function specifically processes fields from items where 'code' is either "visibility"
 * or "managerComponent" and 'isStart' is true.
 *
 * @param {Array<Object>} jsonArray - An array of JSON objects, data under node `info.ruleStrong`
 * @returns {Array<string>} `fieldsDisableNotInvisible` - A unique array of strings containing the names of the disable fields.
 */
function getFieldsDisable(jsonArray) {
    let fieldsDisableNotInvisible = []; // Array to store the final list of disable fields
    if (!Array.isArray(jsonArray)) {
        console.error("Error in getFieldsDisable: jsonArray is not a valid Array.");
        return fieldsDisableNotInvisible;
    }
    let finalArray = [];
    for (const item of jsonArray) {
        if (String(item.isStart) === "true" && (item.code=="visibility" || item.code== "managerComponent")) {
            if (String(item.config.ena_dis) === "true") {
                const tempArray = item.config.component_result.split(';');
                finalArray = finalArray.concat(tempArray)
            }
        }
    }
    const filteredArray = finalArray.filter(item => item !== "");
    const fieldsDisable = [...new Set(filteredArray)];
    let fieldsInvisible = getFieldsInvisible(jsonArray)
    const invisibleSet = new Set(fieldsInvisible);
    fieldsDisableNotInvisible = fieldsDisable.filter(field => !invisibleSet.has(field));
    return fieldsDisableNotInvisible;
}

/**
 * Checks if a specific field name exists within an array of field names.
 *
 * @param {string} fieldName - The name of the field to search for.
 * @param {Array<string>} fieldArray - The array of field names (strings) to search within.
 * @returns {boolean} `true` if the `fieldName` is found in the `fieldArray`, `false` otherwise.
 */
function hasField(fieldName, fieldArray) {
    return fieldArray.includes(fieldName);
}

/**
 * Checks if a given `inputType` represents a valid input type.
 *
 * @param {string} inputType - The input type want to validate.
 * @returns {boolean} - `true` if the `inputType` is considered a valid input type (i.e., it's NOT in the list of invalid types);
 * `false` if the `inputType` is found in the list of invalid types.
 */
function isValidInputType(inputType) {
    const invalidInputTypeArray = [
        "jLabel",
        "jSameMain",
        "jSignature",
        "cTableDefault",
        "jTableForm",
        "jPrintVoucher",
        "jProgressBar",
        "cButton",
        "jTableSearch",
        "jListActivity",
        "jButtonSignature",
        "jFullCalendar",
        "cView",
        "cLayout",
        "jUploadFileAndView"
    ]
    return !invalidInputTypeArray.includes(inputType);
}

function getFieldsIsGroup(listLayoutObjects, fieldsInvisible) {
    const groupedFieldList = [];
    for (const listLayoutObj of listLayoutObjects) {
        if (listLayoutObj?.list_view && Array.isArray(listLayoutObj.list_view)) {
            for (const viewObj of listLayoutObj.list_view) {
                if (viewObj?.list_input && Array.isArray(viewObj.list_input)) {
                    let i = 0;
                    while (i < viewObj.list_input.length) {
                        const inputItem = viewObj.list_input[i];
                        const currentOfGroup = inputItem.default?.ofgroup?.trim() ?? "";
                        const potentialGroupItems = [];
                        if (currentOfGroup !== "") {
                            let j = i;
                            while (j < viewObj.list_input.length) {
                                const potentialItem = viewObj.list_input[j];
                                const potentialOfGroup = potentialItem?.default?.ofgroup?.trim() ?? "";
                                if (potentialOfGroup === currentOfGroup) {
                                    potentialGroupItems.push(potentialItem);
                                    j++;
                                } else {
                                    break;
                                }
                            }
                            if (potentialGroupItems.length >= 2) {
                                for (const item of potentialGroupItems) {
                                    if (!hasField(item.default.code, fieldsInvisible)) {
                                        if (isValidInputType(item.inputtype)){
                                            groupedFieldList.push(item.default.code);
                                        }
                                    }
                                }
                            }
                            i = j;
                        } else {
                            i++;
                        }
                    }
                }
            }
        }
    }
    return groupedFieldList;
}

const formDataChange = fs
    .readdirSync(pathInputForms, { withFileTypes: true })
    .map((el) => el.name);
formDataChange.forEach(function (file) {
    let fileContents = fs.readFileSync(pathInputForms + "/" + file).toString();
    try {
        const jsonFileContents = JSON.parse(fileContents);
        const formType = file.split('.')[0].substring(0, 2);
        if (formType !== 'FO' || formType !== 'fo') {
            const transactionCode = file.split('.')[0].substring(3);
            const ConfigFilesNname = toSnakeCase(transactionCode);
            const convertedFields = convertToFieldListBO(jsonFileContents, transactionCode);
            if (Object.keys(convertedFields).length !== 0) {
                const configFiles = {
                    ...convertedFields,
                    "menu_level_01": "",
                    "menu_level_02": "",
                    "menu_level_03": "",
                    "add_fee": "",
                    "field_fee": []
                }
                fs.writeFile(pathConfigFiles + "/bo/form_action/" + ConfigFilesNname + ".py.jcodegen.json", JSON.stringify(configFiles, null, 4), function (err) {
                    if (err) throw err;
                });
            }
        }
    } catch (error) {
        console.error("Error: ", error);
    }
});
console.info("Config Files BO converted!");
