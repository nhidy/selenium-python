//requiring path and fs modules
const path = require("path");
const fs = require("fs");
const folderInputForms = "./input_forms/fo";
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
function convertToFieldListFO(jsonFileContents, transactionCode) {
    let fieldList = []; // Array to store the final list of fields after conversion
    const fieldListDisable = [];
    const fieldListEnable = [];
    let configFiles = {};
    let i = 1;
    let formId = "";
    let formTitle = "";
    for (const formContents of jsonFileContents) {
        // // DEBUG
        // fs.writeFile(pathConfigFiles + "/fo/" + transactionCode + "_1_" + i + "_info.json", JSON.stringify(formContents.info, null, 4), function (err) {
        //     if (err) throw err;
        // });
        // // DEBUG
        // fs.writeFile(pathConfigFiles + "/fo/" + transactionCode + "_1_" + i + "_list_layout.json", JSON.stringify(formContents.list_layout, null, 4), function (err) {
        //     if (err) throw err;
        // });
        // i ++;
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
        // console.warn("Form Id: ", formId);
        // console.warn("Form Title: ", formTitle);
        // DEBUG
        // fs.writeFile(pathConfigFiles + "/fo/" + formId + "_1_" + i + "_field_is_group.json", JSON.stringify(fieldsIsGroup, null, 4), function (err) {
        //     if (err) throw err;
        // });
        // i++;
        // Check listLayoutObjects is an array
        if (!Array.isArray(listLayoutObjects)) {
            console.error("Error: JSON structure is not an array.");
            return configFiles;
        }
        let orderCounter = 1;
        let orderListView = 1;
        let isGroup = "";
        for (const listLayoutObj of listLayoutObjects) {
            // DEBUG
            // fs.writeFile(pathConfigFiles + "/fo/" + transactionCode + "_1_" + i + "_data_listLayoutObj.json", JSON.stringify(listLayoutObj, null, 4), function (err) {
            //     if (err) throw err;
            // });
            // check `list_view` exists and is an array
            if (listLayoutObj?.list_view && Array.isArray(listLayoutObj.list_view)) {
                // DEBUG
                // fs.writeFile(pathConfigFiles + "/fo/" + formId + "_1_" + i + "_list_view.json", JSON.stringify(listLayoutObj.list_view, null, 4), function (err) {
                //     if (err) throw err;
                // });
                for (const viewObj of listLayoutObj.list_view) {
                    // check `list_input` exists and is an array
                    let borderName = "";
                    if (viewObj?.list_input && Array.isArray(viewObj.list_input)) {
                        // DEBUG
                        // fs.writeFile(pathConfigFiles + "/viewObj/" + formId + "_2_" + i + "_" + orderListView + "_viewObj.json", JSON.stringify(viewObj, null, 4), function (err) {
                        //     if (err) throw err;
                        // });
                        if (String(viewObj.isBorder) === "true") {
                            borderName = viewObj.name;
                        }
                        for (const inputItem of viewObj.list_input) {
                            if (hasField(inputItem.default.code, fieldsIsGroupDisable) || hasField(inputItem.default.code, fieldsIsGroupInvisible)) {
                                isGroup = "y";
                            } else {
                                isGroup = "";
                            }
                            // DEBUG
                            // fs.writeFile(pathConfigFiles + "/inputItem/" + transactionCode + "_" + orderCounter + "_inputItem.json", JSON.stringify(inputItem, null, 4), function (err) {
                            //     if (err) throw err;
                            // });
                            if (!hasField(inputItem.default.code, fieldsInvisible)) {
                                if (isValidInputType(inputItem.inputtype)){
                                    if (!hasField(inputItem.default.code, fieldsDisable)) {
                                        // DEBUG
                                        // fs.writeFile(pathConfigFiles + "/fo/" + transactionCode + "_3_" + i + "_" + orderListView + "_" + orderCounter + borderName + "_enable.json", JSON.stringify(inputItem, null, 4), function (err) {
                                        //     if (err) throw err;
                                        // });
                                        const field = getFieldFO(inputItem, "y", borderName, orderCounter, isGroup);
                                        fieldListEnable.push(field);
                                    } else {
                                        // DEBUG
                                        // fs.writeFile(pathConfigFiles + "/fo/" + transactionCode + "_4_" + i + "_" + orderListView + "_" + orderCounter + borderName + "_disable.json", JSON.stringify(inputItem, null, 4), function (err) {
                                        //     if (err) throw err;
                                        // });
                                        const field = getFieldFO(inputItem, "n", borderName, orderCounter, isGroup);
                                        fieldListDisable.push(field);
                                    }
                                }
                            }
                            orderCounter++;
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
    fieldList = [...fieldListEnable, ...fieldListDisable];
    configFiles = {
        "template": "./ui_test/fo_form_action.sbn",
        "transaction_code": transactionCode,
        "transaction_name": formTitle,
        "form_title": formTitle,
        "field_list": fieldList
    }
    return configFiles;
}

function getFieldFO(inputItem, isEnable, borderName, orderCounter, isGroup){
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
    } else if (inputItem.inputtype === "jMaskInputVer2") {
        fieldType = "input";
    } else if (inputItem.inputtype === "jMaskAdvanced") {
        fieldType = "input";
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

    valueDefault = inputItem.config.data_default ?? "";
    decimalNumber = (inputItem.inputtype === "jCurrency" && inputItem.config?.decimal_length != null) ? inputItem.config.decimal_length : "";
    maskType = inputItem.config?.mask_format ?? "";
    isMulti = (inputItem.config?.structable.startsWith("muti.") === true) ? "y" : "";
    isRequired = (String(inputItem.validate?.request) === "true") ? "y" : "";
    isLookup = (String(inputItem.config?.isLookup) === "true") ? "y" : "";
    maxLength = inputItem.validate?.max !== undefined && inputItem.validate?.max !== null ? String(inputItem.validate.max) : "";
    minLength = inputItem.validate?.min !== undefined && inputItem.validate?.min !== null ? String(inputItem.validate.min) : "";
    orderNumber = String(orderCounter);

    switch (true) {
        case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fw";
            break;
        case fieldType === "input" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "fwg";
            break;
        case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "":
            fieldMethod = "fwm";
            break;
        case fieldType === "input" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "fwb";
            break;
        case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fav";
            break;
        case fieldType === "input" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "favg";
            break;
        case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "y" && borderName === "":
            fieldMethod = "favm";
            break;
        case fieldType === "input" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "favb";
            break;
        case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fwt";
            break;
        case fieldType === "text" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "fwtg";
            break;
        case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "y" && borderName === "":
            fieldMethod = "fwtm";
            break;
        case fieldType === "text" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "fwtb";
            break;
        case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fat";
            break;
        case fieldType === "text" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "fatg";
            break;
        case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "y" && borderName === "":
            fieldMethod = "fatm";
            break;
        case fieldType === "text" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "fatb";
            break;
        case fieldType === "text_multi" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fwtml";
            break;
        case fieldType === "text_multi" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fatml";
            break;
        case fieldType === "date" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fwd";
            break;
        case fieldType === "date" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "fwdb";
            break;
        case fieldType === "date" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fad";
            break;
        case fieldType === "date" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "favb";
            break;
        case fieldType === "number" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fwn";
            break;
        case fieldType === "number" && isEnable === "y" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "fwng";
            break;
        case fieldType === "number" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "fwnb";
            break;
        case fieldType === "number" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fav";
            break;
        case fieldType === "number" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "favg";
            break;
        case fieldType === "number" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "favb";
            break;
        case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fs";
            break;
        case fieldType === "select" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "fsb";
            break;
        case fieldType === "select" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fas";
            break;
        case fieldType === "select" && isEnable === "n" && isGroup === "y" && isMulti === "" && borderName === "":
            fieldMethod = "fasg";
            break;
        case fieldType === "select" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName !== "":
            fieldMethod = "favb";
            break;
        case fieldType === "select_multi" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fsm";
            break;
        case fieldType === "select_multi" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fasm";
            break;
        case fieldType === "checkbox" && isEnable === "y" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fcc";
            break;
        case fieldType === "checkbox" && isEnable === "n" && isGroup === "" && isMulti === "" && borderName === "":
            fieldMethod = "fac";
            break;
    }

    switch (true) {
        case fieldType === "input" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgv";
            break;
        case fieldType === "input" && isGroup === "y" && isMulti === "" && borderName === "":
            outMethod = "fgvg";
            break;
        case fieldType === "input" && isGroup === "" && isMulti === "y" && borderName === "":
            outMethod = "fgvm";
            break;
        case fieldType === "input" && isGroup === "" && isMulti === "" && borderName !== "":
            outMethod = "fgvb";
            break;
        case fieldType === "number" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgv";
            break;
        case fieldType === "number" && isGroup === "y" && isMulti === "" && borderName === "":
            outMethod = "fgvg";
            break;
        case fieldType === "number" && isGroup === "" && isMulti === "y" && borderName === "":
            outMethod = "fgvm";
            break;
        case fieldType === "number" && isGroup === "" && isMulti === "" && borderName !== "":
            outMethod = "fgvb";
            break;
        case fieldType === "date" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgd";
            break;
        case fieldType === "select" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgs";
            break;
        case fieldType === "select" && isGroup === "y" && isMulti === "" && borderName === "":
            outMethod = "fgsg";
            break;
        case fieldType === "select" && isGroup === "" && isMulti === "" && borderName !== "":
            outMethod = "fgvb";
            break;
        case fieldType === "select_multi" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgsm";
            break;
        case fieldType === "text" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgt";
            break;
        case fieldType === "text" && isGroup === "y" && isMulti === "" && borderName === "":
            outMethod = "fgtg";
            break;
        case fieldType === "text" && isGroup === "" && isMulti === "y" && borderName === "":
            outMethod = "fgtm";
            break;
        case fieldType === "text" && isGroup === "" && isMulti === "" && borderName !== "":
            outMethod = "fgtb";
            break;
        case fieldType === "text_multi" && isGroup === "" && isMulti === "" && borderName === "":
            outMethod = "fgtml";
            break;
    }

    switch (true) {
        case fieldType === "input" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fav";
            break;
        case fieldType === "input" && isGroup === "y" && isMulti === "" && borderName === "":
            viewMethod = "favg";
            break;
        case fieldType === "input" && isGroup === "" && isMulti === "y" && borderName === "":
            viewMethod = "favm";
            break;
        case fieldType === "input" && isGroup === "" && isMulti === "" && borderName !== "":
            viewMethod = "favb";
            break;
        case fieldType === "number" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fav";
            break;
        case fieldType === "number" && isGroup === "y" && isMulti === "" && borderName === "":
            viewMethod = "favg";
            break;
        case fieldType === "number" && isGroup === "" && isMulti === "y" && borderName === "":
            viewMethod = "favm";
            break;
        case fieldType === "number" && isGroup === "" && isMulti === "" && borderName !== "":
            viewMethod = "favb";
            break;
        case fieldType === "date" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fad";
            break;
        case fieldType === "select" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fas";
            break;
        case fieldType === "select" && isGroup === "y" && isMulti === "" && borderName === "":
            viewMethod = "fasg";
            break;
        case fieldType === "select" && isGroup === "" && isMulti === "" && borderName !== "":
            viewMethod = "favb";
            break;
        case fieldType === "select_multi" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fasm";
            break;
        case fieldType === "text" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fat";
            break;
        case fieldType === "text" && isGroup === "y" && isMulti === "" && borderName === "":
            viewMethod = "fatg";
            break;
        case fieldType === "text" && isGroup === "" && isMulti === "y" && borderName === "":
            viewMethod = "fatm";
            break;
        case fieldType === "text" && isGroup === "" && isMulti === "" && borderName !== "":
            viewMethod = "fatb";
            break;
        case fieldType === "text_multi" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fatml";
            break;
        case fieldType === "checkbox" && isGroup === "" && isMulti === "" && borderName === "":
            viewMethod = "fac";
            break;
    }

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

function isJson(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
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
        "cButton"
    ]
    return !invalidInputTypeArray.includes(inputType);
}

/**
 * Checks if a given `formId` represents a valid file type FO.
 *
 * @param {string} formId - The form id want to validate.
 * @returns {boolean} - `true` if the `formId` is considered a valid form type (i.e., it's NOT in the list of invalid types);
 * `false` if the `formId` is found in the list of invalid types.
 */
function isValidFormFO(formId) {
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
        "pmtacc"
    ]
    const containsInvalidType = invalidformTypeArray.some(invalidType => formId.includes(invalidType));
    return !containsInvalidType;
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
        if (formType === 'BO' || formType === 'bo') {
            // const convertedFields = convertJsonToFieldListWithOrder(listLayout);
            // const convertedFields = convertToFieldListBO(listLayout, formId, fieldsDisable, fieldsInvisible);
            // const ConfigFilesNname = toSnakeCase(formTitle);
            // console.warn("ConfigFilesNname BO: ", ConfigFilesNname);
            // console.warn("convertedFields:", convertedFields);
            // fs.writeFile(pathConfigFiles + "/bo/" + ConfigFilesNname + ".py.jcodegen.json", JSON.stringify(convertedFields, null, 4), function (err) {
            //     if (err) throw err;
            // });
        }

        if (formType === 'FO' || formType === 'fo') {
            const transactionCode = file.split('.')[0].substring(3);
            const convertedFields = convertToFieldListFO(jsonFileContents, transactionCode);
            const ConfigFilesNname = toSnakeCase(transactionCode);
            // console.warn("ConfigFilesNname FO: ", ConfigFilesNname);
            // console.warn("transactionCode FO: ", transactionCode);
            const configFiles = {
                ...convertedFields,
                "add_fee": "y",
                "field_fee": []
            }
            fs.writeFile(pathConfigFiles + "/fo/form_action/" + ConfigFilesNname + ".py.jcodegen.json", JSON.stringify(configFiles, null, 4), function (err) {
                if (err) throw err;
            });
        }
    } catch (error) {
        console.error("Error: ", error);
    }
});
console.info("Config Files converted!");
