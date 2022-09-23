
// function onDropFileLoaded(fileName, fileFormat, fileData) {
function onDropFileLoaded(file, fileFormat) {
  let boxFileObj;
  switch (fileFormat) {
    case "h5":
      boxFileObj = boxFileH5Obj;
      btnConvert.show();
      setFormFileH5(file);
      break;
      case "json":
        boxFileObj = boxFileJsonObj;
        setFormFileJson(file);
      break;
  }

  boxFileObj.setLoadVisibility(true);
  boxFileObj.setFileName(file.name);

}


function onConverterResponse(jsonResponse) {
  const codeModel = jsonResponse.model;
  // const codeFormat = jsonResponse.format;
  const codeFormat = "py";
  const modelName = "model";
  setDownloadContent(codeModel, modelName, codeFormat);
  btnDownload.show();
  btnRestart.show();
  btnConvert.hide();
}